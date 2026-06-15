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

## Mobile Sync Guide: Obsidian Git on Android

Using Obsidian with the **Obsidian Git** community plugin works beautifully on Android without requiring an Obsidian Sync subscription. Because Android allows direct access to the local file system, the plugin can handle cloning, committing, pulling, and pushing directly inside the app.

### Step-by-Step Setup

1. **Generate a GitHub Personal Access Token (PAT):**
   - On GitHub, go to **Settings -> Developer Settings -> Personal Access Tokens -> Tokens (classic)**.
   - Generate a new token with the `repo` scope. Copy it (you will use this as your password).

2. **Set up the Vault on Android:**
   - Install **Obsidian** from the Google Play Store.
   - Create a new empty vault on your device (e.g., named `Notes`).
   - Open settings in Obsidian, go to **Community Plugins**, turn them on, and search for and install **Obsidian Git**. Enable the plugin.

3. **Clone Your Repository:**
   - In Obsidian, open the Command Palette (`Ctrl/Cmd + P` or swipe down).
   - Search for **Obsidian Git: Clone an existing remote repo**.
   - Enter your repository HTTPS URL: `https://github.com/GianRomani/Notes.git`.
   - When prompted for credentials, use your GitHub username and paste the Personal Access Token (PAT) as the password.
   - Once cloned, restart Obsidian. Your entire vault, including the coffee guides, templates, and logs, will be synced onto your phone.

4. **Configure Auto-Sync Settings:**
   - Open **Obsidian Git** plugin settings on your phone:
     - **Vault backup interval (minutes):** Set to `30` or `60` to automatically commit and push your mobile edits.
     - **Pull updates on startup:** Enable this so your phone pulls any changes you made on your desktop before you start writing on the go.
     - **Push on backup:** Enable this to ensure changes make it to GitHub (and trigger Netlify) automatically.

---
*Created: 2026-06-15 | Happy Brewing!*
