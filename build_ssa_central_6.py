#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Central, installment 6: Angola, Cameroon & the Wider Central Africa.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1955-2000.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of Central African Music — Installment 6: "
         "Angola, Cameroon & the Wider Central Africa (c. 1955-2000)")

FRAMING = (
    "The Congo river basin was never the whole story. This installment steps outside the Congolese "
    "rumba/soukous engine to the region's other great music cultures. In ANGOLA, the Luanda social "
    "dance SEMBA -- a cousin of the rhythm that helped seed Brazilian samba -- turned political under "
    "Portuguese rule and then, in exile, gave the world Bonga's aching 'Mona Ki Ngi Xica'; after a "
    "brutal independence war and civil war, Angolans fused semba with Antillean zouk to invent "
    "KIZOMBA, now a global slow-dance. In CAMEROON, the Douala coast produced MAKOSSA -- catapulted "
    "worldwide by Manu Dibango's 1972 'Soul Makossa' and polished in 1980s Paris into a pan-African "
    "pop -- while the forest peoples around Yaounde electrified their fast 6/8 BIKUTSI into a wild "
    "guitar music. GABON added Pierre-Claver Akendengue's poetry and Oliver N'Goma's silky 'Bane'. "
    "Cross-links: semba <-> Brazilian samba (Latin survey); zouk -> kizomba (Caribbean survey to "
    "come); 'Soul Makossa' into global funk/disco. Content notes: Portuguese colonial war and Angola's "
    "civil war are kept with context. Region: Angola, Cameroon, Gabon & the wider Central Africa "
    "(Congo-Brazzaville and CAR edges), distinct from the DR Congo/Zaire thread of Installments 1-5."
)

