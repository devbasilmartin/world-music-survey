# World Music Survey — Master Roadmap

A living plan for building a deep, chronological, listenable survey of **every major music region on
Earth**, in the same style as the completed United States and Europe surveys. This file is the
reference for future sessions: it defines the regions, the era-structure for each, the shared
conventions, and a status tracker. Update the status table as installments are completed.

---

## The mission

For each region: tell the story of how its music evolved, from the earliest we can represent through
today, weaving **art/classical + folk/traditional + popular music** into one chronological narrative,
delivered as (1) readable `.md` installments with per-strand context and (2) clean `Title - Artist`
`.txt` import files for YouTube Music (via TuneMyMusic).

The goal is not exhaustiveness but a **coherent through-line** per region — roughly 6–12 tracks per
strand to *tell the story*, not catalog every scene. Target ~300–800 tracks per region depending on
size and documented history.

---

## Shared conventions (locked in from the US & Europe surveys)

1. **Deliverables per installment:** one `<region>_N_<ERA>.md` (narrative) + one
   `<region>_N_<ERA>_IMPORT.txt` (clean `Title - Artist`, one per line, no headers/notes).
2. **Master files per region:** a `MASTER_GUIDE_<region>_survey.md` (continuous narrative + manifest)
   and a deduplicated `MASTER_<REGION>_FULL_SURVEY_IMPORT.txt`.
3. **Import format:** `Title - Artist`. For traditional pieces with no single definitive recording,
   use a **bare title** (no artist) so the search surfaces a version to choose. Mark it "(Traditional)"
   in the `.md` only.
4. **Pre-recording eras:** name period-authentic or canonical performers where they genuinely exist;
   otherwise "(Traditional)". Be honest that these will need manual searching in the "Missing" report.
5. **Classical/art music:** name the **work, not the performer** (many recordings exist).
6. **Scope calls get flagged, not buried:** when an artist's nationality/region is a judgment call,
   keep or cut with a stated reason (as with Drake in the US survey, Hendrix in the Europe survey).
7. **Weave the streams:** every era section should show art music, folk, and pop running in parallel
   and cross-feeding — that braid IS the story.
8. **Cross-links:** note where a region interlocks with others (e.g., West Africa -> US blues;
   Latin salsa -> US survey; Arab maqam -> Andalusian/Spanish music). The surveys are a connected web.
9. **Content honesty:** preserve difficult/ugly history with context and content warnings rather
   than sanding it off (as with US minstrelsy).
10. **Watch for two recurring errors:** (a) garbled two-songs-in-one-line entries — write ONE clean
    entry per line; (b) artists from the wrong region sneaking in — verify region per artist.

---

## The regions (planned build order)

Ordered roughly by closeness to what's already built and by how self-contained the story is.

### DONE
- **United States** — complete. 839 tracks, 11 era files + master. (colonial recreations -> 2020s)
- **Europe** — complete. 403 tracks, 9 installments + master. (Gregorian chant c.800 -> modern EDM)
- **Latin America** — complete. 371 tracks, 7 installments + master. (Indigenous/colonial -> reggaeton)
- **Sub-Saharan Africa: West** — complete. 256 tracks, 7 installments + master. (griot/kora -> Afrobeats)
- **Sub-Saharan Africa: Southern** — complete. 249 tracks, 7 installments + master. (San/mbira -> amapiano)
- **Sub-Saharan Africa: Central** — complete. 268 tracks, 7 installments + master. (maringa/Cuban rumba -> ndombolo/kuduro/global Afropop)
- **Sub-Saharan Africa: East** — complete. 229 tracks, 5 installments + master. (taarab/nyatiti -> benga/dansi -> bongo flava/singeli/gengetone)
- **Sub-Saharan Africa: Sahel** — complete. 175 tracks, 4 installments + master. (Moorish/Tuareg/Songhai roots -> desert blues -> Tinariwen/wassoulou -> crisis & today) ★ **ALL SUB-SAHARAN AFRICA COMPLETE** (West+Southern+Central+East+Sahel = 5 sub-surveys, 1177 tracks)

### TIER 1 — the big, self-contained stories (build next, in this order)
1. **Latin America** — closest sibling to the US survey; same colonial start + Indigenous/European/
   African fusion, different result. Interlocks with the US survey.
2. **Sub-Saharan Africa** — the deep rhythmic root of both existing surveys. Too big for one story;
   split into sub-surveys (see below).
3. **India / South Asia** — one of Earth's great classical systems (two, really) + the Bollywood
   pop juggernaut. Enormous, self-contained.
4. **East Asia** — build as SEPARATE surveys per country (distinct classical traditions + very
   different modern pop): **China**, **Japan**, **Korea**.

### TIER 2 — coherent regional traditions
5. **Middle East & North Africa (MENA)** — the Arab classical/maqam lineage + Persian + Turkish +
   modern pop. (Persian and Turkish may warrant their own sub-threads.)
6. **Southeast Asia** — gamelan (Indonesia), Thai/Vietnamese/Filipino traditions, and distinct
   modern pop scenes.
7. **The Caribbean** — arguably could pair with Latin America, but reggae/ska/dancehall/soca/calypso
   is its own huge story that feeds global pop. Decide: standalone or Latin-America annex.

### TIER 3 — rounding out the planet
8. **Central Asia & the Caucasus** — Silk Road traditions, throat singing, Azeri mugham, etc.
9. **Oceania / Pacific** — Aboriginal Australian, Maori, Pacific Islander traditions + modern.
10. **The Jewish diaspora** — a cross-regional thread (Sephardic, Ashkenazi/klezmer, Mizrahi,
    Israeli) that could be its own survey given how it threads through many regions.

---

## Sub-Saharan Africa — sub-survey breakdown (it's too big for one)

Build as connected but separate surveys:
- **West Africa** — griot tradition, highlife, juju, Afrobeat (Fela), Mande music, modern Afrobeats
  (Nigeria/Ghana). The most direct root of American blues/jazz rhythm — cross-link heavily to the US.
- **Southern Africa** — mbaqanga, isicathamiya (Ladysmith), township jazz, kwela, kwaito, amapiano.
- **Central Africa** — Congolese rumba/soukous, the continent's most influential dance-music engine.
- **East Africa** — Ethiopian jazz (Ethio-jazz/Mulatu), taarab (Swahili coast), benga, modern
  bongo flava.
- **Sahel & the Islamic north edge** — desert blues (Tinariwen), Malian traditions (crosslinks to
  both West Africa and MENA).

---

## Standard era-template per region (adapt as the region's history requires)

Most regions follow a version of this arc; not every region has every stage, and start-dates vary
enormously (Europe starts ~800 CE; some oral traditions can only be represented via 20th-c.
recordings):

1. **Ancient / deep traditional roots** — the oldest representable layer (often via modern
   recordings of living tradition; be honest about this).
2. **Classical / court / art-music tradition** — where one exists (Hindustani/Carnatic, Chinese
   court music, Arab classical, gamelan, etc.).
3. **Colonial / cross-contact era** — fusion begins (especially in the Americas, Africa, SE Asia).
4. **Early recording era** — first captured popular forms, ~1900–1940s.
5. **Mid-century golden age** — the classic era of the region's popular music.
6. **Independence / modern nation-building era** — often a musical flowering (post-colonial 1950s-70s).
7. **Late 20th-c. pop** — the region's distinct popular mainstream.
8. **Contemporary / global era** — how the region's music sounds now and how it feeds/draws from
   global pop (Afrobeats, reggaetón, K-pop, etc.).

---

## Status tracker (update each session)

| Region | Status | Installments | Tracks | Notes |
|---|---|---|---|---|
| United States | COMPLETE | 11 + master | 839 | colonial -> 2020s |
| Europe | COMPLETE | 9 + master | 403 | chant -> EDM |
| Latin America | COMPLETE | 7 + master | 371 | Colonial→streaming era; master built, deduped, zero cross-installment dups |
| Sub-Saharan Africa: West | COMPLETE | 7 + master | 256 | griot/kora→Afrobeats; master built, deduped, zero cross-installment dups |
| Sub-Saharan Africa: Southern | COMPLETE | 7 + master | 249 | San/mbira→amapiano; master built, deduped, zero cross-installment dups |
| Sub-Saharan Africa: Central | COMPLETE | 7 | 268 | #1-7 rumba roots→golden age→soukous→Zaiko→ndombolo→Angola/Cameroon→modern global; master: MASTER_GUIDE_ssa_central_survey.md (268 tracks, 0 dups) |
| Sub-Saharan Africa: East | COMPLETE | 5 | 229 | #1-5 taarab/nyatiti→benga→cassette→bongo flava/genge→streaming/global; master: MASTER_GUIDE_ssa_east_survey.md (229 tracks, 0 dups) |
| Sub-Saharan Africa: Sahel | COMPLETE | 4 | 175 | #1-4 desert roots→Malian foundation→global desert-blues→crisis/today; master: MASTER_GUIDE_ssa_sahel_survey.md (175 tracks, 0 dups). **All Sub-Saharan Africa now COMPLETE.** |
| India / South Asia | IN PROGRESS | 5 | 229 | ACTIVE. #1-5 classical→folk→devotional→Bollywood golden age; next #6 modern filmi & Indipop (R.D. Burman→A.R. Rahman→Indipop, ~1970-2010) |
| East Asia: China | not started | — | — | Tier 1 #4a |
| East Asia: Japan | not started | — | — | Tier 1 #4b |
| East Asia: Korea | not started | — | — | Tier 1 #4c |
| MENA (Arab/Persian/Turkish) | not started | — | — | Tier 2 #5 |
| Southeast Asia | not started | — | — | Tier 2 #6 |
| Caribbean | not started | — | — | Tier 2 #7 (standalone vs Latin annex — decide) |
| Central Asia & Caucasus | not started | — | — | Tier 3 #8 |
| Oceania / Pacific | not started | — | — | Tier 3 #9 |
| Jewish diaspora | not started | — | — | Tier 3 #10 (cross-regional) |

