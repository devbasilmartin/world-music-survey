#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Sahel, installment 3: The Global Desert-Blues & Wassoulou Breakout.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1990-2010.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of Sahelian Music — Installment 3: "
         "The Global Desert-Blues & Wassoulou Breakout (c. 1990-2010)")

FRAMING = (
    "In the 1990s and 2000s the Sahel conquered the world-music stage. ALI FARKA TOURE won a Grammy for "
    "'Talking Timbuktu' (1994, with Ry Cooder) and another for his luminous kora-and-guitar duets with "
    "Toumani Diabate, proving to the West that the blues had Malian roots. TINARIWEN carried the Tuareg "
    "ishumar guitar from rebel cassettes to global festivals, birthing a whole 'desert blues' genre "
    "(Terakaft, Tartit, Etran Finatawa in their wake). A generation of WASSOULOU divas led by OUMOU "
    "SANGARE turned the non-griot women's tradition into fierce, danceable pop with pointed lyrics on "
    "polygamy and women's lives. The blind Bamako couple AMADOU & MARIAM became genuine global pop "
    "stars (with Manu Chao), Habib Koite charmed the world with acoustic Malian song, and Boubacar "
    "Traore was rediscovered. The FESTIVAL AU DESERT near Timbuktu made the dunes a pilgrimage site for "
    "world music -- until jihadist violence shut it down in 2012. Cross-links: US blues (the "
    "Mali-Mississippi kinship, now global); the Mande griot world (Toumani Diabate, Habib Koite flagged "
    "as Mande/West cross-over, from the separate COMPLETE West Africa survey). Content note: the "
    "gathering crisis in northern Mali is flagged forward. Region: Mali (with Mauritania, Niger & the "
    "Tuareg north)."
)

