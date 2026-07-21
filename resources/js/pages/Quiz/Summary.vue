<script setup lang="ts">
import { Head } from '@inertiajs/vue3'
import AppLayout from '../../layouts/AppLayout.vue'
import BackButton from '../../components/BackButton.vue'
import QuizSummarySidebar from '../../components/quiz/QuizSummarySidebar.vue'
import QuizReviewItem from '../../components/quiz/QuizReviewItem.vue'

defineOptions({ layout: AppLayout })

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
  questions: {
    id: number
    text: string
    image: string | null
    options: { id: number; text: string; isCorrect: boolean }[]
    selectedOptionId: number | null
    isCorrect: boolean | null
  }[]
}>()
</script>

<template>
  <Head title="Quiz Summary" />

  <div class="flex-1 flex flex-col">
    <div
      class="md:max-w-[85vw] mx-auto w-full flex flex-col gap-8 p-6 md:p-0 md:mb-10"
    >
      <div class="md:mt-10">
        <BackButton
          :label="
            quizAttempt.quizType
              ? `${quizAttempt.quizType} quiz summary`
              : 'Quiz summary'
          "
        />
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-start">
        <div class="md:col-span-1 md:sticky md:top-10">
          <QuizSummarySidebar :quiz-attempt="quizAttempt" />
        </div>

        <div class="md:col-span-2 flex flex-col gap-4">
          <div class="border border-[#2a2a30] bg-[#0a0a0f] px-6 py-4">
            <span
              class="text-[10px] text-gray-500 uppercase tracking-[0.15em] font-medium"
              >Review Answers</span
            >
          </div>

          <QuizReviewItem
            v-for="(question, idx) in questions"
            :key="question.id"
            :question="question"
            :index="idx"
          />
        </div>
      </div>
    </div>
  </div>
</template>
