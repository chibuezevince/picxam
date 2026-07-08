export const setFlash = (key: string, value: unknown) => {
  sessionStorage.setItem(key, JSON.stringify(value))
}

export const getFlash = <T = unknown>(key: string): T | null => {
  const raw = sessionStorage.getItem(key)
  if (raw === null) return null
  return JSON.parse(raw) as T
}

export const pullFlash = <T = unknown>(key: string): T | null => {
  const value = getFlash<T>(key)
  if (value !== null) sessionStorage.removeItem(key)
  return value
}

export const removeFlash = (key: string) => sessionStorage.removeItem(key)
