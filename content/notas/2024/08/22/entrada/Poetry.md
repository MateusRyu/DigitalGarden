---
title: Poetry
tags:
  - Entrada
aliases:
  - Poetry
draft: true
created_at: 2024-08-22T11:58:26-03:00
updated_at: 2025-02-14T16:30:42-03:00
---

Poetry é um [Gerenciador_de_dependencias](../../../../2025/02/14/atomo/Gerenciador_de_dependencias.md) e um [empacotador](../../../../2025/02/14/atomo/Empacotador.md) de projetos [Python](../../../07/09/atomo/Linguagem_Python.md). 

---

[Site oficial](https://python-poetry.org)

## Iniciando projeto

Se estiver começando do zero, execute o seguinte comando para criar a pasta com os arquivos básicos pra iniciar o projeto:
```sh
poetry new [Nome_do_projeto]
```

## Inicializar o poetry em um projeto 

Se já tiver uma pasta com o projeto, pode usar o seguinte comando pra inicializar o `Poetry` dentro da pasta:

```sh
cd Nome_do_projetoq
poetry init
```

## Adicionar pacotes

```sh 
# poetry add --group [Nome_do_grupo] [Nome_do_pacote]
poetry add --group dev pytest
poetry add --group doc mkdocs-material
```

## Iniciar o ambiente virtual

```sh
poetry shell
```