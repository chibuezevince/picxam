import { router } from '@inertiajs/vue3'
import { useDebounceFn } from '@vueuse/core'
import { watch, type Ref } from 'vue'
import type { QuizAttempt } from '../types'

export const sync = (
  currentIndex: Ref<number>,
  quizAttempt: QuizAttempt,
  lastAnswer: Ref<Record<number, number>>,
  submitting: Ref<boolean>,
) => {
  const debouncedSync = useDebounceFn(async () => {
    const [questionId, optionId] = Object.entries(lastAnswer.value)[0] ?? [
      null,
      null,
    ]

    router.post(`/quiz/${quizAttempt.reference}/sync/`, {
      question_id: questionId,
      option_id: optionId,
      current_index: currentIndex.value,
      submitting: submitting.value,
    })
  }, 500)

  watch(lastAnswer, () => debouncedSync())
  watch(submitting, () => debouncedSync())
}