SECTIONS = [
    (
        "ALI FARKA TOURE CONQUERS THE WORLD (c. 1990-2006)",
        "Ali Farka Toure's global moment came with 'Talking Timbuktu' (1994, with Ry Cooder), a Grammy "
        "winner that made his Niger-bend guitar world-famous, followed by his home-recorded 'Niafunke' "
        "and the exquisite duets with kora master Toumani Diabate. His posthumous 'Savane' (2006) sealed "
        "his stature as one of Africa's greatest. Cross-link: the US blues, its African source revealed.",
        [
            ("Ai Du", "Ali Farka Toure"),
            ("Talking Timbuktu (the 1994 Grammy album, with Ry Cooder)", None),
            ("Niafunke (the home-recorded river-blues album)", None),
            ("In the Heart of the Moon (the Toumani Diabate duets)", None),
            ("Savane (the posthumous masterpiece, 2006)", None),
            ("Toumani & Ali (kora-and-guitar, flagged Mande/West)", None),
        ],
    ),
    (
        "TINARIWEN & THE GLOBAL DESERT BLUES (c. 2001-2010)",
        "Tinariwen emerged from the Tuareg rebellion into world fame: 'The Radio Tisdas Sessions' (2001) "
        "and 'Aman Iman' (2007) turned their hypnotic assouf guitar and communal chants into a global "
        "phenomenon, and they defined 'desert blues' as an international genre. Their rebel-poet history "
        "gave the music its weight. Content note: their roots in armed rebellion are kept in view.",
        [
            ("Cler Achel", "Tinariwen"),
            ("Tinariwen goes global (the Aman Iman era)", None),
            ("The Radio Tisdas Sessions (2001, the first album)", None),
            ("Assouf guitar & communal chant (the Tinariwen sound)", None),
            ("Desert blues becomes a world genre", None),
            ("From rebel cassettes to world festivals", None),
        ],
    ),
    (
        "THE TUAREG GUITAR SPREADS (c. 2000-2010)",
        "Tinariwen's success opened a whole scene. Terakaft (a Tinariwen offshoot), the women's group "
        "Tartit from Timbuktu, and the Tuareg-Wodaabe fusion of Etran Finatawa carried the guitar "
        "onward, while in Niger a young Bombino was learning the style that would soon make him a star. "
        "The ishumar sound was now a Saharan movement.",
        [
            ("Terakaft (the Tinariwen offshoot)", None),
            ("Tartit (the Tuareg women's group, Timbuktu)", None),
            ("Etran Finatawa (Tuareg-Wodaabe desert fusion, Niger)", None),
            ("The Niger Tuareg scene stirs (Bombino ahead)", None),
            ("The ishumar guitar movement (a Saharan genre)", None),
        ],
    ),
    (
        "OUMOU SANGARE & THE WASSOULOU DIVAS (c. 1990-2010)",
        "Oumou Sangare's debut 'Moussolou' (1990) made her the queen of WASSOULOU -- the earthy, "
        "non-griot, women-led music of southern Mali -- and a fearless voice against polygamy and for "
        "women's dignity ('Saa Magni'). Around her rose Sali Sidibe, Coumba Sidibe, and a wave of divas "
        "riding the kamale ngoni's rolling groove. Content note: her lyrics challenged social norms.",
        [
            ("Moussolou", "Oumou Sangare"),
            ("Saa Magni", "Oumou Sangare"),
            ("Oumou Sangare (the queen of wassoulou)", None),
            ("Sali Sidibe & Coumba Sidibe (wassoulou divas)", None),
            ("Wassoulou women's pop (feminist lyrics)", None),
            ("The kamale ngoni groove goes pop", None),
        ],
    ),
    (
        "AMADOU & MARIAM: THE BLIND COUPLE OF BAMAKO (c. 1998-2010)",
        "Amadou Bagayoko and Mariam Doumbia -- who met at Bamako's institute for the blind -- became "
        "the Sahel's biggest global pop stars. Their Afro-blues-rock, crowned by Manu Chao's production "
        "on 'Dimanche a Bamako' (2004) and Damon Albarn's touch on 'Sabali', filled arenas worldwide. "
        "They made Malian pop a mainstream European sound.",
        [
            ("Beaux Dimanches", "Amadou & Mariam"),
            ("Sabali", "Amadou & Mariam"),
            ("Amadou & Mariam (the blind couple of Bamako)", None),
            ("Dimanche a Bamako (the Manu Chao album, 2004)", None),
            ("Afro-blues-rock (the Amadou & Mariam sound)", None),
            ("Malian pop fills European arenas", None),
        ],
    ),
    (
        "HABIB KOITE, KAR KAR'S RETURN & THE SONGWRITERS (c. 1995-2010)",
        "A gentler Malian songcraft went global too. Habib Koite's warm, cross-ethnic acoustic pop "
        "('Cigarette Abana') made him one of Africa's most beloved troubadours, and Boubacar Traore was "
        "movingly rediscovered ('Mariama', the film 'Je Chanterai Pour Toi'). Region note: Koite is "
        "Khassonke/Mande (flagged), but his sound is pan-Malian.",
        [
            ("Cigarette Abana", "Habib Koite"),
            ("Mariama", "Boubacar Traore"),
            ("Habib Koite & Bamada (cross-ethnic Malian song, flagged Mande)", None),
            ("Kar Kar's rediscovery (Je Chanterai Pour Toi)", None),
            ("The acoustic Malian singer-songwriter", None),
        ],
    ),
    (
        "MAURITANIA, NIGER & THE WIDER SAHEL MODERNIZE (c. 1990-2010)",
        "The breakout was Sahel-wide. In Mauritania, Malouma modernized Moorish music (and became a "
        "senator); in Niger, the reissued synth reveries of Mamman Sani and new Tuareg bands stirred; "
        "and in Timbuktu, Khaira Arby -- 'the nightingale of the north' -- sang powerfully of her city. "
        "The desert's many traditions were all going electric and outward.",
        [
            ("Malouma (modern Moorish music, Mauritania)", None),
            ("Khaira Arby (the nightingale of Timbuktu)", None),
            ("Mamman Sani (Niger's synth pioneer, reissued)", None),
            ("Modern Moorish & Tuareg voices (the wider Sahel)", None),
            ("The desert traditions go electric", None),
        ],
    ),
    (
        "FESTIVAL AU DESERT & THE SAHEL ON THE WORLD STAGE (c. 2001-2010)",
        "The Festival au Desert at Essakane, near Timbuktu, became a global pilgrimage -- Tuareg camel "
        "races and desert blues under the stars, drawing the likes of Robert Plant and Bono. It "
        "symbolized a peaceful, cosmopolitan Sahel. Content note: jihadist violence forced the festival "
        "into exile and shut down northern Mali's scene from 2012 (the crisis of #4 ahead).",
        [
            ("Festival au Desert (Essakane, near Timbuktu)", None),
            ("Desert blues under the stars (the global pilgrimage)", None),
            ("The Sahel as world-music destination", None),
            ("A peaceful, cosmopolitan Timbuktu (before 2012)", None),
            ("The gathering crisis in northern Mali (roads ahead)", None),
        ],
    ),
]

STEM = "ssa_sahel_music_3_GLOBAL_DESERT_BLUES_WASSOULOU"


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
