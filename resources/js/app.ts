import { createApp, h } from "vue"
import { createInertiaApp } from "@inertiajs/vue3"
import "../css/app.css"

document.addEventListener("DOMContentLoaded", () => {
  createInertiaApp({
    id: "app",
    title: (title) => `${title} - Picxam`,
    resolve: (name) => {
      const pages = import.meta.glob("./pages/**/*.vue", { eager: true })
      return pages[`./pages/${name}.vue`] as any
    },
    setup({ el, App, props, plugin }) {
      createApp({ render: () => h(App, props) })
        .use(plugin)
        .mount(el)
    },
    progress: {
      color: "#2cd476",
    },
    defaults: {
      visitOptions: (__, _) => {
        return {
          showProgress: true,
          viewTransition: true,
        }
      },
    },
  })
})
