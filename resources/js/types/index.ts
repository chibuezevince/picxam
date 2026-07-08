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
