---
title: Meu Computador
tags:
  - Mapa
aliases:
  - Meu Computador
created_at: 2024-07-26T13:21:33-03:00
updated_at: 2025-02-14T16:02:59-03:00
---

Dual boot com a [Pasta home](../notas/2024/07/14/atomo/Pasta_home.md) compartilhada para ter um [Sistema Operacional](../notas/2024/08/04/atomo/Sistema_Operacional.md) de backup pra caso algo dê errado no [Sistema Operacional](../notas/2024/08/04/atomo/Sistema_Operacional.md) principal. Ele apresenta o [PCIe bus error](../notas/2024/08/08/entrada/PCIe_bus_error.md).

---

## Particionamento
- `sda1`: `/boot/efi`
- `sda2`: `/` (~~[Crystal_Linux](../notas/2024/08/10/entrada/Crystal_Linux.md)~~ [Zorin OS](../../Zorin%20OS.md))
- `sda3`: `/` ([NixOS](../notas/2025/02/14/entrada/NixOS.md))
- `sda4`: [SWAP](../notas/2024/07/14/atomo/SWAP.md)
-  `sda6`: `/home` 

## Crystal
- [Gnome](../notas/2024/08/10/entrada/Gnome.md)
- [Hyprland](../notas/2024/08/10/entrada/Hyprland.md)
	- Barra de status: [Waybar](../notas/2024/08/11/entrada/Waybar.md)
	- Notificação: [SwayNotificationCenter](../notas/2024/08/10/entrada/SwayNotificationCenter.md)
	- Wallpapers: [sww](../notas/2024/08/12/entrada/sww.md)
	- App launchers: [tofi](../notas/2024/08/11/entrada/tofi.md)
	- Color pickers: [Hyprpicker](../notas/2024/08/11/entrada/Hyprpicker.md)
	- Pipewire: [pipewire](../notas/2024/08/11/entrada/pipewire.md) e [wireplumber](../notas/2024/08/11/entrada/wireplumber.md)
	- Hyprland Desktop Portal: 
		- [xdg-desktop-portal-wlr](../notas/2024/08/11/entrada/xdg_desktop_portal_wlr.md)
		- [xdg-desktop-portal-hyprland](../notas/2024/08/11/entrada/xdg_desktop_portal_hyprland.md)
		- [xdg-desktop-portal-gtk](../notas/2024/08/11/entrada/xdg_desktop_portal_gtk.md)
	- Authentication Agent: [polkit_kde_agent](../notas/2024/08/11/entrada/polkit_kde_agent.md)
	- Qt [Wayland](../notas/2024/08/17/entrada/Wayland.md) Support: [qt5_wayland](../notas/2024/08/11/entrada/qt5_wayland.md) e [qt6-wayland](../notas/2024/08/11/entrada/qt6_wayland.md)