SECTIONS = [
    (
        "ANGOLAN SEMBA: THE LUANDA ROOTS (c. 1955-1974)",
        "Semba is the buoyant social dance-music of Luanda's musseques (shanty neighborhoods) -- a "
        "belly-bounce rhythm older than, and an ancestor of, Brazilian samba. Under Portuguese "
        "colonial rule, Liceu Vieira Dias's group Ngola Ritmos made semba a vehicle of national "
        "identity and quiet defiance. Cross-link: the Angola-to-Brazil rhythmic thread of the Latin "
        "survey, seen from the African side.",
        [
            ("Semba (the Luanda social dance)", None),
            ("Ngola Ritmos (Liceu Vieira Dias, semba pioneers)", None),
            ("Liceu Vieira Dias (father of modern Angolan music)", None),
            ("Semba and the roots of samba (Angola-Brazil cross-link)", None),
            ("Massemba rhythm (the belly-bounce dance)", None),
            ("Carnival semba of the Luanda musseques", None),
        ],
    ),
    (
        "BONGA & THE VOICE OF EXILE (c. 1972)",
        "Bonga Kuenda -- a former national-champion athlete turned political exile -- recorded the "
        "landmark album Angola 72 in the Netherlands, his gravelly voice riding the scrape of the "
        "dikanza. 'Mona Ki Ngi Xica' ('the child I left behind') became an anthem of longing and "
        "anti-colonial resistance, sung across the Lusophone world. He is Angola's defining voice.",
        [
            ("Mona Ki Ngi Xica", "Bonga"),
            ("Balumukeno", "Bonga"),
            ("Muadiakime", "Bonga"),
            ("Bonga (the exile voice of Angolan semba)", None),
            ("Angola 72 (the landmark exile album)", None),
            ("Dikanza scraper & the semba groove", None),
        ],
    ),
    (
        "INDEPENDENCE, WAR & THE BIRTH OF KIZOMBA (c. 1975-2000)",
        "Independence came in 1975 and was swallowed almost at once by a long, ruinous civil war; "
        "Waldemar Bastos turned that grief into luminous, orchestral song. Meanwhile, from the 1980s, "
        "Angolan and diaspora musicians married semba to the Antillean ZOUK beat and created KIZOMBA "
        "-- a slow, sensual couple-dance that would sweep Lusophone Africa and Europe. Content note: "
        "the civil war's toll is kept in view. Cross-link: zouk (the Caribbean survey to come).",
        [
            ("Velha Chica", "Waldemar Bastos"),
            ("Waldemar Bastos (Angola's poet of exile)", None),
            ("Kizomba (semba meets zouk, the slow romantic dance)", None),
            ("Eduardo Paim (the father of kizomba)", None),
            ("Zouk into kizomba (the Antillean cross-current)", None),
            ("Angolan civil war & the music of endurance", None),
            ("Ruy Mingas (independence-era Angolan song)", None),
        ],
    ),
    (
        "CAMEROON'S MAKOSSA & MANU DIBANGO (c. 1972)",
        "Makossa is the electric dance music of the Douala coast -- a driving bassline under bright "
        "guitars and horns. Saxophonist Manu Dibango launched it into orbit with 'Soul Makossa' "
        "(1972), a global funk/disco landmark whose chant echoed through decades of pop worldwide "
        "(a much-litigated influence -- noted, not dwelt on). He became Africa's great musical "
        "ambassador.",
        [
            ("Soul Makossa", "Manu Dibango"),
            ("Makossa (the Douala dance groove)", None),
            ("Manu Dibango (saxophone, the makossa ambassador)", None),
            ("Eboa Lotin (early makossa pioneer)", None),
            ("Ekambi Brillant (makossa modernizer)", None),
            ("The makossa bassline & horn punch", None),
        ],
    ),
    (
        "THE MAKOSSA GOLDEN AGE (c. 1980-1995, Douala & Paris)",
        "In the 1980s makossa went slick, romantic, and pan-African, cut in Paris studios and sold "
        "across the continent. Sam Fan Thomas's 'African Typic Collection' was a continental smash; "
        "Moni Bile, the Decca family, and Petit Pays's 'makossa-love' kept the dancefloors full, with "
        "Toto Guillaume's guitar and production defining the era's sheen.",
        [
            ("African Typic Collection", "Sam Fan Thomas"),
            ("Bijou", "Moni Bile"),
            ("Sam Fan Thomas & makassi (the makossa offshoot)", None),
            ("Petit Pays (makossa-love / makossa-choc)", None),
            ("Ben Decca & Grace Decca (makossa royalty)", None),
            ("Toto Guillaume (makossa guitar & production)", None),
            ("Makossa goes pan-African from Paris", None),
        ],
    ),
    (
        "BIKUTSI: THE BEAT OF THE BETI (c. 1960-1995)",
        "Bikutsi is the fast, hard-swinging 6/8 rhythm of the Beti peoples of the forest around "
        "Yaounde -- once women's ritual percussion, later electrified into a wild guitar music. "
        "Anne-Marie Nzie was its grande dame, Messi Martin its guitar pioneer, and Les Tetes Brulees "
        "took its facepaint energy on world tours. Content note: bikutsi's frank sexuality (and "
        "K-Tino's provocations) sparked moral panic -- part of its story.",
        [
            ("Anne-Marie Nzie (the golden voice of Cameroon)", None),
            ("Bikutsi (the fast Beti 6/8 forest rhythm)", None),
            ("Messi Martin (the bikutsi guitar pioneer)", None),
            ("Les Tetes Brulees (facepaint bikutsi on world tour)", None),
            ("K-Tino (the queen of bikutsi)", None),
            ("Bikutsi versus makossa (Cameroon's two poles)", None),
            ("Balafon & women's percussion roots of bikutsi", None),
        ],
    ),
    (
        "GABON, THE WIDER CENTRAL & CROSS-CURRENTS",
        "Beyond Cameroon and Angola, Gabon gave the region Pierre-Claver Akendengue -- a blind "
        "poet-troubadour of huge stature -- and Oliver N'Goma's silky zouk-makossa hit 'Bane'. Around "
        "the edges lie Congo-Brazzaville and the Central African Republic. Cross-link: all these "
        "streams -- makossa, bikutsi, kizomba -- feed forward into modern Afropop.",
        [
            ("Africa Obota", "Pierre-Claver Akendengue"),
            ("Bane", "Oliver N'Goma"),
            ("Pierre-Claver Akendengue (Gabon's poet-troubadour)", None),
            ("Oliver N'Goma (Gabonese zouk-makossa)", None),
            ("Hilarion Nguema (Gabonese guitar & satire)", None),
            ("Central African Republic & the region's edges", None),
            ("Makossa, bikutsi & kizomba into modern Afropop (forward cross-link)", None),
        ],
    ),
]

STEM = "ssa_central_music_6_ANGOLA_CAMEROON_MAKOSSA_BIKUTSI"


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
