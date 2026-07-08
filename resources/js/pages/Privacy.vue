<script setup lang="ts">
import { Head } from "@inertiajs/vue3"
import GuestLayout from "../layouts/GuestLayout.vue"

defineOptions({
  layout: GuestLayout,
})
</script>

<template>
  <Head title="Privacy Policy" />

  <section class="max-w-3xl mx-auto py-12 md:py-16">
    <h1 class="text-3xl md:text-4xl font-medium tracking-tight mb-2">
      Privacy Policy
    </h1>
    <p class="text-xs text-gray-500 mb-10">Last updated: July 5, 2026</p>

    <div class="space-y-8 text-sm leading-relaxed text-gray-300">
      <div>
        <h2 class="text-lg font-medium text-white mb-3">
          1. Information We Collect
        </h2>
        <p class="opacity-80">
          We collect information you provide when creating an account, including
          your name and email address. We also collect the documents and images
          you upload to the Service for the purpose of generating questions.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">
          2. How We Use Your Information
        </h2>
        <p class="opacity-80">
          Your information is used to provide, maintain, and improve the
          Service. This includes processing uploaded content, generating
          questions, communicating with you about your account, and sending
          service-related notifications.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">
          3. Data Storage and Security
        </h2>
        <p class="opacity-80">
          We implement reasonable security measures to protect your data.
          However, no method of transmission or storage is completely secure. We
          retain your data for as long as your account is active or as needed to
          provide the Service.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">4. Data Sharing</h2>
        <p class="opacity-80">
          We do not sell your personal information. We may share your data with
          third-party service providers who assist us in operating the Service,
          such as cloud storage providers, and only to the extent necessary to
          provide the Service.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">5. Cookies</h2>
        <p class="opacity-80">
          We use essential cookies to maintain your session and authenticate
          your account. We do not use tracking cookies or third-party analytics
          cookies.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">6. Your Rights</h2>
        <p class="opacity-80">
          You have the right to access, update, or delete your personal
          information at any time. You may contact us to request a copy of your
          data or to close your account.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">
          7. Changes to This Policy
        </h2>
        <p class="opacity-80">
          We may update this Privacy Policy from time to time. We will notify
          you of any changes by posting the new policy on this page and updating
          the "Last updated" date.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">8. Contact</h2>
        <p class="opacity-80">
          If you have any questions about this Privacy Policy, please contact us
          at support@picxam.com.
        </p>
      </div>
    </div>
  </section>
</template>
