import { PageProps as InertiaPageProps } from "@inertiajs/core"

declare module "@inertiajs/core" {
  interface PageProps extends InertiaPageProps {
    auth?: {
      user?: {
        name: string
        email: string
      }
    }
    errors?: Record<string, string[]>
    resetKey?: string
  }
}
