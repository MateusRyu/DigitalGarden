---
title: PCIe bus error
tags:
  - Entrada
aliases:
  - PCIe bus error
created_at: 2024-08-08T10:18:55-03:00
updated_at: 2025-02-11T00:41:47-03:00
---

`PCIe bus error` é uma mensagem de erro de comunicação com algum periférico. A mensagem em si não costuma  ser para problemas graves e significa apenas que ocorreu alguma pequena falha que pode afetar o comportamento esperado. Entretanto, pode ocorrer que a falta de compatibilidade de algum periférico gere uma sobrecarga de `PCIe bus error` que impede que a máquina execute novas tarefas e travando ela em um looping.

---

## Possíveis soluções

As soluções envolvem editar o arquivo `/etc/default/grub` (necessário ter privilégio de `super user` ou `root`), atualizar o grub (`sudo update-grub`) e reiniciar a máquina.
### Desativando alerta de erros
Adicionar o parâmetro `pci=noaer

```text
 GRUB_CMDLINE_LINUX_DEFAULT="quiet splash pci=noaer"
```

### Desativando o MSI
Para desativar o [MSI](MSI.md), adicione o parâmetro `pci=nomsi`

```text
 GRUB_CMDLINE_LINUX_DEFAULT="quiet splash pci=nomsi"
```

### Desativando o mmconf
Para desativar o [mmconf](mmconf.md), adicione o parâmetro `pci=nommconf`

```text
 GRUB_CMDLINE_LINUX_DEFAULT="quiet splash pci=nommconf"
```
