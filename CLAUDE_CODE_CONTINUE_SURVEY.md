# Claude Code — Continue the World Music Survey (COLD-START RUNBOOK)

You are one iteration of an **unattended, self-re-arming loop**. Each firing is a **fresh session
with zero prior context** — everything you need is in this repo. Your job: build **exactly ONE
installment**, push it, then **re-arm the loop** so the next fresh session builds the next one.
Make sensible editorial calls; **do not ask the user questions** — you are running unattended.

The project is a deep, chronological, *listenable* survey of the world's music, region by region.
Each installment is a narrative `.md` + a clean `_IMPORT.txt` (one track per line) that imports
straight into YouTube Music / Spotify via TuneMyMusic.

**The roadmap file `WORLD_MUSIC_SURVEY_ROADMAP.md` is the single source of truth for what's next.**
Never guess the next installment from memory — read the roadmap.

---

## STEP 0 — Git setup (you may be in a cold container)

The survey lives in its own repo: `github.com/devbasilmartin/world-music-survey`, working copy at
`/home/user/world-music-survey`. The git **push proxy is spawn-specific** — a persisted clone's
remote URL can be stale, so refresh access every run:

1. Ensure the repo is in session scope + get a fresh clone command:
   call the `add_repo` MCP tool with `owner=devbasilmartin, repo=world-music-survey`. It returns a
   clone command containing the **current** proxy URL (looks like
   `http://local_proxy@127.0.0.1:<PORT>/git/devbasilmartin/world-music-survey`). Note that URL.
2. If `/home/user/world-music-survey` does **not** exist: run the clone command `add_repo` gave you.
   If it **does** exist: `cd /home/user/world-music-survey`, point the remote at the fresh URL
   (`git remote set-url origin <fresh-url>`), then `git pull --ff-only origin main`.
3. One-time-per-session config:
   `git -C /home/user/world-music-survey config http.proxyauthmethod basic`
   `git config user.name "Claude"` and `git config user.email "noreply@anthropic.com"` if unset.
4. `cd /home/user/world-music-survey` for everything below.

If a push later fails with a network/proxy error, re-run `add_repo`, `git remote set-url` to the new
URL, and retry (up to 4x, exponential backoff 2s/4s/8s/16s).

---

## STEP 1 — Pick the next installment (from the roadmap)

Read `WORLD_MUSIC_SURVEY_ROADMAP.md`: the **status tracker table** + the **Progress log** at the
bottom. Determine the next unit of work:

- The **active region** = the first region marked `IN PROGRESS`. Its next installment number = (done
  count) + 1. The most recent Progress-log entry for that region ends with a `Next: ...` line naming
  exactly what to build and its era/scope — **follow it**.
- If **no** region is `IN PROGRESS`, the active region = the first `not started` region in build
  order; build its installment **#1**.
- If **every** region is `COMPLETE`, the survey is done — see STEP 8 (do NOT re-arm).

Region build order (from the roadmap):
Latin America → Sub-Saharan Africa [West, Southern, Central, East, Sahel] → India/South Asia →
East Asia [China, Japan, Korea] → MENA → Southeast Asia → Caribbean → Central Asia & Caucasus →
Oceania/Pacific → Jewish diaspora → (optional global-fusion capstone + grand master index).

Before writing, read the region's existing `<region>_*_IMPORT.txt` files so you don't duplicate, and
skim `MASTER_GUIDE_american_music_survey.md` / `MASTER_GUIDE_european_music_survey.md` once if you
need a reminder of the finished style/tone.

---

## STEP 2 — Build the installment (write a Python build script)

Hold the data in a Python script `build_<stem>.py` (mirror the existing `build_*.py`) as
`SECTIONS = [(section_title, intro, [(title, artist_or_None), ...]), ...]`, then emit both files with
this exact function (keeps data in one place, avoids copy errors):

```python
def build():
    md = [f"# {TITLE}", "", FRAMING, ""]
    imp = []
    for sec_title, intro, tracks in SECTIONS:
        md += [f"## {sec_title}", "", intro, ""]
        for title, artist in tracks:
            if artist:
                md.append(f"- {title} — {artist}")
                imp.append(f"{title} - {artist}")
            else:
                md.append(f"- {title} — (Traditional)")
                imp.append(title)          # artist=None => BARE title in the import file
        md.append("")
    with open(f"{STEM}.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md).rstrip() + "\n")
    with open(f"{STEM}_IMPORT.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(imp) + "\n")
```

