<script setup lang="ts">
defineProps<{
  modelValue?: boolean
  error?: string
}>()

const emit = defineEmits<{
  "update:modelValue": [value: boolean]
}>()
</script>

<template>
  <div>
    <label
      class="flex items-center gap-3 cursor-pointer select-none"
      :class="{ 'animate-shake': error }"
      @click.prevent="emit('update:modelValue', !modelValue)"
    >
      <span
        class="w-5 h-5 flex items-center justify-center border-2 transition-all shrink-0"
        :class="
          modelValue
            ? 'bg-[#2cd476] border-[#2cd476]'
            : 'bg-[#121214] border-[#333]'
        "
      >
        <svg
          v-if="modelValue"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          class="w-3.5 h-3.5 text-black"
        >
          <path
            fill-rule="evenodd"
            d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z"
            clip-rule="evenodd"
          />
        </svg>
      </span>
      <span class="text-xs font-light opacity-70">
        <slot />
      </span>
    </label>
  </div>
</template>

<style scoped>
@keyframes shake {
  0%,
  100% {
    transform: translateX(0);
  }
  20% {
    transform: translateX(-6px);
  }
  40% {
    transform: translateX(6px);
  }
  60% {
    transform: translateX(-4px);
  }
  80% {
    transform: translateX(4px);
  }
}

.animate-shake {
  animation: shake 0.4s ease-in-out;
}
</style>