---

## Progress log
- 2026-07-19 — Latin America #2 "Independence & the Criollo Century (c. 1800-1900)" built:
  `latam_music_2_INDEPENDENCE_CRIOLLO.md` + `_IMPORT.txt` (55 tracks, 8 sections). Anthems +
  creole salon/opera + Cuban danzon + Rioplatense proto-tango + Brazilian choro + Mexican
  vals/mariachi seeds + criollo folk + Afro-descendant currents. Scope calls flagged: Gottschalk
  cut (US); Iradier's "La Paloma" kept as the Spain↔Cuba habanera hinge. No dups vs #1. Next: #3
  early-recording golden age (~1900-1940: tango-cancion/Gardel, samba, son cubano, bolero).

- 2026-07-19 — Latin America #3 "The Recording Era & the Golden Age (c. 1900-1940)" built:
  `latam_music_3_RECORDING_GOLDEN_AGE.md` + `_IMPORT.txt` (53 tracks, 8 sections). Tango golden
  age/Gardel + birth of samba + son cubano/rumba craze + revolution corridos & ranchera + Agustin
  Lara's bolero + pan-Latin songbook + Andean criollo song + nationalist art music (Villa-Lobos,
  Chavez, Revueltas, Ginastera) + coastal-Colombia cumbia/vallenato seeds. Scope calls: Carmen
  Miranda kept (Portuguese-born, Rio-made); Rafael Hernandez (PR) kept as pan-Latin bolero, with
  the open Caribbean-survey question flagged. No dups vs #1/#2. Next: #4 mid-century golden age
  (~1940-1960: mambo/Pérez Prado, Los Panchos, ranchera cinema/Negrete-Infante, bossa nova onset).

- 2026-07-19 — Latin America #4 "The Mid-Century Golden Age (c. 1940-1960)" built:
  `latam_music_4_MIDCENTURY_GOLDEN_AGE.md` + `_IMPORT.txt` (53 tracks, 8 sections). Mambo
  explosion/Pérez Prado & Beny Moré + Afro-Cuban big band/Latin-jazz roots + Los Panchos bolero-trio
  era + ranchera cinema (Negrete/Infante/José Alfredo/Lola Beltrán) + Brazilian samba-canção to the
  bossa-nova threshold (João Gilberto 1959) + Andean/criollo revival & nueva-canción roots + Colombian
  cumbia/vallenato going national + mid-century art music + cha-cha-chá crossover. Scope calls flagged:
  Historia de un Amor (Panama) and Tito Puente (Nuyorican) kept as pan-Latin/shared-axis, noted. No
  dups vs #1-3. Next: #5 the Boom (~1960-1975: bossa nova & Tropicália, nueva canción/Violeta &
  Víctor Jara, salsa's birth in NY, Nueva Trova).

---

- 2026-07-19 — Latin America #5 "The Boom (c. 1960-1975)" built:
  `latam_music_5_THE_BOOM.md` + `_IMPORT.txt` (58 tracks, 8 sections). Bossa nova goes global
  (Jobim/Gilberto/Baden Powell) + MPB festival era (Chico Buarque, Vandré, Milton) + Tropicália
  (Caetano, Gil, Os Mutantes, Gal, Tom Zé) + nueva canción (Violeta Parra, Víctor Jara, Quilapayún,
  Inti-Illimani, Mercedes Sosa) + Cuban nueva trova (Silvio, Pablo Milanés) & Mexican canto nuevo
  (Amparo Ochoa, Óscar Chávez, Los Folkloristas) + birth of salsa/Fania in NY (Palmieri, Willie Colón
  & Héctor Lavoe, Celia Cruz, Barretto) + Andean/folk-roots deepening (Simón Díaz, Cafrune, Perú Negro)
  + the international art-music vanguard (Ginastera's Bomarzo, Brouwer, late Villa-Lobos). Content
  warnings kept: Víctor Jara's 1973 murder, the Tropicalistas' jailing/exile, Vandré's exile. Scope
  call flagged: NY-made Fania salsa kept as the direct continuation of the Cuban/Latin dance lineage
  (also lives in the US and open Caribbean surveys). No dups vs #1-4. Next: #6 late-20th-c. pop
  (~1975-95: salsa's romantic turn & Rubén Blades, Brazilian rock/MPB maturity, rock en español's
  birth, the rise of Andean/tropical crossover, cumbia's continental spread).

- 2026-07-19 — Latin America #6 "Late-20th-Century Pop (c. 1975-1995)" built:
  `latam_music_6_LATE20C_POP.md` + `_IMPORT.txt` (62 tracks, 9 sections). Salsa dura/consciente &
  the Fania peak (Rubén Blades, Héctor Lavoe, Oscar D'León) + salsa romántica & merengue crossover
  (Juan Luis Guerra) + MPB's golden maturity/Clube da Esquina (Elis, Milton, Djavan, Ivan Lins) +
  BRock (Legião Urbana, Paralamas, Titãs, Cazuza) + Argentine rock nacional under the junta (Charly
  García, Spinetta, Fito Páez) + rock en español going continental (Soda Stereo, Los Prisioneros,
  Cadillacs, Caifanes, Maná) + cumbia/chicha's continental conquest (Carlos Vives, Los Mirlos,
  Chacalón, Los Kjarkas) + the balada & ranchera revival (José José, Juan Gabriel, Roberto Carlos,
  Vicente Fernández) + Piazzolla's nuevo tango & the instrumental vanguard (Gismonti). Content
  warnings kept: the Southern Cone dictatorships and rock-as-coded-resistance, Cazuza & AIDS. Scope
  calls flagged: Blades (Panama), Lavoe/salsa romántica (PR), Guerra/merengue (DR) kept as pan-Latin;
  Rocío Dúrcal (Spain) cut. No dups vs #1-5. Next: #7 contemporary/global (~1995-present: reggaetón's
  rise, Latin-pop crossover & the "Latin explosion", axé/pagode & Brazilian funk, nueva/indie, and
  the streaming-era global takeover) — the region's final planned installment, so also build the
  region master then flip COMPLETE.

- 2026-07-19 — Latin America #7 "Contemporary / Global (c. 1995-present)" built:
  `latam_music_7_CONTEMPORARY_GLOBAL.md` + `_IMPORT.txt` (61 tracks, 9 sections). Reggaetón's birth
  (El General, Vico C, Daddy Yankee, Tego, Ivy Queen) + the Latin explosion (Ricky Martin, Shakira,
  Juanes, Carlos Vives) + Brazilian axé/pagode/samba revival (Daniela Mercury, Olodum, Zeca
  Pagodinho) + funk carioca/sertanejo (Anitta, Michel Teló) + Latin alternative (Café Tacvba,
  Molotov, Aterciopelados, Cerati) + new folk/nueva-canción heirs (Drexler, Lafourcade, Lila Downs,
  Susana Baca, Chavela Vargas) + neo-tango & bossa revival (Gotan Project, Bajofondo, Santaolalla,
  Marisa Monte) + streaming-era takeover (Despacito, J Balvin, Karol G, Bad Bunny, Maluma, Peso
  Pluma) + contemporary art music (Márquez's Danzón No. 2, Golijov, Gabriela Ortiz). Scope calls
  flagged: PR/Panama/DR urbano kept pan-Latin; Enrique Iglesias, Rosalía, Rocío Dúrcal, Gabriela
  Lena Frank cut as European/US. No dups vs #1-6.

- 2026-07-19 — **Latin America COMPLETE.** Region master built: `MASTER_GUIDE_latam_survey.md`
  (continuous narrative + braid + cross-links + manifest) and `MASTER_LATAM_FULL_SURVEY_IMPORT.txt`.
  The seven installments sum to **371 tracks with ZERO cross-installment duplicates** — every track
  in the master is unique (raw 371 → deduped 371). Region flipped COMPLETE; next active region set to
  Sub-Saharan Africa: West (Tier 1 #2a). Next: SSA-West #1, the earliest representable layer —
  griot/Mande roots (Sundiata/kora, praise song), then work forward toward highlife/juju/Afrobeat/
  modern Afrobeats, cross-linking heavily to the US blues/jazz rhythmic root.

- 2026-07-19 — **Sub-Saharan Africa: West #1** "Griot / Mande Roots (deep-traditional layer)" built:
  `ssa_west_music_1_GRIOT_MANDE_ROOTS.md` + `_IMPORT.txt` (43 tracks, 7 sections; 23 living-tradition
  bare titles). The jeli/griot & the Sunjata epic + the kora (Toumani Diabaté, Ballaké Sissoko, the
  Gambian Konte/Jobarteh lines, Sona Jobarteh) + balafon & ngoni (Sosso Bala, Bassekou Kouyaté, Neba
  Solo) + the jelimuso women singers (Kandia Kouyaté, Ami Koïta, Tata Bambo, Fanta Damba) + djembe/
  dunun percussion (Mamady Keïta, Famoudou Konaté) + non-Mande deep traditions (Wolof sabar, Fula
  flute, Hausa court music, Yoruba dùndún/bàtá, Akan royal drums) + the Atlantic cross-links (akonting
  → banjo, Mande pentatonic → blues, Yoruba orisha drums → Cuban batá/Brazilian candomblé, bell →
  clave). Region-integrity flag: Sona Jobarteh (UK-raised, Gambian griot lineage) kept as West
  African. Content note kept: the diaspora transmission is inseparable from slavery. First file of the
  region, so no dedup priors. Next: SSA-West #2 palm-wine guitar & the early recording era (~1900-1950:
  the Kru sailors' guitar, maringa/Ghanaian & Sierra Leonean palm-wine, early highlife dance bands,
  E.T. Mensah's precursors, ashiko/gome).

- 2026-07-19 — **Sub-Saharan Africa: West #2** "Palm-Wine Guitar & the Early Recording Era (c. 1900-1950)"
  built: `ssa_west_music_2_PALMWINE_EARLY_RECORDING.md` + `_IMPORT.txt` (33 tracks, 8 sections; only 4
  named 78s, rest living-tradition/genre bare titles, honestly flagged). The Kru mariners bringing the
  guitar ashore + Sierra Leone maringa/palm-wine (Ebenezer Calender) + Ghana osibisaaba/adaha & the
  1928 Kumasi Trio "Yaa Amponsah" (root of highlife) + the birth of Lagos juju (Tunde King era) +
  gumbe & the Maroon/returnee Black-Atlantic networks + the first Zonophone/HMV West African 78s + the
  dance-band/brass seedbed + Black-Atlantic guitar cross-links. Scope call flagged: S.E. Rogie's "My
  Lovely Elizabeth" (~1962) placed here as the definitive surviving palm-wine recording. Cross-links:
  palm-wine ↔ calypso/son ↔ Congo rumba; returnee gumbe ↔ Caribbean/Brazil. No dups vs #1. Next:
  SSA-West #3 highlife's golden age (~1950s-60s: E.T. Mensah & the Tempos dance-band highlife, the
  guitar-band highlife of E.K. Nyame, the Ghana/Nigeria spread, independence-era optimism).

- 2026-07-19 — **Sub-Saharan Africa: West #3** "Highlife's Golden Age (c. 1950-1969)" built:
  `ssa_west_music_3_HIGHLIFE_GOLDEN_AGE.md` + `_IMPORT.txt` (30 tracks, 6 sections; 14 named). E.T.
  Mensah & the Tempos (dance-band highlife, "the king") + guitar-band highlife & the concert party
  (E.K. Nyame, Kwaa Mensah, Nana Ampadu's 1967 "Ebi Te Yie") + Lagos dance bands (Bobby Benson's
  "Taxi Driver", Victor Olaiya) + Eastern/Igbo highlife & the Biafra shadow (Rex Lawson, Celestine
  Ukwu, Osadebe seeds) + the Latin tinge & Congo connection + the dance-band circuit/songbook.
  Cross-links: Louis Armstrong's 1956 jam with Mensah (US), Cuban GV son 78s' "Latin tinge" (Latin),
  Congo rumba crossing west (Central Africa to come). Content note kept: independence-era optimism and
  the Biafran war (1967-70) that shattered the Eastern scene (Rex Lawson d.1971, Ukwu d.1977). All
  named artists Ghanaian/Nigerian; no scope flags. No dups vs #1-2. Next: SSA-West #4 juju & fuji
  explode + Congo-inflected guitar pop (~1965-1980: King Sunny Adé, Ebenezer Obey, Barrister fuji,
  I.K. Dairo, and the soukous influence).

- 2026-07-19 — **Sub-Saharan Africa: West #4** "Juju & Fuji Explode + Congo-Inflected Guitar Pop
  (c. 1965-1980)" built: `ssa_west_music_4_JUJU_FUJI_GUITARPOP.md` + `_IMPORT.txt` (30 tracks, 6
  sections; 16 named). I.K. Dairo (father of modern juju) + King Sunny Adé's syncro-system juju +
  Ebenezer Obey's philosophical miliki juju + fuji's birth from were (Barrister & Kollington) + the
  Yoruba roots stars apala/sakara (Haruna Ishola, Ayinla Omowura, Yusuf Olatunji) + Congo-inflected
  guitar pop (Victor Uwaifo's "Joromi", Prince Nico Mbarga's "Sweet Mother"). Cross-links: juju's
  pedal steel ← US country/Hawaiian; soukous tide → Central Africa survey. Scope calls flagged: KSA's
  "Ja Funmi"/"Synchro System" (1982-83, just past window) kept as defining the 70s sound; Prince Nico
  Mbarga (Nigerian-Cameroonian, Nigeria-based) kept as West African. Content note: Ayinla Omowura's
  1980 murder. Dedup care: renamed apala/sakara descriptors to avoid collision with #2's bare titles.
  No dups vs #1-3. Next: SSA-West #5 Afrobeat & Afro-funk (~1968-1980: Fela Kuti & Africa 70, Tony
  Allen, Geraldo Pino, Orlando Julius, the Nigerian funk/rock scene).

