# Specialty Coffee Corner

Welcome to your coffee notebook. This section contains your study guides, brewing configurations, and coffee profile logs. Because your vault is connected to GitHub and deployed via Netlify, updates you make here can be published directly to your website.

---

## Reference Guides

Discover the science of extraction, dial in recipes, and master sensory tasting:

> [!abstract] **Core Guides**
> 1. **[[Guides/Tasting & Flavours|Tasting & Flavours Guide]]** — Learn how to train your palate, use the SCA flavor wheel, and recognize extraction balance (sweet vs. sour vs. bitter).
> 2. **[[Guides/Pour Over Techniques|Pour Over Techniques]]** — Mastering V60 and Origami, comparing filters, and brewing with Kasuya’s 4:6 and Hoffmann's 1-cup recipes.
> 3. **[[Guides/Espresso & Latte Art|Espresso & Latte Art Guide]]** — Dialing in your Sage Barista Express, frothing microfoam, pouring basic patterns, and Moka pot brewing.

---

## Coffee Station Configurations

Keep track of your equipment configurations and sweet-spot settings:

| Equipment | Type / Model | Notes / Default Settings |
| :--- | :--- | :--- |
| **Espresso Machine** | Sage Barista Express | Double shot (single wall basket) ~18g in, 36-40g out. |
| **Grinder** | Sage Built-in (Conical Burr) | Espresso settings range: ~3 to 8 (varies by beans). |
| **Filter Dripper A** | Hario V60 (02) | Cone filters. Focus on high clarity. |
| **Filter Dripper B** | Origami Dripper (S) | Uses Kalita Wave (sweetness) or V60 (clarity) papers. |
| **Traditional** | Moka Pot (3-cup) | Pre-heated water, low heat, stop extraction with cold water. |
| **Scale** | Digital with Timer | Essential for tracking yield and time. |

---

## Coffee Profiles & Tasting Logs

Create a new file for each coffee bean bag you buy using the template: `Templates/Coffee Profile Template`. Save it under the `Coffee/Tasting Logs/` folder.

This template lets you log the details of the bean once, upload photos of the bag or your latte art, and add multiple rows to the **Brew Log & Recipe Trials** table to compare how different parameters (grind, temperature, ratio) affect the taste of that specific bean.

### Active Coffee Inventory

*Update this table as you add new coffee profiles, or use the automated Dataview query below.*

| Date | Coffee Name | Roaster | Origin | Best Method | Overall Rating | Note Link |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| 2026-06-15 | Ethiopia Hambela | Gardelli Coffee | Ethiopia | V60 | ⭐️⭐️⭐️⭐️⭐️ | [[Tasting Logs/Example Coffee Log\|View Profile]] |

<br>

> [!tip] **Using the Obsidian Dataview Plugin (Optional)**
> If you have the **Dataview** plugin enabled in Obsidian, paste this block into any note to automatically generate a table of all your logs:
> 
> \`\`\`dataview
> TABLE roaster AS Roaster, origin AS Origin, process AS Process, rating AS Rating
> FROM "Coffee/Tasting Logs"
> SORT date DESC
> \`\`\`

---

## Mobile Logging & Sync Workflows (No Subscription Required)

Since your vault is a Git repository hosted on GitHub and built on Netlify, you can log coffee from your phone and sync it for free without an Obsidian Sync subscription.

### Option A: GitJournal App (Android & iOS)
- **What it is:** A free, open-source markdown editor designed to sync directly with Git repositories.
- **How it works:** You point GitJournal to your `GianRomani/Notes` GitHub repository. When you open GitJournal on your phone, you can view your notes, select your current coffee profile, and add a brew trial directly to the table.
- **Sync:** GitJournal commits and pushes changes back to GitHub automatically, which immediately triggers a Netlify deploy, updating your website.

### Option B: iOS Shortcuts + GitHub API
- **What it is:** A fast, one-tap shortcut on your iOS home screen.
- **How it works:** You create a shortcut that asks for: "Bean Name", "Method", "Grind", "Ratio", and "Sensory Notes". The shortcut makes a POST request to the GitHub API to append a line to your coffee log.
- **Sync:** Runs in milliseconds, updates your repo, and triggers the Netlify build without opening any app.

---
*Created: 2026-06-15 | Happy Brewing!*
