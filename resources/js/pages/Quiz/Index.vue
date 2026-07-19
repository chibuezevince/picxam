<script setup lang="ts">
import { Head, Link } from "@inertiajs/vue3"
import AppLayout from "../../layouts/AppLayout.vue"
import { onMounted, reactive, ref, watch } from "vue"
import { useEventSource, useSessionStorage } from "@vueuse/core"
import type { Question, QuizAttempt, ReasoningBox } from "../../types/index.ts"
import { sync } from "../../composables/useSyncQuiz.ts"
import AiSummary from "../../components/quiz/AiSummary.vue"
import LoadingSkeleton from "../../components/quiz/LoadingSkeleton.vue"
import QuestionNumbers from "../../components/quiz/QuestionNumbers.vue"
import QuestionArea from "../../components/quiz/QuestionArea.vue"

defineOptions({
  layout: AppLayout,
})

const props = defineProps<{
  quizAttempt: QuizAttempt
  questions: Question[]
}>()

const questions = ref<Question[]>(props.questions)
const reasoningBox = reactive<ReasoningBox>({
  text: props.quizAttempt.reasoning ?? "",
  container: null as HTMLElement | null,
})
const currentIndex = ref<number>(props.quizAttempt.currentIndex)

const selectedOptions = useSessionStorage<Record<number, number>>(
  `quiz-${props.quizAttempt.reference}`,
  props.quizAttempt.answers,
)

const selectOption = (questionId: number, optionId: number) =>
  (selectedOptions.value = { ...selectedOptions.value, [questionId]: optionId })
const questionsLoaded = ref(false)
const direction = ref<"forward" | "backward">("forward")

const goNext = () => {
  if (currentIndex.value < questions.value.length) {
    direction.value = "forward"
    currentIndex.value++
  }
}

const goPrevious = () => {
  if (currentIndex.value > 1) {
    direction.value = "backward"
    currentIndex.value--
  }
}

let reasoningQueue = ""
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

    if (parsed.type === "done") {
      questionsLoaded.value = true
      close()
      return
    }

    if (parsed.type === "reasoning") {
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

sync(currentIndex, props.quizAttempt, selectedOptions, questions)
</script>

<template>
  <Head title="Quiz" />

  <div class="flex-1 flex flex-col overflow-y-auto">
    <div
      class="md:max-w-[85vw] mx-auto w-full flex flex-col gap-6 p-6 md:p-0 md:mb-10"
    >
      <div class="flex items-center gap-4 md:mt-10">
        <Link
          href="/dashboard"
          class="w-8 h-8 border border-[#2a2a30] flex items-center justify-center hover:border-gray-500 transition-colors"
        >
          <svg
            class="w-4 h-4 text-gray-400"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M15 19l-7-7 7-7"
            />
          </svg>
        </Link>
        <span class="text-xs text-gray-500 tracking-widest uppercase">
          {{ quizAttempt.quizType }}
        </span>
      </div>

      <div class="flex items-center gap-3">
        <div class="flex-1 h-1 bg-[#1a1a20]">
          <div class="h-full w-1/3 bg-[#3aff8c]" />
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
      />
    </div>
  </div>
</template>