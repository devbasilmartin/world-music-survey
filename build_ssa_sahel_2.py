#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Sahel, installment 2: The Modern Malian Foundation & Desert Blues' Birth.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1960-1990.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of Sahelian Music — Installment 2: "
         "The Modern Malian Foundation & the Birth of Desert Blues (c. 1960-1990)")

FRAMING = (
    "Independence remade Sahelian music. When Mali freed itself in 1960, Modibo Keita's government made "
    "culture a matter of state: RADIO MALI broadcast the nation to itself, regional biennale festivals "
    "fed talent upward, and a system of modern dance ORCHESTRAS -- brass, electric guitars, and Cuban "
    "and Congolese grooves fused with Mande and Songhai song -- became the sound of the young republic. "
    "The RAIL BAND, house band of Bamako's railway-station hotel, was its crucible (a young Salif Keita "
    "and Mory Kante both passed through). Alongside the orchestras, two solitary geniuses invented what "
    "the world would later call DESERT BLUES: ALI FARKA TOURE, from the Niger-bend town of Niafunke, "
    "whose hypnotic Songhai-Fulani guitar was so close to the Mississippi Delta that he was dubbed 'the "
    "African John Lee Hooker'; and BOUBACAR TRAORE 'Kar Kar', whose 'Mali Twist' was the anthem of "
    "independence. And in exile camps to the north, a Tuareg generation traded the imzad for the "
    "electric guitar -- ISHUMAR -- and TINARIWEN was born. Cross-links: US blues (the Mali-Mississippi "
    "affinity made explicit); Cuban son (Latin survey) under the orchestras; the Mande griot world "
    "(covered in the separate COMPLETE West Africa survey -- Salif Keita and Mory Kante flagged as "
    "cross-over). Content notes: Tuareg exile and rebellion are kept. Region: Mali, with the Tuareg "
    "north (Niger/Algeria/Libya)."
)

