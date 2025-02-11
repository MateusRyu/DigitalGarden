---
title: CNAME
tags:
  - plugin/emitter
created_at: 2025-01-30T22:12:02-03:00
updated_at: 2025-02-02T13:45:06-03:00
---

This plugin emits a `CNAME` record that points your subdomain to the default domain of your site.

If you want to use a custom domain name like `quartz.example.com` for the site, then this is needed.

See [[hosting|Hosting]] for more information.

> [!note]
> For information on how to add, remove or configure plugins, see the [[../configuration#Plugins|Configuration]] page.

This plugin has no configuration options.

## API

- Category: Emitter
- Function name: `Plugin.CNAME()`.
- Source: [`quartz/plugins/emitters/cname.ts`](https://github.com/jackyzha0/quartz/blob/v4/quartz/plugins/emitters/cname.ts).
