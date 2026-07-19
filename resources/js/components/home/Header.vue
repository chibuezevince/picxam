<script setup lang="ts">
import { UserIcon } from "@heroicons/vue/24/outline"
import { Head, Link, usePage } from "@inertiajs/vue3"
import { computed } from "vue"

const url = computed(() => usePage().url)

const isActive = (path: string) => url.value === path
</script>

<template>
  <Head title="Login" />
  <header
    class="flex flex-col md:flex-row items-center justify-between mb-12 md:mb-16 gap-4 md:gap-0"
  >
    <div class="flex items-center gap-4 text-sm">
      <Link
        href="/"
        view-transition
        class="hover:opacity-80 transition-opacity"
      >
        <svg
          width="28"
          height="28"
          viewBox="0 0 28 28"
          fill="none"
          class="text-white"
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
    </div>

    <nav class="flex items-center gap-6 text-xs font-medium tracking-wide">
      <Link
        href="/"
        prefetch
        view-transition
        :class="[
          'transition-colors',
          isActive('/')
            ? 'bg-white text-black px-5 py-2 font-semibold'
            : 'opacity-80 hover:text-white',
        ]"
      >
        Home
      </Link>
      <Link
        href="/#features"
        prefetch
        :class="[
          'transition-colors',
          isActive('/#features')
            ? 'bg-white text-black px-5 py-2 font-semibold'
            : 'opacity-80 hover:text-white',
        ]"
      >
        Features
      </Link>
      <Link
        href="/#how-it-works"
        prefetch
        :class="[
          'transition-colors',
          isActive('/#how-it-works')
            ? 'bg-white text-black px-5 py-2 font-semibold'
            : 'opacity-80 hover:text-white',
        ]"
      >
        How It Works
      </Link>
    </nav>

    <div class="flex items-center gap-6 text-xs font-medium">
      <Link
        href="/login"
        prefetch
        view-transition
        :class="[
          'cursor-pointer transition-colors',
          isActive('/login')
            ? 'bg-white text-black px-5 py-2 font-semibold'
            : 'opacity-80 hover:text-white',
        ]"
      >
        Login
      </Link>
      <Link
        href="/onboarding"
        view-transition
        prefetch
        class="bg-[#2cd476] cursor-pointer text-black px-5 py-2 flex items-center gap-2 text-xs font-semibold hover:bg-opacity-90 active:bg-black active:text-white transition-all"
      >
        Get Started
        <UserIcon class="size-4 text-black" />
      </Link>
    </div>
  </header>
</template>
