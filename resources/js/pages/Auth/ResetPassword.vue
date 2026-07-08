<script setup lang="ts">
import { reactive, watch } from "vue"
import { Head, Link, router } from "@inertiajs/vue3"
import GuestLayout from "../../layouts/GuestLayout.vue"
import Input from "../../components/form/Input.vue"
import Button from "../../components/Button.vue"
import { useFormErrors } from "../../composables/useFormErrors.ts"
import { resetPassword } from "../../composables/useAuth.ts"
import { setFlash } from "../../composables/useFlashSession.ts"

defineOptions({
  layout: GuestLayout,
})

const props = defineProps<{
  resetKey: string
}>()

const form = reactive({
  password: "",
  passwordConfirmation: "",
  submitting: false,
  errors: {} as Record<string, string[]>,
})

const { formatErrors, fieldError, modified, markModified } = useFormErrors(form)

watch([() => form.password], markModified)

const handleSubmit = async () => {
  if (form.password !== form.passwordConfirmation) {
    form.errors.passwordConfirm = ["Passwords do not match."]
    return
  }

  form.submitting = true
  form.errors = {}

  const response = await resetPassword(props.resetKey, form.password)

  form.submitting = false
  if (!response) return

  const { errors, status } = response

  if (errors) formatErrors(errors)

  if (fieldError("key")) {
    setFlash(
      "message",
      "Password reset link has expired. Please, request a new one.",
    )
    router.visit("/forgot-password")
  }

  switch (status) {
    case 200:
      setFlash("message", "Password reset successfully.")
      router.visit("/dashboard")
      return

    case 409:
      setFlash(
        "message",
        "Password reset link has expired. Please, request a new one.",
      )
      router.visit("/forgot-password")
      return
  }
}
</script>

<template>
  <Head title="Reset Password" />

  <section class="grid grid-cols-1 md:grid-cols-12 min-h-[70vh]">
    <div
      class="md:col-span-6 flex flex-col justify-center items-center text-center gap-6"
    >
      <div class="space-y-4">
        <h1
          class="text-3xl md:text-4xl lg:text-5xl font-medium leading-[1.1] tracking-tight"
        >
          Set a New<br />Password<br />for Your Account.
        </h1>
        <p
          class="text-sm md:text-base font-light opacity-70 max-w-md leading-relaxed"
        >
          Enter your new password below to regain access to your account.
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
          v-if="fieldError('key')"
          class="bg-red-500/10 border border-red-500/30 px-5 py-3 text-sm text-red-400"
        >
          {{ fieldError("key") }}
        </div>

        <form class="space-y-4 mt-3" @submit.prevent="handleSubmit">
          <Input
            id="password"
            v-model="form.password"
            label="New Password"
            type="password"
            placeholder="Enter your new password"
            :error="fieldError('password')"
          />

          <Input
            id="passwordConfirm"
            v-model="form.passwordConfirmation"
            label="Confirm Password"
            type="password"
            placeholder="Confirm your new password"
          />

          <Button
            :loading="form.submitting"
            :disabled="!modified && Object.keys(form.errors).length > 0"
          >
            Reset Password
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
