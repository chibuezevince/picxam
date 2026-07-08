export const verifyEmailForm = {
  code: "",
  error: "",
  verifying: false,
  resending: false,
  resent: false,
}

export const navItems = [
  { icon: "+", label: "New", action: "new" },
  { icon: "≡", label: "Docs", route: "/documents" },
  { icon: "?", label: "Questions", route: "/questions" },
  { icon: "⚙", label: "Settings", route: "/settings" },
  { icon: "⏏", label: "Sign Out", action: "logout" },
]
