# Claude Code — Continue the World Music Survey (loop instructions)

You are continuing a large, multi-session project: a deep, chronological, listenable survey of the
world's music, region by region. The United States and Europe are COMPLETE. Latin America is IN
PROGRESS. Your job is to keep building installments in order until the roadmap is done, following the
established conventions exactly.

## Read these first (context)
1. `WORLD_MUSIC_SURVEY_ROADMAP.md` — the plan, region order, conventions, and STATUS TRACKER.
2. `MASTER_GUIDE_american_music_survey.md` and `MASTER_GUIDE_european_music_survey.md` — reference
   examples of the finished style, structure, and tone.
3. Any existing `<region>_*_IMPORT.txt` files for the region in progress — so you don't duplicate.

## The loop (repeat until roadmap complete)
1. Open the roadmap's status tracker. Find the first region that is IN PROGRESS or, if none, the
   first "not started" region in build order.
2. Determine the next installment for that region (per its planned installment list / era template).
3. Build that ONE installment (see "How to build an installment" below).
4. Update the roadmap: mark progress in the status table AND append a line to the Progress log.
5. If that was the region's LAST installment, also build the region's master:
   `MASTER_GUIDE_<region>_survey.md` + deduplicated `MASTER_<REGION>_FULL_SURVEY_IMPORT.txt`
   (dedup logic below), then flip the region to COMPLETE.
6. Stop and report what you built, or continue to the next installment if running unattended.

## How to build an installment
Produce TWO files:
- `<region>_<N>_<ERA>.md` — narrative. Start with a title + a short framing paragraph. Then 5-10
  sections; each section = a bold-ish header, a 2-4 sentence intro explaining WHAT it is and what it
  fed into, then a list of `- Title — Artist` (or `- Title — (Traditional)`).
- `<region>_<N>_<ERA>_IMPORT.txt` — clean import: one `Title - Artist` per line; for traditional
  pieces with no definitive recording, a BARE title (no " - Artist"). No headers, notes, or blanks.

Aim ~30-90 tracks per installment, ~6-12 per section. Weave art music + folk/traditional + popular
music chronologically. Name canonical performers where they exist; for classical/art music name the
WORK not the performer; use "(Traditional)"/bare title otherwise.

## HARD RULES (these caused repeated errors — do not repeat them)
- ONE song per line. NEVER cram two titles into one entry (no "SongA style - SongB", no "flag").
  If you catch a garbled entry, fix it before presenting.
- Region integrity: every artist must actually belong to the region. Verify. When an artist is a
  judgment call (e.g. broke in a different region), keep or cut with a STATED reason in the .md.
- Preserve difficult/ugly history with context + content warnings; don't sanitize it away.
- Cross-link to other regions where traditions connect (note it in the intro prose).
- Deduplicate within each region's master by normalized key = lowercased title + artist, with
  parentheticals and punctuation stripped, keeping first occurrence in chronological file order.

## Build method (recommended)
Write a small Python script (like the existing `build_*.py`) that holds the data as
`(section_title, intro, [(title, artist_or_None), ...])`, then emits both the `.md` and the
`_IMPORT.txt`. This keeps data in one place and avoids copy errors. Save outputs to the working
directory. Then present/commit the two files.

## Region build order (from roadmap)
Latin America (IN PROGRESS) -> Sub-Saharan Africa [West, Southern, Central, East, Sahel] ->
India/South Asia -> East Asia [China, Japan, Korea] -> MENA -> Southeast Asia -> Caribbean ->
Central Asia & Caucasus -> Oceania/Pacific -> Jewish diaspora -> (optional global-fusion capstone
+ grand master index).

## Definition of done
Every region COMPLETE in the status tracker, each with its installments + master guide + deduplicated
full-survey import file, and the roadmap's progress log reflecting all of it.
