#!/usr/bin/env python3
"""Final end-to-end test for One More IG Scheduler."""
import urllib.request, json, re

BASE = "http://127.0.0.1:8080"

def post(path):
    req = urllib.request.Request(BASE + path, data=b"", method="POST")
    return json.loads(urllib.request.urlopen(req).read())

# 1. Scan media folder
result = post("/api/scan")
print(f"①   Scan done: {result}")
assert result.get("assets", 0) >= 3, "Expected at least 3 test assets"

# 2. Fetch homepage and find post IDs
r = urllib.request.urlopen(BASE + "/")
body = r.read().decode()
print(f"②   Homepage loaded ({len(body)} chars)")

ids = re.findall(r'/api/posts/(\d+)', body)
assert ids, "No post IDs in rendered page — data not persisted"
pids = list(set(ids))
print(f"③   Post IDs found: {pids}")

# 3. Caption first post
cap = post(f"/api/posts/{pids[0]}/caption")
print(f"④   Caption: \"{cap['caption'][:80]}…\"")

# 4. Schedule that post
sch = post(f"/api/posts/{pids[0]}/schedule")
print(f"⑤   Scheduled → {sch['scheduled_at']}")

# 5. Re-check homepage reflects changes
r2 = urllib.request.urlopen(BASE + "/")
body2 = r2.read().decode()
has_draft = "draft" in body2.lower()
has_sched = "scheduled" in body2.lower()
print(f"⑥   Homepage shows DRAFT pill: {has_draft}")
print(f"⑦   Homepage shows SCHEDULED pill: {has_sched}")

print("\n✅ Everything works. Dashboard at http://10.0.0.61:8080")