SECTIONS = [
    (
        "INDEPENDENCE & RADIO MALI (1960s)",
        "The newly independent Mali built a cultural machine: Radio Mali carried music nationwide, the "
        "state sponsored regional orchestras, and biennale festivals in Bamako funneled the best "
        "players into national ensembles. Music was nation-building -- modern, pan-African, and proud, "
        "a Malian answer to the era's independence optimism.",
        [
            ("Radio Mali & the broadcast nation (1960s)", None),
            ("Malian independence & state cultural policy", None),
            ("The biennale festival system (feeding the orchestras)", None),
            ("Modern orchestra Mali (the new republic's sound)", None),
            ("Cuban & Congolese grooves in Malian pop", None),
        ],
    ),
    (
        "THE RAIL BAND & THE BAMAKO SOUND (c. 1970)",
        "The Rail Band -- resident at the Buffet Hotel de la Gare in Bamako -- was the era's great "
        "incubator, turning Mande epics into electric orchestra music under bandleader Tidiani Kone. "
        "Both Salif Keita and Mory Kante sang there before fame. Region-integrity note: Keita and Kante "
        "belong to the Mande/West Africa story too (flagged); the Rail Band itself is quintessential "
        "Bamako.",
        [
            ("Mali Sadio", "Rail Band"),
            ("Rail Band (the Buffet de la Gare orchestra)", None),
            ("Tidiani Kone (Rail Band's founding leader)", None),
            ("Salif Keita & Mory Kante pass through (flagged Mande/West)", None),
            ("Electric Mande epic (the Bamako orchestra sound)", None),
        ],
    ),
    (
        "THE STATE & REGIONAL ORCHESTRAS (c. 1965-1985)",
        "Across Mali, each region fielded its orchestra, and the national bands set the standard. Super "
        "Biton de Segou, the National Badema, Kanaga de Mopti, and the Orchestre Regional de Kayes "
        "blended horns, guitars, and local repertoire into a distinctive Malian modernism -- stately, "
        "danceable, and rooted.",
        [
            ("Super Biton de Segou (the Segou orchestra)", None),
            ("National Badema du Mali (the national band)", None),
            ("Kanaga de Mopti (the Mopti regional orchestra)", None),
            ("Orchestre Regional de Kayes", None),
            ("The Malian modern-orchestra template", None),
            ("Horns, guitars & the regional repertoire", None),
        ],
    ),
    (
        "SUPER DJATA & THE MALIAN GUITAR (c. 1975-1985)",
        "A harder, guitar-driven Bamako sound arrived with Zani Diabate and his Super Djata Band, whose "
        "electric Bambara-rooted playing turned traditional hunter and dance rhythms into fiery pop. "
        "The Malian guitar -- fast, wiry, pentatonic -- was becoming an instrument as distinctive as "
        "any in Africa.",
        [
            ("Zani Diabate & the Super Djata Band", None),
            ("The electric Bambara guitar (Bamako dance pop)", None),
            ("Hunter-rhythm rock (Super Djata's fire)", None),
            ("The wiry pentatonic Malian guitar sound", None),
            ("Bamako club music of the 1970s-80s", None),
        ],
    ),
    (
        "ALI FARKA TOURE & THE RIVER BLUES (c. 1976-1990)",
        "From Niafunke on the Niger, Ali Farka Toure played a spare, hypnotic guitar rooted in Songhai "
        "and Fulani song and uncannily close to the Mississippi Delta -- 'the African John Lee Hooker'. "
        "He always insisted the blues came FROM Africa, not to it. 'Diaraby' and his desert sound made "
        "the Mali-Mississippi kinship undeniable. Cross-link: the US blues survey.",
        [
            ("Diaraby", "Ali Farka Toure"),
            ("The river blues of Niafunke", None),
            ("Songhai-Fulani guitar (the Farka sound)", None),
            ("The African John Lee Hooker (the Mali-Mississippi kinship)", None),
            ("Timbuktu-region desert blues (the Niger bend, electrified)", None),
            ("The blues came from here (Farka's claim)", None),
        ],
    ),
    (
        "BOUBACAR TRAORE \"KAR KAR\" (c. 1963-1990)",
        "Boubacar Traore's 'Mali Twist' rang out from Radio Mali at independence -- a young man's "
        "guitar hymn to the new nation. His warm, bluesy fingerpicking blended Arab, Mande, and "
        "American strains. Content note: after early fame he vanished into hardship and manual labor "
        "for years before a moving 1990s rediscovery.",
        [
            ("Mali Twist", "Boubacar Traore"),
            ("Boubacar Traore Kar Kar (the independence troubadour)", None),
            ("Bluesy Malian fingerpicking (Arab-Mande-American blend)", None),
            ("The lost years & the rediscovery (Kar Kar's story)", None),
            ("Independence-optimism song (Radio Mali's guitar)", None),
        ],
    ),
    (
        "THE TUAREG ELECTRIFY: ISHUMAR & TINARIWEN (c. 1979-1990)",
        "In Tuareg exile camps in Algeria and Libya, a dispossessed generation -- the ISHUMAR -- swapped "
        "the imzad for the electric guitar and sang of drought, exile, and rebellion. Around 1979-82 "
        "the collective that became TINARIWEN formed, and their raw cassettes circulated hand to hand "
        "as the anthems of the Tuareg cause. Content note: Tuareg displacement and the coming rebellions "
        "are kept in view.",
        [
            ("Ishumar (the Tuareg exile-guitar generation)", None),
            ("Tinariwen forms in the ishumar camps (~1979-82)", None),
            ("The electric guitar replaces the imzad (Tuareg turn)", None),
            ("Cassette anthems of the Tuareg cause", None),
            ("Drought, exile & rebellion in Tamashek song", None),
            ("Tamanrasset & the Libyan camps (the desert-blues forge)", None),
        ],
    ),
    (
        "WASSOULOU STIRS & THE ROADS AHEAD (c. 1980-1990)",
        "South of Bamako, the Wassoulou region's hunter-music heritage and its kamale ngoni (youth "
        "harp) were feeding a new, non-griot, women-led style; Nahawa Doumbia and others began to rise. "
        "The stage was set for the global desert-blues and wassoulou breakout of the 1990s. Cross-"
        "links: the West Africa survey's Mande world; the electric desert blues to come (#3).",
        [
            ("Wassoulou hunter-music roots (south of Bamako)", None),
            ("Kamale ngoni (the Wassoulou youth harp)", None),
            ("Nahawa Doumbia (early Wassoulou voice, seed)", None),
            ("Non-griot, women-led Malian song (Wassoulou rising)", None),
            ("Toward the 1990s desert-blues breakout (roads ahead)", None),
        ],
    ),
]

STEM = "ssa_sahel_music_2_MALIAN_FOUNDATION_DESERT_BLUES"


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
                imp.append(title)
        md.append("")
    with open(f"{STEM}.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md).rstrip() + "\n")
    with open(f"{STEM}_IMPORT.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(imp) + "\n")
    print(f"Wrote {STEM}.md and {STEM}_IMPORT.txt")
    print(f"Tracks: {len(imp)}  |  Sections: {len(SECTIONS)}")


if __name__ == "__main__":
    build()
