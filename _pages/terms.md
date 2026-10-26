---
layout: page
title: شروط الاستخدام - Terms of Use
description: شروط استخدام موقع Cyber Silicon واستخدام
permalink: /terms/
lang: ar
---

<div class="legal-page" dir="ltr" style="text-align:left;">

# Terms of Service for Cyber Silicon

**Last Updated: October 26, 2026**

Welcome to Cyber Silicon (https://cyber-silicon.github.io). By accessing our website, you agree to these Terms.

### 1. Acceptance of Terms

By using our site, you agree to these Terms, our Privacy Policy (/privacy/), and TikTok's Terms if you interact with TikTok embeds.

### 2. Description of Service

Cyber Silicon is a technical blog providing:
- Electronics maintenance tutorials
- Cybersecurity guides
- Programming and AI content
- Embedded TikTok tutorial videos (our own public videos)

Our GitHub Pages site uses Jekyll with Plus UI Pro theme and integrates TikTok videos via automatic matching (lesson number → TikTok video).

### 3. TikTok Integration Terms

**How it works:**
- Each article file (e.g., `lesson-12-laptop.md`) contains lesson number
- Our script `github_publisher.py` searches local file `data/my_tiktok_videos.json` (containing our public TikTok videos metadata)
- If match found (title contains "Lesson 12"), embeds TikTok player iframe in article
- Cover image from TikTok used as article thumbnail if no other image exists

**User Obligations:**
- You may view embedded TikTok videos without TikTok account
- If you interact with TikTok player (like, comment, share via TikTok), you are subject to TikTok Terms: https://www.tiktok.com/legal/terms-of-service
- You will not attempt to extract private TikTok data via our site

**Our Obligations:**
- We only embed our own public TikTok videos, not private or other users' videos without permission
- We comply with TikTok API Rate Limits and Terms
- We do not modify TikTok player to hide attribution

### 4. Intellectual Property

- **Our Content:** Articles, tutorials, code snippets written by us are © Cyber Silicon. You may share with attribution and link back. No commercial reproduction without permission.
- **TikTok Videos:** Our TikTok videos © us. Embedded via official TikTok embed - TikTok retains rights per their Terms.
- **Theme:** Plus UI Pro theme based on Plus UI inspiration, MIT licensed for this site.
- **User Comments:** By commenting via Giscus, you grant us license to display your comment. You retain ownership.

### 5. User Conduct

You agree not to:
- Scrape our site excessively (respect GitHub Pages limits)
- Attempt to hack, inject code, or bypass security
- Post spam, hate speech, or illegal content in comments
- Misuse TikTok embeds to collect data
- Impersonate us or others

### 6. Disclaimer - Technical Content

- Tutorials provided "as is" for educational purposes
- Electronics repair involves risk (electric shock, damage). Follow safety precautions. We are not liable for damage/injury from following tutorials.
- Always unplug devices, use ESD protection, seek professional help if unsure.

### 7. Third-Party Links

Our site may link to GitHub, TikTok, YouTube, etc. We are not responsible for third-party content or privacy practices.

### 8. Limitation of Liability

- Our site is free, hosted on GitHub Pages
- We do not guarantee uptime, accuracy, or that TikTok embeds will always work (depends on TikTok)
- To maximum extent allowed by law, we are not liable for indirect, incidental damages

### 9. Termination

We may remove content, disable comments, or block access if you violate these Terms.

### 10. Changes to Terms

We may update Terms. Continued use after changes means acceptance. Check /terms/ periodically.

### 11. Governing Law

These Terms governed by laws of Sudan and GitHub Pages jurisdiction, without regard to conflict of law principles. Any disputes regarding TikTok integration also subject to TikTok Developer Agreement.

### 12. Contact & DMCA

For questions, takedown requests, or TikTok API concerns:

- **Email:** mylif2021@gmail.com (replace with real)
- **GitHub Issues:** https://github.com/cyber-silicon/cyber-silicon.github.io/issues
- **About Page:** /about/

If you believe content infringes your copyright, contact us with details (DMCA notice).

### 13. TikTok API Approval - Additional Info for Reviewers

**For TikTok API Review Team:**

- **App Name:** Cyber Silicon Blog
- **Website:** https://cyber-silicon.github.io
- **Use Case:** Display our own TikTok tutorial videos alongside matching blog posts to help users learn electronics repair
- **Client Key:** [Will be provided in TikTok Developer Portal]
- **Scopes Requested:** Currently none (public embeds only). If we request `user.info.basic` in future, it's to allow users to comment with TikTok identity (optional).
- **Privacy Policy URL:** https://USERNAME.github.io/privacy/
- **Terms URL:** https://USERNAME.github.io/terms/
- **Demo Video:** Embedded TikTok videos visible on any post like /2026/10/26/lesson-... 
- **Test Account:** Not required for public embeds

We attest we comply with TikTok API Terms, will not misuse data, and will display TikTok attribution.

</div>

<style>
.legal-page h1 { font-size:28px; margin-bottom:20px; }
.legal-page h3 { margin-top:24px; font-size:18px; color: var(--primary); }
.legal-page p, .legal-page li { font-size:14px; line-height:1.8; margin-bottom:10px; }
.legal-page ul { padding-left:20px; }
</style>
