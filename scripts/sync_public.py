#!/usr/bin/env python3
"""
sync_public.py — Syncs workspace-heidi to heidi-public with redaction.

Usage:
  python3 sync_public.py          # sync and commit
  python3 sync_public.py --push   # sync, commit, and push to GitHub
  python3 sync_public.py --dry-run  # preview what would be copied/redacted
"""

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

SOURCE = Path("/Users/heidi/.openclaw/workspace-heidi")
DEST = Path("/Users/heidi/heidi-public")
CONFIG = SOURCE / "redact.json"

def load_config():
    with open(CONFIG) as f:
        return json.load(f)

def should_exclude(path: Path, config: dict, source_root: Path) -> bool:
    rel = path.relative_to(source_root)
    parts = rel.parts

    # Exclude dirs
    for excl_dir in config.get("exclude_dirs", []):
        if excl_dir in parts:
            return True

    # Exclude specific files
    for excl_file in config.get("exclude_files", []):
        if rel == Path(excl_file) or rel.name == Path(excl_file).name:
            return True

    return False

def strip_sections(content: str, config: dict) -> str:
    """Remove entire markdown sections by heading name."""
    for heading in config.get("exclude_sections", []):
        # Match ## Heading through the next ## heading (or end of file)
        pattern = rf'(\n|^)## {re.escape(heading)}.*?(?=\n## |\Z)'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    return content

def redact_content(content: str, config: dict) -> str:
    # Apply string substitutions (longest first to avoid partial matches)
    strings = config.get("strings", {})
    for original, replacement in sorted(strings.items(), key=lambda x: -len(x[0])):
        content = content.replace(original, replacement)

    # Apply pattern-based redaction
    patterns = config.get("patterns", {})

    if "email" in patterns:
        content = re.sub(
            r'\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b',
            patterns["email"], content
        )
    if "phone" in patterns:
        content = re.sub(
            r'\b(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}\b',
            patterns["phone"], content
        )
    if "api_key" in patterns:
        # Catches common API key patterns (long hex/base64 strings)
        content = re.sub(
            r'\b(sk-[A-Za-z0-9\-_]{20,}|[A-Za-z0-9\-_]{32,})\b',
            patterns["api_key"], content
        )

    return content

def sync(dry_run=False, push=False):
    config = load_config()
    copied = []
    skipped = []

    # Files/dirs to preserve in dest even if not in source
    preserve = set(config.get("exclude_files", []) + [".git", ".gitignore"])

    # Clear dest except preserved files and .git
    for item in DEST.iterdir():
        if item.name in (".git", ".gitignore"):
            continue
        rel = str(item.relative_to(DEST))
        if rel in preserve or item.name in preserve:
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()

    # Walk source
    for src_path in sorted(SOURCE.rglob("*")):
        if not src_path.is_file():
            continue
        if should_exclude(src_path, config, SOURCE):
            skipped.append(str(src_path.relative_to(SOURCE)))
            continue

        rel = src_path.relative_to(SOURCE)
        dest_path = DEST / rel

        if dry_run:
            print(f"  COPY  {rel}")
            continue

        dest_path.parent.mkdir(parents=True, exist_ok=True)

        # Text files: redact. Binary files: copy as-is.
        try:
            content = src_path.read_text(encoding="utf-8")
            content = strip_sections(content, config)
            for inline in config.get("exclude_inline", []):
                content = content.replace(inline, "")
            redacted = redact_content(content, config)
            dest_path.write_text(redacted, encoding="utf-8")
        except (UnicodeDecodeError, IsADirectoryError):
            shutil.copy2(src_path, dest_path)

        copied.append(str(rel))

    if dry_run:
        print(f"\nSkipped ({len(skipped)}):")
        for s in skipped:
            print(f"  SKIP  {s}")
        return

    print(f"Synced {len(copied)} files, skipped {len(skipped)}")

    # Git commit
    os.chdir(DEST)
    subprocess.run(["git", "add", "-A"], check=True)
    result = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if result.returncode == 0:
        print("Nothing changed — no commit needed.")
    else:
        subprocess.run(["git", "commit", "-m", "sync: update from workspace-heidi"], check=True)
        print("Committed.")

        if push:
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print("Pushed to GitHub.")

if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    push = "--push" in sys.argv
    sync(dry_run=dry_run, push=push)
