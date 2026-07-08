<script setup lang="ts">
import { Head } from "@inertiajs/vue3"
import AppLayout from "../layouts/AppLayout.vue"
import type { User } from "../types/index.ts"

defineOptions({
  layout: AppLayout,
})

const props = defineProps<{
  user: User
  documentCount: number
  quizCount: number
  documentsCount: number
}>()
</script>

<template>
  <Head title="Dashboard" />

  <div class="grid grid-cols-12 border-b border-[#2a2a30]">
    <div
      class="col-span-12 lg:col-span-6 border-r border-[#2a2a30] p-8 lg:p-10"
    >
      <p class="text-xs text-gray-500 tracking-widest uppercase mb-3">
        {{
          new Date().toLocaleDateString("en-US", {
            weekday: "short",
            month: "short",
            day: "numeric",
          })
        }}
      </p>
      <h1
        class="text-3xl md:text-4xl lg:text-5xl font-semibold tracking-tight leading-[1.05] mb-4"
      >
        Hey {{ (user?.name || "User").split(" ")[0] }},<br />
        <span class="text-gray-600 font-light">ready to generate?</span>
      </h1>
      <div class="flex items-center gap-3">
        <button
          class="bg-[#3aff8c] text-[#050508] text-xs font-bold px-5 py-2.5 tracking-wider uppercase hover:bg-white transition-colors"
        >
          New Document
        </button>
        <button
          class="border border-[#2a2a30] text-xs text-gray-400 px-5 py-2.5 tracking-wider uppercase hover:border-gray-500 hover:text-gray-200 transition-colors"
        >
          View All
        </button>
      </div>
    </div>

    <div class="col-span-12 lg:col-span-6 grid grid-cols-3 items-center">
      <div class="p-8 lg:p-10 border-r border-[#2a2a30]">
        <p class="text-3xl font-bold tracking-tight text-white">
          {{ documentCount }}
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
          {{ documentsCount }}
        </p>
        <p class="text-[11px] text-gray-400 tracking-widest uppercase mt-2">
          Documents
        </p>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-12">
    <div
      class="col-span-12 lg:col-span-7 border-r border-[#2a2a30] p-8 lg:p-10"
    >
      <div class="flex items-center justify-between mb-6">
        <h2 class="text-xs text-gray-400 tracking-widest uppercase">
          Recent Activity
        </h2>
        <button
          class="text-[10px] text-[#3aff8c] tracking-wider uppercase font-semibold hover:text-white transition-colors"
        >
          View All
        </button>
      </div>
      <div class="space-y-0">
        <div
          class="border-t border-[#2a2a30] py-4 flex items-center justify-between hover:bg-[#0a0a0f] px-3 -mx-3 transition-colors"
        >
          <div class="flex items-center gap-3">
            <span
              class="w-6 h-6 bg-[#3aff8c]/10 border border-[#3aff8c]/30 flex items-center justify-center text-[10px] text-[#3aff8c] font-bold"
              >+</span
            >
            <div>
              <p class="text-sm font-medium text-white">Biology 101 Quiz</p>
              <p class="text-xs text-gray-500 mt-0.5">12 questions generated</p>
            </div>
          </div>
          <span class="text-[11px] text-gray-600">2h ago</span>
        </div>
        <div
          class="border-t border-[#2a2a30] py-4 flex items-center justify-between hover:bg-[#0a0a0f] px-3 -mx-3 transition-colors"
        >
          <div class="flex items-center gap-3">
            <span
              class="w-6 h-6 bg-[#3aff8c]/10 border border-[#3aff8c]/30 flex items-center justify-center text-[10px] text-[#3aff8c] font-bold"
              >+</span
            >
            <div>
              <p class="text-sm font-medium text-white">History Notes</p>
              <p class="text-xs text-gray-500 mt-0.5">8 questions generated</p>
            </div>
          </div>
          <span class="text-[11px] text-gray-600">5h ago</span>
        </div>
        <div
          class="border-t border-[#2a2a30] py-4 flex items-center justify-between hover:bg-[#0a0a0f] px-3 -mx-3 transition-colors"
        >
          <div class="flex items-center gap-3">
            <span
              class="w-6 h-6 bg-[#3aff8c]/10 border border-[#3aff8c]/30 flex items-center justify-center text-[10px] text-[#3aff8c] font-bold"
              >+</span
            >
            <div>
              <p class="text-sm font-medium text-white">Math Formulas</p>
              <p class="text-xs text-gray-500 mt-0.5">15 questions generated</p>
            </div>
          </div>
          <span class="text-[11px] text-gray-600">1d ago</span>
        </div>
      </div>
    </div>

    <div class="col-span-12 lg:col-span-5 p-8 lg:p-10">
      <h2 class="text-xs text-gray-400 tracking-widest uppercase mb-4">
        Quick Upload
      </h2>
      <div
        class="border border-dashed border-[#3aff8c]/40 bg-[#3aff8c]/5 p-8 text-center"
      >
        <p class="text-sm text-gray-300 font-medium">Drop file here</p>
        <p
          class="text-[10px] text-gray-600 mt-2 tracking-wider uppercase font-medium"
        >
          PDF PNG JPG
        </p>
      </div>
      <div class="mt-6 border-t border-[#2a2a30] pt-5">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs text-gray-500 tracking-wider uppercase"
            >Total Generated</span
          >
          <span class="text-lg font-bold text-white">0</span>
        </div>
        <div class="w-full h-px bg-[#2a2a30]" />
        <div class="flex items-center justify-between mt-2">
          <span class="text-xs text-gray-500 tracking-wider uppercase"
            >This Week</span
          >
          <span class="text-lg font-bold text-[#3aff8c]">0</span>
        </div>
      </div>
    </div>
  </div>
</template>
