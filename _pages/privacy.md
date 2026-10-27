---
layout: page
title: سياسة الخصوصية - Privacy Policy
description: سياسة الخصوصية لموقع Cyber Silicon
permalink: /privacy/
lang: ar
---

# Privacy Policy for Cyber Silicon

**Last Updated: October 26, 2026**

This Privacy Policy describes how Cyber Silicon ("we", "us", "our") collects, uses, and protects your personal information when you use our website https://USERNAME.github.io and our integration with TikTok API.

### 1. Information We Collect

#### 1.1 Information You Provide
- Email address when you subscribe to our newsletter
- Comments via Giscus (GitHub Discussions) - your GitHub username and comment content
- Contact form inquiries

#### 1.2 Automatically Collected Information
- Browser type, device type, IP address (anonymized)
- Pages visited, time spent, via GitHub Pages analytics (no personal tracking)
- Cookies for theme preferences (color, dark mode) stored locally in your browser - no server tracking

#### 1.3 TikTok API Data
When you view a post that includes an embedded TikTok video:
- We display the TikTok video using TikTok's official embed player (iframe)
- We **do not** collect, store, or process your TikTok login, password, or personal TikTok data
- We use `my_tiktok_videos.json` which contains **our own public TikTok videos** metadata (title, URL, cover image) - not user data
- The TikTok embed player may set cookies according to TikTok's own Privacy Policy: https://www.tiktok.com/legal/privacy-policy

We **do NOT** access:
- Your private TikTok messages
- Your TikTok followers/following list
- Your TikTok account settings
- Any non-public TikTok data

### 2. How We Use Your Information

- To provide and improve our content (tutorials, maintenance guides)
- To display relevant TikTok tutorial videos alongside articles (e.g., Lesson 5 article shows Lesson 5 TikTok video)
- To respond to comments and inquiries
- To send newsletter if you subscribed (you can unsubscribe anytime)
- To remember your theme preferences locally

### 3. TikTok API Integration - Detailed Disclosure (Required for TikTok Approval)

**Purpose of TikTok Integration:**
Our website integrates with TikTok to:
1. Automatically fetch metadata of **our own TikTok channel videos** (not user videos) from a local JSON file `my_tiktok_videos.json`
2. Match article lesson number (e.g., "Lesson 12") with TikTok video title containing "Lesson 12" and embed that video in the article
3. Use TikTok video cover image as fallback article thumbnail if no other image exists

**Data Flow:**
```
queue/lesson-12.md -> script searches my_tiktok_videos.json for "Lesson 12" -> finds URL + cover -> embeds in Jekyll post -> displayed via TikTok Player iframe
```

**No User TikTok Authentication:** We do NOT require users to log in with TikTok to view our site. The embed is public.

**Future Scope (if we request user login):** If in future we implement "Login with TikTok" for commenting, we will:
- Only request `user.info.basic` and `video.list` scopes if needed
- Clearly disclose scope usage
- Allow revocation via TikTok settings

### 4. Data Sharing

We **do not sell, trade, or share** your personal data with third parties, except:
- GitHub Pages (hosting) - https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement
- Giscus (comments, powered by GitHub Discussions) - data stored in GitHub Discussions
- TikTok (when you interact with embedded TikTok player) - subject to TikTok Privacy Policy
- If required by law

### 5. Cookies

- **Essential:** Theme preferences (color, dark mode, font size) stored in `localStorage` - no tracking, stays in your browser
- **Third-party:** TikTok embed may set cookies - see TikTok's policy
- **No advertising cookies** - we don't run ads

You can disable cookies in browser settings, but theme preferences won't be saved.

### 6. Data Retention

- Newsletter emails: until you unsubscribe
- Comments: as long as GitHub Discussion exists (you can delete via GitHub)
- Theme preferences: until you clear browser storage
- TikTok metadata JSON: contains only our public videos, retained as long as site operates

### 7. Your Rights

- Access: request what data we have about you (contact us)
- Deletion: request deletion of newsletter email, comments
- Opt-out: unsubscribe from newsletter, disable cookies
- TikTok: revoke access via https://www.tiktok.com/setting if you ever authorized us (currently not required)

### 8. Children's Privacy

Our site is not directed to children under 13. We do not knowingly collect data from children.

### 9. Security

We use GitHub Pages HTTPS, no server database. Theme preferences are client-side only. We implement reasonable security measures.

### 10. Changes

We may update this policy. Changes posted here with updated date.

### 11. Contact

For privacy questions or TikTok data concerns:

- **Email:** mylif2021@gmail.com
- **Website:** https://cyber-silicon.github.io/about/
- **GitHub Issues:** https://github.com/cyber-silicon/cyber-silicon.github.io/issues

### 12. Compliance

We comply with:
- TikTok API Terms of Service
- TikTok Developer Terms
- GDPR (for EU users)
- GitHub Pages Terms

---

<style>
.legal-page h1 { font-size:28px; margin-bottom:20px; }
.legal-page h3 { margin-top:24px; font-size:18px; color: var(--primary); }
.legal-page p, .legal-page li { font-size:14px; line-height:1.8; margin-bottom:10px; }
.legal-page ul { padding-left:20px; }
</style>
