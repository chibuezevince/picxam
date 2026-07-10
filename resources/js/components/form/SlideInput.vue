<script setup lang="ts">
const model = defineModel<number>({ required: true })

defineProps<{
  min: number
  max: number
}>()
</script>

<template>
  <input
    v-model.number="model"
    type="range"
    :min="min"
    :max="max"
    step="1"
    class="w-full h-1 appearance-none cursor-pointer bg-[#2a2a30] accent-[#3aff8c] [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3 [&::-webkit-slider-thumb]:h-5 [&::-webkit-slider-thumb]:bg-[#3aff8c] [&::-webkit-slider-thumb]:shadow-[0_0_8px_rgba(58,255,140,0.5)]"
  />
  <div
    class="flex justify-between text-[9px] text-gray-600 mt-2 tracking-wider"
  >
    <span>{{ min }}</span>
    <span>{{ max }}</span>
  </div>
</template>
