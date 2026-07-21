<script setup lang="ts">
import { Link } from "@inertiajs/vue3"

defineProps<{
  label: string
}>()
</script>

<template>
  <div class="flex items-center gap-4">
    <Link
      href="/dashboard"
      class="w-8 h-8 border border-[#2a2a30] flex items-center justify-center hover:border-gray-500 transition-colors"
    >
      <svg
        class="w-4 h-4 text-gray-400"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M15 19l-7-7 7-7"
        />
      </svg>
    </Link>
    <span class="text-xs text-gray-500 tracking-widest uppercase">
      {{ label }}
    </span>
  </div>
</template>
