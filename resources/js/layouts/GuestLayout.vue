<script setup lang="ts">
import Header from "../components/home/Header.vue"
import Footer from "../components/home/Footer.vue"
import "vue-sonner/style.css"
import { Toaster } from "vue-sonner"
</script>

<template>
  <div class="fixed inset-0 bg-[#0a0a0c] font-sans">
    <div
      class="absolute inset-0"
      style="
        background-image: radial-gradient(
          circle,
          rgba(58, 255, 140, 0.15) 1.5px,
          transparent 1.5px
        );
        background-size: 28px 28px;
      "
    ></div>

    <div class="relative z-10 h-full overflow-y-auto flex flex-col p-4 md:p-8">
      <div class="flex-1 flex items-center justify-center">
        <div
          class="w-full max-w-350 text-white p-6 md:p-12 lg:p-16 relative flex flex-col"
          style="
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(2px);
            -webkit-backdrop-filter: blur(2px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
          "
        >
          <Header />
          <div class="flex-1">
            <slot />
          </div>
          <Footer />
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
