---
title: Golang
tags:
  - Átomo
aliases:
  - Golang
  - Go
  - Go Language
draft: false
created_at: 2026-06-21T19:17:27-03:00
updated_at: 2025-02-14T16:03:32-03:00
---
Golang ou simplesmente Go é uma [linguagem de programação](../../../../2024/07/08/atomo/Linguagem_de_programacao.md) desenvolvida pela [Google](../entrada/Google.md). A linguagem foi criado após a existência de [processadores](Processador.md) de múltiplos núcleos e se aproveita dessas tecnologias. Ela se propõe a ser uma linguagem com alta performance (como as linguagens de baixo nível) e fácil de se programar (como as linguagens de alto nível).

---

## Origem
Ele foi desenvolvido por [Ken Thompson](../entrada/Ken%20Thompson.md), [Rob Pike](../entrada/Rob%20Pike.md), e [Robert Griesemer](../entrada/Robert%20Griesemer.md) em 2006. Nessa época, não existia uma [linguagem de programação](../../../../2024/07/08/atomo/Linguagem_de_programacao.md) que fosse rápida (para compilar e para executar) e fácil de programar. Sendo assim, ela tem o objetivo de permitir resolver problemas complexos com alta permanence, de uma forma mais simples para os programadores.

## Detalhes técnicos
- Linguagem compilada
- Tipagem forte e estática
- Tem pouquíssimas palavras reservadas

## Quando usar Go
- Serviços que precisa de escalar
- Serviços web, redes, servers (machine learning, image processing, crypto, ...) 
- Quando precisar de uma linguagem rápida, simples, fácil de aprender, e fácil de usar. 

## Exemplos de uso
- APIs
- CLIs
- microservices
- libraries/framework
- processamento de dados
- É a base dos serviços de cloud e orquestração de containers.

## Estrutura básica
Go sempre vai buscar a função `main` do pacote `main` para ser executado. Exemplo:

```go
package main

func main() {
	// code...
}
```

## Fontes
https://go.dev/doc/faq#creating_a_new_language