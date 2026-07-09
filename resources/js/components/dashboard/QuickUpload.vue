<template>
  <div class="col-span-12 lg:col-span-5 p-8 lg:p-10">
    <h2 class="text-xs text-gray-400 tracking-widest uppercase mb-4">
      Quick Upload
    </h2>
    <div
      class="border border-dashed border-[#3aff8c]/40 bg-[#3aff8c]/5 p-8 text-center"
    >
      <p class="text-sm text-gray-300 font-medium">Drop file here</p>
      <p
        class="text-[10px] text-gray-600 mt-2 tracking-wider uppercase font-medium"
      >
        PDF PNG JPG
      </p>
    </div>
    <div class="mt-6 border-t border-[#2a2a30] pt-5">
      <p class="text-xs text-gray-500 tracking-wider uppercase mb-3">
        Supported Formats
      </p>
      <div class="grid grid-cols-3 gap-2">
        <div
          class="border border-[#2a2a30] py-2.5 px-3 text-center hover:border-[#3aff8c]/40 transition-colors"
        >
          <span class="text-xs font-semibold text-white block">PDF</span>
          <span class="text-[10px] text-gray-600">Documents</span>
        </div>
        <div
          class="border border-[#2a2a30] py-2.5 px-3 text-center hover:border-[#3aff8c]/40 transition-colors"
        >
          <span class="text-xs font-semibold text-white block">PNG</span>
          <span class="text-[10px] text-gray-600">Images</span>
        </div>
        <div
          class="border border-[#2a2a30] py-2.5 px-3 text-center hover:border-[#3aff8c]/40 transition-colors"
        >
          <span class="text-xs font-semibold text-white block">JPG</span>
          <span class="text-[10px] text-gray-600">Images</span>
        </div>
      </div>
      <div class="mt-3 flex items-center gap-2 text-[10px] text-gray-600">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="w-3 h-3 shrink-0"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="1.5"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="m18.375 12.739-7.693 7.693a4.5 4.5 0 0 1-6.364-6.364l10.94-10.94A3 3 0 1 1 19.5 7.372L8.552 18.32a1.5 1.5 0 0 1-2.122-2.122l10.94-10.94"
          />
        </svg>
        <span>Max file size: 10MB</span>
      </div>
    </div>
  </div>
</template>
