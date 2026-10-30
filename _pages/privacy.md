---
layout: page
title: Privacy Policy
description: Privacy Policy for Cyber Silicon and TikTok API integration
permalink: /privacy/
---

## Privacy Policy for Cyber Silicon

**Last Updated: October 27, 2026**

This Privacy Policy describes how Cyber Silicon ("we", "us", "our") collects, uses, and protects your personal information when you use our website https://cyber-silicon.github.io and our integration with TikTok API.

### 1. Information We Collect

**1.1 Information You Provide**

- Email address when you subscribe to our newsletter
- Comments via Giscus (GitHub Discussions) - your GitHub username and comment content
- Contact form inquiries

**1.2 Automatically Collected Information**

- Browser type, device type, IP address (anonymized)
- Pages visited, time spent via GitHub Pages
- Cookies for theme preferences (color, dark mode) stored locally in your browser

**1.3 TikTok API Data**

When you view a post that includes an embedded TikTok video:

- We display the TikTok video using TikTok's official embed player (iframe)
- We do not collect, store, or process your TikTok login, password, or personal TikTok data
- We use a local file `my_tiktok_videos.json` which contains metadata of our own public TikTok videos only (title, URL, cover image) - not user data
- The TikTok embed player may set cookies according to TikTok's own Privacy Policy

We do NOT access:

- Your private TikTok messages
- Your TikTok followers or following list
- Your TikTok account settings
- Any non-public TikTok data

### 2. How We Use Your Information

- To provide and improve our content (tutorials, maintenance guides)
- To display relevant TikTok tutorial videos alongside articles
- To respond to comments and inquiries
- To send newsletter if you subscribed
- To remember your theme preferences locally

### 3. TikTok API Integration - Detailed Disclosure

**Purpose of TikTok Integration:**

Our website integrates with TikTok to:

1. Automatically fetch metadata of our own TikTok channel videos (not user videos) from a local JSON file
2. Match article lesson number (e.g., "Lesson 12") with TikTok video title containing "Lesson 12" and embed that video in the article
3. Use TikTok video cover image as fallback article thumbnail if no other image exists

**Data Flow:**

Article file `lesson-12.md` -> Script searches `my_tiktok_videos.json` for "Lesson 12" -> Finds URL and cover -> Embeds in Jekyll post -> Displayed via TikTok Player iframe

**No User TikTok Authentication:**

We do NOT require users to log in with TikTok to view our site. The embed is public.

### 4. Data Sharing

We do not sell, trade, or share your personal data with third parties, except:

- GitHub Pages (hosting)
- Giscus (comments, powered by GitHub Discussions)
- TikTok (when you interact with embedded TikTok player)
- If required by law

### 5. Cookies

- Essential: Theme preferences stored in localStorage - no tracking
- Third-party: TikTok embed may set cookies
- No advertising cookies

You can disable cookies in browser settings.

### 6. Data Retention

- Newsletter emails: until you unsubscribe
- Comments: as long as GitHub Discussion exists
- Theme preferences: until you clear browser storage

### 7. Your Rights

- Access: request what data we have about you
- Deletion: request deletion of newsletter email and comments
- Opt-out: unsubscribe from newsletter, disable cookies
- TikTok: revoke access via TikTok settings if you ever authorized us

### 8. Children's Privacy

Our site is not directed to children under 13. We do not knowingly collect data from children.

### 9. Security

We use GitHub Pages HTTPS, no server database. Theme preferences are client-side only.

### 10. Changes

We may update this policy. Changes will be posted here with updated date.

### 11. Contact

For privacy questions:

- Email: mylif2021@gmail.com
- Website: https://cyber-silicon.github.io/about/
- GitHub: https://github.com/cyber-silicon/cyber-silicon.github.io/issues
