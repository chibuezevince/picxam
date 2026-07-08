<script setup lang="ts">
import { Head } from "@inertiajs/vue3"
import Hero from "../components/home/Hero.vue"
import GuestLayout from "../layouts/GuestLayout.vue"

defineOptions({
  layout: GuestLayout,
})
</script>

<template>
  <Head title="Home" />

  <Hero />

  <section class="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-16 relative">
    <div
      class="bg-[#2cd476] text-black p-6 md:p-8 relative flex flex-col h-full min-h-75"
    >
      <div class="absolute top-4 left-4">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path
            d="M12 2L12 22M2 12L22 12M4.93 4.93L19.07 19.07M4.93 19.07L19.07 4.93"
          />
        </svg>
      </div>
      <div class="absolute top-6 right-6 flex gap-3">
        <div class="bg-black/10 p-1.5">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="14"
            height="14"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <path d="M5 12h14M12 5l7 7-7 7" />
          </svg>
        </div>
        <div class="bg-black/10 p-1.5">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="14"
            height="14"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <path d="M12 2v20M2 12h20" />
          </svg>
        </div>
      </div>

      <div class="mt-10 flex flex-col items-center w-full relative">
        <div
          class="bg-[#111] text-white px-3 py-1.5 flex items-center gap-2.5 text-xs shadow-lg mb-8 z-10"
        >
          <div class="w-5 h-5 bg-gray-600 overflow-hidden">
            <img
              src="https://i.pravatar.cc/100?img=11"
              alt="avatar"
              class="w-full h-full object-cover"
            />
          </div>
          <span class="font-medium text-gray-300">Arthur King</span>
          <div class="w-1.5 h-1.5 bg-blue-400"></div>
          <span class="text-[10px] bg-[#a855f7] text-white px-1.5 rounded"
            >PRO</span
          >
          <span class="text-[10px]">⭐</span>
        </div>

        <svg
          class="absolute top-16 left-1/2 -translate-x-1/2 w-[80%] h-32 pointer-events-none z-0 text-black/30"
          viewBox="0 0 400 100"
          fill="none"
        >
          <path
            d="M200 20 C 200 40, 50 50, 50 80"
            stroke="currentColor"
            stroke-width="1.5"
            stroke-dasharray="4 4"
          />
          <path
            d="M200 20 C 200 40, 350 50, 350 80"
            stroke="currentColor"
            stroke-width="1.5"
            stroke-dasharray="4 4"
          />
        </svg>

        <div
          class="flex flex-wrap justify-center gap-3 md:gap-6 mt-4 w-full px-2"
        >
          <div
            class="bg-[#1a1a1c] px-4 py-2.5 flex flex-col items-start shadow-lg min-w-25"
          >
            <span class="text-[10px] font-bold tracking-wider text-gray-400"
              >Project Created</span
            >
            <div class="w-full h-1.5 bg-[#2cd476]/30 mt-1.5"></div>
          </div>

          <div
            class="bg-[#1a1a1c] px-4 py-2.5 flex items-center gap-3 shadow-lg min-w-25"
          >
            <div
              class="w-4 h-4 bg-orange-500/20 flex items-center justify-center text-[8px] text-orange-400"
            >
              ◎
            </div>
            <div class="flex flex-col">
              <span class="text-[10px] font-medium">New Request</span>
              <span class="text-[8px] text-gray-500">High Priority</span>
            </div>
          </div>

          <div
            class="bg-[#1a1a1c] px-4 py-2.5 flex items-center gap-3 shadow-lg min-w-25"
          >
            <div
              class="w-4 h-4 bg-purple-500/20 flex items-center justify-center text-[8px] text-purple-400"
            >
              ◑
            </div>
            <div class="flex flex-col">
              <span class="text-[10px] font-medium">Work Assigned</span>
              <span class="text-[8px] text-gray-500">In Progress</span>
            </div>
            <div class="ml-auto text-[10px] text-gray-400">-2d</div>
          </div>

          <div
            class="bg-[#1a1a1c] px-4 py-2.5 flex items-center gap-3 shadow-lg min-w-25"
          >
            <div
              class="w-4 h-4 bg-blue-500/20 flex items-center justify-center text-[8px] text-blue-400"
            >
              ◉
            </div>
            <div class="flex flex-col">
              <span class="text-[10px] font-medium">Process Started</span>
              <span class="text-[8px] text-gray-500">Waiting</span>
            </div>
          </div>
        </div>

        <div class="absolute bottom-4 right-4 text-black/40 rotate-12">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <path
              d="M12 2L12 22M2 12L22 12M4.93 4.93L19.07 19.07M4.93 19.07L19.07 4.93"
            />
          </svg>
        </div>
      </div>
    </div>

    <div
      class="bg-[#d48aff] p-6 flex items-center justify-center relative h-full min-h-75"
    >
      <div
        class="bg-[#1a1a1c] w-full max-w-65 h-120 p-4 shadow-2xl relative flex flex-col text-[10px] text-white"
      >
        <div
          class="flex justify-between items-center mb-4 px-1 text-[8px] text-gray-400"
        >
          <span>9:41</span>
          <div class="flex gap-1">
            <span>📶</span>
            <span>🔋</span>
          </div>
        </div>

        <div
          class="flex justify-between items-center mb-3 border-b border-gray-700 pb-2"
        >
          <div class="flex items-center gap-1">
            <div class="w-3 h-3 bg-yellow-400"></div>
            <span class="font-medium text-[8px]">tract</span>
          </div>
          <div class="flex gap-2 text-gray-400">
            <span>⚙</span>
            <span>💬</span>
            <span
              class="bg-gray-600 w-3 h-3 flex items-center justify-center text-[6px]"
              >👤</span
            >
          </div>
        </div>

        <div class="flex-1 flex flex-col gap-3 overflow-hidden">
          <div class="bg-[#2a2a2c] p-2">
            <div
              class="flex justify-between items-center mb-2 text-[6px] text-gray-400"
            >
              <span>← Chat</span>
              <span>•••</span>
            </div>

            <div class="bg-[#a855f7]/20 p-2 mb-2 border border-purple-500/30">
              <div class="font-semibold text-[9px] text-white mb-1">
                Schedule Me An Appointment With My Endocrinologist
              </div>
            </div>

            <div class="space-y-1.5">
              <div class="flex justify-between">
                <span class="text-[6px] text-gray-400">Requester:</span>
                <span class="text-[7px]">Arthur King</span>
              </div>
              <div class="flex justify-between">
                <span class="text-[6px] text-gray-400">Due Date:</span>
                <span class="text-[7px]">Jan 15, 2026</span>
              </div>
              <div class="flex justify-between">
                <span class="text-[6px] text-gray-400">Priority:</span>
                <div class="flex items-center gap-1">
                  <span class="text-[7px]">3 Issues</span>
                  <span
                    class="bg-yellow-500/20 text-yellow-300 px-1 rounded text-[5px]"
                    >High</span
                  >
                </div>
              </div>
              <div class="flex justify-between">
                <span class="text-[6px] text-gray-400">Labels:</span>
                <span class="text-[7px]">⚕️</span>
              </div>
            </div>

            <div class="mt-2 pt-2 border-t border-gray-700">
              <span class="text-[6px] text-gray-400">Description:</span>
              <p class="text-[7px] text-gray-300 leading-tight mt-0.5">
                Schedule and attend an appointment...
              </p>
            </div>
          </div>
        </div>

        <div
          class="flex justify-around pt-2 border-t border-gray-700 text-[6px] text-gray-400"
        >
          <span>Home</span>
          <span>🕒</span>
          <span>👤</span>
        </div>
      </div>
    </div>
  </section>

  <section
    class="grid grid-cols-2 md:grid-cols-5 gap-8 mb-16 items-center opacity-70"
  >
    <div class="flex items-center gap-2">
      <span class="text-xl font-bold">Rakuten</span>
    </div>
    <div class="flex items-center gap-2 text-sm font-bold tracking-wider">
      <span class="text-xl">◎</span> NCR
    </div>
    <div class="flex items-center gap-1">
      <span class="text-xl font-bold">m.</span
      ><span class="text-sm font-bold tracking-tight">monday.com</span>
    </div>
    <div class="text-xl font-bold font-display tracking-wider">Disney</div>
    <div class="flex items-center gap-1 text-sm font-bold">
      <span class="text-xl">✦</span> Dropbox
    </div>
  </section>

  <section
    class="grid grid-cols-1 md:grid-cols-2 border-t border-white/10 pt-8 mb-8"
  >
    <div
      class="pb-6 md:pb-0 md:pr-8 border-b md:border-b-0 md:border-r border-white/10"
    >
      <div class="text-7xl md:text-8xl font-light tracking-tight">82.7%</div>
      <div class="text-xs text-gray-400 mt-2 tracking-wide">
        4X Automate Workflows Departments
      </div>
    </div>

    <div class="pt-6 md:pt-0 md:pl-8 flex flex-col justify-center">
      <h3 class="text-xl md:text-2xl font-medium mb-2">
        Amplify Your Impact With Ai
      </h3>
      <p class="text-sm text-gray-400 mb-6 max-w-sm">
        Work smarter and faster with a suite of AI Teammates that maximize
        efficiency
      </p>
      <button
        class="bg-white text-black px-6 py-2.5 flex items-center gap-2 text-sm font-medium w-fit hover:bg-gray-100 transition-colors"
      >
        Get Started
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="2"
          stroke="currentColor"
          class="w-4 h-4"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3"
          />
        </svg>
      </button>
    </div>
  </section>
</template>
