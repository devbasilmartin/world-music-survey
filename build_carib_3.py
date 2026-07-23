#!/usr/bin/env python3
"""Build the Caribbean, installment 3: Calypso, Soca, Steelpan & the Wider Isles.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Caribbean Music — Installment 3: "
         "Calypso, Soca, Steelpan & the Wider Isles (Trinidad, Haiti, the Dominican Republic, Puerto Rico & the French Antilles)")

FRAMING = (
    "Beyond Cuba and Jamaica, the Caribbean teems with island musics as distinct as their languages. "
    "Trinidad gave the world CALYPSO -- the witty, topical 'kaiso' song of the calypsonians and Carnival "
    "(Mighty Sparrow, Lord Kitchener) -- its faster child SOCA, and the STEELPAN, the only acoustic "
    "instrument invented in the 20th century, hammered from discarded oil drums. HAITI carries the "
    "Vodou-rooted rara and mizik rasin and the sweet dance music KOMPA; the DOMINICAN REPUBLIC swings to "
    "the fast MERENGUE and the once-scorned, now-global BACHATA; PUERTO RICO beats with the Afro-Rican "
    "BOMBA and PLENA; and the FRENCH ANTILLES (Martinique, Guadeloupe) gave the biguine and then ZOUK, "
    "the sound of Kassav' that swept Africa. This installment maps the wider archipelago before the "
    "modern dancehall-and-reggaeton present (#4). Content notes: Haiti's Vodou-rooted music and the "
    "wartime satire of 'Rum and Coca-Cola' are treated factually and with respect. Cross-links: salsa and "
    "reggaeton in the Latin America survey (cross-linked; reggaeton's finale is #4); zouk -> kizomba "
    "(Africa). Names as commonly romanized. Region: the wider Caribbean."
)

SECTIONS = [
    (
        "TRINIDAD: CALYPSO & CARNIVAL",
        "Calypso -- descended from the West African-rooted 'kaiso' and the Carnival of Trinidad -- is a "
        "sharp, witty, topical song of social commentary, gossip, and satire, sung by 'calypsonians' with "
        "grand sobriquets. It was the island's newspaper set to music, and the roar of Carnival and the "
        "calypso tent. Content note: its verses often carried pointed political critique.",
        [
            ("Calypso (the topical song of Trinidad)", None),
            ("Kaiso & the calypso tent (the Carnival root)", None),
            ("The calypsonian (the sobriquet & the picong)", None),
            ("Trinidad Carnival (the fete & the road march)", None),
        ],
    ),
    (
        "THE GREAT CALYPSONIANS",
        "The golden age of calypso crowned larger-than-life stars. The Mighty Sparrow, the 'Calypso King "
        "of the World', reigned for decades ('Jean and Dinah'); Lord Kitchener was his great rival and "
        "the master of Carnival road marches; and Lord Invader's 'Rum and Coca-Cola' became a wartime "
        "sensation. Content note: the song satirized the US wartime base and was famously copied abroad.",
        [
            ("Jean and Dinah", "Mighty Sparrow"),
            ("Sugar Bum Bum", "Lord Kitchener"),
            ("Rum and Coca-Cola", "Lord Invader"),
            ("Mighty Sparrow (the Calypso King of the World)", None),
            ("Lord Kitchener (the road-march master)", None),
        ],
    ),
    (
        "SOCA: THE SOUL OF CALYPSO",
        "In the 1970s Lord Shorty fused calypso with Indian-Caribbean rhythms and funk to create SOCA -- "
        "the 'soul of calypso' -- a faster, more danceable party music that became the driving sound of "
        "modern Carnival. Machel Montano turned it into a stadium-filling, globally-touring force, "
        "alongside the raucous chutney-soca of the Indo-Trinidadian community.",
        [
            ("Soul of Calypso (the birth of soca)", "Lord Shorty"),
            ("Soca (the modern Carnival party music)", None),
            ("Machel Montano (the soca superstar)", None),
            ("Chutney soca (the Indo-Trinidadian fusion)", None),
            ("The soca road march (the Carnival anthem)", None),
        ],
    ),
    (
        "THE STEELPAN: MUSIC FROM OIL DRUMS",
        "From the banned drums of Carnival, the people of Trinidad hammered a new instrument out of "
        "discarded oil barrels -- the STEELPAN, the only acoustic instrument family invented in the 20th "
        "century. Full steel bands (the 'steel orchestra') play everything from calypso to Bach, and "
        "compete fiercely in the Panorama Carnival championship.",
        [
            ("Steelpan (the Trinidadian oil-drum instrument)", None),
            ("The steel band / steel orchestra", None),
            ("Panorama (the steelpan competition)", None),
            ("The pan yard & the tuning of the pan", None),
            ("From banned drums to the steelpan (the invention)", None),
        ],
    ),
    (
        "HAITI: KOMPA, RARA & MIZIK RASIN",
        "Haiti's music runs deep. KOMPA (konpa), the sweet, meringue-derived dance music of Nemours "
        "Jean-Baptiste, is the national pop sound; RARA is the raucous Vodou-rooted street procession of "
        "bamboo horns; and MIZIK RASIN ('roots music', by Boukman Eksperyans) fused Vodou drumming with "
        "rock. Content note: Vodou-rooted music treated as living heritage, with respect.",
        [
            ("Kompa (the Haitian national dance music)", None),
            ("Nemours Jean-Baptiste (the father of kompa)", None),
            ("Ke'm Pa Sote", "Boukman Eksperyans"),
            ("Rara (the Vodou-rooted street procession)", None),
            ("Mizik rasin (the Haitian roots-music movement)", None),
        ],
    ),
    (
        "THE DOMINICAN REPUBLIC: MERENGUE & BACHATA",
        "The Dominican Republic gave two great genres. MERENGUE -- a fast, joyous two-step of accordion, "
        "saxophone, tambora, and guira -- is the national dance (Juan Luis Guerra, Johnny Ventura); and "
        "BACHATA, once scorned as poor rural bar music, became a global romantic pop sensation. Content "
        "note: merengue was heavily promoted under the Trujillo dictatorship, kept factual.",
        [
            ("Ojala Que Llueva Cafe", "Juan Luis Guerra"),
            ("Merengue (the Dominican national dance)", None),
            ("Johnny Ventura (the merengue showman)", None),
            ("Bachata (the Dominican romantic guitar music)", None),
            ("Bachata goes global (from the margins to the world)", None),
        ],
    ),
    (
        "PUERTO RICO: BOMBA & PLENA",
        "Puerto Rico's deepest folk roots are Afro-Rican: BOMBA, a call-and-response of drum and dance in "
        "which the dancer leads the drummer, from the sugar-plantation communities; and PLENA, the "
        "narrative 'sung newspaper' of the streets with its hand-held panderetas. These roots underlie "
        "salsa and reggaeton. Cross-links: salsa & reggaeton in the Latin America survey (reggaeton finale #4).",
        [
            ("Bomba (the Afro-Puerto Rican drum-and-dance)", None),
            ("Plena (the Puerto Rican sung newspaper)", None),
            ("The panderetas & the bomba barriles (the drums)", None),
            ("The dancer leads the drum (the bomba dialogue)", None),
            ("Afro-Rican roots (bomba & plena as the foundation)", None),
        ],
    ),
    (
        "THE FRENCH ANTILLES: BIGUINE & ZOUK",
        "Martinique and Guadeloupe gave the elegant BIGUINE of the early-20th-century Paris ballrooms and "
        "the gwoka drums of Guadeloupe -- and then ZOUK, the pulsing, Creole-language dance-pop that the "
        "band Kassav' launched in the 1980s ('Zouk La Se Sel Medikaman Nou Ni'), a sensation across the "
        "Caribbean and Africa. Cross-link: zouk -> kizomba (Angola/Africa survey).",
        [
            ("Zouk La Se Sel Medikaman Nou Ni", "Kassav'"),
            ("Zouk (the French Antillean dance-pop)", None),
            ("Kassav' (the band that launched zouk)", None),
            ("Biguine (the Martinican ballroom music)", None),
            ("Gwoka (the Guadeloupean drum tradition)", None),
        ],
    ),
    (
        "THE WIDER ARCHIPELAGO & THE ROAD AHEAD",
        "From Trinidad's calypso and steelpan to Haitian kompa, Dominican merengue, Puerto Rican bomba, "
        "and French-Antillean zouk, the wider Caribbean is a mosaic of Afro-Creole dance musics, each its "
        "island's own voice. From these roots the survey turns to the modern present: dancehall, "
        "reggaeton, and the global Caribbean (#4). Cross-links: Cuba (#1); Jamaica (#2); Latin America; Africa.",
        [
            ("The wider Caribbean mosaic (many isles, many sounds)", None),
            ("The Afro-Creole dance tradition (the shared thread)", None),
            ("Carnival across the islands (the fete culture)", None),
            ("Toward dancehall & reggaeton (roads ahead)", None),
        ],
    ),
]

STEM = "carib_music_3_CALYPSO_SOCA_WIDER_ISLES"


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
