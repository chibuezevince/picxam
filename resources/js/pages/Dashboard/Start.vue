<script setup lang="ts">
import { Head, useForm, usePage } from "@inertiajs/vue3"
import AppLayout from "../../layouts/AppLayout.vue"
import { ref, computed } from "vue"
import { useFileDialog } from "@vueuse/core"
import { toast } from "vue-sonner"
import type { QuizGenerationForm } from "../../types/index.ts"
import QuizTypeButton from "../../components/start/QuizTypeButton.vue"
import {
  ArrowUpTrayIcon,
  BoltIcon,
  DocumentTextIcon,
  ExclamationTriangleIcon,
  XMarkIcon,
} from "@heroicons/vue/24/outline"
import FormBadge from "../../components/form/FormBadge.vue"
import Button from "../../components/Button.vue"

const { open, onChange } = useFileDialog({
  accept: ".docx,.pptx,.pdf",
})

const allowedFileTypes: string[] = usePage().props
  .accepted_file_types as string[]

const form = useForm<QuizGenerationForm>({
  document: null,
  quiz_type: "mcq",
})

const appendFile = (uploadedFile: File) => {
  const splitName = uploadedFile.name.split(".")
  if (
    splitName?.length &&
    !allowedFileTypes.includes(`${splitName[splitName.length - 1]}`)
  ) {
    toast.error("Invalid file type", {
      position: "bottom-left",
    })
    return
  }
  form.document = uploadedFile
}

onChange((selected) => {
  if (!selected?.[0]) return
  return appendFile(selected[0])
})

defineOptions({ layout: AppLayout })

const dragOver = ref(false)

const formattedFileTypes = computed(() =>
  allowedFileTypes
    .map((t) => t.replace(".", "").toUpperCase())
    .join(" &middot; "),
)

const onDragOver = (e: DragEvent) => {
  e.preventDefault()
  dragOver.value = true
}

const onDragLeave = () => (dragOver.value = false)

const onDrop = (e: DragEvent) => {
  e.preventDefault()
  dragOver.value = false
  const dropped = e.dataTransfer?.files[0]
  if (!dropped) return
  return appendFile(dropped)
}

const submit = () => form.post("/start")

const removeFile = () => (form.document = null)

const fileSize = computed(() => {
  if (!form.document) return ""
  const mb = form.document.size / 1024 / 1024
  return mb >= 1
    ? `${mb.toFixed(1)} MB`
    : `${Math.round(form.document.size / 1024)} KB`
})
</script>

