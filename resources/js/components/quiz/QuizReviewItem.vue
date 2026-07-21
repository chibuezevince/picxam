<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{
  question: {
    id: number
    text: string
    image: string | null
    options: { id: number; text: string; isCorrect: boolean }[]
    selectedOptionId: number | null
    isCorrect: boolean | null
  }
  index: number
}>()

const isExpanded = ref(false)

const toggleImage = () => (isExpanded.value = !isExpanded.value)
</script>

<template>
  <div class="border border-[#2a2a30] bg-[#0a0a0f] overflow-hidden">
    <div class="flex items-center gap-4 px-6 py-4 border-b border-[#2a2a30]">
      <span
        class="w-7 h-7 flex items-center justify-center text-xs font-bold font-mono shrink-0"
        :class="
          question.isCorrect === true
            ? 'bg-[#3aff8c]/10 text-[#3aff8c]'
            : question.isCorrect === false
              ? 'bg-red-400/10 text-red-400'
              : 'bg-gray-500/10 text-gray-500'
        "
      >
        {{ index + 1 }}
      </span>
      <p class="text-sm text-white/80 leading-relaxed">
        {{ question.text }}
      </p>
      <span
        v-if="question.selectedOptionId === null"
        class="ml-auto text-[10px] uppercase tracking-widest text-gray-400 border border-[#2a2a30] px-2 py-0.5 shrink-0"
        >Unanswered</span
      >
    </div>

    <div class="px-6 py-3 flex flex-col gap-2">
      <div
        v-for="option in question.options"
        :key="option.id"
        class="flex items-center gap-3 px-4 py-2.5 text-sm transition-colors"
        :class="[
          option.isCorrect
            ? 'bg-[#3aff8c]/5 border-l-2 border-[#3aff8c]'
            : option.id === question.selectedOptionId
              ? 'bg-red-400/5 border-l-2 border-red-400'
              : 'border-l-2 border-transparent',
        ]"
      >
        <span class="w-5 h-5 flex items-center justify-center shrink-0">
          <svg
            v-if="option.isCorrect"
            class="w-3.5 h-3.5 text-[#3aff8c]"
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
          <svg
            v-else-if="option.id === question.selectedOptionId"
            class="w-3.5 h-3.5 text-red-400"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="3"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
          <span
            v-else
            class="w-1.5 h-1.5 rounded-full bg-[#2a2a30]"
          />
        </span>
        <span
          :class="[
            option.isCorrect
              ? 'text-[#3aff8c]/90'
              : option.id === question.selectedOptionId
                ? 'text-red-400/90'
                : 'text-gray-400',
          ]"
        >
          {{ option.text }}
        </span>
      </div>
    </div>

    <div
      v-if="question.image"
      class="border-t border-[#2a2a30]"
    >
      <button
        @click="toggleImage"
        class="w-full px-6 py-3 text-left flex items-center justify-between text-xs text-gray-500 hover:text-white transition-colors"
      >
        <span class="uppercase tracking-widest font-medium">View Image</span>
        <svg
          :class="[
            'w-4 h-4 transition-transform duration-200',
            isExpanded ? 'rotate-180' : '',
          ]"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </button>
      <div
        v-if="isExpanded"
        class="px-6 pb-6 pt-2"
      >
        <img
          :src="`/media/${question.image}`"
          class="w-full h-auto rounded border border-[#2a2a30] max-h-125 object-contain bg-black/20"
          alt="Question image"
        />
      </div>
    </div>
  </div>
</template>
