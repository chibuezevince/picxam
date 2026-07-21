<script lang="ts" setup>
import type { Question } from "../../types"

const emit = defineEmits<{
  changeIndex: [i: number]
}>()

defineProps<{
  questions: Question[]
  currentIndex: number
  selectedOptions: Record<number, number>
}>()
</script>
<template>
  <div
    v-if="questions.length > 0"
    class="w-full"
  >
    <TransitionGroup
      name="pop-in"
      tag="div"
      class="flex gap-1.5 justify-end flex-wrap"
    >
      <button
        v-for="i in questions.length"
        :key="i"
        @click="emit('changeIndex', i)"
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
    </TransitionGroup>
  </div>
</template>
