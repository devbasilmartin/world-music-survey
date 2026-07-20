#!/usr/bin/env python3
"""Build Sub-Saharan Africa: East, installment 1: East African Roots (Taarab, Guitar & Dansi).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1900-1970.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of East African Music — Installment 1: "
         "Roots — Taarab, the Guitar & the Birth of Dansi (c. 1900-1970)")

FRAMING = (
    "East Africa's music grows where three worlds meet: the SWAHILI COAST (Zanzibar, Mombasa, Dar es "
    "Salaam), where Arab, Persian, and Indian currents crossed with Bantu Africa; the interior of "
    "Kenya, Tanzania, and Uganda with its deep traditions of the nyatiti lyre, ngoma drumming, and "
    "sung praise; and the modern port cities where guitars, gramophones, and radio arrived. From the "
    "coast came TAARAB -- sung Swahili poetry over an orchestra of oud, violin, qanun, and accordion -- "
    "and its first great star, SITI BINTI SAAD, the first East African to make commercial records "
    "(cut in Bombay in the late 1920s). In the towns, a bright acoustic GUITAR pop was born (Fundi "
    "Konde, Fadhili William's immortal 'Malaika'), fed by the Katanga fingerstyle of Jean Bosco Mwenda "
    "and, crucially, by Congolese rumba pouring in over the radio and via emigre bands (the direct "
    "cross-link to the Central Africa survey). In Tanzania, Cuban and Congolese grooves fused into "
    "DANSI -- 'muziki wa dansi', the Swahili jazz of Salum Abdallah and the great jazz bands. This "
    "installment lays the roots; benga, Swahili rumba, and the golden dance-band age follow. Cross-"
    "links: Congo rumba/soukous (Central survey) seeding the guitar and the bands; Cuban son (Latin "
    "survey) reaching Dar es Salaam. Region: Kenya, Tanzania (with Zanzibar) & the wider East African "
    "coast and lakes; Congolese and Cuban inputs flagged."
)

SECTIONS = [
    (
        "THE SWAHILI COAST: TAARAB IS BORN (Zanzibar & Mombasa, c. 1900-1945)",
        "On the Swahili coast, a cosmopolitan sung poetry crystallized into TAARAB -- Swahili verse set "
        "to an orchestra of oud, violin, qanun, nay, and later accordion, steeped in Egyptian and "
        "Arab-Andalusian models. Zanzibar's Ikhwani Safaa Musical Club (founded 1905) became its "
        "institution. Taarab is at once entertainment, courtly art, and coded social commentary.",
        [
            ("Taarab (the Swahili sung-poetry orchestra)", None),
            ("Ikhwani Safaa Musical Club (Zanzibar, founded 1905)", None),
            ("Egyptian & Arab-Andalusian roots of taarab", None),
            ("The taarab orchestra (oud, violin, qanun, accordion)", None),
            ("Swahili poetry in song (utenzi & shairi sung)", None),
            ("Zanzibar as the taarab capital", None),
        ],
    ),
    (
        "SITI BINTI SAAD & THE VOICE OF TAARAB (c. 1928-1950)",
        "Siti binti Saad -- a potter's daughter who sang in Swahili rather than courtly Arabic -- became "
        "the mother of taarab and the first East African to record commercially (her 78s were cut in "
        "Bombay from 1928). Singing for and about ordinary people, her songs (like 'Kijiti', on a "
        "notorious murder trial) made taarab a popular art and a woman's voice a public power.",
        [
            ("Kijiti", "Siti binti Saad"),
            ("Siti binti Saad (mother of taarab, first East African to record)", None),
            ("Taarab in Swahili (song for the common people)", None),
            ("The Bombay 78s (East Africa's first recordings)", None),
            ("Women's voice & social commentary in taarab", None),
        ],
    ),
    (
        "TRADITIONAL ROOTS: THE NYATITI, NGOMA & THE LAKES",
        "Beneath the coastal cosmopolitanism lie deep interior traditions. Among the Luo of western "
        "Kenya, the eight-string NYATITI lyre accompanies sung praise and lament -- a direct ancestor "
        "of the guitar styles to come. Across the region, NGOMA (drum-and-dance) marks every ritual, "
        "and the Kamba, Kikuyu, Luhya, and interlacustrine peoples each carry distinct song traditions.",
        [
            ("Nyatiti (the Luo eight-string lyre)", None),
            ("Ngoma (East African drum-and-dance)", None),
            ("Luo sung praise & lament (nyatiti tradition)", None),
            ("Litungu & the Luhya lyre", None),
            ("Kikuyu & Kamba song traditions", None),
            ("Orutu (the Luo one-string fiddle)", None),
        ],
    ),
    (
        "THE KENYAN GUITAR & THE BIRTH OF POP SONG (c. 1945-1962)",
        "In Nairobi and Mombasa a bright acoustic-guitar pop emerged after the war -- lilting, "
        "close-harmony, and sung in Swahili. Fundi Konde, a pioneer, cut some of the first Kenyan pop "
        "hits; and Fadhili William's 'Malaika' became the most famous song in all of East Africa (its "
        "authorship still debated -- noted). This 'dry' guitar style is the seed of Kenyan pop.",
        [
            ("Malaika", "Fadhili William"),
            ("Fundi Konde (pioneer of Kenyan guitar pop)", None),
            ("The dry acoustic guitar (early Nairobi pop)", None),
            ("Swahili close-harmony song (the Jambo Boys era)", None),
            ("Malaika & the disputed-authorship question", None),
            ("Mombasa & Nairobi as recording towns", None),
        ],
    ),
    (
        "JEAN BOSCO MWENDA & THE KATANGA GUITAR (cross-link, c. 1952)",
        "The single most influential guitar sound in the region came from just over the border: the "
        "Katanga fingerstyle of Jean Bosco Mwenda, whose 1952 'Masanga' -- recorded by Hugh Tracey -- "
        "was studied by guitarists across the continent. Region-integrity note: Mwenda was "
        "Congolese/Katangan, but his style is foundational to East African guitar; kept and flagged. "
        "Cross-link: the Central Africa survey's guitar tide.",
        [
            ("Masanga", "Jean Bosco Mwenda"),
            ("Jean Bosco Mwenda (the Katanga fingerstyle, flagged Congolese)", None),
            ("Katanga two-finger guitar picking", None),
            ("Hugh Tracey's field recordings (East & Central Africa)", None),
            ("The guitar crosses the Congo-Kenya border (cross-link)", None),
        ],
    ),
    (
        "TWIST, RUMBA & THE 1960s KENYAN HITMAKERS (c. 1960-1970)",
        "Independence-era Nairobi buzzed with electric bands and imported dance crazes. Daudi Kabaka, "
        "'the king of the twist', scored a hit so catchy ('Helule Helule') that a British band covered "
        "it; the Equator Sound Band and producers like Charles Worrod built a studio scene; and the Luo "
        "guitarists began bending the nyatiti's runs onto electric strings -- the first stirrings of "
        "benga (to come).",
        [
            ("Helule Helule", "Daudi Kabaka"),
            ("Daudi Kabaka (the king of the Kenyan twist)", None),
            ("Equator Sound Band (1960s Nairobi hitmakers)", None),
            ("The twist & rumba craze in Nairobi", None),
            ("Early benga stirrings (nyatiti runs onto guitar)", None),
            ("John Mwale & the Kenyan guitar-pop 45s", None),
        ],
    ),
    (
        "TANZANIAN DANSI: SWAHILI JAZZ & THE CUBAN-CONGO GROOVE (c. 1950-1970)",
        "In Tanganyika/Tanzania, town bands built 'muziki wa dansi' -- Swahili dance music fusing Cuban "
        "son (from imported 'GV' records) with Congolese rumba and local melody. Salum Abdallah's Cuban "
        "Marimba Band led the way from Morogoro, and NUTA, Morogoro, and Western Jazz filled the halls. "
        "Under Nyerere's ujamaa the bands would become national institutions (installment to come).",
        [
            ("Salum Abdallah & Cuban Marimba Band (Morogoro dansi pioneers)", None),
            ("Muziki wa dansi (Tanzanian Swahili dance music)", None),
            ("Cuban son in Dar es Salaam (the GV records)", None),
            ("NUTA Jazz Band (the union band)", None),
            ("Morogoro Jazz & Western Jazz Band", None),
            ("Dansi's Congo-Cuban fusion (the East African blend)", None),
        ],
    ),
    (
        "CONGO RUMBA ARRIVES & THE ROADS AHEAD (c. 1955-1970)",
        "The decisive outside force was Congolese rumba: emigre musicians settled in Nairobi and Dar es "
        "Salaam and the radio poured soukous across the region, giving East African pop its guitars, "
        "its sebene, and its Lingala-tinged glamour. This is the seedbed of Swahili rumba and benga. "
        "Cross-link: the Central Africa survey (Congolese emigres spreading the sound eastward).",
        [
            ("Congolese rumba reaches Nairobi & Dar (emigre bands)", None),
            ("Radio spreads soukous across East Africa", None),
            ("The seedbed of Swahili rumba & benga", None),
            ("Lingala glamour in East African pop (cross-link)", None),
            ("From roots to the golden dance-band age (roads ahead)", None),
        ],
    ),
]

STEM = "ssa_east_music_1_ROOTS_TAARAB_GUITAR_DANSI"


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
