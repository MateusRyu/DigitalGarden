---
title: Status
tags:
  - v1.1
aliases:
  - Status
created_at: 2024-07-26T13:21:33-03:00
updated_at: 2025-02-07T13:02:58-03:00
---

No [[Toram]], o status é a base matemática para o jogo calcular todas as interações de batalha no jogo, que inclui danos, velocidade de ataque, velocidade de conjuração e entre outros. Os status são os dados que o jogador pode distribuir para cada vez que ele aumentar de nível ou através de recompensas no jogo.

> [!note] Observação
> As informações são baseados no que os jogadores descobriram e alguma informação pode não estar certo!

---

## Calculo do status total
### Regra geral

 - Para todos os casos, o calculo básico sempre segue a ordem: 
	1. Calcula a soma dos modificadores percentual;
	2. Aplica os modificadores percentual;
	3. Arredonda o valor para baixo;
	4. Aplica os modificadores puros.

Por exemplo:
 - Personagem tem 255 de [[Toram_STR|STR]];
 - Armadura tem 8% de [[Toram_STR|STR]];
 - Arma tem -1% de [[Toram_STR|STR]];
 - Buff de comida [[Toram_STR|STR]] +18;

1. Soma dos modificadores percentual = 8% - 1% = 7%
2. Valor com modificadores percentual = 255 * 107% = 272.85
3. Valor arredondado para baixo = 272
4. Valor com modificador puro = 272 + 18 = 290

==STR = 290==

### Status percentual

Alguns status já são valores percentuais (exemplo: [[../09/Toram_Guard_Rate|Guard Rate]], [[../09/Toram_Guard_Power|Guard Power]], [[../09/Toram_Evasion_Rate|Evasion Rate]]). Nesses casos, basta somar todos os valores!

### Calculo final

Alguns status dependem de outros status, então é necessário um calculo na ordem certa! Por exemplo, [[../09/Toram_Critical_Damage|Critical Damage]] é calculado baseado no [[Toram_STR|STR]], então será necessário calcular o [[Toram_STR|STR]] primeiro par poder usar no calculo do [[../09/Toram_Critical_Damage|Critical Damage]].  

Para fins didáticos, os jogadores separaram os status em algumas categorias:
1. [[Toram_Status_basico|Status básicos]]: Aqueles que podem ser adicionados ao aumentar de level;
2. [[../09/Toram_Status_de_equipamento|Status de equipamento]]: ATK da arma, Equipment DEF, Weapon Stability, Refinement Resistance
3. [[../09/Toram_Status_derivados|Status derivados]]: Status que se derivam dos [[Toram_Status_basico|Status básicos]]. 
4. [[../09/Toram_Status não-derivados|Status não-derivados]]: Aqueles obtidos exclusivamente de equipamentos ou habilidade.
5. [[../09/Toram_Status_Especial|Status Especial]]: Status que não se encaixam nas classificações anteriores.

Por exemplo, digamos que queremos calcular o valor de [[../09/Toram_ATK|ATK]] para o usuário da [[../12/Toram_One_Handed_Sword|Espada de uma mão]] Este status é baseada em ([[Toram_Status_basico|Status básicos]]) [[Toram_STR|STR]] e [[../09/Toram_DEX|DEX]] e ([[../09/Toram_Status_de_equipamento|Status de equipamento]]) [[../09/Toram_ATK|ATK]]. Portanto os passos serão os seguintes:
1. Pegue [[Toram_STR|STR]] e [[../09/Toram_DEX|DEX]] originais. Aplique o modificador [[Toram_STR|STR]]% e [[../09/Toram_DEX|DEX]]% a eles.
2. Aplique o modificador plano [[Toram_STR|STR]]+ e [[../09/Toram_DEX|DEX]]+ ao resultado de (1), obtemos [[Toram_STR|STR]] final e [[../09/Toram_DEX|DEX]] final.
3. Pegue o [ATK](content/entrada/2024/07/09/Toram_ATK.md) da arma e calcule seu bônus de refinamento.
4. Pegue o [ATK](content/entrada/2024/07/09/Toram_ATK.md) da arma, aplique o [ATK](content/entrada/2024/07/09/Toram_ATK.md)% da arma e o modificador do [ATK](content/entrada/2024/07/09/Toram_ATK.md)+ da arma a ele.
5. Somando (3) e (4), obtemos o [ATK](content/entrada/2024/07/09/Toram_ATK.md) final da arma.
6. Calcule o [ATK](content/entrada/2024/07/09/Toram_ATK.md) a partir do nível do personagem, resultado de (2) e (5).
7. Aplique [ATK](content/entrada/2024/07/09/Toram_ATK.md)% e [ATK](content/entrada/2024/07/09/Toram_ATK.md)+ em (6), obtemos o [ATK](content/entrada/2024/07/09/Toram_ATK.md) final.

![Toram_status.excalidraw](../../../../../_excalidraw/Toram_status.excalidraw.md)

## Referencia
---
[Coryn Club](https://coryn.club/guide.php?key=status)


