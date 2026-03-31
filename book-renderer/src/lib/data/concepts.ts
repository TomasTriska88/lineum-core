export interface Concept {
  id: string;
  layer?: 'core' | 'enrichment';
  chapterNumber: number;
  chapterTitle: string;
  title: string;
  hook: string;
  explain: string;
  image: {
    path: string;
    prompt: string;
  };
  aha: string;
  proseSegments: {
    label: string;
    body: string;
  }[];
  summary: string;
}
