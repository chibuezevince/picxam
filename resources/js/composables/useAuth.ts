import { toast } from "vue-sonner"
import { getCookie } from "../functions"
import type { SignupForm } from "../types"
import { router } from "@inertiajs/core"

const BASE = "/_allauth/browser/v1"

const request = async (
  path: string,
  method: string = "GET",
  body?: object,
  usePrefix: boolean = true,
): Promise<Record<any, any> | undefined> => {
  try {
    const url = usePrefix ? `${BASE}${path}` : path
    const response = await fetch(url, {
      method,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken") ?? "",
      },
      credentials: "include",
      body: body ? JSON.stringify(body) : undefined,
    })

    if (response.status === 500) {
      toast.error("Something went wrong. Please, try again later.")
      return
    }

    if (response.status === 429) {
      toast.warning(
        "Too many requests. Please, wait for some time and then try again",
      )

      return
    }

    return response.json()
  } catch (error) {
    toast.error("Your request could not be completed. Try again later.")
    return
  }
}

export const login = (
  email: string,
  password: string,
  remember: boolean = false,
) => {
  return request("/auth/login", "POST", { email, password, remember })
}

export const signup = (form: SignupForm) =>
  request("/auth/signup", "POST", form)

export const verifyEmail = (key: string) =>
  request("/auth/email/verify", "POST", { key })

export const resendVerificationEmail = (email: string) =>
  request("/auth/request-new-code", "POST", { email }, false)

export const logout = async () => {
  await request("/auth/session", "DELETE")
  router.clearHistory()
  router.visit("/login")
}

export const requestPasswordReset = (email: string) =>
  request("/auth/password/request", "POST", { email })

export const resetPassword = (key: string, password: string) =>
  request("/auth/password/reset", "POST", { key, password })

export const session = () => request("/auth/session")
