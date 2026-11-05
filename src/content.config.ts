import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    updated: z.date().optional(),
    author: z.string().default('Ben McDonald'),
    image: z.string().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

// Case studies. Client names live only in `client`, so a name swaps in with
// one line. `approved` is Ben's sign-off: unapproved entries build only in
// preview builds (PREVIEW=1), never in the production site.
const work = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/work' }),
  schema: z.object({
    headline: z.string(),
    client: z.string(),
    clientUrl: z.string().url().optional(),
    summary: z.string(),
    track: z.enum(['production', 'sports']),
    order: z.number(),
    stack: z.array(z.string()).default([]),
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    approved: z.boolean().default(false),
  }),
});

export const collections = { blog, work };
