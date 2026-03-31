import { level1Concepts } from './books/foundations';
import { level2Concepts } from './books/motion';
import { level3Concepts } from './books/structure';

export type BookData = {
  id: string;
  frontMatter: {
    title: string;
    subtitle: string;
    imprint: {
      publisher: string;
      copyright: string;
      license: string;
      isbn: string;
    };
    preface: {
      hook: string;
      howToUse: string;
    };
    toc: { number: number; chapter: string; title: string }[];
  };
  concepts: any[]; // Using any for simplicity in routing
  theme: {
    primaryColor: string;
    accentColor: string;
  };
};

export const books: Record<string, BookData> = {
  'foundations': {
    id: 'foundations',
    frontMatter: {
      title: "Foundations",
      subtitle: "A Simple Way to Finally Understand Math Through Shapes",
      imprint: {
        publisher: "Lineum",
        copyright: "© 2026 Tomáš Tříska. All rights reserved.",
        license: "Released under AGPLv3 for code / CC-BY-4.0 for whitepapers.",
        isbn: "978-0-00-000000-0"
      },
      preface: {
        hook: "Imagine sitting in a classroom, staring at a blackboard full of abstract letters. You are told to memorize rules, move variables around, and cross out numbers. School treats math like a rigid code you must obey. But what if you could see the math instead? In this book, we translate abstract math into visual shapes. You won't memorize formulas. You will visualize blocks snapping together and structures stretching. Math makes perfect sense when you watch it happen.",
        howToUse: "Treat this book like a mental sandbox. Read the scenario at the start of each idea. Close your eyes and visualize the shape. Check the image description to anchor your imagination. Read the 'Aha Moment' to lock the concept into memory. Discover the practical steps and the pure geometry governing each rule."
      },
      toc: level1Concepts.map(c => ({
        number: c.chapterNumber,
        chapter: c.chapterTitle,
        title: c.title
      }))
    },
    concepts: level1Concepts,
    theme: {
      primaryColor: '#0EA5E9',
      accentColor: '#8B5CF6'
    }
  },
  'motion': {
    id: 'motion',
    frontMatter: {
      title: "Motion",
      subtitle: "A Visual Language for Calculus and Change",
      imprint: {
        publisher: "Lineum",
        copyright: "© 2027 Tomáš Tříska. All rights reserved.",
        license: "Released under AGPLv3 for code / CC-BY-4.0 for whitepapers.",
        isbn: "978-0-00-000000-2"
      },
      preface: {
        hook: "Calculus is usually taught as abstract equations measuring invisible speeds. But motion is inherently visual. What happens when you track change entirely through expanding shapes and bending curves?",
        howToUse: "Observe how variables warp geometries over time."
      },
      toc: level2Concepts.map(c => ({
        number: c.chapterNumber,
        chapter: c.chapterTitle,
        title: c.title
      }))
    },
    concepts: level2Concepts,
    theme: {
      primaryColor: '#F59E0B',
      accentColor: '#10B981'
    }
  },
  'structure': {
    id: 'structure',
    frontMatter: {
      title: "Structure",
      subtitle: "Geometric Foundations of Physics and Systems",
      imprint: {
        publisher: "Lineum",
        copyright: "© 2028 Tomáš Tříska. All rights reserved.",
        license: "Released under AGPLv3 for code / CC-BY-4.0 for whitepapers.",
        isbn: "978-0-00-000000-3"
      },
      preface: {
        hook: "Once you can describe numbers as blocks and motion as folding fields, you can build universes. This book applies visual mathematics to the physical rules holding our reality together.",
        howToUse: "Look at the tension and equilibrium in the diagrams."
      },
      toc: level3Concepts.map(c => ({
        number: c.chapterNumber,
        chapter: c.chapterTitle,
        title: c.title
      }))
    },
    concepts: level3Concepts,
    theme: {
      primaryColor: '#8B5CF6',
      accentColor: '#EC4899'
    }
  }
};
