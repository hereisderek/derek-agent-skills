---
description: Look up connection details, SSH commands, and network addresses for Derek's Home Proxmox VE and Oracle Cloud hosts and LXCs.
---

# /derek-skills:hosts

Directory and connection manual for Derek's Home Proxmox VE cluster and Oracle Cloud node.

## Live Gist Snapshot
🔗 [https://gist.github.com/hereisderek/9d10d746711c34f3b20c1a07282237f3](https://gist.github.com/hereisderek/9d10d746711c34f3b20c1a07282237f3)

## Quick SSH Reference

- **Home LAN:** `ssh <user>@<hostname>.lab` (e.g. `ssh derek@saltbox.lab`, `ssh derek@agent.lab`, `ssh root@pve.lab`)
- **Remote via ProxyJump:** `ssh <user>@<hostname>.lab.proxy` (e.g. `ssh derek@saltbox.lab.proxy`, `ssh derek@agent.lab.proxy`)
- **Oracle Cloud (Direct):** `ssh derek@pve.oracle.proxy` (`137.23.1.118`), `ssh derek@agent.oracle.proxy` (`10.10.10.12`)

See full inventory in `skills/hosts/SKILL.md`.
