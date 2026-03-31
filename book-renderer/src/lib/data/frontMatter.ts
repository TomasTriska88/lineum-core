import { level1Concepts } from './concepts';

export const frontMatter = {
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
};
