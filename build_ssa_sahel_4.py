#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Sahel, installment 4 (FINAL): Crisis, the New Generation & the Sahel Today.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 2010-present.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of Sahelian Music — Installment 4 (Finale): "
         "Crisis, the New Generation & the Sahel Today (c. 2010-present)")

FRAMING = (
    "The Sahel's newest chapter opens with catastrophe and answers it with music. In 2012 jihadist "
    "groups seized northern Mali and BANNED MUSIC under sharia -- radios silenced, instruments burned, "
    "the Festival au Desert exiled, musicians forced to flee. Out of that trauma came defiance: the "
    "displaced Songhai youth of SONGHOY BLUES turned exile into rock; and across the border a NIGER "
    "GUITAR REVOLUTION -- BOMBINO and MDOU MOCTAR from Agadez -- pushed Tuareg assouf into psych-rock "
    "and took it to the top of the world's stages. A Tuareg new wave (Tamikrest, Imarhan, the women of "
    "Les Filles de Illighadad) matured the desert-blues genre; FATOUMATA DIAWARA carried Malian art-pop "
    "global; ngoni master Bassekou Kouyate recorded defiance during the coup; and Bamako filled with "
    "kora-pop and Bambara rap. Mauritania's Noura Mint Seymali reinvented Moorish music as psychedelia, "
    "and the wider desert -- Niger, Chad -- kept inventing. Through coups and insecurity, the music "
    "remains the Sahel's memory and its resistance. This installment closes the Sahel survey -- and "
    "with it, ALL of Sub-Saharan Africa. Cross-links: US/global rock (the desert-blues crossover); the "
    "Mande griot world (Bassekou, Sidiki Diabate flagged Mande/West). Content notes: the 2012 music "
    "ban, jihadist violence, and the 2020-23 coups are kept with care. Region: Mali, Niger, Mauritania "
    "& Chad."
)

