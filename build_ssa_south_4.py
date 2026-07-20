#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Southern, installment 4: Mbaqanga, Isicathamiya & the Soweto Sound.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1960-1979.
Dedup is by TITLE only (norm() drops artist) -- every title string is unique region-wide.
"""

TITLE = ("The Story of Southern African Music — Installment 4: "
         "Mbaqanga, Isicathamiya & the Soweto Sound (c. 1960-1979)")

FRAMING = (
    "With Sophiatown bulldozed and its stars in exile, the music that stayed home turned inward, "
    "electric, and defiantly Black. In the Gallo studios' Mavuthela unit, the MAKGONA TSOHLE BAND "
    "welded sax jive, marabi, and American guitar into MBAQANGA -- a churning, bass-heavy electric "
    "township groove -- and topped it with the earth-shaking bass 'groaner' Simon 'Mahlathini' "
    "Nkabinde and the high-stepping MAHOTELLA QUEENS (the mgqashiyo style). In the migrant hostels, "
    "Zulu men refined ISICATHAMIYA, the tip-toe a cappella competition music that Joseph Shabalala's "
    "LADYSMITH BLACK MAMBAZO would carry to the world (and, via Paul Simon's 1986 Graceland, to a "
    "Grammy -- Installment 6). Zulu MASKANDI, the guitar-troubadour tradition of John Bhengu "
    "(Phuzushukela), grew alongside, and by the 1970s American soul and funk were washing into Soweto "
    "(Harari, the Movers). Content note: this music was made under high apartheid, through an "
    "exploitative studio system that paid Black artists flat fees for enduring hits, and against the "
    "backdrop of the 1976 Soweto uprising -- kept with full context. Cross-links: isicathamiya -> "
    "Graceland; the mbaqanga bass -> the township-pop bottom end; and, as ever, back to West Africa. "
    "Region: all artists are South African."
)

SECTIONS = [
    (
        "THE MAKGONA TSOHLE BAND & THE INVENTION OF MBAQANGA (c. 1964-1975)",
        "At Gallo's Mavuthela unit under producer Rupert Bopape, the Makgona Tsohle Band ('we can do "
        "anything') -- Marks Mankwane's lead guitar, Joseph Makwela's bass, West Nkosi's sax, Lucky "
        "Monama's drums -- invented the electric MBAQANGA groove around 1964, and cut hundreds of "
        "instrumental sax-jive sides. Content note: this hit factory paid its geniuses flat session "
        "fees while the label kept the royalties.",
        [
            ("Makgona Tsohle Band electric mbaqanga instrumentals", None),
            ("Mavuthela sax-jive groove (Gallo studio)", None),
            ("Marks Mankwane lead-guitar mbaqanga", None),
            ("Joseph Makwela and the mbaqanga bass bottom", None),
            ("Bump jive (electric township instrumental)", None),
            ("West Nkosi sax-jive instrumental", None),
        ],
    ),
    (
        "MAHLATHINI & THE MAHOTELLA QUEENS: MGQASHIYO (c. 1964-1975)",
        "Over that groove came the definitive mbaqanga vocal sound: the Mahotella Queens' bright, "
        "high-kicking female harmony (the mgqashiyo dance) answered by Mahlathini, the 'Lion of "
        "Soweto', whose subterranean growl is one of the great voices in African music. Their Gallo "
        "sides were township anthems for a decade.",
        [
            ("Kazet", "Mahotella Queens"),
            ("Umculo Kawupheli", "Mahotella Queens"),
            ("Sithunywa Yinkosi", "Mahotella Queens"),
            ("Izibani Zomgqashiyo", "Mahotella Queens"),
            ("Marabastad", "Mahotella Queens"),
            ("Mahlathini the groaner (mgqashiyo lead)", None),
            ("Mgqashiyo (the hard mbaqanga dance)", None),
        ],
    ),
    (
        "ISICATHAMIYA & LADYSMITH BLACK MAMBAZO (c. 1964-1979)",
        "In the Saturday-night hostel competitions, Zulu migrant workers perfected ISICATHAMIYA -- "
        "soft, tightly-choreographed a cappella harmony (the name evokes 'stalking on tip-toe', "
        "singing quietly so as not to wake the hostel guards). Joseph Shabalala's Ladysmith Black "
        "Mambazo won so consistently they were barred from competing and turned professional; their "
        "1973 'Amabutho' was the first SA gold album by a Black group. Cross-link: Paul Simon's 1986 "
        "Graceland (Installment 6) makes them global.",
        [
            ("Nomathemba", "Ladysmith Black Mambazo"),
            ("Amabutho", "Ladysmith Black Mambazo"),
            ("Nansi Imali", "Ladysmith Black Mambazo"),
            ("Isitimela", "Ladysmith Black Mambazo"),
            ("Isicathamiya Saturday-night competition (Zulu a cappella)", None),
            ("Cothoza mfana (tip-toe hostel harmony)", None),
        ],
    ),
    (
        "ZULU MASKANDI: THE GUITAR TROUBADOUR (c. 1960-1979)",
        "MASKANDI is the Zulu migrant's own guitar music -- a fast picked style (ukupika), a spoken "
        "praise-shout (izibongo), and lyrics of rural longing and social comment. John Bhengu, known "
        "as Phuzushukela, is its founding father, electrifying the tradition and setting the template "
        "for the maskandi stars to come. Cross-link: the picking descends from the migrant string "
        "music of Installment 2.",
        [
            ("Phuzushukela (John Bhengu, father of maskandi)", None),
            ("Maskandi guitar and concertina (electric Zulu era)", None),
            ("Ukupika (maskandi fast-picking style)", None),
            ("Izibongo praise-shout in maskandi", None),
            ("Concertina maskandi (Zulu migrant song, 1970s)", None),
        ],
    ),
    (
        "THE MBAQANGA GALAXY: THE SIMANJEMANJE VOCAL GROUPS (c. 1968-1979)",
        "The studios spun off dozens of 'manje manje' (now-now) vocal-mbaqanga groups, a whole galaxy "
        "of township pop churned out at speed. Izintombi Zesi Manje Manje, Amaswazi Emvelo, and "
        "Abafana Baseqhudeni were among the biggest -- cheap, joyous, and everywhere.",
        [
            ("Izintombi Zesi Manje Manje (female mbaqanga group)", None),
            ("Amaswazi Emvelo (mbaqanga group)", None),
            ("Abafana Baseqhudeni (mbaqanga group)", None),
            ("Simanjemanje (electric vocal mbaqanga)", None),
            ("Umbaqanga (the homemade township pop)", None),
        ],
    ),
    (
        "SOUL, HARARI & THE SOWETO 1970s (c. 1970-1979)",
        "American soul and funk poured into 1970s Soweto. The Beaters became Harari, pioneering a "
        "Black South African Afro-rock; the Movers played a slick mbaqanga-soul; and spiritual "
        "jazz-funk groups like Batsumi searched for something deeper. This soul crossover is the bridge "
        "to the bubblegum pop of Installment 6. Content note: all of it played out against the 1976 "
        "Soweto student uprising and its brutal suppression.",
        [
            ("Party", "Harari"),
            ("Harari Afro-rock (the Beaters, Soweto)", None),
            ("The Movers (Soweto mbaqanga-soul)", None),
            ("Soweto soul (American R&B meets township)", None),
            ("Batsumi (spiritual township jazz-funk)", None),
            ("Soweto 1976 and the music of the uprising", None),
        ],
    ),
]

STEM = "ssa_south_music_4_MBAQANGA_ISICATHAMIYA"


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