<template>
  <Head title="Start" />

  <div class="flex-1 flex p-0">
    <div
      class="w-full grid grid-cols-1 md:grid-cols-5 divide-y md:divide-y-0 md:divide-x divide-[#2a2a30]"
    >
      <div
        class="md:col-span-3 flex flex-col items-center justify-center p-8 md:p-12 lg:p-16 min-h-80 md:min-h-0 relative"
        @dragover="onDragOver"
        @dragleave="onDragLeave"
        @drop="onDrop"
      >
        <div
          class="absolute top-6 left-6 w-6 h-6 border-t-2 border-l-2 border-[#3aff8c]/30 pointer-events-none"
        />
        <div
          class="absolute top-6 right-6 w-6 h-6 border-t-2 border-r-2 border-[#3aff8c]/30 pointer-events-none"
        />
        <div
          class="absolute bottom-6 left-6 w-6 h-6 border-b-2 border-l-2 border-[#3aff8c]/30 pointer-events-none"
        />
        <div
          class="absolute bottom-6 right-6 w-6 h-6 border-b-2 border-r-2 border-[#3aff8c]/30 pointer-events-none"
        />

        <div
          v-if="!form.document"
          class="relative w-full cursor-pointer group"
          @click="open()"
        >
          <div
            class="border-2 bg-transparent transition-all duration-300 p-12 md:p-16 text-center"
            :class="[
              dragOver
                ? 'border-[#3aff8c] bg-[#3aff8c]/5'
                : 'border-[#2a2a30] group-hover:border-[#3aff8c]/50',
            ]"
          >
            <div class="mb-6">
              <div
                class="w-12 h-12 mx-auto border-2 flex items-center justify-center transition-all duration-300"
                :class="[
                  dragOver
                    ? 'border-[#3aff8c] bg-[#3aff8c]/10'
                    : 'border-[#2a2a30] group-hover:border-[#3aff8c]/30',
                ]"
              >
                <ArrowUpTrayIcon
                  class="w-5 h-5 transition-colors duration-300"
                  :class="
                    dragOver
                      ? 'text-[#3aff8c]'
                      : 'text-gray-500 group-hover:text-[#3aff8c]'
                  "
                />
              </div>
            </div>
            <p
              class="text-xs text-gray-400 uppercase tracking-[0.15em] font-medium"
            >
              <span class="text-white font-semibold">Select</span> or drop
              document
            </p>
            <p
              class="text-[10px] text-gray-600 mt-3 uppercase tracking-[0.12em]"
            >
              <span v-html="formattedFileTypes"></span> - 10MB max
            </p>
          </div>
        </div>

        <div
          v-else
          class="w-full border-2 border-[#2a2a30] bg-[#0a0a0f] p-5"
        >
          <div class="flex items-center gap-4">
            <div
              class="w-12 h-12 border-2 border-[#3aff8c]/30 bg-[#3aff8c]/5 flex items-center justify-center shrink-0"
            >
              <DocumentTextIcon class="size-4 text-[#3aff8c]" />
            </div>
            <div class="min-w-0 flex-1">
              <p class="text-sm font-medium text-white truncate">
                {{ form.document.name }}
              </p>
              <p class="text-[11px] text-gray-500 mt-0.5 tracking-wider">
                {{ fileSize }}
              </p>
            </div>
            <button
              @click="removeFile"
              class="w-8 h-8 border-2 border-[#2a2a30] flex items-center justify-center text-gray-500 hover:text-white hover:border-gray-500 transition-colors shrink-0"
            >
              <XMarkIcon class="w-4 h-4" />
            </button>
          </div>
        </div>
        <FormBadge
          :show="!!form.errors.document"
          type="error"
          class="self-start mt-3"
        >
          {{ form.errors.document }}
        </FormBadge>
      </div>

      <div class="md:col-span-2 flex flex-col p-8 md:p-10 lg:p-12">
        <div class="mb-6">
          <div class="border-2 border-[#3aff8c]/20 bg-[#3aff8c]/5 p-4">
            <p
              class="text-[10px] text-[#3aff8c]/90 uppercase tracking-[0.12em] font-medium"
            >
              4 Questions Per Image
            </p>
            <p class="text-xs text-gray-400 mt-1.5 leading-relaxed">
              Each extracted image from your document will generate 4 questions
              automatically.
            </p>
          </div>
        </div>

        <div class="mb-10">
          <span
            class="text-[10px] text-gray-500 uppercase tracking-[0.15em] font-medium block mb-4"
            >Quiz Type</span
          >
          <div class="grid grid-cols-2 gap-0 border-2 border-[#2a2a30]">
            <QuizTypeButton
              value="mcq"
              label="MCQ"
              :active="form.quiz_type == 'mcq'"
              @select="form.quiz_type = $event"
            />
            <QuizTypeButton
              value="open-ended"
              label="Open-Ended"
              :active="form.quiz_type == 'open-ended'"
              @select="form.quiz_type = $event"
            />
          </div>
          <p class="text-[9px] text-gray-600 mt-2 tracking-wider uppercase">
            {{ form.quiz_type === "mcq" ? "Multiple Choice" : "Open-Ended" }}
          </p>
          <FormBadge
            :show="!!form.errors.quiz_type"
            type="error"
            class="mt-3"
          >
            {{ form.errors.quiz_type }}
          </FormBadge>
        </div>

        <div
          class="mt-auto border-2 border-amber-500/20 bg-amber-500/3 p-4 mb-6"
        >
          <div class="flex items-start gap-3">
            <ExclamationTriangleIcon class="text-amber-400 size-4" />
            <div>
              <p
                class="text-[10px] text-amber-400/90 uppercase tracking-[0.12em] font-medium"
              >
                Document-Based Generation
              </p>
              <p class="text-[10px] text-amber-400/50 mt-1.5 leading-relaxed">
                Questions are generated from uploaded documents. One file at a
                time. Ensure documents are readable and well-formatted.
              </p>
            </div>
          </div>
        </div>

        <Button
          :disabled="!form.document"
          :loading="form.processing"
          hide-arrow
          @click.prevent="submit"
        >
          <BoltIcon class="w-3.5 h-3.5" />
          {{ form.document ? "Generate" : "Select a File" }}
        </Button>
      </div>
    </div>
  </div>
</template>
