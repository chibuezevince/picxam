<script setup lang="ts">
defineProps<{
  value: string
  active: boolean
  label: string
}>()
const emit = defineEmits<{
  (e: "select", value: string): void
}>()
</script>
<template>
  <button
    @click="$emit('select', value)"
    class="py-3.5 text-xs font-semibold uppercase tracking-[0.12em] transition-all duration-200 cursor-pointer"
    :class="[
      active
        ? 'bg-[#3aff8c] text-[#050508]'
        : 'bg-transparent text-gray-500 hover:text-gray-300',
    ]"
  >
    {{ label }}
  </button>
</template>
