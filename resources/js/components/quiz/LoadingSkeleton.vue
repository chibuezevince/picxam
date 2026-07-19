<script lang="ts" setup>
import type { Question, ReasoningBox } from "../../types"

defineProps<{
  questions: Question[]
  currentIndex: number
  reasoningBox: ReasoningBox
}>()
</script>

<template>
  <div
    v-if="questions.length === 0"
    class="grid grid-cols-1 md:grid-cols-5 gap-6"
  >
    <div
      class="md:col-span-3 md:row-span-full border-2 border-[#2a2a30] bg-[#0a0a0e] min-h-64 animate-pulse"
      style="
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(3px);
        -webkit-backdrop-filter: blur(3px);
      "
    />

    <div class="md:col-span-2 flex flex-col gap-6">
      <div
        class="border border-[#2a2a30] overflow-hidden"
        style="
          background: rgba(8, 8, 12, 0.9);
          backdrop-filter: blur(3px);
          -webkit-backdrop-filter: blur(3px);
        "
      >
        <div
          class="px-4 py-2 border-b border-[#2a2a30] flex items-center gap-2"
        >
          <span class="w-2 h-2 bg-[#3aff8c] animate-pulse" />
          <span class="text-[10px] text-gray-500 tracking-widest uppercase"
            >Analyzing images</span
          >
        </div>
        <div class="p-4 max-h-48 overflow-y-auto scrollbar-thin">
          <div
            v-if="!reasoningBox.text"
            class="flex items-center gap-1.5"
          >
            <span
              v-for="i in 3"
              :key="i"
              class="w-1.5 h-1.5 bg-gray-600 animate-bounce"
              :style="{ animationDelay: `${i * 0.15}s` }"
            />
          </div>
        </div>
      </div>

      <div class="flex flex-col gap-2.5">
        <div
          v-for="i in 4"
          :key="i"
          class="w-full h-14 border-2 border-[#2a2a30] bg-[#1a1a20] animate-pulse"
          :style="{ animationDelay: `${i * 0.1}s` }"
        />
      </div>

      <div class="flex items-center justify-between pt-2">
        <div
          class="w-24 h-10 border-2 border-[#2a2a30] bg-[#1a1a20] animate-pulse"
        />
        <div
          class="w-20 h-10 border-2 border-[#2a2a30] bg-[#1a1a20] animate-pulse"
        />
      </div>
    </div>
  </div>
</template>
