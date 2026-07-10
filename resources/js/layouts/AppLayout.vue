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
      v-for="(item, i) in navItems"
      :key="item.label"
      class="fixed z-60 flex items-center gap-3"
      :class="[
        menuOpen && !animating
          ? 'opacity-100 pointer-events-auto'
          : 'opacity-0 pointer-events-none',
      ]"
      :style="{
        transition: `all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) ${i * 0.04}s`,
        bottom: menuOpen ? `${120 + (navItems.length - 1 - i) * 76}px` : '20px',
        right: '20px',
        transform: menuOpen
          ? 'translateX(0) scale(1)'
          : 'translateX(20px) scale(0.6)',
      }"
    >
      <p
        class="text-xs text-gray-400 tracking-wider uppercase font-medium whitespace-nowrap"
        :class="{ 'text-white': menuOpen }"
      >
        {{ item.label }}
      </p>
      <button
        @click="handleNav(item)"
        class="w-12 h-12 border-2 flex items-center justify-center text-lg transition-all duration-200"
        :class="[
          item.color === 'red'
            ? 'bg-[#121214] border-red-800 text-red-400 hover:bg-red-600 hover:text-white hover:border-red-600'
            : 'bg-[#121214] border-[#2a2a30] text-white hover:bg-[#3aff8c] hover:text-[#050508] hover:border-[#3aff8c]',
        ]"
      >
        {{ item.icon }}
      </button>
    </div>

    <button
      @click="toggleMenu"
      class="fixed bottom-3 right-5 z-70 w-14 h-14 text-[#050508] flex items-center justify-center rounded-full group animate-[float_3s_ease-in-out_infinite]"
    >
      <span class="absolute inset-0 rounded-full">
        <svg
          class="w-full h-full animate-spin-slow"
          viewBox="0 0 56 56"
          fill="none"
        >
          <circle
            cx="28"
            cy="28"
            r="26"
            stroke="currentColor"
            stroke-width="1.5"
            class="text-[#3aff8c]/20"
          />
          <circle
            cx="28"
            cy="28"
            r="26"
            stroke="currentColor"
            stroke-width="1.5"
            stroke-dasharray="4 8"
            class="text-[#3aff8c]/60"
            pathLength="1"
            stroke-linecap="round"
          />
        </svg>
      </span>

      <span
        class="absolute -inset-1 rounded-full group-hover:opacity-80 transition-opacity duration-500"
        style="
          background: radial-gradient(
            circle,
            rgba(58, 255, 140, 0.15) 0%,
            transparent 70%
          );
        "
      />

      <span
        class="absolute inset-0.5 rounded-full group-hover:scale-110 transition-transform duration-500"
        style="
          background: radial-gradient(
            circle at 35% 28%,
            #7affb8 0%,
            #2ae67a 35%,
            #0d4f2a 70%,
            #050508 100%
          );
          box-shadow:
            0 4px 16px rgba(58, 255, 140, 0.3),
            inset 0 -2px 4px rgba(0, 0, 0, 0.3);
        "
      />

      <svg
        v-if="!menuOpen"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        class="w-5 h-5 relative z-10 transition-all duration-300 group-hover:scale-110"
      >
        <path d="M4 6h16" />
        <path d="M4 12h16" />
        <path d="M4 18h16" />
      </svg>

      <svg
        v-else
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        class="w-5 h-5 relative z-10 transition-all duration-300"
      >
        <path d="M18 6L6 18" />
        <path d="M6 6l12 12" />
      </svg>
    </button>
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
