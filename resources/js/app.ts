import { createApp, h } from "vue"
import { createInertiaApp } from "@inertiajs/vue3"
import { Confirm, Loading } from "notiflix"
import "../css/app.css"

Loading.init({
  backgroundColor: "rgba(0,0,0,0.6)",
  svgColor: "#3aff8c",
  svgSize: "45px",
  cssAnimation: true,
  cssAnimationDuration: 300,
  messageMaxLength: 60,
  messageColor: "#d1d5db",
  fontFamily: "Poppins, system-ui, sans-serif",
})

Confirm.init({
  width: "360px",
  backgroundColor: "#0a0a0f",
  borderRadius: "0",
  backOverlay: true,
  backOverlayColor: "rgba(0,0,0,0.7)",
  fontFamily: "Poppins, system-ui, sans-serif",
  cssAnimation: true,
  cssAnimationDuration: 250,
  cssAnimationStyle: "zoom",
  titleColor: "#3aff8c",
  titleFontSize: "15px",
  messageColor: "#d1d5db",
  buttonsFontSize: "12px",
  okButtonColor: "#050508",
  okButtonBackground: "#3aff8c",
  cancelButtonColor: "#9ca3af",
  cancelButtonBackground: "#1a1a20",
})

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
