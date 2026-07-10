<script setup lang="ts">
import { ArrowPathIcon, ArrowRightIcon } from "@heroicons/vue/24/outline"

withDefaults(
  defineProps<{
    type?: "button" | "submit" | "reset" | undefined
    loading?: boolean
    disabled?: boolean
    hideArrow?: boolean
  }>(),
  {
    type: "submit",
    loading: false,
    disabled: false,
    hideArrow: false,
  },
)
</script>

<template>
  <button
    :type="type"
    :disabled="disabled || loading"
    class="w-full cursor-pointer bg-[#2cd476] text-black px-6 py-3 flex items-center justify-center gap-2 text-sm font-semibold hover:bg-[#25b865] transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
  >
    <span v-if="loading">Processing</span>
    <slot v-else />
    <ArrowRightIcon
      class="size-5"
      v-if="!loading && !hideArrow"
    />
    <ArrowPathIcon
      class="size-5 animate-spin"
      v-if="loading"
    />
  </button>
</template>
