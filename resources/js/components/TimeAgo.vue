<script setup lang="ts">
import { useTimeAgo } from "@vueuse/core"

const props = defineProps<{
  date: string
}>()

const timeAgo = useTimeAgo(() => props.date)
</script>

<template>
  <span>{{ timeAgo }}</span>
</template>
