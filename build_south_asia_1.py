#!/usr/bin/env python3
"""Build India / South Asia, installment 1: The Classical Roots (Raga, Tala & the Two Systems).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers the deep roots & classical foundations.
Dedup is by TITLE only -- every title unique region-wide. For art music, name the WORK/composer.
"""

TITLE = ("The Story of Indian & South Asian Music — Installment 1: "
         "The Classical Roots — Raga, Tala & the Two Great Systems")

FRAMING = (
    "Indian classical music is one of the oldest continuously living art musics on Earth, and its ideas "
    "-- RAGA (the melodic framework) and TALA (the rhythmic cycle) -- underlie almost everything South "
    "Asia sings and plays. Its roots reach back to the sung SAMAVEDA and the ancient treatise the Natya "
    "Shastra, and to a conception of sound (nada) as sacred. Around the 13th-16th centuries the tradition "
    "split into two great systems: HINDUSTANI in the north (absorbing Persian and Central Asian currents "
    "under the Delhi Sultanate and Mughals) and CARNATIC in the south (preserving a temple-and-devotion "
    "continuity), each with its own instruments, forms, and lineages -- but sharing the raga/tala "
    "grammar and a guru-to-disciple oral transmission (the guru-shishya parampara). This installment "
    "lays the FOUNDATIONS -- the theory, the instruments, the forms, and the two systems' divergence -- "
    "before later installments meet the great masters, the film-song juggernaut, the folk and devotional "
    "worlds, and modern South Asian pop. Cross-links: Persian/Arab maqam and Sufi music (MENA survey); "
    "the raga's later global reach into jazz and rock (forward). Names given as (Traditional) are ragas, "
    "talas, forms, or concepts -- import them as listening seeds. Region focus: India (Hindustani & "
    "Carnatic); the wider South Asia and its pop come in later installments."
)

