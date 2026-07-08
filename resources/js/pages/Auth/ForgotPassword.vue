<script setup lang="ts">
import { reactive, watch, onMounted } from "vue"
import { Head, Link } from "@inertiajs/vue3"
import GuestLayout from "../../layouts/GuestLayout.vue"
import Input from "../../components/form/Input.vue"
import Button from "../../components/Button.vue"
import { useFormErrors } from "../../composables/useFormErrors.ts"
import { toast } from "vue-sonner"
import { pullFlash } from "../../composables/useFlashSession.ts"
import { requestPasswordReset } from "../../composables/useAuth.ts"

const form = reactive({
  email: "",
  submitting: false,
  sent: false,
  errors: {} as Record<string, string[]>,
})

const { formatErrors, fieldError, modified, markModified } = useFormErrors(form)

watch(() => form.email, markModified)

defineOptions({
  layout: GuestLayout,
})

const handleSubmit = async () => {
  form.submitting = true
  form.errors = {}

  const response = await requestPasswordReset(form.email)

  form.submitting = false
  if (!response) return

  const { errors } = response
  if (errors) formatErrors(errors)

  form.sent = true
  toast.success(
    "If an account with that email exists, a password reset link has been sent.",
  )
}

onMounted(() => {
  const message = pullFlash("message")
  if (message) toast.message(message)
})
</script>

<template>
  <Head title="Forgot Password" />

  <section class="grid grid-cols-1 md:grid-cols-12 min-h-[70vh]">
    <div
      class="md:col-span-6 flex flex-col justify-center items-center text-center gap-6"
    >
      <div class="space-y-4">
        <h1
          class="text-3xl md:text-4xl lg:text-5xl font-medium leading-[1.1] tracking-tight"
        >
          Forgot Your<br />Password?<br />No Worries.
        </h1>
        <p
          class="text-sm md:text-base font-light opacity-70 max-w-md leading-relaxed"
        >
          Enter your email address and we will send you a link to reset your
          password.
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
        <h2 class="text-xl font-medium">Reset Password</h2>

        <div
          v-if="form.sent"
          class="bg-[#2cd476]/10 border border-[#2cd476]/30 px-5 py-4 text-sm text-[#2cd476]"
        >
          If an account with that email exists, a password reset link has been
          sent.
        </div>

        <form v-else class="space-y-4 mt-3" @submit.prevent="handleSubmit">
          <Input
            id="email"
            v-model="form.email"
            label="Email Address"
            type="email"
            placeholder="you@example.com"
            :error="fieldError('email')"
          />

          <Button
            :loading="form.submitting"
            :disabled="!modified && Object.keys(form.errors).length > 0"
          >
            Send Reset Link
          </Button>
        </form>

        <div class="text-center">
          <Link
            href="/login"
            class="text-xs font-medium text-[#2cd476] hover:text-[#25b865] transition-colors"
          >
            Back to Login
          </Link>
        </div>
      </div>
    </div>
  </section>
</template>
