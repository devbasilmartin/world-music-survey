#!/usr/bin/env python3
"""Build India / South Asia, installment 3: Folk & Regional Traditions.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/Latin only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Indian & South Asian Music — Installment 3: "
         "Folk & Regional Traditions — the Village India")

FRAMING = (
    "Beneath the classical canopy lies the vast, teeming world of India's FOLK music -- thousands of "
    "living traditions in dozens of languages, the everyday music of harvest and wedding, worship and "
    "work, epic and lament. This is where most Indians actually sing. From the mystic BAULS of Bengal "
    "and the desert MANGANIAR of Rajasthan to Punjab's harvest BHANGRA, Maharashtra's LAVANI, Gujarat's "
    "GARBA, Assam's BIHU, the Tamil south's street theater, and the Adivasi (tribal) drum-and-dance, "
    "folk music is India's true bedrock -- and the endless well that classical, devotional, and film "
    "music all draw from. Cross-links: folk melodies feeding the Bollywood song machine (#5) and the "
    "global rise of bhangra-pop (later/diaspora); the Baul's ecstatic mysticism touching the Sufi world "
    "(#4). Names given as (Traditional) are folk forms, instruments, or living traditions to seed your "
    "listening; canonical figures/songs are named where they exist. Region: all of India's regions "
    "(the wider South Asia -- Pakistan, Bangladesh, etc. -- gets fuller treatment later)."
)

SECTIONS = [
    (
        "BENGAL: BAULS, BOATMEN & TAGORE",
        "Bengal's folk is famously soulful. The wandering BAUL mystics -- ektara in hand, led by the "
        "spirit of the 19th-century saint Lalon -- sing of an inner divine beyond religion; the "
        "boatmen's bhatiali drifts across the rivers; and above them Rabindranath Tagore's RABINDRA "
        "SANGEET and Kazi Nazrul Islam's Nazrul Geeti gave Bengal a vast art-song canon.",
        [
            ("Ekla Cholo Re", "Rabindranath Tagore"),
            ("Amar Sonar Bangla", "Rabindranath Tagore"),
            ("Baul (the wandering mystic minstrels of Bengal)", None),
            ("Lalon Fakir (the great Baul saint, seed)", None),
            ("Bhatiali (the Bengali boatmen's song)", None),
            ("Rabindra Sangeet (Tagore's song tradition)", None),
            ("Nazrul Geeti (Kazi Nazrul Islam's songs)", None),
        ],
    ),
    (
        "RAJASTHAN: THE DESERT MUSICIANS",
        "In the Thar desert, the hereditary Muslim musician castes -- the MANGANIAR and the LANGA -- "
        "have sung for Hindu and Muslim patrons for centuries, on the bowed kamaicha, the clacking "
        "khartal, the double-flute algoza, and the sarangi. Their haunting desert songs are among "
        "India's most beloved folk. Cross-link: the desert-music kinship reaching toward the Sahel and "
        "the Sufi world.",
        [
            ("Manganiar & Langa (the Rajasthani desert musician castes)", None),
            ("Kamaicha & khartal (the Rajasthani folk instruments)", None),
            ("Padharo Mhare Desh (the Rajasthani welcome song)", None),
            ("Kesariya Balam (the classic Rajasthani folk melody)", None),
            ("Nimbooda (Rajasthani folk dance-song)", None),
            ("Algoza & the double-flute drone", None),
        ],
    ),
    (
        "PUNJAB: BHANGRA, DHOL & THE HARVEST",
        "Punjab's folk is pure energy: BHANGRA, the men's harvest dance driven by the booming dhol drum "
        "and the twang of the tumbi, and giddha, the women's answer. The boliyan (couplets) trade wit, "
        "and folk singers like Alam Lohar (whose 'Jugni' became immortal) and Kuldeep Manak carried the "
        "tradition. Cross-link: bhangra's coming global pop explosion.",
        [
            ("Jugni", "Alam Lohar"),
            ("Bhangra (the Punjabi harvest dance)", None),
            ("The dhol drum & the tumbi (bhangra's engine)", None),
            ("Giddha (the women's Punjabi folk dance)", None),
            ("Boliyan (the Punjabi folk couplets)", None),
            ("Kuldeep Manak (the Punjabi kali/folk voice)", None),
        ],
    ),
    (
        "MAHARASHTRA & THE WEST: LAVANI & POWADA",
        "Maharashtra's folk splits into fire and thunder: LAVANI, the sensuous, quicksilver dance-song "
        "driven by the dholki drum and performed by women, and POWADA, the roaring heroic ballads of the "
        "shahir bards recounting Maratha valor. The Koli fisherfolk add their own seaside songs. Content "
        "note: lavani has long fought stigma despite its artistry.",
        [
            ("Lavani (the Maharashtrian dance-song)", None),
            ("Powada (the Marathi heroic ballad)", None),
            ("The dholki drum (lavani's pulse)", None),
            ("Koli songs (the Maharashtrian fisherfolk)", None),
            ("The shahir bard tradition (Maratha ballad-singers)", None),
        ],
    ),
    (
        "GUJARAT & THE NAVRATRI DANCES",
        "Gujarat dances its devotion. During the nine nights of Navratri, whole communities whirl the "
        "GARBA in circles around a lamp and clash sticks in the DANDIYA RAAS, and the dayro storytelling "
        "sessions keep folk wisdom alive. It is participatory folk music at its most joyous.",
        [
            ("Garba (the Gujarati circle dance of Navratri)", None),
            ("Dandiya Raas (the Gujarati stick dance)", None),
            ("Navratri music (the nine nights of dance)", None),
            ("Dayro (Gujarati folk storytelling-song)", None),
            ("Community devotional dance (garba's spirit)", None),
        ],
    ),
    (
        "THE SOUTH: FOLK OF THE TAMIL & DRAVIDIAN LANDS",
        "South India's folk runs parallel to its classical grandeur. Tamil GAANA rises from Chennai's "
        "working-class streets, VILLU PAATU tells epics on a giant musical bow, therukoothu street "
        "theater dramatizes myth, the thundering parai drum marks every rite, and oppari laments grieve "
        "the dead. Karagattam balances pots in dance.",
        [
            ("Gaana (the Tamil working-class street song)", None),
            ("Villu Paatu (the Tamil musical-bow epic song)", None),
            ("Therukoothu (Tamil street theater)", None),
            ("The parai drum (the Tamil folk & ritual drum)", None),
            ("Oppari (the Tamil funeral lament)", None),
            ("Karagattam (the Tamil pot-balancing dance)", None),
        ],
    ),
    (
        "ASSAM & THE NORTHEAST",
        "Assam bursts into song each spring with BIHU -- exuberant dance-music of dhol, pepa (buffalo-"
        "horn pipe), and gogona -- and the wider Northeast holds a world of distinct traditions among "
        "the Naga, Khasi, Mizo, and Manipuri peoples, far from the classical mainstream. Content note: "
        "these cultures are often marginalized in national narratives.",
        [
            ("Bihu (the Assamese spring dance-song)", None),
            ("Pepa & gogona (the Bihu instruments)", None),
            ("Naga folk song (the hill traditions)", None),
            ("Khasi & the Northeast's distinct music", None),
            ("Manipuri song & dance (the eastern hills)", None),
        ],
    ),
    (
        "THE ADIVASI & TRIBAL TRADITIONS",
        "India's Adivasi (indigenous) peoples carry some of its oldest music -- the Santhal's communal "
        "drum-dances, the Gond and Warli rhythms, and the epic PANDAVANI recitation of the Mahabharata "
        "(the great Teejan Bai its star). This is the deep substratum beneath everything. Content note: "
        "Adivasi cultures face displacement and erasure -- kept in view.",
        [
            ("Santhal drum-dance (the Adivasi communal music)", None),
            ("Gond & Warli tribal rhythms", None),
            ("Pandavani (the Chhattisgarhi Mahabharata epic-song)", None),
            ("Teejan Bai (the Pandavani epic singer, seed)", None),
            ("The Adivasi substratum (India's oldest layer)", None),
        ],
    ),
    (
        "FOLK INSTRUMENTS, THEATER & THE ROAD AHEAD",
        "Binding it all is a universe of folk instruments -- the one-string ektara, the dotara, the "
        "bowed ravanahatha, the been, the dholak -- and folk theater like nautanki and jatra that fused "
        "song, dance, and drama for the village. Cross-link: this endless folk reservoir would feed the "
        "Bollywood song machine (#5) and the global bhangra-pop wave.",
        [
            ("Ektara & dotara (the folk drone-lutes)", None),
            ("Ravanahatha & been (bowed & reed folk instruments)", None),
            ("The dholak (the folk hand-drum)", None),
            ("Nautanki & jatra (North & East Indian folk theater)", None),
            ("Folk into film & pop (the reservoir, roads ahead)", None),
        ],
    ),
]

STEM = "south_asia_music_3_FOLK_REGIONAL_TRADITIONS"


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
