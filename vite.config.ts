import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"
import tailwindcss from "@tailwindcss/vite"

export default defineConfig({
  base: "/static/",
  plugins: [vue(), tailwindcss()],
  server: {
    origin: "http://localhost:5173",
  },
  build: {
    outDir: "core/static/dist",
    manifest: true,
    rollupOptions: {
      input: "resources/js/app.ts",
    },
  },
})
