---
title: Backlinks
tags:
  - component
created_at: 2025-01-30T22:12:02-03:00
updated_at: 2025-01-27T20:46:41-03:00
---

A backlink for a note is a link from another note to that note. Links in the backlink pane also feature rich [[popover previews]] if you have that feature enabled.

## Customization

- Removing backlinks: delete all usages of `Component.Backlinks()` from `quartz.layout.ts`.
- Hide when empty: hide `Backlinks` if given page doesn't contain any backlinks (default to `true`). To disable this, use `Component.Backlinks({ hideWhenEmpty: false })`.
- Component: `quartz/components/Backlinks.tsx`
- Style: `quartz/components/styles/backlinks.scss`
- Script: `quartz/components/scripts/search.inline.ts`
