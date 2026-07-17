<script setup lang="ts">
import { Head, Link } from "@inertiajs/vue3"
import AppLayout from "../../layouts/AppLayout.vue"
import { computed, onMounted, ref, watch } from "vue"
import { useEventSource, useSessionStorage } from "@vueuse/core"
import type { Question, QuizAttempt } from "../../types/index.ts"
import { sync } from "../../composables/useSyncQuiz.ts"

defineOptions({
  layout: AppLayout,
})

const props = defineProps<{
  quizAttempt: QuizAttempt
}>()

const questions = ref<Question[]>([])
const currentIndex = ref<number>(props.quizAttempt.currentIndex)
const currentQuestion = computed(
  () => questions.value[currentIndex.value - 1] ?? {},
)
const selectedOptions = useSessionStorage<Record<number, number>>(
  `quiz-${props.quizAttempt.reference}`,
  props.quizAttempt.answers,
)

const selectOption = (questionId: number, optionId: number) =>
  (selectedOptions.value = { ...selectedOptions.value, [questionId]: optionId })

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

onMounted(() => {
  const { data, close } = useEventSource(
    `/quiz/${props.quizAttempt.reference}/stream`,
    [],
    { autoReconnect: false },
  )

  watch(data, (value) => {
    if (!value) return

    const parsed = JSON.parse(value)

    if (parsed.type === "done") {
      close()
      return
    }

    if(parsed.type) return

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
        <span class="text-xs text-gray-500 tabular-nums whitespace-nowrap">
          {{ currentIndex }} / {{ questions.length }}
        </span>
      </div>

      <div
        v-if="questions.length > 0"
        class="flex items-center gap-1.5 flex-wrap"
      >
        <button
          v-for="i in questions.length"
          :key="i"
          @click="currentIndex = i"
          class="w-7 h-7 text-[11px] font-semibold border transition-all duration-200 cursor-pointer"
          :class="[
            currentIndex === i
              ? 'border-[#3aff8c] bg-[#3aff8c] text-[#050508]'
              : selectedOptions[questions[i - 1]?.id] !== undefined
                ? 'border-[#3aff8c]/50 bg-[#3aff8c]/10 text-[#3aff8c]'
                : 'border-[#2a2a30] text-gray-500 hover:border-gray-400',
          ]"
        >
          {{ i }}
        </button>
      </div>

      <div
        v-if="questions.length === 0"
        class="grid grid-cols-1 md:grid-cols-5 gap-6"
      >
        <div
          class="md:col-span-3 md:row-span-full border-2 border-[#2a2a30] bg-[#0a0a0e] min-h-64 animate-pulse"
          style="
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(3px);
            -webkit-backdrop-filter: blur(3px);
          "
        />

        <div class="md:col-span-2 flex flex-col gap-6">
          <div
            class="border-2 border-[#2a2a30] overflow-hidden animate-pulse"
            style="
              background: rgba(255, 255, 255, 0.02);
              backdrop-filter: blur(3px);
              -webkit-backdrop-filter: blur(3px);
            "
          >
            <div class="p-6 md:p-8 lg:p-10">
              <div class="flex items-start gap-4">
                <span
                  class="w-8 h-8 border-2 border-[#2a2a30] bg-[#1a1a20] shrink-0"
                />
                <div class="flex-1 space-y-3 pt-1.5">
                  <div
                    class="h-4 border-2 border-[#2a2a30] bg-[#1a1a20] w-full"
                  />
                  <div
                    class="h-4 border-2 border-[#2a2a30] bg-[#1a1a20] w-3/4"
                  />
                </div>
              </div>
            </div>
          </div>

          <div class="flex flex-col gap-2.5">
            <div
              v-for="i in 4"
              :key="i"
              class="w-full h-14 border-2 border-[#2a2a30] bg-[#1a1a20] animate-pulse"
              :style="{ animationDelay: `${i * 0.1}s` }"
            />
          </div>

          <div class="flex items-center justify-between pt-2">
            <div
              class="w-24 h-10 border-2 border-[#2a2a30] bg-[#1a1a20] animate-pulse"
            />
            <div
              class="w-20 h-10 border-2 border-[#2a2a30] bg-[#1a1a20] animate-pulse"
            />
          </div>
        </div>
      </div>

      <div
        v-else
        class="grid grid-cols-1 md:grid-cols-5 gap-6"
      >
        <Transition
          :name="direction === 'forward' ? 'slide-next' : 'slide-prev'"
          mode="out-in"
          appear
        >
          <div
            :key="currentIndex"
            class="md:col-span-3 md:row-span-full border border-[#2a2a30] bg-[#0a0a0e] flex items-center justify-center text-gray-600 text-sm min-h-64 overflow-hidden"
            style="
              background: rgba(255, 255, 255, 0.02);
              backdrop-filter: blur(3px);
              -webkit-backdrop-filter: blur(3px);
            "
          >
            <img
              v-if="currentQuestion.image"
              :src="`/media/${currentQuestion.image}`"
              alt="Question image"
              class="w-full h-full object-contain"
            />
            <span
              v-else
              class="text-gray-600 text-sm"
              >No image</span
            >
          </div>
        </Transition>

        <Transition
          :name="direction === 'forward' ? 'slide-next' : 'slide-prev'"
          mode="out-in"
          appear
        >
          <div
            :key="currentIndex"
            class="md:col-span-2 flex flex-col gap-6"
          >
            <div
              class="border border-[#2a2a30] overflow-hidden"
              style="
                background: rgba(255, 255, 255, 0.02);
                backdrop-filter: blur(3px);
                -webkit-backdrop-filter: blur(3px);
              "
            >
              <div class="p-6 md:p-8 lg:p-10">
                <div class="flex items-center gap-6">
                  <span
                    class="w-8 h-8 bg-[#1a1a20] border border-[#2a2a30] flex items-center justify-center text-sm font-semibold text-[#3aff8c] shrink-0"
                  >
                    {{ currentIndex }}
                  </span>
                  <p
                    class="text-base md:text-lg text-white/90 leading-relaxed pt-1.5"
                  >
                    {{ currentQuestion.text }}
                  </p>
                </div>
              </div>
            </div>

            <div class="flex flex-col gap-2.5">
              <button
                v-for="option in currentQuestion.options"
                :key="option.id"
                @click="selectOption(currentQuestion.id, option.id)"
                class="w-full text-left px-6 py-4 flex items-center gap-4 transition-all duration-200 cursor-pointer"
                :class="[
                  selectedOptions[currentQuestion.id] === option.id
                    ? 'border-[#3aff8c] bg-[#3aff8c]/10 text-white'
                    : 'border-[#2a2a30] text-gray-400 hover:border-[#3aff8c]/50 hover:text-gray-200',
                ]"
                style="
                  background: rgba(255, 255, 255, 0.02);
                  backdrop-filter: blur(3px);
                  -webkit-backdrop-filter: blur(3px);
                  border-width: 1px;
                  border-style: solid;
                "
              >
                <span
                  class="w-6 h-6 border flex items-center justify-center text-xs shrink-0 transition-all duration-200"
                  :class="[
                    selectedOptions[currentQuestion.id] === option.id
                      ? 'border-[#3aff8c] bg-[#3aff8c] text-[#050508]'
                      : 'border-[#2a2a30]',
                  ]"
                >
                  <svg
                    v-if="selectedOptions[currentQuestion.id] === option.id"
                    class="w-3.5 h-3.5"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="3"
                      d="M5 13l4 4L19 7"
                    />
                  </svg>
                </span>
                <span class="text-sm">{{ option.text }}</span>
              </button>
            </div>

            <div
              v-if="questions.length > 0"
              class="flex items-center justify-between pt-2"
            >
              <button
                @click="goPrevious"
                class="px-5 py-2.5 text-xs tracking-wider uppercase border border-[#2a2a30] text-gray-400 hover:border-gray-500 hover:text-gray-200 transition-colors cursor-pointer"
              >
                Previous
              </button>
              <button
                @click="goNext"
                class="px-5 py-2.5 text-xs tracking-wider uppercase font-semibold bg-[#3aff8c] text-[#050508] hover:bg-white transition-colors cursor-pointer"
              >
                Next
              </button>
            </div>
          </div>
        </Transition>
      </div>
    </div>
  </div>
</template>

<style>
.slide-next-enter-active,
.slide-next-leave-active,
.slide-prev-enter-active,
.slide-prev-leave-active {
  transition:
    transform 0.2s cubic-bezier(0.25, 0.1, 0.25, 1),
    filter 0.15s ease;
  will-change: transform, filter;
}

.slide-next-leave-to {
  transform: translateX(-40px) skewX(3deg) scaleX(0.92);
  filter: blur(1px);
}

.slide-next-enter-from {
  transform: translateX(40px) skewX(-3deg) scaleX(0.92);
  filter: blur(1px);
}

.slide-prev-leave-to {
  transform: translateX(40px) skewX(-3deg) scaleX(0.92);
  filter: blur(1px);
}

.slide-prev-enter-from {
  transform: translateX(-40px) skewX(3deg) scaleX(0.92);
  filter: blur(1px);
}

.slide-next-enter-to,
.slide-prev-enter-to {
  transform: translateX(0) skewX(0) scaleX(1);
  filter: blur(0);
}
</style>
