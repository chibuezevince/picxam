<script setup lang="ts">
import { reactive, computed, watch, onMounted } from "vue"
import { Head, Link, router } from "@inertiajs/vue3"
import GuestLayout from "../../layouts/GuestLayout.vue"
import { EnvelopeIcon } from "@heroicons/vue/24/outline"
import Button from "../../components/Button.vue"
import { verifyEmail, resendVerificationEmail } from "../../composables/useAuth"
import { toast } from "vue-sonner"
import { verifyEmailForm } from "../../constants/index.ts"
import { pullFlash, setFlash } from "../../composables/useFlashSession.ts"

defineOptions({
  layout: GuestLayout,
})

const form = reactive(verifyEmailForm)

const sanitize = (val: string) => val.replace(/[^a-zA-Z0-9]/g, "").slice(0, 4)

const codeGroup1 = computed({
  get: () => form.code.split("-")[0] || "",
  set: (val) => {
    const g2 = form.code.split("-")[1] || ""
    form.code = sanitize(val) + "-" + g2
  },
})

const codeGroup2 = computed({
  get: () => form.code.split("-")[1] || "",
  set: (val) => {
    const group1 = form.code.split("-")[0] || ""
    form.code = group1 + "-" + sanitize(val)
  },
})

const handleVerify = async () => {
  if (form.code.length < 9) {
    form.error = "Please enter the complete verification code."
    return
  }

  const response = await verifyEmail(form.code)
  form.verifying = false

  if (!response) return

  switch (response.status) {
    case 200:
      toast.success("Email verified successfully.")
      router.visit("/dashboard")
      return

    case 400:
      form.error = response.errors[0]?.message
      return

    case 409:
      setFlash("message", "Too many requests. Please, login and try again.")
      router.visit("/login")
      return
  }
}

const handleResend = async () => {
  form.resending = true
  const response = await resendVerificationEmail()

  form.resending = false
  if (!response) return

  if (response.status !== 200) {
    toast.error(
      "Something went wrong and the email could not be resent. Please, try again.",
    )
    return
  }

  form.resent = true
  form.code = ""
  form.error = ""
  toast.success("Verification email resent. Please check your inbox.")
}

watch(
  () => form.error,
  (error) => toast.error(error),
)

onMounted(() => {
  const message = pullFlash("message")
  if (message) toast.message(message)
})
</script>

<template>
  <Head title="Verify Email" />

  <section class="grid grid-cols-1 md:grid-cols-12 min-h-[70vh]">
    <div
      class="md:col-span-6 flex flex-col justify-center items-center text-center gap-6"
    >
      <div class="space-y-4">
        <h1
          class="text-3xl md:text-4xl lg:text-5xl font-medium leading-[1.1] tracking-tight"
        >
          Check Your Email!<br />Verify Your Account<br />to Get Started.
        </h1>
        <p
          class="text-sm md:text-base font-light opacity-70 max-w-md leading-relaxed"
        >
          We sent a verification code to your email address. Enter the code to
          activate your account and start generating questions.
        </p>
      </div>

      <div class="flex flex-wrap gap-3 mt-2 justify-center">
        <div
          class="bg-[#141416] px-4 py-2.5 flex flex-col items-start shadow-lg min-w-28"
        >
          <span class="text-[10px] font-bold tracking-wider text-gray-400"
            >Email Sent</span
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
            <span class="text-[10px] font-medium">Pending</span>
            <span class="text-[8px] text-gray-500">Awaiting Confirmation</span>
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

        <div
          class="bg-[#141416] border border-[#1e1e22] p-8 flex flex-col items-center text-center"
        >
          <div
            class="w-14 h-14 bg-[#2cd476]/10 flex items-center justify-center mb-5"
          >
            <EnvelopeIcon class="size-7 text-[#2cd476]" />
          </div>

          <h2 class="text-xl font-medium mb-2">Verify Your Email</h2>
          <p class="text-sm font-light opacity-70 leading-relaxed mb-6">
            Enter the verification code sent to your email to activate your
            account.
          </p>

          <div class="flex items-center justify-between gap-3 mb-4">
            <input
              v-model="codeGroup1"
              type="text"
              inputmode="text"
              maxlength="4"
              placeholder="QJVF"
              :disabled="form.verifying"
              class="w-[50%] h-13 bg-[#121214] border-2 px-4 text-center text-xl font-bold text-white placeholder:text-[#555] outline-none transition-all"
              :class="
                form.error
                  ? 'border-red-500/50 focus:border-red-500 focus:ring-1 focus:ring-red-500/30'
                  : 'border-[#333] focus:border-[#2cd476] focus:ring-1 focus:ring-[#2cd476]/30'
              "
            />
            <span class="text-[#555] text-xl font-bold select-none">-</span>
            <input
              v-model="codeGroup2"
              type="text"
              inputmode="text"
              maxlength="4"
              placeholder="GWXW"
              :disabled="form.verifying"
              class="w-[50%] h-13 bg-[#121214] border-2 px-4 text-center text-xl font-bold text-white placeholder:text-[#555] outline-none transition-all"
              :class="
                form.error
                  ? 'border-red-500/50 focus:border-red-500 focus:ring-1 focus:ring-red-500/30'
                  : 'border-[#333] focus:border-[#2cd476] focus:ring-1 focus:ring-[#2cd476]/30'
              "
            />
          </div>

          <div
            v-if="form.error"
            class="flex items-center justify-center gap-1.5 text-[11px] text-red-400 mt-2"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
              fill="currentColor"
              class="w-3.5 h-3.5 shrink-0"
            >
              <path
                fill-rule="evenodd"
                d="M18 10a8 8 0 1 1-16 0 8 8 0 0 1 16 0ZM8.28 7.22a.75.75 0 0 0-1.06 1.06L8.94 10l-1.72 1.72a.75.75 0 1 0 1.06 1.06L10 11.06l1.72 1.72a.75.75 0 1 0 1.06-1.06L11.06 10l1.72-1.72a.75.75 0 0 0-1.06-1.06L10 8.94 8.28 7.22Z"
                clip-rule="evenodd"
              />
            </svg>
            <span>{{ form.error }}</span>
          </div>

          <Button
            type="button"
            :loading="form.verifying"
            :disabled="form.code.length < 9"
            @click="handleVerify"
          >
            Verify Email
          </Button>

          <div
            class="w-full bg-[#121214] border border-[#1e1e22] px-4 py-3 text-xs font-light leading-relaxed mt-4"
          >
            <span class="opacity-60"
              >Didn't receive the email? Check your spam folder or
            </span>
            <button
              :disabled="form.resending || form.resent"
              class="text-[#2cd476] font-medium hover:text-[#25b865] transition-colors cursor-pointer disabled:opacity-40"
              @click="handleResend"
            >
              {{
                form.resent
                  ? "Email sent"
                  : form.resending
                    ? "Sending..."
                    : "resend"
              }}
            </button>
          </div>
        </div>

        <p class="text-xs font-light opacity-60 text-center">
          Already verified?
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
