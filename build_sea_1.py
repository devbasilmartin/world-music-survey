#!/usr/bin/env python3
"""Build Southeast Asia, installment 1: Gamelan & Island Classical Traditions.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Southeast Asian Music — Installment 1: "
         "Gamelan & the Island Classical Traditions")

FRAMING = (
    "Southeast Asia's island world -- above all Indonesia -- gave humanity one of its most beautiful "
    "musical inventions: the GAMELAN, a shimmering orchestra of tuned bronze gongs, metallophones, and "
    "drums, tuned to itself rather than any universal pitch, and played as a single communal instrument. "
    "In the refined courts of Central JAVA it flows in meditative, interlocking cycles; in BALI it "
    "erupts into the dazzling, explosive virtuosity of gong kebyar and the hundred-voiced KECAK "
    "'monkey chant'. Its music is organized not by harmony but by CYCLIC TIME -- great gongs marking "
    "nested rhythmic cycles (the colotomic structure) beneath a skeletal melody and its elaborations -- "
    "and colored by the SHIMMER of paired instruments tuned slightly apart. Around it live the all-night "
    "WAYANG KULIT shadow-puppet epics and the Sundanese world of the bamboo flute and zither. This "
    "installment lays the classical island foundation before the mainland traditions and the pop era to "
    "come. Cross-links: gamelan's profound influence on the West (Debussy, Colin McPhee, Lou Harrison, "
    "and American minimalism); the Hindu Ramayana/Mahabharata shared with India; the pentatonic East "
    "Asian world. Names transliterated; (Traditional) marks forms, instruments, or pieces to seed "
    "listening. Region: island Southeast Asia (Indonesia -- Java, Bali, Sunda)."
)

SECTIONS = [
    (
        "GAMELAN: THE BRONZE ORCHESTRA",
        "A gamelan is a complete orchestra of tuned bronze -- gongs, gong-chimes, and metallophones "
        "with drums, strings, and voices -- built and tuned as a single unit, so that no two gamelans "
        "sound quite alike. More than music, it is a communal and sacred object, the beating heart of "
        "Indonesian culture.",
        [
            ("Gamelan (the tuned-bronze orchestra)", None),
            ("The gamelan as one instrument (tuned to itself)", None),
            ("Bronze, gongs & the sacred ensemble", None),
            ("Communal music-making (the gamelan spirit)", None),
        ],
    ),
    (
        "THE JAVANESE COURT GAMELAN",
        "In the royal courts of Solo and Yogyakarta, Central Javanese gamelan is refined, flowing, and "
        "meditative -- soft mallets, a female singer (sindhen) and male chorus (gerong) floating over "
        "the bronze. This courtly art is called karawitan, and its pieces (gendhing) can unfold with "
        "serene, hypnotic patience. 'Ketawang Puspawarna' rode the Voyager Golden Record into space.",
        [
            ("Ketawang Puspawarna (on the Voyager Golden Record)", None),
            ("Central Javanese court gamelan (Solo & Yogyakarta)", None),
            ("The sindhen & gerong (the gamelan voices)", None),
            ("Karawitan & gendhing (the courtly art & its pieces)", None),
            ("The meditative Javanese style (soft & flowing)", None),
        ],
    ),
    (
        "SLENDRO, PELOG & THE TUNING",
        "Gamelan uses two tuning systems -- the five-tone SLENDRO and the seven-tone PELOG -- neither "
        "matching Western tuning, and each gamelan tuned uniquely. Paired instruments are deliberately "
        "set a hair apart so their beating creates the famous acoustic SHIMMER (ombak, 'wave'), the "
        "living glow of the sound.",
        [
            ("Slendro & pelog (the two gamelan tunings)", None),
            ("Non-tempered tuning (each gamelan unique)", None),
            ("The shimmer / ombak (paired-instrument beating)", None),
            ("Embat (the tuning character of a gamelan)", None),
        ],
    ),
    (
        "COLOTOMIC STRUCTURE & CYCLIC TIME",
        "Gamelan music is built on cycles, not chord progressions. Great gongs (gong ageng, kenong, "
        "kempul) punctuate nested rhythmic cycles -- the COLOTOMIC structure -- beneath a skeletal core "
        "melody (balungan) that other instruments elaborate, and the whole can shift density through "
        "levels of tempo (irama). Time itself is circular.",
        [
            ("Colotomic structure (the gong-marked cycles)", None),
            ("Gong ageng, kenong & kempul (the punctuating gongs)", None),
            ("Balungan (the skeletal core melody)", None),
            ("Irama (the levels of tempo & density)", None),
            ("Cyclic time (the circular sense of the gamelan)", None),
        ],
    ),
    (
        "THE GAMELAN INSTRUMENTS",
        "The ensemble is a family of bronze and more: the metallophones (saron, demung, gender), the "
        "gong-chime rows (bonang), the wooden gambang xylophone, the leading kendang drums, and the "
        "melodic softeners -- the bowed rebab, the suling flute, and the siter zither -- with the human "
        "voice above.",
        [
            ("Saron, demung & gender (the metallophones)", None),
            ("Bonang (the gong-chime rows)", None),
            ("Kendang (the leading drums)", None),
            ("Rebab, suling & siter (the melodic instruments)", None),
            ("Gambang (the gamelan xylophone)", None),
        ],
    ),
    (
        "BALINESE GAMELAN: GONG KEBYAR & THE SHIMMER",
        "Balinese gamelan is the opposite of Javanese restraint -- brilliant, fast, and explosive. The "
        "20th-century GONG KEBYAR ('to burst into flame') dazzles with sudden dynamics and KOTEKAN, "
        "lightning interlocking figures split between paired players. Semar pegulingan, gender wayang, "
        "and the giant-bamboo jegog complete a thrilling world.",
        [
            ("Gong kebyar (the explosive Balinese style)", None),
            ("Kotekan (the interlocking Balinese figuration)", None),
            ("Sudden dynamics & brilliance (the kebyar sound)", None),
            ("Semar pegulingan & gender wayang (Balinese ensembles)", None),
            ("Jegog (the giant-bamboo gamelan of West Bali)", None),
        ],
    ),
    (
        "THE KECAK & THE VOICE",
        "Bali's most electrifying music uses no bronze at all: the KECAK, a 'monkey chant' in which "
        "scores of men interlock rhythmic 'cak' syllables into a pulsing human gamelan, telling the "
        "Ramayana. Rooted in the sanghyang trance ritual and shaped in the 1930s, it is a mesmerizing "
        "vocal-percussion masterpiece.",
        [
            ("Kecak (the Balinese monkey chant)", None),
            ("The interlocking vocal percussion (the human gamelan)", None),
            ("Sanghyang trance & the kecak's roots", None),
            ("The Ramayana in the kecak", None),
        ],
    ),
    (
        "WAYANG KULIT & THE SUNDANESE WORLD",
        "Gamelan lives inside theater. The WAYANG KULIT shadow-puppet play -- a single dalang voicing "
        "all characters through all-night Ramayana and Mahabharata epics, cued to the gamelan -- is a "
        "pinnacle of Javanese-Balinese art. To the west, the Sundanese of Java sing tembang Sunda over "
        "the kacapi zither and suling flute, a gentler, plaintive sound.",
        [
            ("Wayang kulit (the shadow-puppet theater)", None),
            ("The dalang (the puppeteer-narrator-conductor)", None),
            ("The all-night epic (Ramayana & Mahabharata in wayang)", None),
            ("Sundanese kacapi suling (zither & flute of West Java)", None),
            ("Tembang Sunda & degung (the Sundanese styles)", None),
        ],
    ),
    (
        "THE SHIMMER GOES GLOBAL & THE ROAD AHEAD",
        "Gamelan reshaped Western music: Debussy heard it at the 1889 Paris Exposition, Colin McPhee and "
        "Lou Harrison devoted careers to it, and it fed American minimalism (Steve Reich, Philip Glass). "
        "Today gamelan ensembles thrive worldwide. Cross-link: from this island classical world to the "
        "mainland traditions (#2) and the modern pop era ahead.",
        [
            ("Gamelan influences the West (Debussy, 1889 Paris, cross-link)", None),
            ("Colin McPhee & Lou Harrison (the Western gamelan devotees)", None),
            ("Gamelan & American minimalism (Reich & Glass, cross-link)", None),
            ("The global gamelan (ensembles worldwide)", None),
            ("Toward the mainland & the pop era (roads ahead)", None),
        ],
    ),
]

STEM = "sea_music_1_GAMELAN_ISLAND_CLASSICAL"


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
