<script setup lang="ts">
import { Link, router, usePage } from "@inertiajs/vue3"
import { logout } from "../composables/useAuth"
import { navItems } from "../constants"
import { ref, onMounted, onUnmounted, computed } from "vue"
import type { User } from "../types"
import "vue-sonner/style.css"
import { Toaster } from "vue-sonner"

const menuOpen = ref(false)
const animating = ref(false)

const toggleMenu = () => {
  if (menuOpen.value) {
    animating.value = true
    setTimeout(() => {
      menuOpen.value = false
      animating.value = false
    }, 350)
  } else {
    menuOpen.value = true
  }
}

const handleKeydown = (e: KeyboardEvent) => {
  if (e.key === "Escape" && menuOpen.value) toggleMenu()
}
const handleNav = (item: (typeof navItems)[0]) => {
  if (item.action === "logout") {
    toggleMenu()
    setTimeout(() => logout(), 350)
    return
  }
  if (item.action === "new") {
    toggleMenu()
    setTimeout(() => router.visit("/start"), 350)
    return
  }
  if (item.route) {
    toggleMenu()
    setTimeout(() => router.visit(item.route), 350)
  }
}
const user = computed(() => usePage().props.user as User)
onMounted(() => document.addEventListener("keydown", handleKeydown))
onUnmounted(() => document.removeEventListener("keydown", handleKeydown))
</script>
<template>
  <div class="fixed inset-0 bg-[#050508] font-sans">
    <div
      class="absolute inset-0"
      style="
        background-image: radial-gradient(
          circle,
          rgba(58, 255, 140, 0.25) 2px,
          transparent 2px
        );
        background-size: 28px 28px;
      "
    ></div>

    <div class="relative z-10 h-full overflow-y-auto flex flex-col p-4 md:p-8">
      <div class="flex-1 flex items-stretch justify-center">
        <div
          class="w-full max-w-350 text-white relative flex flex-col min-h-full"
          style="
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(3px);
            -webkit-backdrop-filter: blur(3px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
          "
        >
          <div
            class="flex items-center justify-between px-6 md:px-8 h-14 border-b border-[#2a2a30]"
          >
            <div class="flex items-center gap-4">
              <Link
                href="/"
                view-transition
                class="hover:opacity-80 transition-opacity"
              >
                <svg
                  width="20"
                  height="20"
                  viewBox="0 0 28 28"
                  fill="none"
                  class="text-[#3aff8c]"
                >
                  <rect
                    x="4"
                    y="2"
                    width="3"
                    height="24"
                    fill="currentColor"
                    transform="rotate(25 4 2)"
                  />
                  <rect
                    x="9"
                    y="2"
                    width="3"
                    height="24"
                    fill="currentColor"
                    transform="rotate(25 9 2)"
                  />
                  <rect
                    x="14"
                    y="2"
                    width="3"
                    height="24"
                    fill="currentColor"
                    transform="rotate(25 14 2)"
                  />
                  <rect
                    x="19"
                    y="2"
                    width="3"
                    height="24"
                    fill="currentColor"
                    transform="rotate(25 19 2)"
                  />
                </svg>
              </Link>
              <span class="w-px h-4 bg-[#2a2a30]" />
              <span class="text-[11px] text-gray-500 tracking-widest uppercase"
                >Dashboard</span
              >
            </div>
            <div class="flex items-center gap-4">
              <div
                class="w-7 h-7 bg-[#1a1a20] border border-[#2a2a30] flex items-center justify-center text-[10px] font-semibold text-[#3aff8c]"
              >
                {{ (user?.name || "U")[0] }}
              </div>
            </div>
          </div>

          <slot />
        </div>
      </div>
    </div>

    <transition name="fade">
      <div
        v-if="menuOpen"
        class="fixed inset-0 bg-black/40 backdrop-blur-sm z-50"
        @click="toggleMenu"
      />
    </transition>

    <div
      v-if="!menuOpen"
      class="fixed left-0 top-1/2 -translate-y-1/2 z-70"
    >
      <button
        @click="toggleMenu"
        class="relative cursor-pointer group focus:outline-none"
      >
        <div
          class="w-10 h-32 md:h-40 border-l-0 border-t border-r border-b border-[#3aff8c]/30 flex items-center justify-center transition-all duration-300 hover:border-[#3aff8c]/60"
          style="
            background: rgba(15, 15, 18, 0.85);
            backdrop-filter: blur(1px);
            -webkit-backdrop-filter: blur(1px);
            box-shadow:
              4px 0 20px rgba(0, 0, 0, 0.5),
              0 0 12px rgba(58, 255, 140, 0.08);
          "
        >
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="1.5"
            class="w-4 h-4 text-gray-400 transition-all duration-300 group-hover:text-[#3aff8c]"
          >
            <path d="M4 6h16" />
            <path d="M4 12h16" />
            <path d="M4 18h16" />
          </svg>
        </div>
      </button>
    </div>

    <div
      class="fixed left-0 top-0 h-full z-60 flex items-center pointer-events-none"
    >
      <div
        class="h-[80vh] border-t border-r border-b border-[#3aff8c]/30 flex flex-col items-center justify-center gap-6 px-5 transition-all duration-400"
        :class="[
          menuOpen && !animating
            ? 'translate-x-0 opacity-100 pointer-events-auto'
            : '-translate-x-full opacity-0 pointer-events-none',
        ]"
        style="
          background: rgba(8, 8, 12, 0.92);
          backdrop-filter: blur(16px);
          -webkit-backdrop-filter: blur(16px);
          box-shadow: 4px 0 32px rgba(0, 0, 0, 0.6);
          border-left: none;
          transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        "
      >
        <div
          v-for="(item, i) in navItems"
          :key="item.label"
          class="flex flex-col items-center gap-2 transition-all duration-300 cursor-pointer group"
          :class="[
            menuOpen && !animating
              ? 'opacity-100 translate-x-0'
              : 'opacity-0 -translate-x-4',
          ]"
          :style="{
            transitionDelay: menuOpen ? `${i * 0.06}s` : '0s',
          }"
          @click="handleNav(item)"
        >
          <button
            class="w-12 h-12 border-2 flex items-center justify-center text-lg transition-all duration-200"
            :class="[
              item.color === 'red'
                ? 'bg-[#121214] border-red-800 text-red-400 hover:bg-red-600 hover:text-white hover:border-red-600'
                : 'bg-[#121214] border-[#2a2a30] text-white hover:bg-[#3aff8c] hover:text-[#050508] hover:border-[#3aff8c]',
            ]"
          >
            {{ item.icon }}
          </button>
          <p
            class="text-[10px] text-gray-500 tracking-widest uppercase whitespace-nowrap"
          >
            {{ item.label }}
          </p>
        </div>
      </div>
    </div>
  </div>

  <Toaster
    theme="dark"
    :toast-options="{
      style: {
        background: '#0b0b0d',
        color: '#ffffff',
        borderRadius: '12px',
        padding: '12px 14px',
        fontFamily: 'var(--font-sans)',
        boxShadow: '0 10px 30px rgba(0,0,0,0.35)',
      },
    }"
  />
</template>

<style scoped>
@keyframes float {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-6px);
  }
}

.animate-spin-slow {
  animation: spin 4s linear infinite;
  transform-origin: center;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
