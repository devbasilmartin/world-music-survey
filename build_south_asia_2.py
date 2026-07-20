#!/usr/bin/env python3
"""Build India / South Asia, installment 2: The Classical Masters (Hindustani & Carnatic, ~1900-present).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. For art music, name the WORK/raga/performer.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of Indian & South Asian Music — Installment 2: "
         "The Classical Masters (Hindustani & Carnatic, c. 1900-present)")

FRAMING = (
    "The twentieth century turned India's classical music from a courtly art into a public glory. As "
    "the princely patrons faded after independence (1947), the CONCERT HALL, the sabha, All India "
    "Radio, and the LP created a new golden age of virtuoso soloists known by a single name across the "
    "subcontinent. In the north, the sitar of RAVI SHANKAR and Vilayat Khan, the sarod of ALI AKBAR "
    "KHAN, and the khyal voices of BHIMSEN JOSHI and Kishori Amonkar reached new heights, while ALLA "
    "RAKHA and ZAKIR HUSSAIN made the tabla a solo art. In the south, M.S. SUBBULAKSHMI became the "
    "most revered voice in India (singing at the UN in 1966), amid a constellation of Carnatic singers "
    "and instrumentalists centered on the Madras December season. And Ravi Shankar carried the RAGA to "
    "the WORLD -- to Yehudi Menuhin, George Harrison and the Beatles, Woodstock and Monterey -- seeding "
    "a global fascination that still runs through jazz, rock, and minimalism. Cross-links: the raga's "
    "reach into the US/Western surveys (the Beatles, Coltrane, Terry Riley) -- those are Western works, "
    "flagged as influence flowing OUT. Names given as (Traditional) are ragas, forms, or artists as "
    "listening seeds; specific performances/works are named. Region: India (Hindustani north & Carnatic "
    "south)."
)

SECTIONS = [
    (
        "THE CONCERT AGE & THE RECORDING REVOLUTION (c. 1900-1960)",
        "As the princely courts that once patronized musicians dissolved, classical music moved to the "
        "public stage. All India Radio, the 78 and the LP, the great music conferences, and the sabha "
        "halls created a mass audience -- and made touring soloists into national celebrities for "
        "the first time.",
        [
            ("From court patronage to the concert hall (post-1947)", None),
            ("All India Radio & the classical broadcast", None),
            ("The 78 & the LP (recording remakes the raga)", None),
            ("The music conference & the public concert", None),
            ("The rise of the celebrity soloist", None),
        ],
    ),
    (
        "THE HINDUSTANI SITAR & SAROD GIANTS",
        "The plucked-string masters became India's most famous musicians. Ravi Shankar's dazzling, "
        "architectural sitar and Ali Akbar Khan's profound sarod -- both disciples of the legendary guru "
        "Allauddin Khan of Maihar -- defined the era, with Vilayat Khan's singing 'gayaki' sitar and "
        "Nikhil Banerjee's lyricism beside them.",
        [
            ("Raga Jog", "Ravi Shankar"),
            ("Raga Chandranandan", "Ali Akbar Khan"),
            ("Ravi Shankar (the sitar architect, to the world)", None),
            ("Vilayat Khan (the singing gayaki-ang sitar)", None),
            ("Nikhil Banerjee (the lyrical sitar master)", None),
            ("Allauddin Khan & the Maihar gharana (the great guru)", None),
        ],
    ),
    (
        "THE HINDUSTANI VOCAL MASTERS",
        "The human voice remained the summit. Bhimsen Joshi's thundering Kirana-gharana khyal, Kishori "
        "Amonkar's transcendent Jaipur style, and Kumar Gandharva's iconoclasm led the age; Kesarbai "
        "Kerkar's 'Jaat Kahan Ho' was chosen for the Voyager Golden Record, carrying a raga into "
        "interstellar space; and the Dagar family kept the ancient dhrupad alive.",
        [
            ("Jaat Kahan Ho", "Kesarbai Kerkar"),
            ("Bhimsen Joshi (the Kirana-gharana khyal titan)", None),
            ("Kishori Amonkar (the Jaipur-gharana voice)", None),
            ("Kumar Gandharva (the khyal iconoclast)", None),
            ("The Dagar brothers & the dhrupad revival", None),
            ("Mile Sur Mera Tumhara (the national-integration anthem, 1988)", None),
        ],
    ),
    (
        "TABLA & THE ART OF ACCOMPANIMENT",
        "The tabla rose from accompaniment to solo glory. Alla Rakha, Ravi Shankar's dazzling partner, "
        "and his son Zakir Hussain -- perhaps the most famous drummer India ever produced -- turned the "
        "tabla's spoken rhythms into concert showpieces and the jugalbandi (duel-duet) into high drama.",
        [
            ("Alla Rakha (the tabla partner of Ravi Shankar)", None),
            ("Zakir Hussain (the tabla to the world)", None),
            ("The tabla solo (accompaniment becomes art)", None),
            ("Jugalbandi (the duet-duel of two masters)", None),
            ("The spoken rhythm recited (padhant)", None),
        ],
    ),
    (
        "SHEHNAI, FLUTE & SANTOOR ENNOBLED",
        "Instruments once tied to temples, weddings, or folk life were raised to the concert stage. "
        "Bismillah Khan made the reedy shehnai a classical voice (and played at India's independence "
        "dawn in 1947); Hariprasad Chaurasia elevated the bansuri flute; and Shivkumar Sharma brought "
        "the Kashmiri santoor into raga music.",
        [
            ("Bismillah Khan (the shehnai, voice of independence)", None),
            ("Hariprasad Chaurasia (the bansuri flute ennobled)", None),
            ("Shivkumar Sharma (the santoor into raga music)", None),
            ("Folk & temple instruments reach the concert stage", None),
            ("Raga Ahir Bhairav (a Chaurasia dawn favorite, seed)", None),
        ],
    ),
    (
        "THE CARNATIC VOICE: M.S. SUBBULAKSHMI & THE SINGERS",
        "In the south, the voice reigned, and none was more revered than M.S. Subbulakshmi -- her "
        "'Venkatesa Suprabhatam' woke a nation each dawn, her 'Kurai Onrum Illai' became a prayer, and "
        "in 1966 she sang at the United Nations. Around her stood Semmangudi Srinivasa Iyer, the prodigy "
        "M. Balamuralikrishna, and the pioneering women D.K. Pattammal and M.L. Vasanthakumari.",
        [
            ("Kurai Onrum Illai", "M.S. Subbulakshmi"),
            ("Venkatesa Suprabhatam", "M.S. Subbulakshmi"),
            ("Semmangudi Srinivasa Iyer (the pitamaha of Carnatic)", None),
            ("M. Balamuralikrishna (the prodigy composer-singer)", None),
            ("D.K. Pattammal & M.L. Vasanthakumari (the women singers)", None),
            ("The Carnatic kutcheri (the concert format)", None),
        ],
    ),
    (
        "CARNATIC INSTRUMENTALISTS & THE MADRAS SEASON",
        "The south's instrumental art centered on Madras (Chennai) and its December Music Season. The "
        "violin -- adopted and made wholly Indian -- sang through Lalgudi Jayaraman and the prodigy "
        "L. Subramaniam; Palghat Mani Iyer set the standard on the mridangam; and the nadaswaram of "
        "T.N. Rajarathnam Pillai carried temple grandeur to the stage.",
        [
            ("Lalgudi Jayaraman (the lyrical Carnatic violin)", None),
            ("L. Subramaniam (the global Carnatic violinist)", None),
            ("Palghat Mani Iyer (the mridangam master)", None),
            ("T.N. Rajarathnam Pillai (the nadaswaram to the stage)", None),
            ("The Madras December Music Season (the sabha calendar)", None),
            ("The Carnatic violin (adopted & Indianized)", None),
        ],
    ),
    (
        "THE RAGA GOES GLOBAL (c. 1955-1980)",
        "Ravi Shankar opened the raga to the world -- collaborating with violinist Yehudi Menuhin "
        "('West Meets East'), teaching George Harrison, and playing Monterey, Woodstock, and the Concert "
        "for Bangladesh. Zakir Hussain's group Shakti fused Carnatic and jazz. Content/cross-link: the "
        "raga's mark on the Beatles, Coltrane, and minimalism belongs to the US/Western surveys "
        "(influence flowing OUT, flagged).",
        [
            ("West Meets East", "Ravi Shankar & Yehudi Menuhin"),
            ("Ravi Shankar at Monterey & Woodstock (the raga on the world stage)", None),
            ("Ravi Shankar teaches George Harrison (the Beatles' sitar, cross-link)", None),
            ("Shakti (Carnatic-jazz fusion — McLaughlin, Zakir, L. Shankar)", None),
            ("The raga's mark on jazz & minimalism (Coltrane, Riley, flagged Western)", None),
            ("The Concert for Bangladesh (Shankar & Harrison, 1971)", None),
        ],
    ),
]

STEM = "south_asia_music_2_CLASSICAL_MASTERS"


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
