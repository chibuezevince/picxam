export const getCookie = (name: string) => {
  const value = `; ${document.cookie}`
  const parts = value.split(`; ${name}=`)
  if (parts.length === 2) return parts.pop()?.split(";").shift()
  return null
}
export const renderMarkdown = (text: string): string => {
  const escape = (s: string) =>
    s
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")

  // 1. Pull out fenced code blocks first so nothing inside them gets
  //    touched by later inline rules (bold/italic/links/etc).
  const codeBlocks: string[] = []
  let working = text.replace(/```(\w*)\n?([\s\S]*?)```/g, (_m, _lang, code) => {
    const idx = codeBlocks.length
    codeBlocks.push(`<pre><code>${escape(code.replace(/\n$/, ""))}</code></pre>`)
    return `\u0000CODEBLOCK${idx}\u0000`
  })

  // 2. Escape everything else.
  working = escape(working)

  // 3. Inline rules (order matters: images before links, bold before italic).
  const applyInline = (line: string): string =>
    line
      .replace(/!\[([^\]]*)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)/g, (_m, alt, src, title) =>
        `<img src="${src}" alt="${alt}"${title ? ` title="${title}"` : ""}>`
      )
      .replace(/\[([^\]]+)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)/g, (_m, label, href, title) =>
        `<a href="${href}"${title ? ` title="${title}"` : ""} target="_blank" rel="noopener noreferrer">${label}</a>`
      )
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*\*([^*]+)\*\*\*/g, "<strong><em>$1</em></strong>")
      .replace(/___([^_]+)___/g, "<strong><em>$1</em></strong>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/__([^_]+)__/g, "<strong>$1</strong>")
      .replace(/~~([^~]+)~~/g, "<del>$1</del>")
      .replace(/\*([^*\n]+)\*/g, "<em>$1</em>")
      .replace(/(^|[^\w])_([^_\n]+)_(?!\w)/g, "$1<em>$2</em>")

  // 4. Block-level parsing, line by line, so lists/blockquotes/headers
  //    get proper wrapping elements instead of leaking raw <li>/<blockquote>.
  const lines = working.split("\n")
  const html: string[] = []

  type ListState = { type: "ul" | "ol"; indent: number }
  const listStack: ListState[] = []

  const closeListsTo = (indent: number) => {
    while (listStack.length && listStack[listStack.length - 1].indent >= indent) {
      html.push(`</${listStack.pop()!.type}>`)
    }
  }
  const closeAllLists = () => closeListsTo(-1)

  let inBlockquote = false
  let paragraphBuffer: string[] = []

  const flushParagraph = () => {
    if (paragraphBuffer.length) {
      html.push(`<p>${paragraphBuffer.map(applyInline).join("<br>")}</p>`)
      paragraphBuffer = []
    }
  }

  for (const raw of lines) {
    const line = raw

    // Placeholder code block lines pass straight through.
    const codeMatch = line.match(/^\u0000CODEBLOCK(\d+)\u0000$/)
    if (codeMatch) {
      flushParagraph()
      closeAllLists()
      if (inBlockquote) {
        html.push("</blockquote>")
        inBlockquote = false
      }
      html.push(codeBlocks[Number(codeMatch[1])])
      continue
    }

    // Horizontal rule
    if (/^\s*(-{3,}|\*{3,}|_{3,})\s*$/.test(line)) {
      flushParagraph()
      closeAllLists()
      if (inBlockquote) {
        html.push("</blockquote>")
        inBlockquote = false
      }
      html.push("<hr>")
      continue
    }

    // Headers
    const headerMatch = line.match(/^(#{1,6})\s+(.*)$/)
    if (headerMatch) {
      flushParagraph()
      closeAllLists()
      if (inBlockquote) {
        html.push("</blockquote>")
        inBlockquote = false
      }
      const level = headerMatch[1].length
      html.push(`<h${level}>${applyInline(headerMatch[2])}</h${level}>`)
      continue
    }

    const quoteMatch = line.match(/^\s*>\s?(.*)$/)
    if (quoteMatch) {
      flushParagraph()
      closeAllLists()
      if (!inBlockquote) {
        html.push("<blockquote>")
        inBlockquote = true
      }
      html.push(`<p>${applyInline(quoteMatch[1])}</p>`)
      continue
    } else if (inBlockquote) {
      html.push("</blockquote>")
      inBlockquote = false
    }

    const ulMatch = line.match(/^(\s*)([-*+])\s+(.*)$/)
    const olMatch = line.match(/^(\s*)(\d+)\.\s+(.*)$/)

    if (ulMatch || olMatch) {
      flushParagraph()
      const [, indentStr, , content] = (ulMatch ?? olMatch)!
      const indent = indentStr.length
      const type: "ul" | "ol" = ulMatch ? "ul" : "ol"

      closeListsTo(indent + 1)
      const top = listStack[listStack.length - 1]

      if (!top || top.indent < indent) {
        html.push(`<${type}>`)
        listStack.push({ type, indent })
      } else if (top.type !== type && top.indent === indent) {
        html.push(`</${top.type}>`)
        listStack.pop()
        html.push(`<${type}>`)
        listStack.push({ type, indent })
      }

      html.push(`<li>${applyInline(content)}</li>`)
      continue
    } else {
      closeAllLists()
    }

    if (line.trim() === "") {
      flushParagraph()
      continue
    }

    paragraphBuffer.push(line)
  }

  flushParagraph()
  closeAllLists()
  if (inBlockquote) html.push("</blockquote>")

  return html.join("\n")
}