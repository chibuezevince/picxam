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
  questions_count: number
  quiz_type: string
}
