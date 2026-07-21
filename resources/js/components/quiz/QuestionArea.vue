<script lang="ts" setup>
import { computed } from "vue"
import type { Question } from "../../types"
import {
  BoltIcon,
  ChevronLeftIcon,
  ChevronRightIcon,
} from "@heroicons/vue/24/outline"

const props = defineProps<{
  currentIndex: number
  questions: Question[]
  direction: "forward" | "backward"
  selectedOptions: Record<number, number>
  isLastQuestion: boolean
}>()

const emit = defineEmits<{
  (e: "selectOption", questionId: number, optionId: number): void
  (e: "goNext"): void
  (e: "goPrevious"): void
  (e: 'submit'): void
}>()

const imageMap = computed(() => {
  const seen = new Map<string, number>()
  let idx = 0
  for (const question of props.questions) {
    if (question.image && !seen.has(question.image)) {
      seen.set(question.image, idx++)
    }
  }
  return seen
})

const currentQuestion = computed(() => {
  const q = props.questions[props.currentIndex - 1] ?? ({} as Question)
  const imageIndex = q.image ? (imageMap.value.get(q.image) ?? 0) + 1 : null
  const questionOnImage = q.image
    ? props.questions.filter((x) => x.image === q.image).indexOf(q) + 1
    : null
  return { ...q, imageIndex, questionOnImage }
})
</script>
<template>
  <div class="grid grid-cols-1 md:grid-cols-5 gap-6">
    <Transition
      name="split-left"
      mode="out-in"
      appear
    >
      <div
        :key="currentIndex"
        class="md:col-span-2 border border-[#3a3a41] bg-[#0a0a0e] flex flex-col overflow-hidden"
        style="
          background: rgba(255, 255, 255, 0.02);
          backdrop-filter: blur(3px);
          -webkit-backdrop-filter: blur(3px);
        "
      >
        <div
          v-if="currentQuestion.image"
          class="px-4 py-2 border-b border-[#333333] text-[10px] text-gray-500 tracking-widest uppercase"
        >
          Image {{ currentQuestion.imageIndex }}, Question
          {{ currentQuestion.questionOnImage }}
        </div>
        <div
          class="flex-1 flex items-center justify-center text-gray-600 text-sm"
        >
          <img
            v-if="currentQuestion.image"
            :src="`/media/${currentQuestion.image}`"
            alt="Question image"
            class="w-full max-h-[75dvh] object-contain"
          />
          <span
            v-else
            class="text-gray-600 text-sm"
            >No image</span
          >
        </div>
      </div>
    </Transition>

    <Transition
      name="split-right"
      mode="out-in"
      appear
    >
      <div
        :key="currentIndex"
        class="md:col-span-3 flex flex-col gap-6"
      >
        <div
          class="border border-[#333333] overflow-hidden"
          style="
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(3px);
            -webkit-backdrop-filter: blur(3px);
          "
        >
          <div class="p-6 md:p-8 lg:p-10">
            <div class="flex items-center gap-6">
              <span
                class="w-8 h-8 bg-[#1a1a20] border border-[#333333] flex items-center justify-center text-sm font-semibold text-[#3aff8c] shrink-0"
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
            @click="emit('selectOption', currentQuestion.id, option.id)"
            class="w-full text-left px-6 py-4 flex items-center gap-4 transition-all duration-200 cursor-pointer"
            :class="[
              selectedOptions[currentQuestion.id] === option.id
                ? 'border-[#3aff8c] bg-[#3aff8c]/10 text-white'
                : 'border-[#333333] text-gray-400 hover:border-[#3aff8c]/50 hover:text-gray-200',
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
                  : 'border-[#333333]',
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
            @click="emit('goPrevious')"
            class="px-5 py-2.5 text-xs tracking-wider uppercase border border-[#333333] text-gray-400 hover:border-gray-500 hover:text-gray-200 transition-colors cursor-pointer"
          >
            <div class="flex gap-3">
              <ChevronLeftIcon class="size-4" /> Previous
            </div>
          </button>
          <div class="flex gap-3">
            <button
              @click="emit('submit')"
              :class="
                isLastQuestion
                  ? `bg-[#3aff8c] text-[#050508] hover:bg-white`
                  : `text-gray-400 hover:border-gray-500 hover:text-gray-200`
              "
              class="px-5 py-2.5 text-xs tracking-wider uppercase border border-[#333333] transition-colors cursor-pointer"
            >
              <div class="flex gap-3"><BoltIcon class="size-4" /> Submit</div>
            </button>
            <button
              v-if="!isLastQuestion"
              @click="emit('goNext')"
              class="px-5 py-2.5 text-xs tracking-wider uppercase font-semibold bg-[#3aff8c] text-[#050508] hover:bg-white transition-colors cursor-pointer"
            >
              <div class="flex gap-3">
                Next <ChevronRightIcon class="size-4" />
              </div>
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>
