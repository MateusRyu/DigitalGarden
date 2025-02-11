---
title: Roam Research Compatibility
tags:
  - feature/transformer
created_at: 2025-01-30T22:12:02-03:00
updated_at: 2025-02-03T23:53:52-03:00
---

[Roam Research](https://roamresearch.com) is a note-taking tool that organizes your knowledge graph in a unique and interconnected way.

Quartz supports transforming the special Markdown syntax from Roam Research (like `{{[[components]]}}` and other formatting) into
regular Markdown via the [[../plugins/RoamFlavoredMarkdown]] plugin.

```typescript title="quartz.config.ts"
plugins: {
  transformers: [
    // ...
    Plugin.RoamFlavoredMarkdown(),
    Plugin.ObsidianFlavoredMarkdown(),
    // ...
  ],
},
```

> [!warning]
> As seen above placement of `Plugin.RoamFlavoredMarkdown()` within `quartz.config.ts` is very important. It must come before `Plugin.ObsidianFlavoredMarkdown()`.

## Customization

This functionality is provided by the [[../plugins/RoamFlavoredMarkdown]] plugin. See the plugin page for customization options.
