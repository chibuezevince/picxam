export const verifyEmailForm = {
  code: '',
  error: '',
  verifying: false,
  resending: false,
  resent: false,
}

export const navItems = [
  { icon: '◈', label: 'Dashboard', route: '/dashboard' },
  { icon: '+', label: 'New', action: 'new' },
  { icon: '≡', label: 'Docs', route: '/documents' },
  { icon: '⚙', label: 'Settings', route: '/settings' },
  { icon: '⏏', label: 'Sign Out', action: 'logout', color: 'red' },
]

export const loadingLogo = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32" width="56" height="64"><style>@keyframes wave{0%,100%{transform:translateY(0) rotate(25deg)}50%{transform:translateY(-10px) rotate(25deg)}}.bar{animation:wave 1s ease-in-out infinite;transform-origin:left center}.b2{animation-delay:0.15s}.b3{animation-delay:0.3s}.b4{animation-delay:0.45s}</style><rect class="bar b1" x="4" y="2" width="3" height="24" fill="#3aff8c" transform="rotate(25 4 2)"/><rect class="bar b2" x="9" y="2" width="3" height="24" fill="#3aff8c" transform="rotate(25 9 2)"/><rect class="bar b3" x="14" y="2" width="3" height="24" fill="#3aff8c" transform="rotate(25 14 2)"/><rect class="bar b4" x="19" y="2" width="3" height="24" fill="#3aff8c" transform="rotate(25 19 2)"/></svg>`
