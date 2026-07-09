<script setup lang="ts">
import type { RecentDocument } from "../../types"
import TimeAgo from "../TimeAgo.vue"

defineProps<{
  recentDocuments: RecentDocument[]
}>()
</script>
<template>
  <div class="col-span-12 lg:col-span-7 border-r border-[#2a2a30] p-8 lg:p-10">
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-xs text-gray-400 tracking-widest uppercase">
        Recent Activity
      </h2>
      <button
        class="text-[10px] text-[#3aff8c] tracking-wider uppercase font-semibold hover:text-white transition-colors"
        v-if="recentDocuments.length"
      >
        View All
      </button>
    </div>
    <div class="space-y-0">
      <div
        v-if="recentDocuments.length === 0"
        class="border-t border-[#2a2a30] pt-14 pb-12 flex flex-col items-center justify-center text-center px-4"
      >
        <div class="relative mb-6">
          <div
            class="w-16 h-16 rounded-full border border-[#3aff8c]/20 bg-[#3aff8c]/5 flex items-center justify-center"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="w-7 h-7 text-[#3aff8c]"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="1.2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z"
              />
            </svg>
          </div>
          <span
            class="absolute -top-0.5 -right-0.5 w-5 h-5 rounded-full bg-[#3aff8c] flex items-center justify-center"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="w-3 h-3 text-[#050508]"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="3"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 4.5v15m7.5-7.5h-15"
              />
            </svg>
          </span>
        </div>
        <p class="text-sm text-gray-300 font-medium mb-1.5">Nothing yet</p>
        <p class="text-xs text-gray-600 max-w-[200px] leading-relaxed">
          Upload your first document and<br />start generating quizzes
        </p>
      </div>
      <div
        v-for="doc in recentDocuments"
        :key="doc.title"
        class="border-t border-[#2a2a30] py-4 flex items-center justify-between hover:bg-[#0a0a0f] px-3 -mx-3 transition-colors group"
      >
        <div class="flex items-center gap-3 min-w-0">
          <span
            class="w-6 h-6 bg-[#3aff8c]/10 border border-[#3aff8c]/30 flex items-center justify-center text-[10px] text-[#3aff8c] font-bold shrink-0"
            >+</span
          >
          <div class="min-w-0">
            <p class="text-sm font-medium text-white truncate">
              {{ doc.title }}
            </p>
            <p class="text-xs text-gray-500 mt-0.5">
              {{ doc.questions_count }} questions
              <span
                v-if="doc.quizzes_count"
                class="text-gray-600"
                >· {{ doc.quizzes_count }} quiz{{
                  doc.quizzes_count !== 1 ? "zes" : ""
                }}</span
              >
            </p>
          </div>
        </div>
        <span class="text-[11px] text-gray-600 shrink-0 ml-3">
          <TimeAgo :date="doc.created_at" />
        </span>
      </div>
    </div>
  </div>
</template>
