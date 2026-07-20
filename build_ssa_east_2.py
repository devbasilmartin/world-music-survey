#!/usr/bin/env python3
"""Build Sub-Saharan Africa: East, installment 2: The Golden Dance-Band Age & the Rise of Benga.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1965-1980.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of East African Music — Installment 2: "
         "The Golden Dance-Band Age & the Rise of Benga (c. 1965-1980)")

FRAMING = (
    "In the first decades of independence, East Africa built its own pop from the roots of Installment "
    "1. In western Kenya, Luo guitarists translated the nyatiti lyre's fast runs onto electric strings "
    "and created BENGA -- a bright, tumbling, bass-driven guitar dance music that became Kenya's "
    "national pop, led by the 'king of benga', D.O. MISIANI, and spread on cheap 45s from the Luo west "
    "to the Kikuyu highlands (Joseph Kamaru). Meanwhile NAIROBI became a pan-African recording capital: "
    "Congolese exiles -- Baba Gaston, Super Mazembe (whose 'Shauri Yako' became THE East African "
    "anthem), Samba Mapangala -- naturalized Congo rumba into a distinct East African SWAHILI RUMBA, "
    "and the soft-grooving Wanyika bands ('Sina Makosa') filled the clubs. Across the border, "
    "Tanzania's UJAMAA-era dance bands -- DDC Mlimani Park, the union-sponsored Juwata Jazz, and the "
    "great Mbaraka Mwinshehe -- made 'muziki wa dansi' a national institution under Nyerere's cultural "
    "policy. Cross-links: Congo rumba/soukous (Central survey), now settled and remade in Nairobi; "
    "Cuban son underlying dansi (Latin survey). Region-integrity note: several Nairobi-based stars were "
    "Congolese emigres who became pillars of East African music -- kept and flagged. Content note: "
    "Mbaraka Mwinshehe's death (1979) is kept. Region: Kenya & Tanzania (with the Congolese diaspora)."
)

SECTIONS = [
    (
        "KENYAN BENGA: THE LUO GUITAR SOUND (c. 1965-1975)",
        "Benga is Kenya's great gift to guitar pop: Luo musicians remapped the nyatiti lyre and orutu "
        "fiddle onto electric guitar and a galloping bass, producing a crisp, cascading dance music. "
        "Daniel Owino 'D.O.' Misiani and his Shirati Jazz were its towering institution, cutting "
        "hundreds of sides of sharp, story-telling Dholuo song. Cross-link: the nyatiti roots of "
        "Installment 1, electrified.",
        [
            ("Pole Musa", "D.O. Misiani & Shirati Jazz"),
            ("Benga (the Luo fast-picked guitar dance)", None),
            ("D.O. Misiani & Shirati Jazz (the king of benga)", None),
            ("Nyatiti runs remapped onto electric guitar", None),
            ("Dholuo storytelling song (benga lyricism)", None),
            ("The galloping benga bassline", None),
        ],
    ),
    (
        "THE BENGA BOOM & THE KENYAN 45 (c. 1970-1980)",
        "Benga became a national industry of cheap seven-inch singles. Gabriel Omolo's 'Lunchtime' -- a "
        "wry hit about a broke office worker -- crossed every ethnic line; Collela Mazee and the "
        "Victoria Kings, George Ramogi, and Ochieng Nelly kept the Luo benga machine roaring. The 45 "
        "rpm single was the beating heart of Kenyan pop.",
        [
            ("Lunchtime", "Gabriel Omolo"),
            ("Collela Mazee & the Victoria Kings (benga heavyweights)", None),
            ("George Ramogi & Continental Kilo Jazz", None),
            ("The Kenyan seven-inch single culture", None),
            ("Ochieng Nelly & the Luo benga bands", None),
            ("Benga crosses ethnic lines (national pop)", None),
        ],
    ),
    (
        "KIKUYU BENGA & VERNACULAR POP (c. 1967-1980)",
        "Benga jumped from the Luo west to the Kikuyu highlands, where Joseph Kamaru became a superstar "
        "and moral voice, and D.K. Daniel Kamau spun sweet Gikuyu love songs. Vernacular pop in Gikuyu, "
        "Kamba, and Luhya turned benga into the shared grammar of Kenyan music -- each community singing "
        "its own stories to the same tumbling beat.",
        [
            ("Joseph Kamaru (Kikuyu benga superstar & moralist)", None),
            ("D.K. Daniel Kamau (sweet Gikuyu benga)", None),
            ("Gikuyu vernacular pop (Mount Kenya sound)", None),
            ("Kamba benga (the Kalambya sound emerging)", None),
            ("Benga as Kenya's shared musical grammar", None),
            ("Vernacular 45s & the up-country market", None),
        ],
    ),
    (
        "NAIROBI, THE PAN-AFRICAN HUB: CONGOLESE EXILES (c. 1970-1980)",
        "Nairobi's studios and clubs drew Congolese musicians fleeing Zaire's collapse, and they made "
        "the city a pan-African capital. Baba Gaston, Super Mazembe -- whose 'Shauri Yako' became the "
        "single most beloved song in East Africa -- and Samba Mapangala's Orchestra Virunga naturalized "
        "Congo rumba on Kenyan soil. Region-integrity note: these stars were Congolese emigres, kept as "
        "pillars of East African music and flagged.",
        [
            ("Shauri Yako", "Orchestra Super Mazembe"),
            ("Baba Gaston (Congolese bandleader in Nairobi, flagged)", None),
            ("Samba Mapangala & Orchestra Virunga (flagged Congolese)", None),
            ("Congo rumba naturalized in Nairobi", None),
            ("Nairobi as a pan-African recording capital", None),
            ("Zairean exiles & the East African club scene", None),
        ],
    ),
    (
        "SWAHILI RUMBA & THE WANYIKA BANDS (c. 1975-1980)",
        "Out of the Congo-in-Nairobi ferment grew a distinct SWAHILI RUMBA -- gentler and more melodic "
        "than the Kinshasa original, sung in Swahili with a soft, rolling guitar. The Wanyika family of "
        "bands led it: Les Wanyika's 'Sina Makosa' became a timeless standard, with Simba Wanyika and "
        "Orchestra Makassy close behind.",
        [
            ("Sina Makosa", "Les Wanyika"),
            ("Swahili rumba (the gentle East African rumba)", None),
            ("Simba Wanyika (the Wanyika family bands)", None),
            ("Orchestra Makassy (Swahili rumba in Nairobi/Dar)", None),
            ("The soft rolling Swahili guitar", None),
            ("Swahili lyric rumba (love & everyday life)", None),
        ],
    ),
    (
        "TANZANIA'S UJAMAA DANCE BANDS (c. 1965-1980)",
        "In Nyerere's socialist Tanzania, 'muziki wa dansi' became a national institution -- big brass-"
        "and-guitar dance orchestras, often sponsored by unions, parastatals, or the party. DDC Mlimani "
        "Park Orchestra, the union band Juwata (heir to NUTA), Orchestra Safari Sound, and Vijana Jazz "
        "filled Dar es Salaam's halls with a stately, singalong Swahili dance music.",
        [
            ("Muziki wa dansi golden age (Tanzania's dance orchestras)", None),
            ("DDC Mlimani Park Orchestra (the Dar es Salaam giant)", None),
            ("Juwata Jazz Band (the union band, heir to NUTA)", None),
            ("Orchestra Safari Sound (Dar dance-band rivalry)", None),
            ("Vijana Jazz Band (the youth-league orchestra)", None),
            ("Ujamaa & the parastatal dance bands (Nyerere's policy)", None),
        ],
    ),
    (
        "MBARAKA MWINSHEHE & THE TANZANIAN STAR (c. 1968-1979)",
        "Mbaraka Mwinshehe was Tanzania's greatest dance-band star -- a gifted guitarist and songwriter "
        "with Morogoro Jazz and then his own Orchestra Super Volcano, whose 'Shida' and hundreds of "
        "other songs defined the era. Content note: he died in a car crash in 1979 at the height of his "
        "fame; his records remained beloved for decades.",
        [
            ("Shida", "Mbaraka Mwinshehe"),
            ("Mbaraka Mwinshehe (Tanzania's dance-band king)", None),
            ("Orchestra Super Volcano (Mbaraka's band)", None),
            ("Morogoro Jazz in the 1970s", None),
            ("Swahili social-comment dansi (Mbaraka's lyrics)", None),
        ],
    ),
    (
        "THE SOUND SPREADS & THE ROADS AHEAD (c. 1975-1980)",
        "By 1980 East Africa had a pop of its own: benga's guitar rippled out across the continent "
        "(reaching as far as the Congo and beyond), Swahili rumba was the region's lingua franca of "
        "love songs, and the dance bands were national treasures. Cross-links: benga's influence "
        "outward; the modern era (hip-hop, bongo flava, genge) still to come.",
        [
            ("Benga's continental influence (the guitar ripples out)", None),
            ("East African radio & the pan-regional hit", None),
            ("Swahili as the language of East African pop", None),
            ("From dance bands to the cassette era (roads ahead)", None),
            ("The regional star system (Kenya-Tanzania crossover)", None),
        ],
    ),
]

STEM = "ssa_east_music_2_BENGA_DANCE_BAND_GOLDEN_AGE"


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
