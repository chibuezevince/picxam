<script setup lang="ts">
import { Link } from "@inertiajs/vue3"
</script>

<template>
  <footer
    class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 pt-6 mt-8 border-t border-[#1e1e22] text-xs text-gray-500"
  >
    <span
      >&copy; {{ new Date().getFullYear() }} Picxam. All rights reserved.</span
    >

    <div class="flex items-center gap-5">
      <Link href="/terms" class="hover:text-gray-300 transition-colors">
        Terms of Service
      </Link>
      <Link href="/privacy" class="hover:text-gray-300 transition-colors">
        Privacy Policy
      </Link>
    </div>
  </footer>
</template>