SECTIONS = [
    (
        "THE VEDIC & ANCIENT ROOTS",
        "Indian music's taproot is ritual sound. The SAMAVEDA set sacred verses to melody over three "
        "millennia ago -- arguably the world's oldest living musical tradition -- and the concept of "
        "NADA BRAHMA ('sound is God') made music a spiritual discipline. The ancient Natya Shastra of "
        "Bharata codified drama, music, and the theory of rasa (aesthetic emotion).",
        [
            ("Samaveda chant (the sung Veda, music's ancient root)", None),
            ("Nada Brahma (sound as the sacred, the philosophy)", None),
            ("The Natya Shastra (Bharata's ancient treatise)", None),
            ("Rasa (the theory of aesthetic emotion)", None),
            ("Om & the primordial sound", None),
            ("Marga to desi (sacred to regional music, the old split)", None),
        ],
    ),
    (
        "RAGA: THE MELODIC SOUL",
        "A RAGA is not a scale but a living melodic framework -- a set of notes, characteristic phrases, "
        "ornaments, and a mood, often tied to a time of day or season. Melody unfolds over a constant "
        "drone (the tanpura), against the twelve microtonally-inflected swaras. To play a raga is to "
        "inhabit and slowly reveal a whole emotional world.",
        [
            ("Raga (the melodic framework, not a scale)", None),
            ("The seven swaras (Sa Re Ga Ma Pa Dha Ni)", None),
            ("The tanpura drone (the ever-present ground)", None),
            ("Time-of-day & seasonal ragas (raga & mood)", None),
            ("Aroha & avaroha (ascending/descending phrases)", None),
            ("Shruti & microtonal inflection (the notes between notes)", None),
            ("Alap (the unmetered raga exposition)", None),
        ],
    ),
    (
        "TALA: THE RHYTHMIC CYCLE",
        "TALA is time organized as a repeating cycle of beats, not a bar-by-bar meter. Teental's 16 "
        "beats, the emphatic downbeat (sam) that soloist and drummer race to meet, and the intricate "
        "play of tempo (layakari) make Indian rhythm a cyclical, conversational art -- the drummer both "
        "keeper and provocateur.",
        [
            ("Tala (the cyclical rhythmic framework)", None),
            ("Teental (the 16-beat cycle)", None),
            ("The sam (the cycle's returning downbeat)", None),
            ("Layakari (the play of tempo & subdivision)", None),
            ("Matra & vibhag (beats & measures of a tala)", None),
            ("Tihai (the thrice-repeated rhythmic cadence)", None),
        ],
    ),
    (
        "THE GURU-SHISHYA PARAMPARA & THE ORAL TRADITION",
        "Indian classical music is transmitted person to person, guru to disciple (shishya), over years "
        "of devoted apprenticeship -- the guru-shishya parampara. There is no fixed score; the music "
        "lives in memory, improvisation, and the distinct styles of family/lineage schools (GHARANAS). "
        "Riyaz -- relentless practice -- is its discipline.",
        [
            ("Guru-shishya parampara (the master-disciple lineage)", None),
            ("Gharana (the stylistic school/lineage)", None),
            ("Improvisation within tradition (the raga made new)", None),
            ("The oral tradition (music beyond notation)", None),
            ("Riyaz (the discipline of practice)", None),
        ],
    ),
    (
        "THE HINDUSTANI / CARNATIC SPLIT (c. 13th-16th c.)",
        "Once one tradition, Indian classical music diverged. In the north, contact with Persian and "
        "Central Asian music under the Delhi Sultanate and Mughals (the polymath Amir Khusrau a legendary "
        "figure) produced HINDUSTANI music; the south, more insulated, kept a temple-and-devotion "
        "continuity as CARNATIC music. Same raga/tala grammar, two divergent worlds.",
        [
            ("The Hindustani-Carnatic divergence (north & south)", None),
            ("Persian & Central Asian influence on the north", None),
            ("Amir Khusrau (legendary north-Indian innovator, seed)", None),
            ("Carnatic continuity (the temple-devotion south)", None),
            ("One grammar, two systems (the shared raga/tala)", None),
        ],
    ),
    (
        "THE INSTRUMENTS OF THE NORTH (HINDUSTANI)",
        "Hindustani music gave the world its most iconic Indian instruments: the shimmering SITAR and the "
        "fretless SAROD, the weeping SARANGI and the bamboo BANSURI flute, the hammered SANTOOR, the "
        "double-reed SHEHNAI, and above all the TABLA, whose spoken drum-language (bols) is a whole art. "
        "The ustad (master) tradition presides.",
        [
            ("Sitar (the iconic Hindustani plucked lute)", None),
            ("Sarod (the fretless north-Indian lute)", None),
            ("Sarangi (the bowed voice-of-a-hundred-colors)", None),
            ("Bansuri (the bamboo transverse flute)", None),
            ("Tabla & the bols (the drum's spoken language)", None),
            ("Shehnai & santoor (reed & hammered dulcimer)", None),
            ("Dhrupad & khyal (the oldest and the classic Hindustani forms)", None),
        ],
    ),
    (
        "THE INSTRUMENTS & FORMS OF THE SOUTH (CARNATIC)",
        "Carnatic music is song-centered and devotional. The plucked VEENA, the barrel-drum MRIDANGAM, "
        "the clay-pot GHATAM, and the (adopted) violin accompany the KRITI -- a devotional composition in "
        "three parts. The 18th-century TRINITY -- Tyagaraja, Muthuswami Dikshitar, and Syama Sastri -- "
        "wrote its core repertoire; here are two of its most beloved works.",
        [
            ("Endaro Mahanubhavulu", "Tyagaraja"),
            ("Vatapi Ganapatim", "Muthuswami Dikshitar"),
            ("Veena (the south-Indian plucked lute)", None),
            ("Mridangam & ghatam (the Carnatic drums)", None),
            ("The kriti (the Carnatic devotional composition)", None),
            ("The Carnatic Trinity (Tyagaraja, Dikshitar, Syama Sastri)", None),
            ("Melakarta & kalpana swara (the raga-scale system & improvisation)", None),
        ],
    ),
    (
        "THE DEVOTIONAL HEART & THE ROADS AHEAD",
        "At bottom this music is devotional -- born of the BHAKTI movement's ecstatic worship and the "
        "temple, its purpose the divine as much as the beautiful. Purandara Dasa systematized Carnatic "
        "teaching; the raga's meditative power would later enthrall the world (jazz, the Beatles). Cross-"
        "links ahead: the classical masters (#2), Sufi qawwali (#4), and the raga goes global.",
        [
            ("Bhakti (the devotional movement behind the music)", None),
            ("Temple music & the sacred purpose", None),
            ("Purandara Dasa (father of Carnatic pedagogy, seed)", None),
            ("The meditative power of the raga (toward the global reach)", None),
            ("From the Vedas to the concert stage (the classical arc)", None),
        ],
    ),
]

STEM = "south_asia_music_1_CLASSICAL_ROOTS_RAGA_TALA"


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
