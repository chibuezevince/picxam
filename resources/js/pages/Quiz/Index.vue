<script setup lang="ts">
import { Head } from '@inertiajs/vue3'
import AppLayout from '../../layouts/AppLayout.vue'
import { computed, onMounted, onUnmounted, reactive, ref, watch } from 'vue'
import { useEventSource, useSessionStorage } from '@vueuse/core'
import type { Question, QuizAttempt, ReasoningBox } from '../../types/index.ts'
import { sync } from '../../composables/useSyncQuiz.ts'
import AiSummary from '../../components/quiz/AiSummary.vue'
import BackButton from '../../components/BackButton.vue'
import LoadingSkeleton from '../../components/quiz/LoadingSkeleton.vue'
import QuestionNumbers from '../../components/quiz/QuestionNumbers.vue'
import QuestionArea from '../../components/quiz/QuestionArea.vue'
import { Confirm, Loading } from 'notiflix'
import { loadingLogo } from '../../constants'
defineOptions({
  layout: AppLayout,
})

const props = defineProps<{
  quizAttempt: QuizAttempt
  questions: Question[]
}>()

const questions = ref<Question[]>(props.questions)
const reasoningBox = reactive<ReasoningBox>({
  text: props.quizAttempt.reasoning ?? '',
  container: null as HTMLElement | null,
})
const currentIndex = useSessionStorage<number>(
  `${props.quizAttempt.reference}-index`,
  props.quizAttempt.currentIndex,
)
const isLastQuestion = computed<boolean>(
  () => currentIndex.value === props.questions.length,
)

const progressPercent = computed(() => {
  if (!props.questions.length) return 0
  return Math.round((currentIndex.value / props.questions.length) * 100)
})

const lastAnswer = ref<Record<number, number>>({})

const submitting = ref<boolean>(false)

const selectedOptions = useSessionStorage<Record<number, number>>(
  `${props.quizAttempt.reference}-answers`,
  props.quizAttempt.answers,
)

const selectOption = (questionId: number, optionId: number) => {
  lastAnswer.value = {}
  lastAnswer.value = {
    [questionId]: optionId,
  }
  selectedOptions.value = {
    ...selectedOptions.value,
    ...lastAnswer.value,
  }
}
const questionsLoaded = ref(false)
const direction = ref<'forward' | 'backward'>('forward')

const goNext = (forceSubmit = false) => {
  if (!forceSubmit && currentIndex.value < questions.value.length) {
    direction.value = 'forward'
    currentIndex.value++
    return
  }

  if (isLastQuestion.value || forceSubmit) {
    const answeredQuestionIds = Object.keys(selectedOptions.value)

    const unansweredQuestions = props.questions.filter(
      (question) => !answeredQuestionIds.includes(String(question.id)),
    )

    const unansweredIndex = props.questions.findIndex(
      (question) => !answeredQuestionIds.includes(String(question.id)),
    )

    const submit = () => {
      submitting.value = true
      Loading.custom('Submitting Quiz...', {
        customSvgCode: loadingLogo,
      })
    }

    if (unansweredQuestions.length) {
      Confirm.show(
        'Unanswered Questions',
        `You still have ${unansweredQuestions.length} unanswered ${unansweredQuestions.length == 1 ? 'question' : 'questions'}. Submit anyway?`,
        'Yes, Submit',
        'No, Cancel',
        () => submit(),
        () => {
          if (unansweredIndex !== -1) currentIndex.value = unansweredIndex + 1
        },
        {
          titleColor: '#f4fc03',
        },
      )

      return
    }

    submit()
  }
}

const goPrevious = () => {
  if (currentIndex.value > 1) {
    direction.value = 'backward'
    currentIndex.value--
  }
}

let reasoningQueue = ''
let reasoningWriting = false

const typewriteReasoning = (text: string) => {
  reasoningQueue += text
  if (reasoningWriting) return
  reasoningWriting = true
  const write = () => {
    if (reasoningQueue.length > 0) {
      reasoningBox.text += reasoningQueue[0]
      reasoningQueue = reasoningQueue.slice(1)
      if (reasoningBox.container) {
        reasoningBox.container.scrollTop = reasoningBox.container.scrollHeight
      }
      setTimeout(write, 15)
    } else {
      reasoningWriting = false
    }
  }
  write()
}
onMounted(() => {
  if (reasoningBox.text && reasoningBox.container) {
    reasoningBox.container.scrollTop = reasoningBox.container.scrollHeight
  }

  const { data, close } = useEventSource(
    `/quiz/${props.quizAttempt.reference}/stream/`,
    [],
    { autoReconnect: false },
  )

  watch(data, (value) => {
    if (!value) return

    const parsed = JSON.parse(value)

    if (parsed.type === 'done') {
      questionsLoaded.value = true
      close()
      return
    }

    if (parsed.type === 'reasoning') {
      if (reasoningBox.text.endsWith(parsed.text)) return
      if (parsed.text.startsWith(reasoningBox.text.slice(-100))) {
        const overlap = reasoningBox.text.slice(-100)
        const newText = parsed.text
        const commonEnd = Math.min(overlap.length, newText.length)
        let split = 0
        for (let i = 1; i <= commonEnd; i++) {
          if (overlap.slice(-i) === newText.slice(0, i)) split = i
        }
        typewriteReasoning(newText.slice(split))
        return
      }
      typewriteReasoning(parsed.text)
      return
    }

    if (parsed.type) return

    if (questions.value.some((question) => question.id === parsed.id)) return

    questions.value.push(parsed)
  })
})

onUnmounted(() => {
  Loading.remove()
})

sync(currentIndex, props.quizAttempt, lastAnswer, submitting)
</script>

<template>
  <Head title="Quiz" />

  <div class="flex-1 flex flex-col overflow-y-auto">
    <div
      class="md:max-w-[85vw] mx-auto w-full flex flex-col gap-6 p-6 md:p-0 md:mb-10"
    >
      <div class="md:mt-10">
        <BackButton
          :label="quizAttempt.quizType ? `${quizAttempt.quizType} quiz` : ''"
        />
      </div>

      <div class="flex items-center gap-3">
        <div class="flex-1 h-1 bg-[#1a1a20]">
          <div
            class="h-full bg-[#3aff8c] transition-all duration-300 ease-out"
            :style="{ width: progressPercent + '%' }"
          />
        </div>
        <div class="flex items-center gap-2">
          <Transition name="fade">
            <span
              v-if="!questionsLoaded && questions.length > 0"
              class="flex items-center gap-1.5 text-[10px] text-[#3aff8c]/70 uppercase tracking-widest"
            >
              <span class="w-1.5 h-1.5 bg-[#3aff8c] animate-pulse" />
              Generating
            </span>
          </Transition>
          <span class="text-xs text-gray-500 tabular-nums whitespace-nowrap">
            {{ currentIndex }} / {{ questions.length }}
          </span>
        </div>
      </div>

      <AiSummary :reasoning-box="reasoningBox" />

      <QuestionNumbers
        :questions="questions"
        :current-index="currentIndex"
        :selected-options="selectedOptions"
        @change-index="currentIndex = $event"
      />

      <LoadingSkeleton
        :questions="questions"
        :current-index="currentIndex"
        :reasoning-box="reasoningBox"
        v-if="!questions.length"
      />

      <QuestionArea
        v-else
        :current-index="currentIndex"
        :questions="questions"
        :direction="direction"
        :selected-options="selectedOptions"
        @select-option="selectOption"
        @go-next="goNext"
        @go-previous="goPrevious"
        @submit="goNext(true)"
        :is-last-question="isLastQuestion"
      />
    </div>
  </div>
</template>
