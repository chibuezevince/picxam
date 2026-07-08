<script setup lang="ts">
import { Head, Link, router } from "@inertiajs/vue3"
import GuestLayout from "../../layouts/GuestLayout.vue"
import Input from "../../components/form/Input.vue"
import Checkbox from "../../components/Checkbox.vue"
import { reactive, watch } from "vue"
import { signup } from "../../composables/useAuth.ts"
import Button from "../../components/Button.vue"
import { useFormErrors } from "../../composables/useFormErrors.ts"

defineOptions({
  layout: GuestLayout,
})

const form = reactive({
  name: "",
  email: "",
  password: "",
  agree: false,
  submitting: false,
  errors: {} as Record<string, string[]>,
})

const { formatErrors, fieldError, modified, markModified } = useFormErrors(form)

watch(
  [() => form.name, () => form.email, () => form.password, () => form.agree],
  markModified,
)

const handleSubmit = async () => {
  form.submitting = true
  form.errors = {}

  const response = await signup({
    name: form.name,
    email: form.email,
    password: form.password,
    agree: form.agree,
  })

  form.submitting = false
  if (!response) return

  const { errors, status } = response
  if (errors) formatErrors(errors)

  if (status === 401) return router.visit("/email/verify")
}
</script>

<template>
  <Head title="Get Started" />

  <section class="grid grid-cols-1 md:grid-cols-12 min-h-[70vh]">
    <div
      class="md:col-span-6 flex flex-col justify-center items-center text-center gap-6"
    >
      <div class="space-y-4">
        <h1
          class="text-3xl md:text-4xl lg:text-5xl font-medium leading-[1.1] tracking-tight"
        >
          Get Started!<br />Create Your Account<br />and Start Generating.
        </h1>
        <p
          class="text-sm md:text-base font-light opacity-70 max-w-md leading-relaxed"
        >
          Sign up to start generating questions from your documents and pictures
          in minutes.
        </p>
      </div>

      <div class="flex flex-wrap gap-3 mt-2 justify-center">
        <div
          class="bg-[#141416] px-4 py-2.5 flex flex-col items-start shadow-lg min-w-28"
        >
          <span class="text-[10px] font-bold tracking-wider text-gray-400"
            >Project Created</span
          >
          <div class="w-full h-1.5 bg-[#2cd476]/30 mt-1.5"></div>
        </div>

        <div
          class="bg-[#141416] px-4 py-2.5 flex items-center gap-3 shadow-lg min-w-28"
        >
          <div
            class="w-4 h-4 bg-orange-500/20 flex items-center justify-center text-[8px] text-orange-400"
          >
            ◎
          </div>
          <div class="flex flex-col">
            <span class="text-[10px] font-medium">New Request</span>
            <span class="text-[8px] text-gray-500">High Priority</span>
          </div>
        </div>

        <div
          class="bg-[#141416] px-4 py-2.5 flex items-center gap-3 shadow-lg min-w-28"
        >
          <div
            class="w-4 h-4 bg-purple-500/20 flex items-center justify-center text-[8px] text-purple-400"
          >
            ◑
          </div>
          <div class="flex flex-col">
            <span class="text-[10px] font-medium">Work Assigned</span>
            <span class="text-[8px] text-gray-500">In Progress</span>
          </div>
          <div class="ml-auto text-[10px] text-gray-400">-2d</div>
        </div>
      </div>
    </div>

    <div class="md:col-span-6 flex flex-col justify-center">
      <div class="w-full max-w-md mx-auto space-y-6">
        <br />
        <h2 class="text-xl font-medium">Get Started</h2>

        <form class="space-y-4 mt-3" @submit.prevent="handleSubmit">
          <Input
            id="name"
            label="Full Name"
            placeholder="John Doe"
            :error="fieldError('name')"
            v-model="form.name"
          />

          <Input
            id="email"
            label="Email Address"
            type="email"
            placeholder="you@example.com"
            :error="fieldError('email')"
            v-model="form.email"
          />

          <Input
            id="password"
            label="Password"
            type="password"
            placeholder="Create a password"
            :error="fieldError('password')"
            v-model="form.password"
          />

          <div class="flex items-center">
            <Checkbox v-model="form.agree" :error="fieldError('agree')">
              I agree to the
              <Link href="/terms" class="text-[#2cd476] hover:text-[#25b865]"
                >Terms</Link
              >
              and
              <Link href="/privacy" class="text-[#2cd476] hover:text-[#25b865]"
                >Privacy Policy</Link
              >
            </Checkbox>
          </div>

          <Button
            :loading="form.submitting"
            :disabled="!modified && Object.keys(form.errors).length > 0"
          >
            Get Started
          </Button>
        </form>

        <div class="flex items-center gap-3">
          <div class="flex-1 h-px bg-[#1e1e22]"></div>
          <span class="text-[10px] font-light opacity-50"
            >Or continue with</span
          >
          <div class="flex-1 h-px bg-[#1e1e22]"></div>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <button
            class="flex items-center justify-center gap-2 bg-[#141416] border border-[#1e1e22] px-4 py-2.5 text-xs font-medium hover:bg-[#1a1a1c] transition-colors"
          >
            <svg viewBox="0 0 24 24" class="w-4 h-4">
              <path
                fill="#4285F4"
                d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 0 1-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z"
              />
              <path
                fill="#34A853"
                d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
              />
              <path
                fill="#FBBC05"
                d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
              />
              <path
                fill="#EA4335"
                d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
              />
            </svg>
            Google
          </button>
          <button
            class="flex items-center justify-center gap-2 bg-[#141416] border border-[#1e1e22] px-4 py-2.5 text-xs font-medium hover:bg-[#1a1a1c] transition-colors"
          >
            <svg viewBox="0 0 24 24" class="w-4 h-4">
              <path
                fill="#00A4EF"
                d="M11.4 24H2.7c-.3 0-.6-.1-.8-.3-.5-.5-.2-1.2.3-1.4l9.2-5.3c.4-.2.8-.1 1 .2.3.3.4.7.2 1.1l-1.2 5.2c-.1.4-.4.5-1 .5z"
              />
              <path
                fill="#737373"
                d="M11.4 0H2.7c-.3 0-.6.1-.8.3-.5.5-.2 1.2.3 1.4l9.2 5.3c.4.2.8.1 1-.2.3-.3.4-.7.2-1.1l-1.2-5.2c-.1-.4-.4-.5-1-.5z"
              />
              <path
                fill="#0078D4"
                d="M23.4 11.4l-3.3-1.9c-.3-.2-.6-.2-.9 0l-8 4.6c-.3.2-.5.5-.5.9v3.8c0 .4.2.7.5.9l3.3 1.9c.3.2.6.2.9 0l8-4.6c.3-.2.5-.5.5-.9v-3.8c0-.3-.2-.7-.5-.9z"
              />
            </svg>
            Microsoft
          </button>
        </div>

        <p class="text-xs font-light opacity-60 text-center">
          Already have an account?
          <Link
            href="/login"
            class="text-[#2cd476] font-medium hover:text-[#25b865] transition-colors"
          >
            Sign In
          </Link>
        </p>
      </div>
    </div>
  </section>
</template>
