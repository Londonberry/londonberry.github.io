import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

// Build a URL → lastmod map from blog frontmatter so the sitemap surfaces
// publish dates to crawlers. Reads the content files directly (astro:content
// isn't available in astro.config.mjs).
function buildLastmodMap() {
  const map = new Map();
  const dir = './src/content/blog';
  try {
    for (const file of readdirSync(dir)) {
      if (!file.endsWith('.md')) continue;
      const slug = file.replace(/\.md$/, '');
      const raw = readFileSync(join(dir, file), 'utf8');
      const m = raw.match(/^---\s*\n([\s\S]*?)\n---/);
      if (!m) continue;
      const dateMatch = m[1].match(/^date:\s*(\S+)/m);
      if (!dateMatch) continue;
      const date = new Date(dateMatch[1]);
      if (Number.isNaN(date.getTime())) continue;
      map.set(`https://londonberry.com/blog/${slug}/`, date);
    }
  } catch {
    // Content dir missing at config-load time is fine — sitemap just won't have lastmods.
  }
  return map;
}

const lastmodMap = buildLastmodMap();

export default defineConfig({
  site: 'https://londonberry.com',
  output: 'static',
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/api/'),
      serialize(item) {
        const lm = lastmodMap.get(item.url);
        if (lm) {
          item.lastmod = lm.toISOString();
          item.changefreq = 'monthly';
          item.priority = 0.8;
        } else if (item.url === 'https://londonberry.com/') {
          item.changefreq = 'weekly';
          item.priority = 1.0;
        } else if (item.url.endsWith('/blog/')) {
          item.changefreq = 'weekly';
          item.priority = 0.9;
        } else {
          item.changefreq = 'monthly';
          item.priority = 0.7;
        }
        return item;
      },
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
});
