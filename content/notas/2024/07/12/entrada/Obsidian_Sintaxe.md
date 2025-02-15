---
title: Sintaxe do Obssidian
tags:
  - Entrada
aliases:
  - Sintaxe
created_at: 2024-07-12T19:18:56-03:00
updated_at: 2025-02-14T16:34:25-03:00
---

O obsidian tem uma [Sintaxe](../atomo/Sintaxe.md) baseado no [Markdown](../../08/atomo/Markdown.md) e traz algumas outras extras para auxiliar na conexões dos [Grafos](../atomo/Grafos.md).

---

## Sintaxe

![Cabeçalho](../../08/atomo/Markdown.md#Cabeçalho)

![Lista](../../08/atomo/Markdown.md#Lista)
### Link
#### Link interno
##### Wikilink
```md
[[Nome do documento]]
[[Nome do documento#Cabeçalho da seção]]
[[Nome do documento#^ID_do_Bloco]]
```
##### Markdown
```md
[Nome do documento](Nome%20do%20documento.md)
[Nome do documento](Nome%20do%20documento.md#Cabeçalho%20da%20seção)
[Nome do documento](Nome%20do%20documento.md#^ID_do_bloco)
```

> Observação: É preciso seguir a [Codificação URL](../atomo/Codificação_URL.md) para o caminho de onde está localizado o arquivo que o link se refere!
#### Apelido
```md
[[Nome do documento|apelido usado para exibição do texto]]
[[Nome do documento#Cabeçalho da seção|apelido usado para exibição do texto]]
```

#### Embed
Para incorporar um arquivo no seu vault, adicione um ponto de exclamação (`!`) na frente de um link interno.

##### Imagem
No caso de imagens, é possível redimensionar o tamanho dela ao adicionar `|larguraxaltura`, como por exemplo:

- `![[imagem.png|100x150]]`
- `![Imagem](imagem.png|100x150)`

##### Audio
```
![[track.ogg]]
![track](track.ogg)
```

#### PDF
```md
![[Document.pdf]]
```

É possível especificar um página ao adicionar `#page=N` no final do link, onde `N` é o número da página:

```md
![[Document.pdf#page=3]]
```

Também é possível especificar a largura em [Pixel](../atomo/Pixel.md) para o PDF, adicionando `#height=[number]` no final do link. Por exemplo:

```md
![[Document.pdf#height=400]]
```
#### Lista

```md
- list item 1
- list item 2

^my-list-id
```

```md
![[My note#^my-list-id]]
```
##### Resultado de busca

````md
```query
embed OR search
```
````
