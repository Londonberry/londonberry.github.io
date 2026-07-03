#!/usr/bin/env python3
"""Push Londonberry blog social posts to Postiz.

Safe by default: creates DRAFTS you review in the Postiz UI before anything
goes live. Nothing is scheduled or published unless you pass --schedule or
--now, mirroring the dry-run-first rule on the email rail.

Config comes from ~/.lb-claude/postiz-londonberry.env (base, token, channel ids).
The API token is account-wide; if POSTIZ_API_TOKEN is blank it falls back to
POSTIZ_NFM_API_TOKEN from postiz-nfm.env.

Usage:
  post.py --list                       # show connected channels + their ids
  post.py                              # create drafts for all posts (default)
  post.py --slug top-10-ai-uses-in-sports
  post.py --schedule --at 2026-06-25T14:00:00Z
  post.py --now                        # publish immediately (asks nothing, be sure)
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

LB_DIR = Path.home() / ".lb-claude"
POSTS_FILE = Path(__file__).with_name("social_posts.json")

# Platform -> (identifier substring Postiz reports, settings __type).
PLATFORM_META = {
    "linkedin": {"env": "LONDONBERRY_LINKEDIN_ID", "type": "linkedin"},
    "x": {"env": "LONDONBERRY_X_ID", "type": "x"},
}


def load_env(path):
    """Parse a KEY=VALUE .env file into a dict. Missing file is fine."""
    out = {}
    if not path.exists():
        return out
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def config():
    env = load_env(LB_DIR / "postiz-londonberry.env")
    nfm = load_env(LB_DIR / "postiz-nfm.env")
    base = env.get("POSTIZ_API_BASE") or nfm.get("POSTIZ_NFM_API_BASE") or "https://api.postiz.com"
    token = env.get("POSTIZ_API_TOKEN") or nfm.get("POSTIZ_NFM_API_TOKEN") or ""
    if not token:
        sys.exit("No Postiz token. Set POSTIZ_API_TOKEN in postiz-londonberry.env.")
    return base.rstrip("/"), token, env


def api(base, token, method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(base + path, data=data, method=method)
    req.add_header("Authorization", token)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw.strip() else None)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def cmd_list(base, token):
    status, data = api(base, token, "GET", "/public/v1/integrations")
    if status != 200:
        sys.exit(f"integrations HTTP {status}: {data}")
    print(f"{'id':<28} {'platform':<20} name / profile")
    for it in data:
        print(f"{it['id']:<28} {it['identifier']:<20} {it['name']} / {it.get('profile','')}"
              + ("  [disabled]" if it.get("disabled") else ""))


def build_post(post_type, when, integration_id, settings_type, content):
    return {
        "type": post_type,
        "date": when,
        "shortLink": False,
        "tags": [],
        "posts": [
            {
                "integration": {"id": integration_id},
                "value": [{"content": content, "image": []}],
                "settings": {"__type": settings_type},
            }
        ],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="list channels and exit")
    ap.add_argument("--slug", help="only this post slug")
    ap.add_argument("--platforms", default="linkedin,x", help="comma list: linkedin,x")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--schedule", action="store_true", help="queue instead of draft")
    g.add_argument("--now", action="store_true", help="publish immediately")
    ap.add_argument("--at", help="ISO-8601 time for --schedule, e.g. 2026-06-25T14:00:00Z")
    args = ap.parse_args()

    base, token, env = config()

    if args.list:
        cmd_list(base, token)
        return

    post_type = "schedule" if args.schedule else "now" if args.now else "draft"
    when = args.at or "2026-01-01T09:00:00.000Z"  # ignored for draft/now
    if post_type == "schedule" and not args.at:
        sys.exit("--schedule needs --at <ISO-8601>")

    posts = json.loads(POSTS_FILE.read_text())
    if args.slug:
        posts = [p for p in posts if p["slug"] == args.slug]
        if not posts:
            sys.exit(f"no post with slug {args.slug}")

    platforms = [p.strip() for p in args.platforms.split(",") if p.strip()]
    for plat in platforms:
        if plat not in PLATFORM_META:
            sys.exit(f"unknown platform {plat}")
        if not env.get(PLATFORM_META[plat]["env"]):
            sys.exit(f"{PLATFORM_META[plat]['env']} not set in postiz-londonberry.env "
                     f"(connect the Londonberry {plat} account in Postiz first, then --list)")

    made = 0
    for post in posts:
        for plat in platforms:
            meta = PLATFORM_META[plat]
            content = post.get(plat)
            if not content:
                continue
            body = build_post(post_type, when, env[meta["env"]], meta["type"], content)
            status, resp = api(base, token, "POST", "/public/v1/posts", body)
            ok = status in (200, 201)
            print(f"[{post_type}] {post['slug']} -> {plat}: HTTP {status} {'OK' if ok else resp}")
            made += ok
    print(f"\n{made} post(s) created as '{post_type}'.")
    if post_type == "draft":
        print("Review + publish them in the Postiz calendar.")


if __name__ == "__main__":
    main()
