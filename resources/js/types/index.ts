export type SignupForm = {
  name: string
  email: string
  password: string
  agree: boolean
}

export type Error = {
  message: string
  code: string
  param: string
}

export type User = {
  name: string
  email: `${string}@${string}`
}

export type RecentDocument = {
  title: string
  questions_count: number
  quizzes_count: number
  created_at: string
}

export type QuizGenerationForm = {
  document: File | null
  quiz_type: string
  thinking_effort: string
  difficulty: string
}

export type Question = {
  id: number
  text: string
  image: string
  options: Option[]
}

export type Option = {
  id: number
  text: string
}

export type QuizAttempt = {
  reference: string
  quizType: string | null
  currentIndex: number
  reasoning: string
  answers: Record<number, number>
}

export type ReasoningBox = {
  text: string
  container: HTMLElement | null
}
