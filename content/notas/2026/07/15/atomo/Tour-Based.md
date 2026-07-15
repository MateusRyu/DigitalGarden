---
title: Tour-Based
tags:
  - Átomo
aliases:
  - Tour-Based
draft: false
created_at: 2026-07-15T20:12:55-03:00
updated_at: 2025-02-14T16:03:32-03:00
---
Tour-Based (ou Testes baseados em Roteiros/Passeios) é uma das abordagens do [Teste exploratório](Teste%20exploratório.md). Ela utiliza a metáfora de uma viagem turística dar estrutura, foco e direção à exploração. O objetivo é evitar que o teste vire uma "andança sem ruma" ([Teste ad-hoc](Teste%20ad-hoc.md)), fornecendo um tema ou lente específica para o testador guiar as suas ações.

---

## Roteiros
### Feature Tour
Feature Tour é um roteiro focado em mapear, conhecer e interagir com as principais funcionalidades e elementos de interface do sistema ([SUT](System%20Under%20Test.md)). Ela explora o produto e fornece uma descrição concisa de como a funcionalidade funciona e qual problema ela resolve. 

Primeiramente, é feita um levantamento dos recursos e comportamentos do [software](../../../../2024/07/26/atomo/Software.md), então mapeado a interface dele e o fluxo básico do usuário para que depois possa testar as funcionalidade em profundidade.

### Transaction Tour
Uma transação é uma tarefa do começo ao fim. Portanto, esse roteiro foca em garantir que todos os passos de um processo estejam funcionando corretamente, tanto individualmente quanto em conjunto. Além disso, é avaliado se a experiência do usuário final seja fluida e coerente. Ela é útil para verificar a integridade dos processos de negócio e se está ocorrendo o gerenciamento dos dados corretamente ao longo das operações do roteiro.

Ela pode avaliar diversas funcionalidades de um [software](../../../../2024/07/26/atomo/Software.md) e percorrer mais de um caminho de cada uma delas. Dessa forma, ela identifica o que pode ser feito no sistema (a transação) e quais são os comandos ou funcionalidades do sistema. 