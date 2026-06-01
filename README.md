# z2w-templates

Public mirror of the **Zero2Webmaster canonical Templates folder**.

Served at **https://templates.z2w.us** via Cloudflare Pages and consumed by [`@zero2webmaster/starter-kit`](https://www.npmjs.com/package/@zero2webmaster/starter-kit) as the HTTPS fallback when a local Templates folder is not present.

## What's here

- **`AGENTS_v2.13.0.md`** — Canonical generic AGENTS body (3-layer architecture framework). Embedded into every non-WordPress Z2W project scaffold.
- **`AGENTS_WP_v3.1.0.md`** — Canonical WordPress-plugin AGENTS body (framework v3.1.0 conventions). Embedded into every Z2W WordPress plugin scaffold.
- **`Resources/`** — Setup guides, templates, and helper scripts (SYMLINK-SAFETY-GUIDE, TERMINAL_GUIDE, handoff/roadmap/status templates, `copy_to_new_project.sh`, `tools/protect-git.sh`).

## How it's used

The `@zero2webmaster/starter-kit` CLI reads canonical content from this mirror when the user does not have a local `~/Desktop/Zero2Webmaster/AI/Templates/` folder. Resolution chain:

1. Local Templates folder (if present)
2. Fresh local cache at `~/.cache/z2w-templates/` (24h TTL)
3. HTTPS fetch from `https://templates.z2w.us` (this mirror)
4. Stale local cache (with warning, when network is down)
5. Hard fail (with `--templates-path <path>` hint)

The CLI's `--refresh-templates` flag forces a fresh fetch from this mirror, bypassing the local cache.

## Layout

Files are served flat — `templates.z2w.us/{name}` returns the file at `./{name}` in this repo. The CLI's `readTemplate("AGENTS_v2.13.0.md")` translates to `GET https://templates.z2w.us/AGENTS_v2.13.0.md`.

## Source of truth

Kerry's working copy at `~/Desktop/Zero2Webmaster/AI/Templates/` is the canonical source. This repo is a downstream snapshot, kept in sync via [`sync.sh`](./sync.sh). Run `./sync.sh` from this repo after editing the working copy to push the public-safe subset here; Cloudflare Pages auto-deploys on push to `main`.

## Integrity

v0.2.0 trusts TLS for transport integrity. A SHA-256 manifest is on the v0.3.x roadmap if a real threat model warrants it.

## License

Same terms as the canonical Templates folder. Use freely for Z2W and personal projects.

## Companion projects

- **`@zero2webmaster/starter-kit`** — the CLI that consumes this mirror (npm)
- **`zero2webmaster/z2w-starter-kit`** — CLI source repo (private)
- **`zero2webmaster/z2w-agent-coordination`** — cross-project agent bulletin (private)

---

*Mirror landed 2026-06-01. Maintained by Kerry Kriger.*
