<script setup lang="ts">
defineProps<{
  documentsCount: number
  quizCount: number
  questionsCount: number
}>()
</script>
<template>
  <div class="col-span-12 lg:col-span-6 grid grid-cols-3 items-center">
    <div class="p-8 lg:p-10 border-r border-[#2a2a30]">
      <p class="text-3xl font-bold tracking-tight text-white">
        {{ documentsCount }}
      </p>
      <p class="text-[11px] text-gray-400 tracking-widest uppercase mt-2">
        Documents
      </p>
    </div>
    <div class="p-8 lg:p-10 border-r border-[#2a2a30]">
      <p class="text-3xl font-bold tracking-tight text-white">
        {{ quizCount }}
      </p>
      <p class="text-[11px] text-gray-400 tracking-widest uppercase mt-2">
        Quizzes
      </p>
    </div>
    <div class="p-8 lg:p-10">
      <p class="text-3xl font-bold tracking-tight text-white">
        {{ questionsCount }}
      </p>
      <p class="text-[11px] text-gray-400 tracking-widest uppercase mt-2">
        Questions
      </p>
    </div>
  </div>
</template>