- 2026-07-19 — **Sub-Saharan Africa: West #5** "Afrobeat & Afro-Funk (c. 1968-1980)" built:
  `ssa_west_music_5_AFROBEAT_AFROFUNK.md` + `_IMPORT.txt` (36 tracks, 6 sections; 35 named). The
  invention of Afrobeat (Fela & Africa 70: Water No Get Enemy, Zombie, Shakara, Expensive Shit) +
  Tony Allen's drumming + Fela the political prophet & Kalakuta (Coffin for Head of State, Unknown
  Soldier) + the soul-invasion precursors (Geraldo Pino, Orlando Julius) + the Nigerian funk/rock/
  psych underground (BLO, Ofege, William Onyeabor, Monomono, The Funkees) + Ghanaian Afro-funk/rock
  (Ebo Taylor, Hedzoleh Soundz, K. Frimpong, Osibisa). Cross-links: James Brown funk in (US) →
  Afrobeat's DNA out into global hip-hop sampling. Content note kept: the 1977 army raid on Kalakuta
  and the death of Funmilayo Ransome-Kuti. Scope calls flagged: Geraldo Pino (Sierra Leone, in-region);
  Osibisa (London-formed, Ghanaian-led) kept. No dups vs #1-4. Next: SSA-West #6 the 80s/90s Mande
  superstars & the world-music era (Salif Keita, Youssou N'Dour & mbalax, Baaba Maal, Ali Farka Touré,
  Toumani Diabaté, Mory Kanté's "Yé Ké Yé Ké", Angélique Kidjo).

- 2026-07-19 — **Sub-Saharan Africa: West #6** "The Mande Superstars & the World-Music Era (c. 1980-2000)"
  built: `ssa_west_music_6_MANDE_SUPERSTARS_WORLDMUSIC.md` + `_IMPORT.txt` (39 tracks, 8 sections; 36
  named). Salif Keita (the golden voice) + Mory Kanté's electric kora ("Yé Ké Yé Ké") + Youssou N'Dour
  & mbalax ("7 Seconds") + the Senegambian wave (Baaba Maal, Ismaël Lô, Touré Kunda, Orchestra Baobab)
  + Ali Farka Touré & desert blues + the Wassoulou women (Oumou Sangaré, Nahawa Doumbia) + the world
  stage (Angélique Kidjo, Toumani's Symmetric Orchestra, Amadou & Mariam) + the Bamako orchestra roots.
  Cross-links: Ali Farka ↔ US blues/John Lee Hooker; Orchestra Baobab ↔ Cuban son; Kidjo's Yoruba roots
  ↔ batá/candomblé (Latin). Scope/duet notes: Cesária Évora on "Yamore", Neneh Cherry on "7 Seconds",
  Ry Cooder on "Talking Timbuktu" — West African lead credited; Kidjo (Benin) in-region. Dedup guard
  honored: avoided #1's Toumani/Ballaké pairs (used "Boulevard de l'Independance" & the Ali Farka duet
  "Debe" instead). No dups vs #1-5. Next: SSA-West #7 modern Afrobeats & the global takeover
  (~2000-present) — THE REGION'S FINAL INSTALLMENT: also build the region master
  (MASTER_GUIDE_ssa_west_survey.md + MASTER_SSA_WEST_FULL_SURVEY_IMPORT.txt) and flip SSA-West COMPLETE;
  set next active region = Sub-Saharan Africa: Southern.

- 2026-07-19 — **Sub-Saharan Africa: West #7** "Modern Afrobeats & the Global Takeover (c. 2000-present)"
  built: `ssa_west_music_7_MODERN_AFROBEATS_GLOBAL.md` + `_IMPORT.txt` (45 tracks, 7 sections; all
  named). The digital dawn (2Baba's "African Queen") + P-Square/D'banj/Mo'Hits + Wizkid + Davido +
  Burna Boy & the Grammy era + the new global-chart generation (CKay, Rema, Tems, Ayra Starr, Asake) +
  Ghana's hiplife/azonto (Sarkodie, Shatta Wale, King Promise, Gyakie). Cross-links: Afrobeats ↔
  Drake/Beyoncé; Burna samples Fela (full circle to #5); amapiano ↔ Southern Africa survey. Scope
  calls flagged: Beyoncé on "Already", Fuse ODG (British-Ghanaian) kept with Ghanaian lead credited.
  No dups vs #1-6.
- 2026-07-19 — **Sub-Saharan Africa: West COMPLETE.** Region master built:
  `MASTER_GUIDE_ssa_west_survey.md` (griot→Afrobeats arc, the braid, cross-links to US blues & Latin,
  recurring scope calls, manifest) + `MASTER_SSA_WEST_FULL_SURVEY_IMPORT.txt`. Seven installments sum
  to **256 tracks with ZERO cross-installment duplicates** (raw 256 → deduped 256). Region flipped
  COMPLETE and added to the DONE list; next active region = Sub-Saharan Africa: Southern (Tier 1 #2b).
  Next: SSA-Southern #1, the deep-traditional layer — Zulu/Xhosa/Sotho song, the mbira/Shona of
  Zimbabwe, San/Khoi music, isicathamiya roots, and the migrant-labour & mission-hymn backdrop.

- 2026-07-20 — **Sub-Saharan Africa: Southern #1** "The Deep-Traditional Layer" built:
  `ssa_south_music_1_DEEP_TRADITIONAL.md` + `_IMPORT.txt` (38 tracks, 7 sections; 29 living-tradition
  bare titles). Zulu/Swazi bow, voice & ngoma (Princess Magogo) + Xhosa overtone/split-tone singing &
  uhadi (Nofinishi Dywili, Madosini, Ngqoko group) + Sotho/Tswana highveld (lesiba, mokhibo) + the
  Shona mbira dzavadzimu of Zimbabwe (Stella Chiweshe, Ephat Mujuru, Dumisani Maraire, Hakurotwi Mude)
  + the San & Khoi (the oldest layer, trance/healing dance) + Venda/Tsonga/Chopi timbila (Mozambique
  UNESCO xylophone orchestras) + the migrant-labour & mission-hymn backdrop (Ntsikana's hymn, makwaya).
  Cross-links: mbira/bow ↔ West African balafon/kora & pan-African roots; isicathamiya roots → later
  Graceland. Content notes kept: colonial dispossession, the mine compounds, the San's marginalization.
  First file of the region, no dedup priors. Next: SSA-Southern #2 marabi, early recording & mission
  choralism (~1900-1940s: marabi keyboard, Solomon Linda's "Mbube"/"The Lion Sleeps Tonight", Reuben
  Caluza's choral songs, the Zulu Christian choral tradition).

- 2026-07-20 — **Sub-Saharan Africa: Southern #2** "Marabi, Early Recording & Mission Choralism
  (c. 1900-1948)" built: `ssa_south_music_2_MARABI_MISSION_EARLY_RECORDING.md` + `_IMPORT.txt` (30
  tracks, 6 sections; 5 named, rest descriptor/traditional for the sparse-recording era). Marabi (the
  shebeen I-IV-V keyboard cycle) + Solomon Linda's 1939 "Mbube" & the royalties injustice + Reuben
  Caluza & mission-modern choral song (iLand Act, protesting the 1913 Land Act) + John Knox Bokwe +
  maskandi/migrant string & concertina (George Sibanda's "Guabi Guabi") + the marabi-to-jazz bridge
  (Jazz Maniacs, Merry Blackbirds) + the recording industry & wider region (Gallo, Motsieloa, Hugh
  Tracey/ILAM, the Copperbelt & Rhodesias). Cross-links: marabi ↔ US ragtime/jazz; Mbube → Wimoweh/
  The Weavers/Disney Lion King (US survey); same colonial guitar-and-record economy as West Africa.
  Content notes kept: segregation, the mine compounds, the Mbube royalties theft (Linda died poor
  1962; heirs settled 2006). Dedup fixes: renamed "Mbube"-descriptor and "Makwaya"-descriptor to avoid
  collision with the Linda entry and #1's makwaya. No dups vs #1. Next: SSA-Southern #3 kwela, sax jive
  & township jazz (~1950s: Spokes Mashiyane pennywhistle kwela, the Sophiatown era, the Manhattan
  Brothers, young Miriam Makeba, Dollar Brand/Abdullah Ibrahim & the Jazz Epistles).

- 2026-07-20 — **Sub-Saharan Africa: Southern #3** "Kwela, Sax Jive & Township Jazz (c. 1950-1962)"
  built: `ssa_south_music_3_KWELA_TOWNSHIP_JAZZ.md` + `_IMPORT.txt` (31 tracks, 6 sections; 17 named).
  Kwela pennywhistle (Spokes Mashiyane, "Tom Hark", Lemmy Special) + Sophiatown vocal-jazz groups
  (Manhattan Brothers, the Skylarks) + the great voices (Miriam Makeba's original "Pata Pata"/"Click
  Song", Dorothy Masuka, Dolly Rathebe) + the Jazz Epistles/modern jazz (Abdullah Ibrahim, Masekela,
  Kippie Moeketsi, Gwangwa) + the "King Kong" musical (Todd Matshikiza) + removals & exile
  ("Meadowlands"). Cross-links: township jazz ↔ US swing/bebop; kwela ↔ UK skiffle; Makeba/Masekela/
  Ibrahim exile → US survey. Content notes kept: the 1955 Sophiatown destruction, pass laws, the
  exile diaspora. NOTE for future installments — the validation norm() dedups by TITLE only (artist
  dropped), so every song title must stay unique region-wide. No dups vs #1-2. Next: SSA-Southern #4
  mbaqanga, isicathamiya & the Soweto sound (~1960s-70s: Mahotella Queens & Mahlathini's mgqashiyo,
  Ladysmith Black Mambazo, West Nkosi, the Makgona Tsohle Band, maskandi).

- 2026-07-20 — **Sub-Saharan Africa: Southern #4** "Mbaqanga, Isicathamiya & the Soweto Sound
  (c. 1960-1979)" built: `ssa_south_music_4_MBAQANGA_ISICATHAMIYA.md` + `_IMPORT.txt` (35 tracks, 6
  sections; 10 named). The Makgona Tsohle Band & the invention of electric mbaqanga (Mavuthela/Gallo)
  + Mahlathini & the Mahotella Queens' mgqashiyo + isicathamiya & Ladysmith Black Mambazo (Joseph
  Shabalala) + Zulu maskandi (Phuzushukela/John Bhengu) + the simanjemanje vocal-mbaqanga galaxy +
  soul/Harari & the Soweto 1970s. Cross-links: isicathamiya → Graceland (#6); mbaqanga bass → township
  pop; back to West Africa. Content notes kept: high apartheid, the exploitative flat-fee studio
  system, the 1976 Soweto uprising. The mbaqanga-instrumental studio era is compilation-based so S1 is
  mostly descriptor titles (honest). No dups vs #1-3 (titles kept unique region-wide). Next:
  SSA-Southern #5 mbira, chimurenga & the liberation era (~1970s-80s: Thomas Mapfumo's chimurenga &
  the Zimbabwe war, Oliver Mtukudzi/Tuku, the Bhundu Boys' jit, Zambian Zamrock, anti-apartheid protest).

- 2026-07-20 — **Sub-Saharan Africa: Southern #5** "Mbira, Chimurenga & the Liberation Era
  (c. 1970-1989)" built: `ssa_south_music_5_MBIRA_CHIMURENGA_LIBERATION.md` + `_IMPORT.txt` (38 tracks,
  7 sections; 23 named). Thomas Mapfumo & chimurenga (electric-mbira liberation music, his 1979
  detention) + the mbira-to-guitar Zimbabwean sound (Stella Chiweshe electric, Zexie Manatsa, sungura)
  + Oliver Mtukudzi's Tuku music + the Bhundu Boys & jit (+ the Four Brothers) + Zambian Zamrock
  (WITCH, Amanaz, Ngozi Family, Copperbelt psych under Kaunda) + Mozambican marrabenta (Fany Mpfumo,
  Orchestra Marrabenta) + crossing the colour line (Juluka/Johnny Clegg & Sipho Mchunu, Sipho Mabuse,
  Sakhile). Cross-links: chimurenga mbira-to-guitar ↔ #1; Zamrock ↔ US/UK psych & funk; liberation
  protest ↔ US/West Africa surveys. Content notes kept: liberation wars, detention/censorship, the AIDS
  epidemic that gutted the Bhundu Boys and Zamrock scenes. Scope call flagged: Johnny Clegg (white
  South African) kept as South African. Avoided #1's Chiweshe titles ("Kasahwa"/"Chapfudza") — used
  "Njuzu". No dups vs #1-4. Next: SSA-Southern #6 Graceland, bubblegum & the birth of kwaito
  (~1985-2000: Paul Simon's Graceland & its controversy, Brenda Fassie & bubblegum, Yvonne Chaka Chaka,
  Lucky Dube's reggae, post-1994 kwaito — Boom Shaka, Arthur Mafokate, TKZee, Mandoza).

- 2026-07-20 — **Sub-Saharan Africa: Southern #6** "Graceland, Bubblegum & the Birth of Kwaito
  (c. 1985-2000)" built: `ssa_south_music_6_GRACELAND_BUBBLEGUM_KWAITO.md` + `_IMPORT.txt` (34 tracks,
  6 sections; 24 named). Graceland & the global spotlight (Ladysmith new titles, Stimela/Ray Phiri,
  Boyoyo Boys, Bakithi Kumalo — Paul Simon treated as US cross-link, NOT listed) + bubblegum (Brenda
  Fassie, Yvonne Chaka Chaka's "Umqombothi", Chicco) + Lucky Dube's reggae + the birth of kwaito
  (Arthur Mafokate, Boom Shaka, Trompies) + kwaito goes big (TKZee's "Shibobo", Mandoza's "Nkalakatha",
  Bongo Maffin, Mafikizolo) + the house roots & stage musicals (Sarafina!). Cross-links: Graceland → US
  survey; kwaito's parent = Chicago/US house via UK; → West African Afrobeats. Content notes kept: the
  boycott-breaking debate, the reclaimed-slur "Kaffir" (Mafokate 1995) preserved in context per the
  survey's content-honesty principle, Brenda Fassie's 2004 death, Lucky Dube's 2007 murder. Region
  integrity handled: only SA artists listed. No dups vs #1-5. Next: SSA-Southern #7 amapiano & the
  global present (~2000-now) — THE REGION'S FINAL INSTALLMENT: also build the region master
  (MASTER_GUIDE_ssa_south_survey.md + MASTER_SSA_SOUTH_FULL_SURVEY_IMPORT.txt) and flip SSA-Southern
  COMPLETE; set next active region = Sub-Saharan Africa: Central.

- 2026-07-20 — **Sub-Saharan Africa: Southern #7** "Amapiano & the Global Present (c. 2000-present)"
  built: `ssa_south_music_7_AMAPIANO_GLOBAL_PRESENT.md` + `_IMPORT.txt` (43 tracks, 7 sections; 26
  named). SA deep/soulful house (Black Coffee) + Durban gqom (DJ Lag, Babes Wodumo, Distruction Boyz)
  + the amapiano log-drum explosion (Scorpion Kings/Kabza & Maphorisa, MFR Souls, Busta 929) + amapiano
  goes global (Focalistic's "Ke Star", DBN Gogo, Uncle Waffles, Young Stunna) + the global crossover
  (Master KG's "Jerusalema", Tyla's Grammy-winning "Water", Sho Madjozi) + Zimbabwe/wider region now
  (Winky D, Jah Prayzah, Sampa the Great) + the 21st-c. jazz & roots revival (Thandiswa Mazwai, Nduduzo
  Makhathini). Cross-links: SA house ↔ US/Chicago house; amapiano ↔ West African Afrobeats/UK.
  Scope calls flagged: Uncle Waffles (Eswatini-born), Sampa the Great (Zambian-born, Australia-based).
  No dups vs #1-6.
- 2026-07-20 — **Sub-Saharan Africa: Southern COMPLETE.** Region master built:
  `MASTER_GUIDE_ssa_south_survey.md` (San/mbira→amapiano arc, the four-strand braid, cross-links to US/
  West Africa/Caribbean, recurring scope calls, manifest) + `MASTER_SSA_SOUTH_FULL_SURVEY_IMPORT.txt`.
  Seven installments sum to **249 tracks with ZERO cross-installment duplicates** (raw 249 → deduped
  249). Region flipped COMPLETE and added to the DONE list; next active region = Sub-Saharan Africa:
  Central (Tier 1 #2c). Next: SSA-Central #1, Congolese rumba's deep roots — the Congo/Zaire rumba
  lineage, Wendo Kolosoy & the 1940s-50s Kinshasa/Leopoldville scene, the Cuban-son influence, likembe/
  folkloric roots.

- 2026-07-20 — **Sub-Saharan Africa: Central #1** "Congolese Rumba's Roots & Birth (c. 1930-1957)"
  built: `ssa_central_music_1_RUMBA_ROOTS_BIRTH.md` + `_IMPORT.txt` (32 tracks, 6 sections; 3 named,
  rest descriptor/traditional for the roots era). The deep Congo folkloric layer (likembe, BaAka forest
  polyphony, Kongo/Luba) + the Cuban "GV" son records that sparked it + the coastal guitar/maringa/
  accordion + Wendo Kolosoy & the birth of rumba ("Marie-Louise" 1948, Adou Elenga's "Ata Ndele") +
  the labels/studio scene (Ngoma, Opika, Loningisa) + the next generation emerging (Kabasele's "Para
  Fifi"/African Jazz 1953, young Franco at Loningisa). Cross-links: Cuban son (Latin survey) → Congo
  rumba → back out across West/East/Southern Africa; Kongo diaspora roots → Cuban/Haitian sacred music.
  Content notes kept: brutal Belgian colonial Congo, the flat-fee label exploitation. First file of the
  region, no dedup priors. Next: SSA-Central #2 the golden age of Congolese rumba (~1953-1965: Le Grand
  Kalle & African Jazz, Franco & OK Jazz, "Independence Cha Cha" 1960, the rumba odemba).

- 2026-07-20 — **Sub-Saharan Africa: Central #2** "The Golden Age of Congolese Rumba (c. 1953-1965)"
  built: `ssa_central_music_2_RUMBA_GOLDEN_AGE.md` + `_IMPORT.txt` (32 tracks, 6 sections; 5 named,
  rest descriptor/traditional — exact 1950s-60s Congo titles beyond the famous ones are genuinely hard,
  so honest descriptors used). Le Grand Kalle & African Jazz (the elegant school) + "Independence Cha
  Cha" & the politics of 1960 + Franco & OK Jazz (the earthy school) + the two schools & guitar masters
  (Dr Nico, Tino Baroza, young Rochereau) + the rumba odemba/arrangement + the Brazzaville scene & the
  continental spread. Cross-links: "Independence Cha Cha" as the pan-African anthem; Cuban son ↔ rumba
  (Latin); Congo rumba → East/West/Southern African guitar pop. Content notes kept: independence, the
  Congo Crisis, Lumumba's 1961 assassination. No dups vs #1. Next: SSA-Central #3 soukous & the second
  generation (~1965-1975: Tabu Ley Rochereau & African Fiesta, Dr Nico Kasanda's guitar, the split from
  Kabasele, Franco's OK Jazz maturing, the birth of soukous/the fast sebene, Mbilia Bel).

- 2026-07-20 — **Sub-Saharan Africa: Central #3** "Soukous & the Second Generation (c. 1965-1975)"
  built: `ssa_central_music_3_SOUKOUS_SECOND_GENERATION.md` + `_IMPORT.txt` (35 tracks, 7 sections; 10
  named). Tabu Ley Rochereau & African Fiesta (the Olympia 1970) + Dr Nico & African Fiesta Sukisa (the
  God of the Guitar) + Franco's OK Jazz maturing into TP OK Jazz + the birth of soukous & the fast
  sebene + Sam Mangwana & the pan-African voice + Mobutu's authenticité/Zairianization (1971) + soukous
  spreads to East Africa. Cross-links: soukous → Nairobi/Dar es Salaam & the East Africa survey; Congo
  guitar → the whole continent. Content notes kept: Mobutu's dictatorship & cultural-nationalist
  machinery. No dups vs #1-2. Next: SSA-Central #4 the Zaiko generation & rumba rock (~1970-1980: Zaiko
  Langa Langa, Papa Wemba, the youth revolt against horn-section rumba, the stripped guitar-and-drums
  sound, the fast sebene/atalaku shouter, Viva La Musica).

- 2026-07-20 — **Sub-Saharan Africa: Central #4** "The Zaiko Generation & Rumba Rock (c. 1970-1980)"
  built: `ssa_central_music_4_ZAIKO_RUMBA_ROCK.md` + `_IMPORT.txt` (36 tracks, 7 sections; 6 named).
  Zaiko Langa Langa & the youth revolt (rumba rock, no horns) + Papa Wemba & Viva La Musica + the
  atalaku & the cavacha + the Zaiko offshoots & clan wars (Langa Langa Stars, Choc Stars, Bozi
  Boziana) + rumba rock/funk & Zaire 74 (the Rumble-in-the-Jungle festival — James Brown, Celia Cruz,
  Fania All Stars in Kinshasa) + the old guard in the 70s (Franco/TP OK Jazz, Tabu Ley/Afrisa, Mbilia
  Bel emerges) + La Sape. Cross-links: the atalaku ↔ hip-hop hype-man; Zaire 74 ↔ US & Latin surveys
  live in Kinshasa. Content notes kept: Mobutu's dictatorship & economic collapse. No dups vs #1-3.
  Next: SSA-Central #5 soukous goes global & the birth of ndombolo (~1980-2000: the Paris soukous
  scene, Kanda Bongo Man & Diblo Dibala's kwassa kwassa, Loketo, then Koffi Olomide, Wenge Musica,
  Awilo Longomba's ndombolo, JB Mpiana & Werrason).
- 2026-07-20 — **Sub-Saharan Africa: Central #5** "Soukous Goes Global & the Birth of Ndombolo (c.
  1980-2000)" built: `ssa_central_music_5_SOUKOUS_GLOBAL_NDOMBOLO.md` + `_IMPORT.txt` (38 tracks, 7
  sections; 10 named). The Paris soukous scene (exile studios, the world-music boom) + Kanda Bongo Man
  & kwassa kwassa (Sai, Zing Zong, Yesu Kristu) + Diblo Dibala's machine-gun guitar, Loketo & Aurlus
  Mabele & the Soukous Stars + Koffi Olomide & the 90s Kinshasa giants (Loi, Papa Ngwasuma, Andrada;
  Quartier Latin, tcha tcha) + Wenge Musica & the birth of ndombolo (the JB Mpiana/Werrason split) +
  Awilo Longomba & ndombolo goes continental (Coupe Bibamba, Karolina) + the end of an era (Papa
  Wemba's Yolele & Maria Valencia; Franco's 1989 death; Tabu Ley to politics; Mobutu's 1997 fall).
  Cross-links: Paris soukous → the world-music industry; ndombolo → West & Southern African pop.
  Content notes kept: the AIDS epidemic (took Franco), Mobutu's fall, the Congo wars. No dups vs #1-4.
  Next: SSA-Central #6 Angola, Cameroon & the wider Central Africa (~1970-2000: Angolan semba & Bonga,
  the birth of kizomba; Cameroon's makossa — Manu Dibango's "Soul Makossa", Sam Fan Thomas' makassi,
  Petit Pays; bikutsi — Les Têtes Brûlées; Gabon/CAR).
- 2026-07-20 — **Sub-Saharan Africa: Central #6** "Angola, Cameroon & the Wider Central Africa (c.
  1955-2000)" built: `ssa_central_music_6_ANGOLA_CAMEROON_MAKOSSA_BIKUTSI.md` + `_IMPORT.txt` (46
  tracks, 7 sections; 9 named). Steps OUT of the Congo rumba thread to the region's other cultures:
  Angolan semba & the Luanda roots (Ngola Ritmos/Liceu Vieira Dias; semba↔samba cross-link) + Bonga &
  the voice of exile (Mona Ki Ngi Xica, Balumukeno, Muadiakime; Angola 72) + independence/civil war &
  the birth of kizomba (Waldemar Bastos' Velha Chica; zouk→kizomba) + Cameroon's makossa & Manu
  Dibango (Soul Makossa) + the makossa golden age (Sam Fan Thomas' African Typic Collection, Moni
  Bile's Bijou, Petit Pays, the Deccas) + bikutsi/the Beti (Anne-Marie Nzie, Messi Martin, Les Tetes
  Brulees, K-Tino) + Gabon & cross-currents (Akendengue's Africa Obota, Oliver N'Goma's Bane).
  Cross-links: semba↔Brazilian samba (Latin), zouk→kizomba (Caribbean), Soul Makossa→global funk.
  Content notes kept: Portuguese colonial war & Angola's civil war. No dups vs #1-5 (TITLE-only norm).
  Next: SSA-Central #7 (FINAL) modern & global Central African pop (~2000-present: the digital-era
  Congolese giants — Fally Ipupa, Ferre Gola, Koffi's heirs; congotronics/Konono Nº1 & Kasai Allstars;
  Jupiter Bokondji; the Central diaspora & Afropop crossovers) — then build the SSA-Central region
  master (MASTER_GUIDE_ssa_central_survey.md + deduped MASTER_SSA_CENTRAL_FULL_SURVEY_IMPORT.txt) and
  flip the region COMPLETE; next active region = Sub-Saharan Africa: East.
- 2026-07-20 — **Sub-Saharan Africa: Central #7 (FINALE)** "Modern & Global Central African Pop (c.
  2000-present)" built: `ssa_central_music_7_MODERN_GLOBAL_AFROPOP.md` + `_IMPORT.txt` (49 tracks, 8
  sections; 11 named). The digital-era Congolese giants (Fally Ipupa's Droit Chemin/Eloko Oyo, Ferre
  Gola's Sens Interdit) + the old guard & UNESCO's 2021 rumba heritage listing + congotronics (Konono
  Nº1's Lufuala Ndonga, Kasai Allstars) + the Kinshasa street underground (Staff Benda Bilili's Polio,
  Jupiter Bokondji, Mbongwana Star, Baloji) + Angolan kuduro (Cabo Snoop's Windeck, Buraka Som
  Sistema's Sound of Kuduro, Titica, Tony Amado) + Cameroon now (Stanley Enow's Hein Père, Charlotte
  Dipanda, mbolé) + the Central diaspora in French pop (Maître Gims' Sapés comme jamais/Bella, Dadju,
  Damso, Innoss'B's Yope) + the seven-installment through-line. Cross-links: rumba→soukous→ndombolo→
  global Afropop; kuduro→European club; diaspora→French pop; Cuban son loop (Latin). Region-integrity
  flags kept in prose for Franco-Belgian/Portugal diaspora (Gims, Dadju, Damso, Buraka). Content notes:
  disability/poverty (Benda Bilili), DR Congo instability. No dups vs #1-6 (TITLE-only norm).
  **REGION MASTER built:** `MASTER_GUIDE_ssa_central_survey.md` (narrative overview of #1-7) +
  `MASTER_SSA_CENTRAL_FULL_SURVEY_IMPORT.txt` (concatenated #1-7 in order, first-occurrence dedup by
  TITLE-only norm — raw 268 → deduped 268, **zero cross-installment dups region-wide**). Region
  **Sub-Saharan Africa: Central flipped COMPLETE** (7 installments, 268 tracks). Next active region =
  **Sub-Saharan Africa: East** (Tier 1 #2d). Next: SSA-East #1 — East African roots (Swahili taarab of
  Zanzibar/Mombasa; the Congolese-seeded Kenyan benga & guitar pop; Tanzanian dansi/muziki wa dansi;
  early Kenyan/Tanzanian recording scenes).
- 2026-07-20 — **Sub-Saharan Africa: East #1** "Roots — Taarab, the Guitar & the Birth of Dansi (c.
  1900-1970)" built: `ssa_east_music_1_ROOTS_TAARAB_GUITAR_DANSI.md` + `_IMPORT.txt` (45 tracks, 8
  sections; 4 named — roots-heavy, so mostly traditions/styles as search seeds). NEW region, stem
  `ssa_east_music_` (dedup scope resets). Swahili-coast taarab & Ikhwani Safaa + Siti binti Saad (the
  mother of taarab, "Kijiti"; first East African to record, Bombay 78s) + traditional roots (Luo
  nyatiti, ngoma, orutu, litungu) + the Kenyan guitar & pop song (Fundi Konde; Fadhili William's
  "Malaika", authorship-dispute flagged) + Jean Bosco Mwenda's Katanga guitar ("Masanga", flagged
  Congolese but foundational to East African guitar) + 1960s twist/rumba hitmakers (Daudi Kabaka's
  "Helule Helule"; early benga stirrings) + Tanzanian dansi (Salum Abdallah's Cuban Marimba Band, NUTA/
  Morogoro/Western Jazz; Cuban GV records) + Congo rumba arriving in Nairobi/Dar. Cross-links: Congo
  rumba/soukous (Central survey) seeding the guitar & bands; Cuban son (Latin survey) into dansi.
  Region-integrity flags: Jean Bosco Mwenda (Congolese/Katanga). No internal dups (fresh region).
  Next: SSA-East #2 — the golden dance-band age & the rise of benga (~1965-1980: Kenyan benga —
  D.O. Misiani & Shirati Jazz, the Luo guitar; Swahili rumba; Tanzania's ujamaa-era bands; Nairobi as
  a pan-African recording hub for Congolese exiles).
- 2026-07-20 — **Sub-Saharan Africa: East #2** "The Golden Dance-Band Age & the Rise of Benga (c.
  1965-1980)" built: `ssa_east_music_2_BENGA_DANCE_BAND_GOLDEN_AGE.md` + `_IMPORT.txt` (46 tracks, 8
  sections; 5 named). Kenyan benga & the Luo guitar (D.O. Misiani & Shirati Jazz's "Pole Musa";
  nyatiti remapped onto guitar) + the benga boom & the 45 (Gabriel Omolo's "Lunchtime", Collela
  Mazee/Victoria Kings, George Ramogi) + Kikuyu/vernacular benga (Joseph Kamaru, D.K. Daniel Kamau) +
  Nairobi the pan-African hub for Congolese exiles (Super Mazembe's "Shauri Yako", Baba Gaston, Samba
  Mapangala/Virunga) + Swahili rumba & the Wanyika bands (Les Wanyika's "Sina Makosa", Simba Wanyika,
  Makassy) + Tanzania's ujamaa dance bands (DDC Mlimani Park, Juwata, Safari Sound, Vijana Jazz) +
  Mbaraka Mwinshehe (Super Volcano's "Shida"; d. 1979) + the sound spreading outward. Cross-links:
  Congo rumba naturalized in Nairobi (Central survey); Cuban son under dansi (Latin). Region-integrity
  flags: Super Mazembe/Baba Gaston/Samba Mapangala (Congolese emigres, pillars of the Nairobi scene).
  Content note: Mbaraka's 1979 death. No dups vs #1 (TITLE-only norm).
  Next: SSA-East #3 — the cassette era & modern Swahili pop (~1980-1995: the cassette boom; Zanzibar
  taarab's modernization & "rusha roho"; Kenyan benga into the 80s; Tanzanian dansi's late golden age;
  the decline of the big bands and the rise of studio pop).
