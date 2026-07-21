<script setup lang="ts">
import { computed } from 'vue'
import { Link } from '@inertiajs/vue3'

const props = defineProps<{
  quizAttempt: {
    reference: string
    quizType: string
    documentName: string
    difficulty: string
    thinkingEffort: string
    score: number
    correctCount: number
    incorrectCount: number
    totalQuestions: number
    startedAt: string | null
    completedAt: string | null
  }
}>()

const gradeLabel = computed(() => {
  const s = props.quizAttempt.score
  if (s >= 90) return { label: 'Excellent', color: 'text-[#3aff8c]' }
  if (s >= 70) return { label: 'Good', color: 'text-[#3aff8c]' }
  if (s >= 50) return { label: 'Average', color: 'text-amber-400' }
  return { label: 'Needs Improvement', color: 'text-red-400' }
})

const duration = computed(() => {
  if (!props.quizAttempt.startedAt || !props.quizAttempt.completedAt) return ''
  const start = new Date(props.quizAttempt.startedAt)
  const end = new Date(props.quizAttempt.completedAt)
  const diff = Math.round((end.getTime() - start.getTime()) / 1000)
  const mins = Math.floor(diff / 60)
  const secs = diff % 60
  return `${mins}m ${secs}s`
})

const answeredCount = computed(
  () => props.quizAttempt.correctCount + props.quizAttempt.incorrectCount,
)

const truncatedName = computed(() => {
  const name = props.quizAttempt.documentName
  if (!name || name.length <= 30) return name
  const front = name.slice(0, 18)
  const back = name.slice(-10)
  return `${front}...${back}`
})
</script>

<template>
  <div class="flex flex-col gap-6">
    <div
      class="border border-[#2a2a30] bg-[#0a0a0f] p-8 flex flex-col items-center text-center"
    >
      <div class="relative w-28 h-28 mb-5">
        <svg
          class="w-full h-full -rotate-90"
          viewBox="0 0 120 120"
        >
          <circle
            cx="60"
            cy="60"
            r="52"
            fill="none"
            stroke="#1a1a20"
            stroke-width="8"
          />
          <circle
            cx="60"
            cy="60"
            r="52"
            fill="none"
            stroke="#3aff8c"
            stroke-width="8"
            stroke-linecap="round"
            :stroke-dasharray="`${(quizAttempt.score / 100) * 326.7} 326.7`"
            class="transition-all duration-700 ease-out"
          />
        </svg>
        <div class="absolute inset-0 flex items-center justify-center">
          <span class="text-3xl font-bold text-white font-mono"
            >{{ quizAttempt.score
            }}<span class="text-lg text-gray-500">%</span></span
          >
        </div>
      </div>
      <span
        :class="[
          gradeLabel.color,
          'text-sm font-medium tracking-wider uppercase',
        ]"
      >
        {{ gradeLabel.label }}
      </span>
    </div>

    <div class="border border-[#2a2a30] divide-y divide-[#2a2a30]">
      <div class="flex items-center justify-between px-5 py-3.5">
        <span class="text-[11px] text-gray-500 uppercase tracking-widest"
          >Correct</span
        >
        <span class="text-sm font-semibold text-[#3aff8c] font-mono">{{
          quizAttempt.correctCount
        }}</span>
      </div>
      <div class="flex items-center justify-between px-5 py-3.5">
        <span class="text-[11px] text-gray-500 uppercase tracking-widest"
          >Incorrect</span
        >
        <span class="text-sm font-semibold text-red-400 font-mono">{{
          quizAttempt.incorrectCount
        }}</span>
      </div>
      <div class="flex items-center justify-between px-5 py-3.5">
        <span class="text-[11px] text-gray-500 uppercase tracking-widest"
          >Unanswered</span
        >
        <span class="text-sm font-semibold text-gray-400 font-mono">{{
          quizAttempt.totalQuestions - answeredCount
        }}</span>
      </div>
      <div class="flex items-center justify-between px-5 py-3.5">
        <span class="text-[11px] text-gray-500 uppercase tracking-widest"
          >Total</span
        >
        <span class="text-sm font-semibold text-white font-mono">{{
          quizAttempt.totalQuestions
        }}</span>
      </div>
    </div>

    <div class="border border-[#2a2a30] divide-y divide-[#2a2a30]">
      <div class="flex items-center justify-between px-5 py-3.5">
        <span class="text-[11px] text-gray-500 uppercase tracking-widest"
          >Document</span
        >
        <span
          class="text-xs text-white/70 font-mono max-w-45 truncate text-right"
          :title="quizAttempt.documentName"
        >
          {{ truncatedName }}
        </span>
      </div>
      <div class="flex items-center justify-between px-5 py-3.5">
        <span class="text-[11px] text-gray-500 uppercase tracking-widest"
          >Duration</span
        >
        <span class="text-xs text-gray-300 font-mono">{{ duration }}</span>
      </div>
      <div class="flex items-center justify-between px-5 py-3.5">
        <span class="text-[11px] text-gray-500 uppercase tracking-widest"
          >Difficulty</span
        >
        <span class="text-xs text-gray-300 capitalize">{{
          quizAttempt.difficulty
        }}</span>
      </div>
      <div class="flex items-center justify-between px-5 py-3.5">
        <span class="text-[11px] text-gray-500 uppercase tracking-widest"
          >Thinking</span
        >
        <span class="text-xs text-gray-300 capitalize">{{
          quizAttempt.thinkingEffort
        }}</span>
      </div>
    </div>

    <Link
      href="/dashboard"
      class="w-full py-3 text-xs tracking-widest uppercase font-semibold bg-[#3aff8c] text-[#050508] text-center hover:bg-white transition-colors"
    >
      Back to Dashboard
    </Link>
  </div>
</template>
