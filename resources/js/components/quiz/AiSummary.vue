<script setup lang="ts">
import { ref } from "vue";
import { renderMarkdown } from "../../functions"
import type { ReasoningBox } from "../../types";

defineProps<{
    reasoningBox: ReasoningBox
}>()
const showReasoning = ref(false)
</script>

<template>
  <div
    v-if="reasoningBox.text"
    class="border border-[#2a2a30] overflow-hidden"
    style="
      background: rgba(8, 8, 12, 0.9);
      backdrop-filter: blur(3px);
      -webkit-backdrop-filter: blur(3px);
    "
  >
    <button
      @click="showReasoning = !showReasoning"
      class="w-full px-4 py-2 border-b border-[#2a2a30] flex items-center gap-2 cursor-pointer hover:bg-white/5 transition-colors"
    >
      <span
        class="w-1.5 h-1.5 shrink-0"
        :class="
          reasoningBox.text ? 'bg-[#3aff8c] animate-pulse' : 'bg-gray-600'
        "
      />
      <span
        class="text-[10px] text-gray-500 tracking-widest uppercase flex-1 text-left"
      >
        AI Summary
      </span>
      <svg
        class="w-3 h-3 text-gray-500 transition-transform duration-200"
        :class="showReasoning ? 'rotate-180' : ''"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M19 9l-7 7-7-7"
        />
      </svg>
    </button>
    <div
      class="grid transition-[grid-template-rows] duration-300 ease-in-out"
      :class="showReasoning ? 'grid-rows-[1fr]' : 'grid-rows-[0fr]'"
    >
      <div class="overflow-hidden">
        <div
          class="p-4 scrollbar-thin"
          :ref="
            (el) => {
              reasoningBox.container = el as HTMLElement
            }
          "
        >
          <p
            class="prose prose-invert text-[14px] text-gray-400 leading-relaxed font-mono"
            v-html="renderMarkdown(reasoningBox.text)"
          />
        </div>
      </div>
    </div>
  </div>
</template>