SECTIONS = [
    (
        "2012: THE MUSIC BAN (northern Mali)",
        "When Ansar Dine, MUJAO, and AQIM seized Timbuktu, Gao, and Kidal in 2012, they outlawed music "
        "entirely -- a devastating blow in a land where music is memory, law, and lifeblood. Radio "
        "stations were shuttered, instruments destroyed, and musicians threatened and driven south or "
        "abroad. Content note: this is one of modern history's starkest assaults on a musical culture.",
        [
            ("The 2012 jihadist occupation of northern Mali", None),
            ("Music banned under sharia (Timbuktu, Gao, Kidal)", None),
            ("Instruments burned & radios silenced", None),
            ("Musicians flee the north (the exile begins)", None),
            ("A culture where music is memory & law (why the ban cut deep)", None),
        ],
    ),
    (
        "SONGHOY BLUES & THE MUSIC IN EXILE (c. 2012-present)",
        "Four young Songhai musicians displaced from the occupied north met in Bamako and formed Songhoy "
        "Blues, turning loss into fierce guitar rock. Championed by Damon Albarn's Africa Express, their "
        "'Soubour' ('Patience') and the album 'Music in Exile' made them global ambassadors of a "
        "defiant, danceable Sahel. Cross-link: the desert blues, now electrified with punk urgency.",
        [
            ("Soubour", "Songhoy Blues"),
            ("Songhoy Blues (the sound of exile from the north)", None),
            ("Music in Exile (the Africa Express debut)", None),
            ("Songhai desert rock (defiant & danceable)", None),
            ("Bamako as refuge for the northern musicians", None),
        ],
    ),
    (
        "THE NIGER GUITAR REVOLUTION: BOMBINO & MDOU MOCTAR (c. 2010-present)",
        "Niger's Agadez became the desert guitar's new capital. Bombino's incendiary Tuareg rock "
        "('Azel', the Dan Auerbach-produced 'Nomad') and Mdou Moctar's psychedelic fireworks ('Afrique "
        "Victime', and the Prince-inspired film 'Akounak') carried assouf to rock audiences worldwide. "
        "Cross-link: Hendrix and psych-rock meet the Sahara.",
        [
            ("Azel", "Bombino"),
            ("Afrique Victime", "Mdou Moctar"),
            ("Bombino (the Agadez guitar star)", None),
            ("Mdou Moctar (Tuareg psych-rock & Akounak)", None),
            ("Agadez (Niger's desert-guitar capital)", None),
            ("Tuareg rock meets Hendrix (the global crossover)", None),
        ],
    ),
    (
        "THE TUAREG ASSOUF NEW WAVE (c. 2010-present)",
        "A deep bench matured the genre. Tamikrest ('Chatma') brought poetry and polish; Imarhan a "
        "younger cool; Kel Assouf a heavier rock; and Les Filles de Illighadad from Niger centered "
        "women's guitar and the tende. Assouf was now a living, evolving international music, not a "
        "museum piece.",
        [
            ("Chatma", "Tamikrest"),
            ("Tamikrest (the poetic new-wave assouf)", None),
            ("Imarhan (the young Tuareg cool)", None),
            ("Les Filles de Illighadad (women's Tuareg guitar & tende, Niger)", None),
            ("Kel Assouf (the heavier desert rock)", None),
            ("Assouf as a living world genre", None),
        ],
    ),
    (
        "FATOUMATA DIAWARA & THE NEW MALIAN VOICES (c. 2011-present)",
        "Fatoumata Diawara -- Wassoulou-descended, actor turned singer -- became Mali's boldest new "
        "international voice, blending wassoulou roots with jazz, soul, and rock ('Nterini', collabs "
        "with Roberto Fonseca and Gorillaz). Alongside her, artists like Rokia Traore (flagged Mande) "
        "carried a globally fluent Malian art-song.",
        [
            ("Nterini", "Fatoumata Diawara"),
            ("Fatoumata Diawara (wassoulou roots into global art-pop)", None),
            ("Rokia Traore (Malian art-song, flagged Mande/West)", None),
            ("Wassoulou meets jazz, soul & rock", None),
            ("The new Malian women's voices (global fluency)", None),
        ],
    ),
    (
        "BAMAKO NOW: NGONI MASTERS, KORA-POP & RAP (c. 2010-present)",
        "Bamako pulses with the modern Sahel. Ngoni master Bassekou Kouyate cut the defiant 'Jama Ko' as "
        "the 2012 coup unfolded; Sidiki Diabate turned the kora into slick Afropop; Oumou Sangare "
        "returned with 'Yere Faga'; and a Bambara-language rap scene (Iba One, Tal B) ruled the youth. "
        "Region note: Bassekou and Sidiki belong to the Mande/griot world too (flagged).",
        [
            ("Jama Ko", "Bassekou Kouyate"),
            ("Yere Faga", "Oumou Sangare"),
            ("Bassekou Kouyate & Ngoni Ba (the ngoni goes electric, flagged Mande)", None),
            ("Sidiki Diabate (kora into Bamako Afropop, flagged Mande)", None),
            ("Iba One & Bamako rap (Bambara-language hip-hop)", None),
            ("Modern Bamako pop (kora, ngoni & the studio)", None),
        ],
    ),
    (
        "MAURITANIA, NIGER & CHAD TODAY (c. 2010-present)",
        "Across the desert belt, tradition kept modernizing. Mauritania's Noura Mint Seymali turned "
        "Moorish music into swirling psychedelia ('Tzenni'); Niger's Etran de L'Air made raucous Agadez "
        "wedding guitar; and Chad's Afrotronix fused Tuareg blues with electronica. The whole Sahel was "
        "plugging in on its own terms.",
        [
            ("Tzenni", "Noura Mint Seymali"),
            ("Noura Mint Seymali (Moorish psychedelia, Mauritania)", None),
            ("Etran de L'Air (Agadez wedding guitar, Niger)", None),
            ("Afrotronix (Chadian desert electro, diaspora)", None),
            ("The desert belt plugs in (Mauritania to Chad)", None),
        ],
    ),
    (
        "THE SAHEL TODAY: RESILIENCE & THE ROAD (c. 2013-present)",
        "Through jihadist insurgency and a wave of coups (Mali, Niger, Burkina, 2020-23), Sahelian music "
        "endures as memory and resistance. Vieux Farka Toure carries his father Ali's legacy ('the "
        "Hendrix of the Sahara'), the desert blues is cherished worldwide, and a new generation keeps "
        "the tradition alive. This closes the Sahel survey -- and ALL of Sub-Saharan Africa.",
        [
            ("Vieux Farka Toure (Ali's heir, the Hendrix of the Sahara)", None),
            ("Music as resistance & memory (the Sahel's answer)", None),
            ("Coups & insecurity (the 2020s Sahel)", None),
            ("The desert blues as world heritage", None),
            ("From imzad to the world stage (the Sahel arc closes)", None),
            ("All of Sub-Saharan Africa, complete (the milestone)", None),
        ],
    ),
]

STEM = "ssa_sahel_music_4_CRISIS_NEW_GENERATION_TODAY"


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
