<script setup lang="ts">
import { Head } from "@inertiajs/vue3"
import GuestLayout from "../layouts/GuestLayout.vue"

defineOptions({
  layout: GuestLayout,
})
</script>

<template>
  <Head title="Terms of Service" />

  <section class="max-w-3xl mx-auto py-12 md:py-16">
    <h1 class="text-3xl md:text-4xl font-medium tracking-tight mb-2">
      Terms of Service
    </h1>
    <p class="text-xs text-gray-500 mb-10">Last updated: July 5, 2026</p>

    <div class="space-y-8 text-sm leading-relaxed text-gray-300">
      <div>
        <h2 class="text-lg font-medium text-white mb-3">
          1. Acceptance of Terms
        </h2>
        <p class="opacity-80">
          By accessing or using Picxam ("the Service"), you agree to be bound by
          these Terms of Service. If you do not agree to these terms, you may
          not use the Service.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">
          2. Description of Service
        </h2>
        <p class="opacity-80">
          Picxam is a platform that allows users to upload documents and images,
          extract text content, and generate questions based on that content. We
          reserve the right to modify, suspend, or discontinue any aspect of the
          Service at any time.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">3. User Accounts</h2>
        <p class="opacity-80">
          You are responsible for maintaining the confidentiality of your
          account credentials and for all activities that occur under your
          account. You must provide accurate and complete information when
          creating your account.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">4. Acceptable Use</h2>
        <p class="opacity-80">
          You agree not to use the Service for any unlawful purpose or in
          violation of any applicable laws. You may not upload content that
          infringes on the intellectual property rights of others, contains
          malware, or is otherwise harmful.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">
          5. Intellectual Property
        </h2>
        <p class="opacity-80">
          The Service and its original content, features, and functionality are
          owned by Picxam and are protected by applicable copyright, trademark,
          and other intellectual property laws. You retain ownership of any
          content you upload to the Service.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">
          6. Limitation of Liability
        </h2>
        <p class="opacity-80">
          Picxam shall not be liable for any indirect, incidental, special,
          consequential, or punitive damages arising out of your use of the
          Service. The Service is provided on an "as is" and "as available"
          basis without warranties of any kind.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">7. Termination</h2>
        <p class="opacity-80">
          We reserve the right to terminate or suspend your account at any time,
          without prior notice, for conduct that we believe violates these Terms
          or is harmful to the Service or other users.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">8. Changes to Terms</h2>
        <p class="opacity-80">
          We reserve the right to update or modify these Terms at any time.
          Changes will be effective immediately upon posting. Your continued use
          of the Service after any changes constitutes acceptance of the new
          Terms.
        </p>
      </div>

      <div>
        <h2 class="text-lg font-medium text-white mb-3">9. Contact</h2>
        <p class="opacity-80">
          If you have any questions about these Terms, please contact us at
          support@picxam.com.
        </p>
      </div>
    </div>
  </section>
</template>
