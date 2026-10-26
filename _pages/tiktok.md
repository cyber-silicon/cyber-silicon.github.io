---
layout: page
title: TikTok Integration - تكامل تيك توك
description: كيف يعمل تكامل TikTok API في مدونة Cyber Silicon
permalink: /tiktok/
---

## TikTok API Integration - How it works

### For TikTok Review Team

**Website:** https://USERNAME.github.io
**Privacy:** /privacy/
**Terms:** /terms/

### What we do

Our blog articles are technical tutorials (e.g., "Lesson 12: Laptop Screen Repair").

We have a TikTok channel with matching tutorial videos (title: "الدرس 12: صيانة شاشة اللابتوب").

Our automation script:

1. Article file: `lesson-12-laptop-screen.md` (in queue/)
2. Script extracts lesson number: `12`
3. Searches local JSON `data/my_tiktok_videos.json` (our public videos list) for title containing "الدرس 12"
4. If found, gets URL like `https://www.tiktok.com/@cybersilicon/video/1234567890`
5. Embeds using official TikTok Player iframe in Jekyll post
6. Uses cover image as article thumbnail if no other image

### Code Example (github_publisher.py)

```python
def get_tiktok_info_from_log(filename):
    lesson_match = re.search(r'lesson_(\d+)', filename)
    lesson_num = lesson_match.group(1)
    with open('my_tiktok_videos.json') as f:
        for vid in json.load(f):
            if f"الدرس {lesson_num}" in vid['title']:
                return vid['url'], vid['cover']
```

### Data We Access

- ONLY our own public TikTok videos metadata (title, url, cover)
- No user private data
- No login required for viewing

### Future

If approved for Login Kit, we will allow users to optionally log in to comment via TikTok identity, with clear scope disclosure.

### Contact

Email: contact@cybersilicon.com
