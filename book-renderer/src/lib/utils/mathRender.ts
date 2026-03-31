import katex from 'katex';

export function renderMath(text: string): string {
  if (!text) return '';
  
  // Handle double-dollar block math and single-dollar inline math
  return text.replace(/\$\$(.*?)\$\$/gs, (_, math) => {
    try {
      return katex.renderToString(math, { displayMode: true, throwOnError: false });
    } catch (e) {
      return `$$${math}$$`;
    }
  }).replace(/\$(.*?)\$/g, (_, math) => {
    try {
      return katex.renderToString(math, { displayMode: false, throwOnError: false });
    } catch (e) {
      return `$${math}$`;
    }
  });
}
