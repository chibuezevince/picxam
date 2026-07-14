<script setup lang="ts">
import { Head, Link } from "@inertiajs/vue3"
import AppLayout from "../../layouts/AppLayout.vue"

defineOptions({
  layout: AppLayout,
})
</script>

<template>
  <Head title="Quiz" />

  <div class="flex-1 flex flex-col overflow-y-auto">
    <div
      class="md:max-w-[70%] mx-auto w-full flex flex-col gap-6 p-6 md:p-0 md:mb-10"
    >
      <div class="flex items-center gap-4 md:mt-10">
        <Link
          href="/dashboard"
          class="w-8 h-8 border border-[#2a2a30] flex items-center justify-center hover:border-gray-500 transition-colors"
        >
          <svg
            class="w-4 h-4 text-gray-400"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M15 19l-7-7 7-7"
            />
          </svg>
        </Link>
        <span class="text-xs text-gray-500 tracking-widest uppercase">
          Multiple Choice
        </span>
      </div>

      <div class="flex items-center gap-3">
        <div class="flex-1 h-1 bg-[#1a1a20]">
          <div class="h-full w-1/3 bg-[#3aff8c]" />
        </div>
        <span class="text-xs text-gray-500 tabular-nums whitespace-nowrap">
          3 / 10
        </span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-5 gap-6">
        <div
          class="md:col-span-3 md:row-span-full border border-[#2a2a30] bg-[#0a0a0e] flex items-center justify-center text-gray-600 text-sm min-h-64"
          style="
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(3px);
            -webkit-backdrop-filter: blur(3px);
          "
        >
          Image placeholder
        </div>

        <div class="md:col-span-2 flex flex-col gap-6">
          <div
            class="border border-[#2a2a30] overflow-hidden"
            style="
              background: rgba(255, 255, 255, 0.02);
              backdrop-filter: blur(3px);
              -webkit-backdrop-filter: blur(3px);
            "
          >
            <div class="p-6 md:p-8 lg:p-10">
              <div class="flex items-start gap-4">
                <span
                  class="w-8 h-8 bg-[#1a1a20] border border-[#2a2a30] flex items-center justify-center text-sm font-semibold text-[#3aff8c] shrink-0"
                >
                  3
                </span>
                <p
                  class="text-base md:text-lg text-white/90 leading-relaxed pt-1.5"
                >
                  What is the primary function of the mitochondria in a cell?
                </p>
              </div>
            </div>
          </div>

          <div class="flex flex-col gap-2.5">
            <button
              class="w-full text-left px-6 py-4 flex items-center gap-4 border border-[#3aff8c] bg-[#3aff8c]/10 text-white transition-all duration-200 cursor-pointer"
              style="
                background: rgba(255, 255, 255, 0.02);
                backdrop-filter: blur(3px);
                -webkit-backdrop-filter: blur(3px);
                border-width: 1px;
                border-style: solid;
              "
            >
              <span
                class="w-6 h-6 border border-[#3aff8c] bg-[#3aff8c] text-[#050508] flex items-center justify-center text-xs shrink-0"
              >
                <svg
                  class="w-3.5 h-3.5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="3"
                    d="M5 13l4 4L19 7"
                  />
                </svg>
              </span>
              <span class="text-sm"
                >Energy production through ATP synthesis</span
              >
            </button>

            <button
              class="w-full text-left px-6 py-4 flex items-center gap-4 border border-[#2a2a30] text-gray-400 hover:border-[#3aff8c]/50 hover:text-gray-200 transition-all duration-200 cursor-pointer"
              style="
                background: rgba(255, 255, 255, 0.02);
                backdrop-filter: blur(3px);
                -webkit-backdrop-filter: blur(3px);
                border-width: 1px;
                border-style: solid;
              "
            >
              <span
                class="w-6 h-6 border border-[#2a2a30] flex items-center justify-center text-xs shrink-0"
              />
              <span class="text-sm">Protein synthesis and folding</span>
            </button>

            <button
              class="w-full text-left px-6 py-4 flex items-center gap-4 border border-[#2a2a30] text-gray-400 hover:border-[#3aff8c]/50 hover:text-gray-200 transition-all duration-200 cursor-pointer"
              style="
                background: rgba(255, 255, 255, 0.02);
                backdrop-filter: blur(3px);
                -webkit-backdrop-filter: blur(3px);
                border-width: 1px;
                border-style: solid;
              "
            >
              <span
                class="w-6 h-6 border border-[#2a2a30] flex items-center justify-center text-xs shrink-0"
              />
              <span class="text-sm">Lipid breakdown and waste removal</span>
            </button>

            <button
              class="w-full text-left px-6 py-4 flex items-center gap-4 border border-[#2a2a30] text-gray-400 hover:border-[#3aff8c]/50 hover:text-gray-200 transition-all duration-200 cursor-pointer"
              style="
                background: rgba(255, 255, 255, 0.02);
                backdrop-filter: blur(3px);
                -webkit-backdrop-filter: blur(3px);
                border-width: 1px;
                border-style: solid;
              "
            >
              <span
                class="w-6 h-6 border border-[#2a2a30] flex items-center justify-center text-xs shrink-0"
              />
              <span class="text-sm">Photosynthesis and glucose storage</span>
            </button>
          </div>
        </div>
      </div>

      <div class="flex items-center justify-between pt-2">
        <button
          class="px-5 py-2.5 text-xs tracking-wider uppercase border border-[#2a2a30] text-gray-400 hover:border-gray-500 hover:text-gray-200 transition-colors cursor-pointer"
        >
          Previous
        </button>
        <button
          class="px-5 py-2.5 text-xs tracking-wider uppercase font-semibold bg-[#3aff8c] text-[#050508] hover:bg-white transition-colors cursor-pointer"
        >
          Next
        </button>
      </div>
    </div>
  </div>
</template>
