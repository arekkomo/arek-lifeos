#!/usr/bin/env python3
"""Full smoke test for One More IG Scheduler."""
import urllib.request, json

BASE = "http://127.0.0.1:8080"

def post(path):
    req = urllib.request.Request(BASE + path, data=b"", method="POST")
    return json.loads(urllib.request.urlopen(req).read())

# Scan for test dishes
result = post("/api/scan")
print(f"Scan: {result}")

# Get index to see current state
r = urllib.request.urlopen(BASE + "/")
body = r.read().decode()
has_detected = "detected" in body.lower()
has_cauliflower = "cauliflower" in body.lower()
has_mushroom = "mushroom" in body.lower()
print(f"Homepage shows detected posts: {has_detected}")
print(f"Shows cauliflower-lasagna: {has_cauliflower}")
print(f"Shows mushroom-risotto: {has_mushroom}")

# Find post IDs from HTML (they're in the table rows)
import re
post_ids = re.findall(r'/api/posts/(\d+)', body)
print(f"Post IDs found in page: {set(post_ids)}")

for pid in set(post_ids):
    try:
        cap = post(f"/api/posts/{pid}/caption")
        print(f"Captioned post {pid}: {cap['caption'][:60]}...")
        sch = post(f"/api/posts/{pid}/schedule")
        print(f"Scheduled post {pid} for: {sch['scheduled_at']}")
    except Exception as e:
        print(f"Post {pid} error: {e}")

print("\n✅ All tests done!")
