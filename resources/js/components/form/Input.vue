<script setup lang="ts">
defineProps<{
  id: string
  label: string
  type?: string
  placeholder?: string
  error?: string
  modelValue?: string
}>()

defineEmits<{
  "update:modelValue": [value: string]
}>()
</script>

<template>
  <div class="space-y-1.5">
    <label :for="id" class="text-xs font-medium tracking-wide opacity-80">
      {{ label }}
    </label>
    <input
      :id="id"
      :type="type || 'text'"
      :placeholder="placeholder"
      :value="modelValue"
      @input="
        $emit('update:modelValue', ($event.target as HTMLInputElement).value)
      "
      class="w-full bg-[#121214] border border-[#1e1e22] px-4 py-3 text-sm text-white placeholder-gray-500 outline-none focus:border-[#2cd476] focus:ring-1 focus:ring-[#2cd476]/30 transition-all"
      :class="
        error
          ? 'border-red-500/50 focus:border-red-500 focus:ring-red-500/30'
          : ''
      "
    />
    <div
      v-if="error"
      class="flex items-center gap-1.5 text-[11px] text-red-400 mt-1"
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
      <span>{{ error }}</span>
    </div>
  </div>
</template>
