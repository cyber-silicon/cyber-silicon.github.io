---
layout: page
title: Terms of Service
description: Terms of Service for Cyber Silicon and TikTok API integration
permalink: /terms/
---

## Terms of Service for Cyber Silicon

**Last Updated: October 27, 2026**

Welcome to Cyber Silicon (https://cyber-silicon.github.io). By accessing our website, you agree to these Terms.

### 1. Acceptance of Terms

By using our site, you agree to these Terms, our Privacy Policy, and TikTok's Terms if you interact with TikTok embeds.

### 2. Description of Service

Cyber Silicon is a technical blog providing:

- Electronics maintenance tutorials
- Cybersecurity guides
- Programming and AI content
- Embedded TikTok tutorial videos (our own public videos)

Our GitHub Pages site uses Jekyll with Plus UI Pro theme and integrates TikTok videos via automatic matching.

### 3. TikTok Integration Terms

**How it works:**

- Each article file (e.g., `lesson-12-laptop.md`) contains lesson number
- Our script `github_publisher.py` searches local file `data/my_tiktok_videos.json` (containing our public TikTok videos metadata)
- If match found (title contains "Lesson 12"), embeds TikTok player iframe in article
- Cover image from TikTok used as article thumbnail if no other image exists

**User Obligations:**

- You may view embedded TikTok videos without TikTok account
- If you interact with TikTok player (like, comment, share via TikTok), you are subject to TikTok Terms
- You will not attempt to extract private TikTok data via our site

**Our Obligations:**

- We only embed our own public TikTok videos, not private or other users' videos
- We comply with TikTok API Rate Limits and Terms
- We do not modify TikTok player to hide attribution

### 4. Intellectual Property

- **Our Content:** Articles and tutorials written by us are copyright Cyber Silicon. You may share with attribution and link back.
- **TikTok Videos:** Our TikTok videos are copyright us, embedded via official TikTok embed.
- **Theme:** Plus UI Pro theme, MIT licensed.
- **User Comments:** By commenting via Giscus, you grant us license to display your comment.

### 5. User Conduct

You agree not to:

- Scrape our site excessively
- Attempt to hack or inject code
- Post spam, hate speech, or illegal content in comments
- Misuse TikTok embeds to collect data
- Impersonate us or others

### 6. Disclaimer - Technical Content

- Tutorials provided "as is" for educational purposes
- Electronics repair involves risk (electric shock, damage). Follow safety precautions. We are not liable for damage or injury.
- Always unplug devices, use ESD protection, seek professional help if unsure.

### 7. Third-Party Links

Our site may link to GitHub, TikTok, YouTube, etc. We are not responsible for third-party content.

### 8. Limitation of Liability

- Our site is free, hosted on GitHub Pages
- We do not guarantee uptime or accuracy
- To maximum extent allowed by law, we are not liable for indirect damages

### 9. Termination

We may remove content, disable comments, or block access if you violate these Terms.

### 10. Changes to Terms

We may update Terms. Continued use after changes means acceptance.

### 11. Governing Law

These Terms are governed by applicable laws.

### 12. Contact and DMCA

For questions or takedown requests:

- Email: legal@cyber-silicon.com
- GitHub Issues: https://github.com/cyber-silicon/cyber-silicon.github.io/issues

### 13. Information for TikTok API Review Team

- **App Name:** Cyber Silicon
- **Website:** https://cyber-silicon.github.io
- **Use Case:** Display our own TikTok tutorial videos alongside matching blog posts
- **Privacy Policy URL:** https://cyber-silicon.github.io/privacy/
- **Terms URL:** https://cyber-silicon.github.io/terms/
- **Demo:** Embedded TikTok videos visible on any post