Naming: `<region-stem>_<N>_<ERA>` — e.g. `ssa_central_music_5_SOUKOUS_GLOBAL_NDOMBOLO`. Keep the
region-stem consistent with the region's existing files.

Shape: a title + a short framing paragraph, then **6–12 sections**; each section = a header, a 2–4
sentence intro (WHAT it is + what it fed into / cross-links), then the track lines. Aim **~30–90
tracks** total. Weave art music + folk/traditional + popular music chronologically. Name canonical
performers where they exist; for classical/art music name the **WORK not the performer**; use
`artist=None` (→ bare title) for living traditions / pieces with no single definitive recording.

---

## HARD RULES (these caused real errors — honor them)

- **DEDUP IS BY TITLE ONLY.** The validation `norm()` takes only the text **before** the first
  ` - ` (it discards the artist), strips parentheticals, folds accents, lowercases, and removes
  non-alphanumerics. **Therefore every song TITLE must be unique across the ENTIRE region** (all of
  that region's installments). Two different songs that share a title collide even with different
  artists — disambiguate one of them (e.g. add a descriptive parenthetical that changes the leading
  words, or reword the bare-title entry). Do NOT reuse a title already used earlier in the region.
- **ONE song per line.** Never put two ` - ` separators on one line (no "SongA - SongB"). One title,
  optionally one ` - Artist`.
- **No blank lines** in the `_IMPORT.txt`.
- **Region integrity:** every named artist must genuinely belong to the region. When an artist is a
  judgment call (broke elsewhere, diaspora, guest), keep or cut with a **stated reason in the .md**
  prose (not in the import file).
- **Preserve difficult/ugly history** with context + content warnings in the prose; don't sanitize.
- **Cross-link** to connected regions in the intro prose where traditions genuinely connect.

---

## STEP 3 — Validation gate (run before committing; must PASS)

Run this inline (adjust `STEM` and the prior-file glob to the region). It must print PASSED:

```python
import re, glob, sys
STEM = "<the stem you just built>"
PRIOR_GLOB = "<region-stem>_*_IMPORT.txt"   # this region's installments (includes the new one)
imp = f"{STEM}_IMPORT.txt"

def norm(s):
    s = s.split(' - ')[0] if ' - ' in s else s          # TITLE ONLY — artist discarded
    s = re.sub(r'\([^)]*\)', '', s)
    for a,b in [('á','a'),('é','e'),('í','i'),('ó','o'),('ú','u'),('ñ','n'),('ü','u'),
                ('ç','c'),('ã','a'),('õ','o'),('â','a'),('ê','e'),('ô','o')]:
        s = s.replace(a,b)
    return re.sub(r'[^a-z0-9]', '', s.lower())

lines = [l.rstrip('\n') for l in open(imp, encoding='utf-8')]
errs = []
for i,l in enumerate(lines,1):
    if l.count(' - ') >= 2: errs.append(f"two-sep line {i}: {l}")
    if l.strip() == '':     errs.append(f"blank line {i}")
seen = {}
for i,l in enumerate(lines,1):
    k = norm(l)
    if k in seen: errs.append(f"internal dup line {i}: '{l}' vs line {seen[k][0]} '{seen[k][1]}'")
    else: seen[k] = (i,l)
prior = {}
for f in sorted(glob.glob(PRIOR_GLOB)):
    if f == imp: continue
    for l in open(f, encoding='utf-8'):
        l = l.rstrip('\n')
        if l.strip(): prior.setdefault(norm(l), f)
for i,l in enumerate(lines,1):
    if norm(l) in prior: errs.append(f"CROSS dup line {i}: '{l}' already in {prior[norm(l)]}")
named = sum(1 for l in lines if ' - ' in l)
print(f"Lines: {len(lines)} | named: {named} | bare: {len(lines)-named}")
if errs: print("VALIDATION FAILED:\n" + "\n".join("  "+e for e in errs)); sys.exit(1)
print("VALIDATION PASSED")
```

If it fails, fix the data in the build script, re-run STEP 2 then STEP 3, until it passes.

---

## STEP 4 — Update the roadmap

Edit `WORLD_MUSIC_SURVEY_ROADMAP.md`:
1. Update the active region's **status-table row**: bump the done count and total track count, and
   rewrite its short summary + the `next #<N+1> ...` hint.
2. Append a dated entry to the **Progress log**: region, installment number + title, filenames, track
   count / section count / named count, a 2–4 sentence content summary, cross-links, content notes,
   dedup confirmation ("No dups vs #1–<N-1>"), and a `Next: <region> #<N+1> <era + scope sketch>`
   line (or, if you just finished the region, `Next: <next region> #1 ...`).

---

## STEP 5 — Region master (ONLY when you just built a region's LAST installment)

If this installment completes the region (per its planned installment count in the roadmap):
1. Build `MASTER_GUIDE_<region>_survey.md` — a narrative guide stitching the region's installments
   into one overview (intro + per-installment section summaries + through-lines).
2. Build `MASTER_<REGION>_FULL_SURVEY_IMPORT.txt` — concatenate the region's installment
   `_IMPORT.txt` files **in order 1..N**, keeping the **first occurrence** of each `norm()` key
   (dedup by the same TITLE-ONLY norm above). Verify raw-line-count vs deduped-count and report both.
3. In the roadmap, flip the region to **COMPLETE** (fill its master filename), and set the next
   region to `IN PROGRESS` / active (or note the survey is done if it was the last region).

---

## STEP 6 — Commit & push

```
git add -A
git commit -m "<Region> #<N>: <Title> (<era>) — <T> tracks"
git push -u origin main        # retry 4x w/ exponential backoff on network error (see STEP 0)
```
Do NOT include any model identifier in the commit message. Do NOT open a pull request.

---

## STEP 7 — Deliver to the user

Use the `SendUserFile` tool to send the new `.md` and `_IMPORT.txt` (and, on a region-completion
run, the two master files) with a one-paragraph caption: what the installment covers, track/section
counts, and the commit hash. Status `normal`.

---

## STEP 8 — Re-arm the loop (spawn the next fresh session)

This is what keeps the loop going. **Unless the survey is fully COMPLETE**, create the next
iteration as a fresh-session one-shot trigger:

- Tool: `create_trigger` (claude-code-remote MCP).
- `create_new_session_on_fire = true`  (fresh session, zero-context — this is the whole point).
- `run_once_at` = **now + ~3 minutes** (RFC3339, UTC). This paces the loop and lets this session
  finish first.
- `name` = e.g. `"World Music Survey — next installment"`.
- `prompt` = the **generic bootstrap** below (identical every iteration — the next session derives
  what to build from the roadmap, so no per-installment pointer is needed):

  > Fresh unattended iteration of the World Music Survey loop. Read
  > `/home/user/world-music-survey/CLAUDE_CODE_CONTINUE_SURVEY.md` and follow it EXACTLY, top to
  > bottom: set up git (STEP 0, use the `add_repo` tool — the git proxy is spawn-specific), read the
  > roadmap to pick the next installment, build ONE installment, run the validation gate, update the
  > roadmap, build the region master if it's the region's last installment, commit & push, deliver
  > with SendUserFile, then re-arm the next fresh session per STEP 8. Build exactly ONE installment.
  > Do not ask questions — make sensible calls. Stop re-arming only if the whole roadmap is COMPLETE
  > or the user said to stop.

If **every** region is COMPLETE: do NOT re-arm. Post a final summary to the user and stop.

**Stop condition:** the loop ends when the roadmap is fully COMPLETE, or when the user says to stop
(if a human is present and says stop, do not re-arm).

---

## Why fresh sessions

Each iteration runs in a brand-new session so context never accumulates (an earlier version re-fired
into one long-lived session and grew to ~400k tokens). All continuity lives on disk: the roadmap
(what's next + the TITLE-ONLY dedup rule), the prior `_IMPORT.txt` files (dedup source), and this
runbook. That's why STEP 0 can rebuild everything from a cold container.

## Definition of done

Every region COMPLETE in the status tracker, each with its installments + master guide + deduplicated
full-survey import file, and the Progress log reflecting all of it. Then the loop stops re-arming.