- 2026-07-20 — **Sub-Saharan Africa: East #3** "The Cassette Era & Modern Swahili Pop (c. 1980-1995)"
  built: `ssa_east_music_3_CASSETTE_ERA_SWAHILI_POP.md` + `_IMPORT.txt` (43 tracks, 8 sections; 5
  named). The cassette revolution (democratization + piracy) + Zanzibar taarab modernizes — rusha roho,
  kidumbak, mipasho, Culture Musical Club, Bi Kidude's "Muhogo wa Jang'ombe" + Mombasa coastal taarab
  (Zein l'Abidin, chakacha) + Kenyan benga into the 80s (Kakai Kilonzo/Kamba benga, Kalambya) + Them
  Mushrooms' "Jambo Bwana"/Hakuna Matata & the tourist-Swahili sound + Tanzania's late dance-band peak
  (DDC Mlimani Park's "Sikinde" vs Safari Sound; Samba Mapangala's "Malako Disco") + Remmy Ongala &
  the conscience of dansi ("Mambo Kwa Soksi", the AIDS/condom song; WOMAD/Real World) + liberalization,
  decline & the seeds of bongo flava. Cross-links: taarab's Arab/Indian roots (#1); toward hip-hop.
  Content notes: the AIDS epidemic; tourist packaging of African music. Region-integrity flags: Remmy
  Ongala & Samba Mapangala (Congolese-born pillars of the East African scene). No dups vs #1-2.
  Next: SSA-East #4 — the modern era: bongo flava, genge & Kenyan hip-hop (~1995-2010: Tanzanian bongo
  flava — Professor Jay, Mr Nice, Lady Jaydee, TID; Kenyan genge & hip-hop — Kalamashaka, Nonini,
  Jua Cali, E-Sir; gospel & Ohangla's revival; the Swahili rap explosion).
- 2026-07-20 — **Sub-Saharan Africa: East #4** "The Modern Era — Bongo Flava, Genge & Hip-Hop (c.
  1995-2010)" built: `ssa_east_music_4_BONGO_FLAVA_GENGE_HIPHOP.md` + `_IMPORT.txt` (47 tracks, 8
  sections; 11 named). Birth of bongo flava in Dar (Kwanza Unit, Mr II/Sugu) + bongo flava mainstream
  (Professor Jay's "Ndio Mzee", Mr Nice's "Kunguru", TID, Juma Nature) + the R&B queens (Lady Jaydee's
  "Wanaonizunguka", Ray C, Dully Sykes) + Kenyan conscious hip-hop from Dandora (Kalamashaka's "Tafsiri
  Hii", Ukoo Flani, Sheng) + genge/kapuka (Nonini's "Manzi wa Nairobi", Jua Cali's "Kiasi", Ogopa DJs)
  + E-Sir's "Boomba Train" (d. 2003) & Nameless's "Megarider" + "Unbwogable" (Gidi Gidi Maji Maji, the
  2002 election anthem), Nazizi/ragga, gospel (Esther Wahome's "Kuna Dawa") + Uganda's Big Three (Jose
  Chameleone's "Mama Mia", Bebe Cool, Bobi Wine; kadongo kamu). Cross-links: US hip-hop/R&B localized
  into Sheng/Swahili; toward Afrobeats/singeli/amapiano. Content notes: E-Sir's death; Bobi Wine's
  later persecution (flagged forward). Widens the region to Uganda. No dups vs #1-3.
  Next: SSA-East #5 (likely FINAL) — the streaming era & global crossover (~2010-present: Diamond
  Platnumz & WCB/Wasafi, the singeli explosion, Sauti Sol, Nyashinski, Sho Madjozi's cross-border hits,
  amapiano/afrobeats crossover, gengetone; the East African diaspora) — then build the SSA-East region
  master and flip the region COMPLETE (next region = Sub-Saharan Africa: Sahel).
- 2026-07-20 — **Sub-Saharan Africa: East #5 (FINALE)** "The Streaming Era & Global Crossover (c.
  2010-present)" built: `ssa_east_music_5_STREAMING_ERA_GLOBAL.md` + `_IMPORT.txt` (48 tracks, 8
  sections; 12 named). Diamond Platnumz & the Wasafi empire ("Number One") + the bongo stars (Rayvanny's
  "Tetema", Harmonize's "Kwangwaru", Zuchu's "Sukari", Nandy) + singeli (Sisso, Bamba Pana, Nyege Nyege)
  + Kenyan gengetone (Ethic's "Lamba Lolo", Sailors' "Wamlambez") + Sauti Sol & the afropop crown ("Sura
  Yako", "Suzanna") + the Kenyan new wave (Nyashinski's "Mungu Pekee", Khaligraph Jones' "Mazishi") +
  Uganda/Rwanda global (Eddy Kenzo's "Sitya Loss", Nyege Nyege) + cross-border (Sho Madjozi's "John
  Cena", flagged SA; amapiano/afrobeats crossover). Cross-links: West African Afrobeats & SA amapiano;
  global streaming. Content notes: gengetone censorship, Uganda politics. No dups vs #1-4.
  **REGION MASTER built:** `MASTER_GUIDE_ssa_east_survey.md` (overview of #1-5) +
  `MASTER_SSA_EAST_FULL_SURVEY_IMPORT.txt` (concatenated #1-5, first-occurrence dedup by TITLE-only norm
  — raw 229 → deduped 229, **zero cross-installment dups region-wide**). Region **Sub-Saharan Africa:
  East flipped COMPLETE** (5 installments, 229 tracks) & added to DONE. Next active region =
  **Sub-Saharan Africa: Sahel** (Tier 1 #2e). Next: SSA-Sahel #1 — Sahelian/desert roots (the griot
  heartland's edge; Malian & Nigerien Tuareg traditions; the Sahel guitar & the roots of desert blues;
  Songhai/Fulani/Hausa music; the pentatonic north).
- 2026-07-20 — **Sub-Saharan Africa: Sahel #1** "Desert & Savanna Roots (c. pre-1970)" built:
  `ssa_sahel_music_1_DESERT_SAVANNA_ROOTS.md` + `_IMPORT.txt` (44 tracks, 8 sections; 0 named — a
  deep-roots installment, all traditions/instruments/seeds). NEW region, stem `ssa_sahel_music_` (dedup
  scope resets). The Sahel as desert-meets-savanna crossroads (Islam, pentatonic north) + Moorish
  azawan of Mauritania (tidinit, ardin, iggawin, Dimi Mint Abba seed) + Tuareg music (imzad, tende,
  assouf — the pre-guitar taproot of desert blues) + Songhai & the Niger bend (takamba, holey) + Fulani/
  Peul herders' music (flute, Wodaabe gerewol) + Hausa court music (kakaki, goje, rok'o) + the Sahelian
  lutes & the roots of the blues (ngoni/tehardent/xalam; ngoni→banjo, Mali-to-Mississippi) + Islam, the
  griot & roads ahead. Cross-links: US blues (American survey); MENA's Arab-Berber north; Mande griot
  (West Africa survey, separate/COMPLETE). Scope: desert-edge Mali/Niger/Mauritania/Chad/N-Nigeria,
  avoiding the coastal Mande material already in the West survey. No internal dups (fresh region).
  Next: SSA-Sahel #2 — the modern Malian foundation & the birth of desert blues (~1960-1990: Mali's
  independence-era Radio Mali orchestras & the Rail Band/Salif Keita's rise; Ali Farka Touré's river
  blues; Boubacar Traoré; the Super Biton/regional orchestras; the electrification of the Sahel).
- 2026-07-20 — **Sub-Saharan Africa: Sahel #2** "The Modern Malian Foundation & the Birth of Desert
  Blues (c. 1960-1990)" built: `ssa_sahel_music_2_MALIAN_FOUNDATION_DESERT_BLUES.md` + `_IMPORT.txt`
  (43 tracks, 8 sections; 3 named). Independence & Radio Mali (state cultural policy, biennales) + the
  Rail Band & the Bamako sound (Tidiani Koné; "Mali Sadio"; Salif Keita/Mory Kanté pass through,
  flagged Mande/West) + the state/regional orchestras (Super Biton de Ségou, National Badema, Kanaga de
  Mopti) + Super Djata & the electric Malian guitar (Zani Diabaté) + Ali Farka Touré & the river blues
  ("Diaraby"; the African John Lee Hooker; Mali-Mississippi kinship) + Boubacar Traoré "Kar Kar"
  ("Mali Twist"; the lost years) + the Tuareg electrify — ishumar & Tinariwen's birth (~1979-82) +
  Wassoulou stirs (kamale ngoni, Nahawa Doumbia seed). Cross-links: US blues; Cuban son under the
  orchestras; Mande griot (West survey). Content notes: Tuareg exile/rebellion; Kar Kar's hardship.
  Avoided the #1 "Ali Farka Touré" bare-title collision (named "Diaraby" only). No dups vs #1.
  Next: SSA-Sahel #3 — the global desert-blues & wassoulou breakout (~1990-2010: Ali Farka Touré's
  "Talking Timbuktu"/Grammy & Toumani collab; Tinariwen goes global; Tartit/Terakaft; the wassoulou
  divas — Oumou Sangaré; Boubacar Traoré's rediscovery; Habib Koité; Festival au Désert).
- 2026-07-20 — **Sub-Saharan Africa: Sahel #3** "The Global Desert-Blues & Wassoulou Breakout (c.
  1990-2010)" built: `ssa_sahel_music_3_GLOBAL_DESERT_BLUES_WASSOULOU.md` + `_IMPORT.txt` (44 tracks, 8
  sections; 8 named). Ali Farka Touré conquers the world (Talking Timbuktu/Grammy, "Ai Du", Niafunké,
  the Toumani duets, Savane) + Tinariwen & the global desert blues ("Cler Achel"/Aman Iman) + the
  Tuareg guitar spreads (Terakaft, Tartit, Etran Finatawa, Bombino ahead) + Oumou Sangaré & the
  wassoulou divas ("Moussolou", "Saa Magni"; Sali/Coumba Sidibé; feminist lyrics) + Amadou & Mariam
  ("Beaux Dimanches", "Sabali"; Manu Chao) + Habib Koité's "Cigarette Abana" & Boubacar Traoré's
  rediscovery ("Mariama") + Mauritania/Niger modernize (Malouma, Khaira Arby, Mamman Sani) + Festival
  au Désert at Essakane. Cross-links: US blues (Mali-Mississippi, now global); Mande griot (Toumani/
  Koité flagged Mande/West). Content notes: Tinariwen's rebel roots; the northern-Mali crisis flagged
  forward. No dups vs #1-2 (avoided a 2nd bare "Ali Farka"/"Boubacar Traoré" collision; named tracks
  only). Next: SSA-Sahel #4 (likely FINAL) — crisis, the new generation & the Sahel today (~2010-
  present: the 2012 jihadist occupation of northern Mali & the music ban, Songhoy Blues & the exiles,
  Bombino & Mdou Moctar's Niger guitar, Fatoumata Diawara, Sidiki Diabaté/Iba One's Bamako rap, Tuareg
  assouf's new wave, Mauritania/Chad now) — then build the SSA-Sahel region master and flip COMPLETE.
