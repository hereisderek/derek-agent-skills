---
name: hosts
description: Infrastructure and host connection directory for Derek's Home Proxmox VE and Oracle Cloud environments. Use when asked to connect to, inspect, run commands on, or check ports/services for any host, LXC container, or VM (pve, saltbox, agent, xui, podman-lxc, etc.).
---

# Host & Infrastructure Directory (`/derek-skills:hosts`)

Directory of all machines, Proxmox hypervisors, and LXC containers across Home Lab and Oracle Cloud, with direct SSH aliases, remote proxy jumping, and service URLs.

> **Live Infrastructure Snapshot (Gist):**  
> 🔗 [https://gist.github.com/hereisderek/9d10d746711c34f3b20c1a07282237f3](https://gist.github.com/hereisderek/9d10d746711c34f3b20c1a07282237f3)  
> Raw snapshot: `https://gist.githubusercontent.com/hereisderek/9d10d746711c34f3b20c1a07282237f3/raw/infrastructure-snapshot.md`

---

## SSH Connection Convention

Every machine uses key-based SSH with `IdentityFile ~/.ssh/key.ed25519`. Hosts are configured in `~/.ssh/config` using a 3-name convention:

| Scheme | Description | Example |
|---|---|---|
| `<name>.lab` | LAN name resolved by Cluster DNS (LXC 1005 `172.16.2.5`) | `ssh derek@saltbox.lab` |
| `<name>.lab.ip` | Fixed LAN IP without DNS dependence | `ssh derek@saltbox.lab.ip` |
| `<name>.lab.proxy` | Remote access from outside LAN (jumps through Oracle node `pve.oracle.proxy`) | `ssh derek@saltbox.lab.proxy` |
| `<name>.oracle` | Oracle internal name resolved by Oracle dnsmasq (`10.10.10.1`) | `ssh derek@agent.oracle` |
| `<name>.oracle.ip` | Oracle internal IP on `10.10.10.0/24` | `ssh derek@agent.oracle.ip` |
| `<name>.oracle.proxy` | Remote direct public access to Oracle node (`137.23.1.118`) | `ssh derek@pve.oracle.proxy` |

---

## 1. Oracle Cloud Infrastructure (OCI Sydney)

- **Hypervisor:** Debian 13 + Proxmox VE 9.2 (Ampere ARM64)
- **Public IPv4:** `137.23.1.118` | **Public IPv6:** `2603:c022:4001:aa00:0:8f07:73d3:bc49`
- **Bridge `vmbr0`:** `10.10.10.1/24` (domain `.oracle`)
- **WireGuard Tunnel:** `10.200.0.1` (LXC 105) connecting to Home (`10.200.0.2`)

### Oracle Quick Connection Reference

| CT ID | Hostname | SSH Command | Direct IP / Port | Web / Remote URL | Description |
|:---:|---|---|---|---|---|
| — | **pve** (Host) | `ssh derek@pve.oracle.proxy` | `10.10.10.1:22` / `137.23.1.118:22` | `https://pve.derekoracle.cc.cd` | Proxmox VE Hypervisor Host (Web UI 8006) |
| **102** | `caddy` | `ssh derek@caddy.oracle.proxy` | `10.10.10.2:22` (ports 80, 443) | `https://sites.derekoracle.cc.cd` | Inbound edge reverse proxy & automated TLS |
| **103** | `apt-cache` | `ssh derek@apt-cache.oracle.proxy`| `10.10.10.3:3142` | — | `apt-cacher-ng` package proxy |
| **104** | `pbs` | `ssh derek@pbs.oracle.proxy` | `10.10.10.4:8007` | — | Proxmox Backup Server |
| **105** | `wireguard` | `ssh derek@wireguard.oracle.proxy`| `10.10.10.5` (UDP 41200) | `wg.derekoracle.cc.cd` | Site-to-site VPN link to Home (`10.200.0.1`) |
| **110** | `podman-lxc`| `ssh derek@podman-lxc.oracle.proxy`| `10.10.10.10` | `https://arcane.derekoracle.cc.cd`<br>`https://homepage.derekoracle.cc.cd` | Rootless Podman: Arcane UI & Homepage |
| **111** | `xui` | `ssh root@xui.oracle.proxy` | `10.10.10.11` (ports 45282-45294) | `https://xui.derekoracle.cc.cd`<br>`proxy.derekoracle.cc.cd` | 3x-ui proxy: VLESS, Trojan, Hysteria2 |
| **112** | `agent` | `ssh derek@agent.oracle.proxy` | `10.10.10.12:22` | — | AI Agent runtime environment |
| **113** | `samba` | `ssh derek@samba.oracle.proxy` | `10.10.10.13:445` | — | SMB network file share |
| **114** | `rustdesk` | `ssh derek@rustdesk.oracle.proxy` | `10.10.10.14:21114-21119` | `rustdesk.derekoracle.cc.cd` | RustDesk server (hbbs/hbbr) |
| **115** | `screengo` | `ssh derek@screengo.oracle.proxy` | `10.10.10.15:5050` | — | Screego WebRTC screen sharing |
| **116** | `libretv` | `ssh derek@libretv.oracle.proxy` | `10.10.10.16:8080` | `https://libre.derekoracle.cc.cd` | LibreTV media streaming server |

---

## 2. Home Proxmox VE Cluster (`proxmox-services`)

- **Hypervisor:** Intel x86_64, PVE 9.2.3, kernel 6.8
- **LAN IP:** `172.16.1.1/16` (mDNS: `pve.local`), Gateway `172.16.0.1`
- **Cluster DNS:** `172.16.2.5` (LXC 1005 `dnsmasq`, domain `.lab`)
- **Remote Gateway:** WireGuard link via LXC 1006 (`172.16.2.6` / `10.200.0.2`) to Oracle

### Home Quick Connection Reference

| CT ID | Hostname | SSH Command (LAN) | SSH Command (Remote via Proxy) | LAN IP / Port | Web / Public URL | Role |
|:---:|---|---|---|---|---|---|
| — | **pve** (Host) | `ssh root@pve.lab` | `ssh root@pve.lab.proxy` | `172.16.1.1:22` | `https://pve.hereisderek.dpdns.org` | Main Proxmox VE host (UI 8006) |
| **1003** | `china-gateway` | `ssh root@china-gateway.lab` | `ssh root@china-gateway.lab.proxy` | `172.16.1.3:22` | — | China split-tunnel NAT router |
| **1004** | `apt-cacher` | `ssh root@apt-cacher.lab` | `ssh root@apt-cacher.lab.proxy` | `172.16.2.4:3142` | — | APT package cache proxy |
| **1005** | `dns` | `ssh root@dns.lab` | `ssh root@dns.lab.proxy` | `172.16.2.5:53` | — | Cluster DNS forwarder (dnsmasq) |
| **1006** | `wireguard` | `ssh root@wireguard.lab` | `ssh root@wireguard.lab.proxy` | `172.16.2.6` | — | WireGuard site-to-site gateway (`10.200.0.2`) |
| **2000** | `ssr` | `ssh root@ssr.lab` | `ssh root@ssr.lab.proxy` | `172.16.3.0:1080` | `https://ssr.hereisderek.dpdns.org` | Shadowsocks-rust outbound proxy |
| **2001** | `xui` | `ssh root@xui.lab` | `ssh root@xui.lab.proxy` | `172.16.2.1:2096` | `https://xui.hereisderek.dpdns.org` | 3x-ui proxy management panel |
| **2006** | `caddy` | `ssh root@caddy.lab` | `ssh root@caddy.lab.proxy` | `172.16.3.6:80,443` | `https://hereisderek.dpdns.org` | Primary edge reverse proxy + DDNS |
| **2008** | `myspeed` | `ssh derek@myspeed.lab` | `ssh derek@myspeed.lab.proxy` | `172.16.3.8:5216` | `https://myspeed.hereisderek.dpdns.org` | Speed test logger & dashboard |
| **2010** | `saltbox` | `ssh derek@saltbox.lab` | `ssh derek@saltbox.lab.proxy` | `172.16.2.10:22` | Plex: `32400`<br>Jellyfin: `8096` | Docker host: 40+ media/cloud services |
| **2011** | `TimeMachine` | `ssh root@timemachine.lab` | `ssh root@timemachine.lab.proxy`| `172.16.3.11:445` | `https://timemachine.hereisderek.dpdns.org`| Samba Time Machine + Bonjour |
| **2012** | `frigate` | `ssh root@frigate.lab` | `ssh root@frigate.lab.proxy` | `172.16.2.12:5000` | `https://frigate.hereisderek.dpdns.org` | Frigate NVR surveillance (Coral TPU) |
| **2014** | `screengo` | `ssh root@screengo.lab` | `ssh root@screengo.lab.proxy` | `172.16.3.14:5050` | `https://screengo.hereisderek.dpdns.org` | Screego screen sharing |
| **2020** | `alpine-rustdesk`| `ssh root@alpine-rustdeskserver.lab`| `ssh root@alpine-rustdeskserver.lab.proxy`| `172.16.3.20` | — | RustDesk server (supersedes 2005) |
| **2022** | `dynamic-pac` | `ssh root@dynamic-pac-proxy.lab` | `ssh root@dynamic-pac-proxy.lab.proxy` | `172.16.2.22:8080` | — | Dynamic PAC proxy router |
| **2023** | `mitmproxy` | `ssh derek@mitmproxy.lab` | `ssh derek@mitmproxy.lab.proxy` | `172.16.2.23:8081` | — | Traffic inspection & mitmweb |
| **2024** | `ai-endpoint` | `ssh derek@ai-endpoint-proxy.lab`| `ssh derek@ai-endpoint-proxy.lab.proxy`| `172.16.2.24:3001` | `https://freellmapi.hereisderek.dpdns.org`<br>`https://fcc.hereisderek.dpdns.org` | FreeLLM API (3001) & FCC proxy (8082) |
| **2025** | `hermesagent` | `ssh derek@hermesagent.lab` | `ssh derek@hermesagent.lab.proxy` | `172.16.2.25:9119` | `https://hermes.hereisderek.dpdns.org` | Hermes Agent gateway & dashboard |
| **2026** | `agent` | `ssh derek@agent.lab` | `ssh derek@agent.lab.proxy` | `172.16.2.26:6768` | `https://orca.hereisderek.dpdns.org` | AI coding workspace & Orca Web IDE |
| **2027** | `koel` | `ssh derek@koel.lab` | `ssh derek@koel.lab.proxy` | `172.16.2.27:8000` | `https://koel.hereisderek.dpdns.org` | Koel personal music streaming server |
| **2028** | `docker-lxc` | `ssh derek@docker-lxc.lab` | `ssh derek@docker-lxc.lab.proxy` | `172.16.2.28:22` | — | Ubuntu 26.04 Docker runtime host |

---

## How to Connect Based on Where You Are

### If you are on the local Home LAN (`172.16.0.0/16`):
```bash
# Connect directly by hostname
ssh derek@saltbox.lab
ssh derek@agent.lab
ssh root@pve.lab

# Oracle machines are routed across the WireGuard tunnel directly
ssh derek@pve.oracle.ip       # 10.10.10.1
ssh derek@agent.oracle.ip     # 10.10.10.12
```

### If you are remote / outside the Home LAN:
```bash
# Suffix with .proxy to jump through the Oracle public IP
ssh derek@saltbox.lab.proxy
ssh derek@agent.lab.proxy
ssh root@pve.lab.proxy

# Connect directly to Oracle
ssh derek@pve.oracle.proxy    # 137.23.1.118
```
