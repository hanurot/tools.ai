# Frase hands-on notes (trial, 2026-11-15, demo site allbirds.com)

## Ch1 Onboarding / Brand Hub
- App at next.frase.io. Onboarding is mandatory: enter a ROOT domain (subpaths like user.github.io/repo are stripped -> fails "couldn't read business information").
- Steps: Your website -> Reading your site (Mapping site: 30 pages; Researching market: searches + visits competitor about pages; Finding topics: 10 topics; Reading business) -> Your brand profile -> Matching criteria -> Your competitors (location, competitors, content gaps) -> Review. ~2-3 min.
- Brand profile auto-filled: business overview, website type (E-commerce), positioning, industry, value proposition, primary offering, target audience (4 personas), brand values, tagline, social links. Editable ("Fix anything that's off now and it carries through").
- Matching criteria (5): e.g. US market focus, natural materials, DTC model, lifestyle footwear, environmental value prop. Used by Brand Hub to score new competitors.
- Competitors found: 3 (Giesswein, Vivaia, Native Shoes), all tracked by default; Change/Skip/Continue.
- After onboarding it "starts right away with a site audit and a scan for article ideas".
- While waiting it shows 7 "things to try first" cards (illustrative sample data): Site audit (site health score, issues ranked High/Med/Low: pages AI can't read, missing meta descriptions, thin pages, broken internal links, missing alt, duplicate titles, redirect chains, missing H1); AI visibility (per engine: ChatGPT, Google AI, Gemini, Perplexity, Claude, Copilot, Grok, DeepSeek -> names you Nth or names rival); Brief creation; Connect to Claude/ChatGPT (MCP); Search Console connect (clicks per page 28 days, flags drops); Content gap ideas with volume & difficulty; Draft content score vs top 10 (topics covered/missing).
- More: Frase agent (ask from any page), Clusters (topic map), Research (what ranks & what those pages cover), Competitive Analysis (your page vs competitor), Calendar, Brand Hub (profile, voice, competitors used in everything it writes).
- Final onboarding step: name workspace; choose first job: "Run a site audit" (default) or "See AI visibility" -> "Create Workspace & Start Audit".

## Ch2 Workspace / navigation
- Top: site switcher (allbirds.com), Search (Cmd+K), "+ New". Header shows date and "5 articles remaining" (trial allowance = 5 articles).
- Sidebar: Home, Projects; Plan & Create: Opportunities, Research, Content, Calendar; Monitor: SEO Analytics (Connect GSC), AI Visibility, Audit, Competitive Analysis, Backlinks; Publish: Review queue, Conversions; Answers; Agent setup: Insights, Signals, Logs; Shared: Results; Help, Automations, Brand Hub, Settings.
- Home: greeting + right rail "Upcoming" (calendar) and "Visibility". Agent bubble (bottom-right mascot) = Frase agent chat available on every page.
- NOTE: screenshots show account name -> blur before publishing.

## Ch6 Site Audit (Monitor > Audit)
- Discovered 500+ URLs from the site. First audit runs on 20 pages automatically; "30 left" badge = remaining audit-page credits in trial (so trial ≈ 50 audit pages, same as Starter monthly).
- Table: Page, State (Never audited/Audited/Failed/Excluded/Not applicable), Score, Issues, Last audited. Tabs: Pages / Issues. Search, Filter, Share, New audit, Stop audit, export icon. Health score top-left. Pagination 50/page.
- Status text: "all 20 pages audited, now analyzing results and computing scores (the longest step)". Auto-refresh.
- Tip: audit credits are scarce on Starter (50/mo) -> select only money pages / top-traffic posts, use Filter.

## Ch7 AI Visibility (Monitor > AI Visibility)
- Header "AI Visibility 2/5" = 2 of 5 tracked prompts used (trial). "+ Add prompt", alert bell. Tabs: Overview, Trends, Prompts, AI referrals, Recommendations, Logs. Date range (Last 7 days), Filter, export.
- KPI cards: Visibility % (answers mentioning you), Share of voice %, Avg. position, Sentiment.
- Rankings scatter (visibility vs share of voice) + table vs tracked competitors (competitors aren't read for sentiment).
- Buyer journey: prompts grouped Awareness / Consideration / Decision; shows where you're missed. Example awareness prompt auto-created: "What are the best sustainable sneakers for everyday wear and travel in 2026?" -> brand not mentioned.
- Platform coverage on trial: Google AI (1 of 2 answers). Higher plans add more engines.
- Citation sources: which domains AI answers cite (13 sites; 93% editorial, 7% community like Reddit/Quora/YouTube); insight "none of it is your site" -> actionable: get featured on those editorial sites / create content AI cites.
- Use case for affiliate/blogger: track prompts like "best AI SEO tool for freelancers" and see which sites AI cites -> target them.
- Recommendations tab: actions with Goal/Result/Priority. Goals: "Get cited" (e.g. "Get into the articles AI quotes" -> 3 sites to pitch, Medium) and "Close gaps" ("Be the first answer to 1 open question", Awareness, Low).

## Ch3 Research (Plan & Create > Research)
- Research hub: views List/Table/Board/Gallery, Search, Group, Filter, "+ New Research". Empty state shows 3 stages: Keyword Discovery -> Search Results (what top pages do) -> Brief Builder.
- "New Research" dialog "What are you writing about?": Topic (topic, search query or working title), Content language (auto-detected from browser! was Vietnamese -> must switch to English (US)), Target market (country for SERP; auto US after language), optional "Audience, goal & brand guidance" (Goal: what should this article accomplish; Audience: who is it for). Then "Run research". Warns when topic language ≠ content language.
- GOTCHA: language/market default to browser locale (Vietnamese/Vietnam for VN users) -> always check before running.
- Research takes ~4-5 min ("Running keywords, SERP, gaps, and evidence together" -> "Collecting supporting evidence..."), Stop button.
- Results page: title + language/market chip; Export; "Generate brief" (disabled until you pin >=1 keyword: "Pin one keyword to begin"). Tabs with pin counters: Keywords, Headings, Questions, Evidence. Tools: Edit setup, Writing inputs, Sources, Ask AI. Left "On this page" nav.
- Sections (each "+N more", "Pin suggestions" to auto-pin):
  1. Keywords: recommended with searches/month + CPC (e.g. "best sustainable sneakers" 20/mo $1.63; "...for women" 10/mo $3.96), +21 more.
  2. What ranks & headings: top results with rank, domain, word count, authority (Low/Medium/High), 1-line summary; pick headings for your outline. +17 more.
  3. Opportunities (content gaps): concrete angles competitors miss with "Research basis" + source domain (e.g. travel-readiness table, wet-weather performance, break-in time ratings). This is the most valuable part.
  4. Questions: audience questions from Reddit and SERP (People Also Ask).
  5. Evidence & insights: citable stats with source names (e.g. market size USD 10.33B 2024 -> 15.98B 2032, CAGR 5.6%, Credence Research). Pin to use as supporting facts -> good for GEO (AI cites stats).
- Pinned inputs feed the brief.

## Ch4 Content Brief
- "Generate brief" -> "Configure Brief" side panel: Content type (18 types: Blog Post, Pillar Guide, How-To, Listicle, Case Study, Tutorial, Page, FAQ, Glossary, Data Report, Resource, Comparison Article ("X vs Y" with verdict/pros/cons), Landing Page, Product Update, Alternatives ("Alternatives to X"), Tool Review (verdict + rating), News, Event) + Target word count (default 1400; Listicle -> 1500; outline distributes sections proportionally). Then "Generate Brief".
- For affiliate sites: Comparison Article, Alternatives, Tool Review, Listicle map 1:1 to the 5 affiliate content types (best/vs/review/alternatives/tutorial).
- Brief generated in <1 min, opens under Content > brief page. Header: Export, Share, "~3m to write", "Generate article".
- Brief contents (all editable via cancel/save):
  * Title suggestion ("8 Best Sustainable Sneakers for Everyday Wear and Travel in 2026"), "View backing research" link.
  * Article details: content type, target words, number of keywords (3-5), sections (8), evidence gathered (30 points ≈ supports ~950 words), reading level (Upper secondary), tone tags (Practical, Authoritative...), funnel stage (Consideration), audience personas (from Brand Hub).
  * Summary; target tone; keyword list (5).
  * KEY FACTS: each fact with ✓ Verified badge, section §, source domain, "I checked this / Use a different page / Remove the link / Quote on file", approve ✓/reject ✕; Add fact, Add source, "Pull key points from your reference docs". Unverified facts show "Add a source".
  * CORE ARGUMENT (thesis).
  * WHAT THE READER WANTS: what they're searching for / how they feel / what they'll do next / connecting theme.
  * WHAT MAKES THIS DIFFERENT (angle vs SERP gaps).
  * ARTICLE OUTLINE: sections with H2, ~words each, "Frase writes" format note (e.g. "H2 + 2 paragraphs + 'Best For' callout"), goal, bullet talking points, EVIDENCE TO INCLUDE (stats/quotes w/ source). Add section, Explore Headings, Assign, Reorder.
- Agent popup appears: "Hi, I am your Frase agent" with suggestions: Audit my site, Find content opportunities, Research a topic.

## Ch5 Writing + Editor + Scores
- From brief: "Generate article" -> Create Content page with steps Topic > Set up > Write. Set up lets you assign each section "Frase writes" vs you write ("Assign sections"). Click "Write" -> "Starting..." -> writes section by section (status bar "Writing '<H2>'"). Took ~3-4 min for ~1,500 words. Uses 1 article credit (5 -> 4 remaining).
- Editor: toolbar (B, I, strike, code, H1-H3, lists, link, image, word count, undo/redo), "Current draft" version dropdown, brand chip, autosave ("Saved just now"), "Connect CMS" button.
- Right rail tools: Score, Checklist, Keyword Research, Brief, Images, Meta Tags, Comments, Ask AI, Share, Guard.
- Checklist panel: Overall "Combined optimization score" gauge (draft went 61 -> 68 while finishing), tiles: Sections x/8, Coverage %, Words, Headers, Links, Images; progress "88% Ready for reviewer". Topic coverage: each target keyword with count; add keyword box. Structure: H1/H2 list with Complete/Writing% per section.
- Observed quirk: structure listed some H2s twice (numbered + unnumbered versions) while finishing -> check for duplicate headings before publishing.
- Draft had 0 images and only 3 links -> add images/alt text and internal links manually to raise score.
- Score panel (content type selector "Listicle" -> weights adjust): Overall 68%; Words 1,484 vs 971 avg of top results; Headers 8 vs 4 avg; Links 3; Images 0. Buttons: "Improve scores" (keeps article current/useful) and "Rewrite" (changes angle/audience/argument) – review before applying.
- Three sub-scores:
  * EEAT 33%: "Get E-E-A-T coaching". Author Profile 13% complete -> completing profile adds up to +14 pts (Author bio +2-4, Job title +2-4, Expertise tags 3+ +1-2, +3 more fields). Trust 68% (3 authority citations, author info), Experience 5% (needs original media), Expertise 25% (good topical depth), Authority 0% (add social profiles & credentials). Note: some EEAT signals (backlinks, brand mentions) only measurable after publishing.
  * GEO 94%: Quotability 88% (standalone stats; tip: turn prose into concise factual statements), Structure 100% (numbered headings, comparison table, bullet summary), Definitions 60% (tip: add glossary/bolded definitions), Takeaways 100% (Bottom Line section), Citable Data 90% (tip: attribute market stats). Shows quoted snippets as evidence. "View authority checklist".
  * SEO 78%: SERP comparison draft vs top 5 (word count, heading count charts), Keywords 74% (primary keyword used; add it to introduction), Meta Tags 100% (title 56 chars, desc 151 chars auto-written), Structure 65% (needs images), Readability 100% (avg 18 words/sentence).
- KEY LESSON: AI draft is strong on GEO/SEO structure but weak on EEAT -> the human must add real experience (own photos/tests), author bio, credentials. This is where to spend editing time.
- "Improve scores" panel: "Keep this article current, useful, and easy to find. Its direction stays the same." Instructions (optional), More options. IMPORTANT: "Counts once toward your monthly content allowance" (= 1 article credit). Article unchanged until you apply. "Back to chat".
- Budget tip: on Starter (10 articles/mo) every Improve/Rewrite eats an article -> fix EEAT manually instead of spending credits.
- Draft quality sample: strong narrative hook ("Mile six of a cobblestone walking tour..."), bolded standalone stat callout with source link, specific product detail, "Best For"/"Packing Score: 9/10" callouts, comparison table, Bottom Line. Reads human-ish; still needs fact check of product claims + personal experience.

## Ch9 Competitive Analysis (Monitor)
- List tabs All/In progress/Complete/Failed, Search, Filter, "+ New analysis".
- New analysis panel: Page to analyze (pick your page or paste ANY URL), Competitors optional (empty = compare vs top search results; or up to 3 URLs head-to-head), Location & Industry optional (defaults from Brand Hub) -> Analyze. Output: what the outranking pages cover that yours doesn't, list of what to add.
- Affiliate use: paste your review URL vs the #1 ranking review to see missing sections.

## Opportunities page: rendered empty in trial at first (likely fills after site scan / needs GSC) – onboarding said it "starts a scan for article ideas".

## Ch11 Automations (sidebar > Automations, URL /autonomy)
- "Automations are the work this site does on its own: publishing content, checking it against your rules, and running playbooks. Turn each one on or off." Buttons: Publishing settings, + Add automation, Runs. Tabs All(9)/Publishing(1)/Rules(3)/Playbooks(5).
- Publishing: FAQ (answers visitors' questions) – "Requires your approval".
- Rules (Created by Frase): AI Citation Ready (GEO signals, takeaways; leaves notes only), Publish-Ready (min SEO, no unverified claims, brand terminology; CAN STOP a publish), Quality Baseline (leaves notes only).
- Playbooks (all "Pauses for approval"): Comparison Article (research options -> brief -> draft -> wait approval), Listicle (research -> brief to approve -> draft list + create images), Product Page (brief -> draft + images -> approve), Quick Update (rewrite an existing page for search, check rules; start from the page), SEO Blog Post (research -> brief approve -> draft -> rule check).
- Toggle on/off per automation. Safety: everything starts with human approval.

## Ch12 Billing / Trial limits (Settings > Billing & Usage) – verified in-app
- "7 days left in your trial", Upgrade Now, Current Plan "trial Plan", Change Plan.
- Trial usage limits: Articles 5, Hero Images 5, AI Images 25, AI Visibility Prompts 5, Research 15, Audit Pages 50, API Requests 5,000, Domains 1, Team Seats 3. Image credits: 5 monthly, purchasable credits never expire.
- Domains, seats and AI Visibility prompts are CONCURRENT limits (don't reset); others reset monthly.
- Our usage after full walkthrough: 1 article, 1 research, 19 audit pages, 2 prompts.
- Settings menu: Profile, Preferences, Organization, Sites, Team, Security & SSO, Content Guard, Billing & Usage, Usage & Budgets, FraseCMS, Frase Answers, Integrations, Webhooks, API & MCP Activity, API Keys, Client Portal, Trash.

## Plans as shown in-app checkout (verified 2026-11-15)
- Feature chips included in all: AI Agent, SEO+GEO Optimization, AI Visibility Tracking, Content Guard, Site Audits, API & MCP, Brand Voice.
- Starter $49/mo monthly, $39/mo billed annually: "Get one site ranking in Google and showing up in AI answers — on your own." 10 articles/mo researched & drafted; AI Visibility on ChatGPT & Google AI; Content Guard watches 10 pages; Playbooks, API, MCP, CLI; 1 seat, 1 domain, 50 audit pages/mo.
- Professional (Most Popular) $129 monthly / $103 annual: 40 articles/mo with Agent; AI Visibility ChatGPT, Perplexity & Google AI; Content Calendar, internal linking & atomization; optional auto-publish FAQs & how-tos (off by default); Content Guard 75 pages; 3 seats, 5 domains, 250 audit pages/mo; extra seats $29/mo.
- Scale (High Volume) $299 monthly / $239 annual: 100 articles/mo across brands; AI Visibility 5 platforms incl. Claude & Gemini; atomization, auto-linking, data exports; optional auto-publish to FraseCMS all types (off by default); Content Guard 300 pages; 5 seats, 10 domains, 1,000 audit pages/mo; extra seats $29/mo.
- Publish anywhere: WordPress, Webflow, Sanity, Wix, FraseCMS. Cancel anytime, no lock-in, Stripe checkout. "Save $312/year with annual billing" (Professional). Enterprise: SSO, white-label, dedicated manager -> talk to sales.
- NOTE: Content Guard limits differ from third-party July data (3/15/50) -> now 10/75/300. Update the published review!
