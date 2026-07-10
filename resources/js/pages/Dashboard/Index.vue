<script setup lang="ts">
import { Head, Link } from "@inertiajs/vue3"
import AppLayout from "../../layouts/AppLayout.vue"
import type { RecentDocument, User } from "../../types/index.ts"
import StatsSection from "../../components/dashboard/StatsSection.vue"
import RecentActivities from "../../components/dashboard/RecentActivities.vue"
import QuickUpload from "../../components/dashboard/QuickUpload.vue"

defineOptions({
  layout: AppLayout,
})

const props = defineProps<{
  user: User
  documentsCount: number
  quizCount: number
  questionsCount: number
  recentDocuments: RecentDocument[]
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
        <Link
          href="/start"
          class="bg-[#3aff8c] text-[#050508] text-xs font-bold px-5 py-2.5 tracking-wider uppercase hover:bg-white transition-colors inline-block"
        >
          New Document
        </Link>
        <button
          class="cursor-pointer border border-[#2a2a30] text-xs text-gray-400 px-5 py-2.5 tracking-wider uppercase hover:border-gray-500 hover:text-gray-200 transition-colors"
        >
          View All
        </button>
      </div>
    </div>

    <StatsSection
      :documents-count="documentsCount"
      :quiz-count="quizCount"
      :questions-count="questionsCount"
    />
  </div>

  <div class="grid grid-cols-12">
    <RecentActivities :recent-documents="recentDocuments" />

    <QuickUpload />
  </div>
</template>