- 2026-07-20 — **Sub-Saharan Africa: Sahel #4 (FINALE)** "Crisis, the New Generation & the Sahel Today
  (c. 2010-present)" built: `ssa_sahel_music_4_CRISIS_NEW_GENERATION_TODAY.md` + `_IMPORT.txt` (44
  tracks, 8 sections; 8 named). The 2012 music ban in occupied northern Mali + Songhoy Blues & the
  music in exile ("Soubour") + the Niger guitar revolution (Bombino's "Azel", Mdou Moctar's "Afrique
  Victime", Agadez) + the Tuareg assouf new wave (Tamikrest's "Chatma", Imarhan, Les Filles de
  Illighadad) + Fatoumata Diawara's "Nterini" & the new Malian voices + Bamako now (Bassekou Kouyaté's
  "Jama Ko", Sidiki Diabaté kora-pop, Oumou Sangaré's "Yere Faga", Bambara rap) + Mauritania/Niger/Chad
  today (Noura Mint Seymali's "Tzenni", Afrotronix) + resilience through the coups (Vieux Farka Touré).
  Cross-links: global rock (desert-blues crossover); Mande griot (Bassekou/Sidiki/Rokia flagged).
  Content notes: the 2012 ban, jihadist violence, 2020-23 coups. No dups vs #1-3.
  **REGION MASTER built:** `MASTER_GUIDE_ssa_sahel_survey.md` (#1-4 overview) +
  `MASTER_SSA_SAHEL_FULL_SURVEY_IMPORT.txt` (concatenated #1-4, TITLE-only first-occurrence dedup — raw
  175 → deduped 175, **zero cross-installment dups**). Region **Sub-Saharan Africa: Sahel COMPLETE** (4
  installments, 175 tracks) & added to DONE. ★★ **MILESTONE: ALL of Sub-Saharan Africa is now COMPLETE**
  — West (256) + Southern (249) + Central (268) + East (229) + Sahel (175) = 5 sub-surveys, 1177 tracks.
  Next active region = **India / South Asia** (Tier 1 #3). Next: India/South Asia #1 — the classical
  roots (Hindustani & Carnatic): raga & tala, the Vedic/temple/bhakti deep roots, and the classical
  instruments (sitar, sarod, veena, tabla, mridangam) — read the roadmap's India plan to confirm the
  installment breakdown (classical → film/Bollywood → folk/regional → devotional → modern/indie/global).
- 2026-07-20 — **India / South Asia #1** "The Classical Roots — Raga, Tala & the Two Great Systems"
  built: `south_asia_music_1_CLASSICAL_ROOTS_RAGA_TALA.md` + `_IMPORT.txt` (48 tracks, 8 sections; 2
  named — a foundations installment, mostly theory/instruments/forms as listening seeds). NEW
  super-region, stem `south_asia_music_` (dedup scope resets). Vedic/ancient roots (Samaveda, Nada
  Brahma, Natya Shastra, rasa) + raga (the melodic framework, swaras, tanpura drone, time-of-day, alap,
  shruti) + tala (the cyclic rhythm, teental, sam, layakari, tihai) + the guru-shishya parampara &
  gharanas + the Hindustani/Carnatic split (Amir Khusrau; Persian influence vs temple continuity) + the
  Hindustani instruments (sitar, sarod, sarangi, bansuri, tabla; dhrupad & khyal) + the Carnatic
  instruments & forms (veena, mridangam, the kriti; the Trinity — named works "Endaro Mahanubhavulu"/
  Tyagaraja & "Vatapi Ganapatim"/Muthuswami Dikshitar; melakarta) + the devotional heart (bhakti,
  temple, Purandara Dasa). Cross-links: Persian/Arab maqam & Sufi (MENA); the raga goes global (jazz/
  Beatles, forward). No internal dups (fresh region). Planned India arc: #1 classical roots → #2 the
  classical masters (Hindustani gharanas & Carnatic in depth) → #3 folk & regional → #4 devotional
  (bhajan/qawwali/Sufi) → #5 film/Bollywood golden age → #6 modern filmi & Indipop → #7 modern/indie/
  global + wider South Asia (Pakistan/Bangladesh/Sri Lanka/Nepal) & diaspora. Next: India/South Asia #2
  — the classical masters (~1900-present): the Hindustani gharanas & giants (Ravi Shankar, Ali Akbar
  Khan, Bismillah Khan, Bhimsen Joshi, Kishori Amonkar, Zakir Hussain) and the modern Carnatic greats
  (M.S. Subbulakshmi, etc.); the concert age, AIR/recordings, and the raga's global reach.
- 2026-07-20 — **India / South Asia #2** "The Classical Masters (Hindustani & Carnatic, c. 1900-
  present)" built: `south_asia_music_2_CLASSICAL_MASTERS.md` + `_IMPORT.txt` (45 tracks, 8 sections; 6
  named). The concert age & recording revolution (court→hall, AIR, LP) + the Hindustani sitar/sarod
  giants (Ravi Shankar's "Raga Jog", Ali Akbar Khan's "Raga Chandranandan", Vilayat Khan, Nikhil
  Banerjee, the Maihar gharana) + the Hindustani vocal masters (Bhimsen Joshi, Kishori Amonkar, Kumar
  Gandharva, Kesarbai Kerkar's "Jaat Kahan Ho" on the Voyager Golden Record, the Dagar dhrupad) + tabla
  as solo art (Alla Rakha, Zakir Hussain) + shehnai/flute/santoor ennobled (Bismillah Khan, Chaurasia,
  Shivkumar Sharma) + the Carnatic voice (M.S. Subbulakshmi's "Kurai Onrum Illai" & "Venkatesa
  Suprabhatam", UN 1966; Semmangudi, Balamuralikrishna, DKP/MLV) + Carnatic instrumentalists & the
  Madras Season (Lalgudi Jayaraman, L. Subramaniam, Palghat Mani Iyer) + the raga goes global (Ravi
  Shankar's "West Meets East"/Menuhin, Harrison/Beatles, Monterey/Woodstock, Shakti). Cross-links: the
  raga's influence OUT into the US/Western surveys (flagged Western). No dups vs #1. Next: India/South
  Asia #3 — folk & regional traditions (Bengal's bauls & Rabindra Sangeet; Rajasthan's Manganiar/Langa;
  Punjab's bhangra & dhol; Lavani, Garba/Dandiya, Bihu; the Northeast & tribal; the vast village India).
- 2026-07-20 — **India / South Asia #3** "Folk & Regional Traditions — the Village India" built:
  `south_asia_music_3_FOLK_REGIONAL_TRADITIONS.md` + `_IMPORT.txt` (50 tracks, 9 sections; 3 named —
  folk-heavy, mostly forms/traditions as seeds). Bengal's bauls, bhatiali & Tagore (Rabindra Sangeet's
  "Ekla Cholo Re", "Amar Sonar Bangla"; Lalon; Nazrul Geeti) + Rajasthan's desert musicians (Manganiar/
  Langa, kamaicha/khartal, Padharo Mhare Desh) + Punjab's bhangra/dhol/giddha (Alam Lohar's "Jugni",
  Kuldeep Manak) + Maharashtra's lavani & powada + Gujarat's garba/dandiya (Navratri) + the Tamil/
  Dravidian south (gaana, villu paatu, therukoothu, parai, oppari) + Assam's Bihu & the Northeast +
  the Adivasi/tribal traditions (Santhal, Gond/Warli, Pandavani/Teejan Bai) + folk instruments &
  theater (ektara, ravanahatha, nautanki/jatra). Cross-links: folk feeding Bollywood (#5) & global
  bhangra-pop; the Baul's mysticism ↔ Sufi (#4). Content notes: lavani's stigma; Adivasi marginalization.
  ASCII-clean; no dups vs #1-2. Next: India/South Asia #4 — devotional traditions (bhajan & kirtan;
  qawwali & the Sufi shrine — Amir Khusrau's legacy, the Sabri Brothers, Nusrat Fateh Ali Khan; Sikh
  Gurbani/shabad kirtan; temple & bhakti song; the abida/Sufi voice; devotion as India's deepest music).
- 2026-07-20 — **India / South Asia #4** "Devotional Traditions — Bhajan, Qawwali & the Sacred Voice"
  built: `south_asia_music_4_DEVOTIONAL_BHAJAN_QAWWALI.md` + `_IMPORT.txt` (43 tracks, 8 sections; 5
  named). The bhakti poet-saints (Mirabai's "Payoji Maine", Kabir, Surdas, Tulsidas's "Hanuman Chalisa",
  Narsinh Mehta's "Vaishnava Jana To") + Hindu bhajan & kirtan (Hare Krishna sankirtan, "Om Jai Jagdish
  Hare", abhang/warkari) + the Sufi shrine & birth of qawwali (Amir Khusrau's "Man Kunto Maula" &
  "Chaap Tilak", the dargah/sama) + Nusrat Fateh Ali Khan ("Allah Hoo", "Mera Piya Ghar Aaya"; global
  via Real World) + the qawwali dynasties (Sabri Brothers' "Bhar Do Jholi", Abida Parveen, Aziz Mian,
  "Dama Dam Mast Qalandar") + the Sufi poets sung (Bulleh Shah, Baba Farid, Shah Abdul Latif) + Sikh
  Gurbani/shabad kirtan (Golden Temple ragis, Guru Nanak & Mardana) + mantra/temple/global kirtan
  (T-Series bhajans, yoga-world kirtan flagged Western). Bridges into Pakistan (Nusrat/Sabris/Abida
  flagged wider-South-Asia). Cross-links: the Baul (#3); Sufi/MENA; film devotional song (#5). ASCII-
  clean; avoided the #1 "Amir Khusrau"/"Bhakti" title collisions (named works only). No dups vs #1-3.
  Next: India/South Asia #5 — the film-song juggernaut / Bollywood's golden age (~1930-1970: the birth
  of playback singing; the great music directors — Naushad, S.D. Burman, Shankar-Jaikishan, C. Ramchandra;
  the legendary voices — Lata Mangeshkar, Mohammed Rafi, Kishore Kumar, Mukesh, Asha Bhosle, Manna Dey;
  filmi ghazal & the golden-age songbook that became India's true pop).
- 2026-07-20 — **India / South Asia #5** "The Film-Song Juggernaut — Bollywood's Golden Age (c. 1931-
  1970)" built: `south_asia_music_5_BOLLYWOOD_GOLDEN_AGE.md` + `_IMPORT.txt` (43 tracks, 8 sections; 14
  named — the pop songbook). Birth of film song & playback (Alam Ara 1931, K.L. Saigal's "Babul Mora")
  + Naushad's classical grandeur (Mughal-e-Azam's "Pyar Kiya To Darna Kya") + Raj Kapoor/Shankar-
  Jaikishan/Mukesh ("Awara Hoon", "Mera Joota Hai Japani"; global to the USSR) + S.D. Burman & Guru
  Dutt's poetic films (Geeta Dutt's "Waqt Ne Kiya Kya Haseen Sitam") + Lata Mangeshkar the Nightingale
  ("Aye Mere Watan Ke Logon", "Lag Ja Gale") + Mohammed Rafi ("Chaudhvin Ka Chand", "Baharon Phool
  Barsao") + Kishore Kumar/Asha/Manna Dey/Talat (Aradhana's "Mere Sapno Ki Rani" & "Roop Tera Mastana",
  "Pyar Hua Ikrar Hua", "Aaiye Meharban", "Jalte Hain Jiske Liye") + the filmi ghazal & golden-age
  songbook. Cross-links: Hindustani classical (#2) & folk (#3) into film song; golden age → modern
  filmi (#6); Indian film music's global reach. Content notes: female-playback monopoly; Guru Dutt's
  tragedy. ASCII-clean; no dups vs #1-4. Next: India/South Asia #6 — modern filmi & Indipop (~1970-
  2010: R.D. Burman's revolution & the disco/Bappi Lahiri era; Gulzar/Jagjit Singh ghazal; A.R. Rahman's
  transformation (Roja→); the 90s Indipop boom (Alisha Chinai, Daler Mehndi, bhangra-pop); Sufi-rock &
  the 2000s composers).
## Open decisions to make along the way
- **Caribbean:** standalone survey or annex to Latin America? (Leaning standalone — reggae alone
  justifies it.)
- **Persian & Turkish:** fold into MENA or give their own installments? (Both have deep independent
  classical traditions — probably their own threads within a MENA master.)
- **A final "global/fusion" capstone?** Once regions are done, a closing survey on world-fusion,
  diaspora crossover, and the fully globalized streaming present could tie all continents together.
- **Grand master index:** eventually, a top-level file linking all regional masters into one
  planet-wide guide.
