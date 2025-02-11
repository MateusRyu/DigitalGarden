---
title: 2024-06-30-Header_HTTP
tags:
  - Átomo
aliases:
  - Header HTTP
draft: true
created_at: 2024-07-05T21:29:10-03:00
updated_at: 2025-02-08T21:54:06-03:00
---

Permitir acesso de uma porta especifica:
`Access-Control-Allow-Origin: http://localhost:3000/`

É possível permitir o acesso de qualquer origem utilizando do símbolo **asterisco**, veja a seguir:

`Access-Control-Allow-Origin: *`

Isso não é uma medida recomendada pois permite que origens desconhecidas acessem o servidor, a não ser que seja intencional como no caso de uma API pública.