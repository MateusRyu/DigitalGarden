---
title: Obsidian Compatibility
tags:
  - feature/transformer
created_at: 2025-01-30T22:12:02-03:00
updated_at: 2025-02-03T23:53:52-03:00
---

Quartz was originally designed as a tool to publish Obsidian vaults as websites. Even as the scope of Quartz has widened over time, it hasn't lost the ability to seamlessly interoperate with Obsidian.

By default, Quartz ships with the [[../plugins/ObsidianFlavoredMarkdown]] plugin, which is a transformer plugin that adds support for [Obsidian Flavored Markdown](https://help.obsidian.md/Editing+and+formatting/Obsidian+Flavored+Markdown). This includes support for features like [[wikilinks]] and [[Mermaid diagrams]].

It also ships with support for [frontmatter parsing](https://help.obsidian.md/Editing+and+formatting/Properties) with the same fields that Obsidian uses through the [[../plugins/Frontmatter]] transformer plugin.

Finally, Quartz also provides [[../plugins/CrawlLinks]] plugin, which allows you to customize Quartz's link resolution behaviour to match Obsidian.

## Configuration

This functionality is provided by the [[../plugins/ObsidianFlavoredMarkdown]], [[../plugins/Frontmatter]] and [[../plugins/CrawlLinks]] plugins. See the plugin pages for customization options.
