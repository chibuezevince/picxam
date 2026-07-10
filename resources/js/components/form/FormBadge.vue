<script setup lang="ts">
defineProps<{
  show?: boolean
  type?: "error" | "info" | "success" | "warning"
}>()
</script>

<template>
  <Transition name="slide-error">
    <div
      v-if="$slots.default && show"
      class="text-[10px] uppercase tracking-[0.08em] leading-relaxed border-l-2 pl-3"
      :class="{
        'text-red-300/90 border-red-900/60': type === 'error',
        'text-sky-300/90 border-sky-900/60': type === 'info',
        'text-green-300/90 border-green-900/60': type === 'success',
        'text-amber-300/90 border-amber-900/60': type === 'warning',
      }"
    >
      <slot />
    </div>
  </Transition>
</template>
