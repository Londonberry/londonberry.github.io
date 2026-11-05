import { getCollection, type CollectionEntry } from 'astro:content';

// Ben signs off on every client feature before it goes live. Production builds
// only include approved case studies; a preview build (PREVIEW=1) shows drafts.
export const isPreview = import.meta.env.PREVIEW === '1' || process.env.PREVIEW === '1';

export async function getCaseStudies(): Promise<CollectionEntry<'work'>[]> {
  const all = await getCollection('work');
  return all
    .filter((entry) => isPreview || entry.data.approved)
    .sort((a, b) => a.data.order - b.data.order);
}
