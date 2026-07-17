import { useDebounceFn, type RemovableRef } from "@vueuse/core"
import { watch, type Ref } from "vue"
import type { Question, QuizAttempt } from "../types"
import { getCookie } from "../functions"

export const sync = (
  currentIndex: Ref<number>,
  quizAttempt: QuizAttempt,
  selectedOptions: RemovableRef<Record<number, number>>,
  questions: Ref<Question[]>,
) => {
  const debouncedSync = useDebounceFn(
    async (questionId: number, optionId: number) => {
      await fetch(`/quiz/${quizAttempt.reference}/sync`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-XSRF-Token": getCookie("XSRF-TOKEN") ?? "",
        },
        body: JSON.stringify({
          question_id: questionId,
          option_id: optionId,
          current_index: currentIndex.value,
        }),
      })
    },
    500,
  )

  watch(currentIndex, (_, oldIdx) => {
    const previousQuestion = questions.value[oldIdx - 1]
    if (!previousQuestion) return

    const selected = selectedOptions.value[previousQuestion.id]
    if (selected === undefined) return

    debouncedSync(previousQuestion.id, selected)
  })
}
