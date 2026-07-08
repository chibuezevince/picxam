import { ref, type Reactive } from "vue"

export const useFormErrors = (
  form: Reactive<{
    errors: Record<string, string[]>
  }>,
) => {
  const modified = ref(true)

  const formatErrors = (errors: Array<Record<any, any>>) => {
    modified.value = false
    for (const err of errors) {
      const field = err.param || "non_field"
      form.errors[field] = form.errors[field] || []
      form.errors[field].push(err.message)
    }
  }

  const fieldError = (field: string) => form.errors[field]?.[0]

  const markModified = () => {
    modified.value = true
  }

  return { formatErrors, fieldError, modified, markModified }
}
