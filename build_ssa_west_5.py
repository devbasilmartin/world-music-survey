#!/usr/bin/env python3
"""Build Sub-Saharan Africa: West, installment 5: Afrobeat & Afro-Funk (c. 1968-1980).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file.
"""

TITLE = ("The Story of West African Music — Installment 5: "
         "Afrobeat & Afro-Funk (c. 1968-1980)")

FRAMING = (
    "This is the moment West African music turns militant -- and changes global pop forever. Fela "
    "Anikulapo Kuti, a Nigerian bandleader who had studied in London and been radicalized by the Black "
    "Power movement in Los Angeles, fused Yoruba rhythm and highlife horns with James Brown's funk and "
    "jazz to invent AFROBEAT: half-hour grooves of interlocking guitars and drums, topped with "
    "scalding pidgin-English political satire. With the drummer Tony Allen as his engine and his "
    "Kalakuta Republic commune as his base, Fela became the Nigerian junta's most dangerous critic -- "
    "and paid for it, most horrifically in the 1977 army raid that led to his mother's death. Around "
    "him a whole AFRO-FUNK and AFRO-ROCK underground caught fire: the soul-invasion precursors Geraldo "
    "Pino and Orlando Julius, the Nigerian funk-rock-psych of BLO, Ofege, and the synth prophet "
    "William Onyeabor, and a Ghanaian Afro-funk led by Ebo Taylor and the world-conquering Osibisa. "
    "Cross-links run straight to the US survey (James Brown's funk in, Afrobeat's DNA out into hip-hop "
    "sampling and the global 'Afrobeat revival') and onward to Latin percussion. Content note: Fela's "
    "story is one of state violence, kept with its full weight. Region: named artists are Nigerian, "
    "Sierra Leonean, or Ghanaian; scope calls flagged."
)

SECTIONS = [
    (
        "THE INVENTION OF AFROBEAT: FELA & AFRICA 70 (c. 1969-1977)",
        "Returning from London and a life-changing 1969 stay in the US, Fela renamed his band Africa 70 "
        "and forged Afrobeat: long, hypnotic, horn-and-organ grooves built for trance and for protest. "
        "These late-1960s-to-mid-70s sides are the genre's foundation. Cross-link: the funk is James "
        "Brown's (US survey), rebuilt on a Yoruba clave.",
        [
            ("Water No Get Enemy", "Fela Kuti"),
            ("Gentleman", "Fela Kuti"),
            ("Lady", "Fela Kuti"),
            ("Shakara", "Fela Kuti"),
            ("Jeun Ko Ku (Chop and Quench)", "Fela Kuti"),
            ("Roforofo Fight", "Fela Kuti"),
            ("Expensive Shit", "Fela Kuti"),
            ("Confusion", "Fela Kuti"),
        ],
    ),
    (
        "TONY ALLEN: THE ENGINE ROOM (c. 1970-1980)",
        "Fela said it himself: 'Without Tony Allen, there would be no Afrobeat.' Allen's four-limbed "
        "drumming -- a fusion of highlife, jazz, and funk that sounded like several drummers at once -- "
        "was the rhythmic invention at the music's core, and his own Africa-70-era solo albums are "
        "essential. Cross-link: Allen's beat later underpins Damon Albarn's projects and modern "
        "producers worldwide.",
        [
            ("No Accommodation for Lagos", "Tony Allen"),
            ("Progress", "Tony Allen"),
            ("Afro Disco Beat", "Tony Allen"),
            ("Jealousy", "Tony Allen"),
        ],
    ),
    (
        "FELA THE PROPHET: KALAKUTA & THE MUSIC OF DEFIANCE (c. 1976-1980)",
        "As Fela declared his compound the independent 'Kalakuta Republic' and named his band Egypt 80, "
        "his music became pure confrontation with military power. Content note: in February 1977 a "
        "thousand soldiers burned Kalakuta to the ground and threw his mother, the activist Funmilayo "
        "Ransome-Kuti, from a window; she died of her injuries. 'Coffin for Head of State' and 'Unknown "
        "Soldier' are his answer -- grief and rage as art.",
        [
            ("Zombie", "Fela Kuti"),
            ("Sorrow Tears and Blood", "Fela Kuti"),
            ("Coffin for Head of State", "Fela Kuti"),
            ("Unknown Soldier", "Fela Kuti"),
            ("Colonial Mentality", "Fela Kuti"),
            ("Trouble Sleep Yanga Wake Am", "Fela Kuti"),
        ],
    ),
    (
        "THE PRECURSORS: THE SOUL INVASION (c. 1966-1974)",
        "Afrobeat did not appear from nowhere. In the late 1960s the Sierra Leonean bandleader Geraldo "
        "Pino stormed Nigeria with a note-perfect James Brown soul revue that lit the fuse under Fela, "
        "and Orlando Julius was already fusing Yoruba highlife with American soul into 'Afro-soul'. "
        "Cross-link: this is the US soul/funk of the US survey landing in Lagos and being rebuilt.",
        [
            ("Heavy Heavy Heavy", "Geraldo Pino"),
            ("Geraldo Pino & the Heartbeats (the 'James Brown of West Africa')", None),
            ("Jagua Nana", "Orlando Julius"),
            ("Super Afro Soul", "Orlando Julius"),
            ("Ijo Soul", "Orlando Julius"),
        ],
    ),
    (
        "NIGERIAN FUNK, ROCK & PSYCH (c. 1971-1979)",
        "Beyond Fela, oil-boom Nigeria threw off an astonishing funk-rock-psychedelic underground -- "
        "much of it rediscovered decades later by crate-diggers. BLO and the teenage Ofege made heavy "
        "Afro-rock; Monomono and The Funkees brought Igbo funk; and the businessman-mystic William "
        "Onyeabor built eerie synthesizer-funk that the 21st century would rapturously reissue.",
        [
            ("Chant to Mother Earth", "BLO"),
            ("Try and Love", "Ofege"),
            ("It's Not Easy", "Ofege"),
            ("Atomic Bomb", "William Onyeabor"),
            ("Fantastic Man", "William Onyeabor"),
            ("Give the Beggar a Chance", "Monomono"),
            ("Akula Owu Onyeara", "The Funkees"),
        ],
    ),
    (
        "GHANAIAN AFRO-FUNK & AFRO-ROCK (c. 1971-1980)",
        "Ghana caught the same fire. Ebo Taylor married highlife to funk and jazz; Hedzoleh Soundz "
        "backed Hugh Masekela; Alhaji K. Frimpong cut the smash 'Kyenkyen Bi Adi M'awu'; and Osibisa "
        "became the first African band to reach the global rock mainstream. (Scope note: Osibisa was "
        "formed in London by Ghanaian founders -- Teddy Osei, Sol Amarfio, Mac Tontoh -- with Caribbean "
        "members; kept as Ghanaian-led Afro-rock, and flagged.)",
        [
            ("Love and Death", "Ebo Taylor"),
            ("Heaven", "Ebo Taylor"),
            ("Rekpete", "Hedzoleh Soundz"),
            ("Kyenkyen Bi Adi M'awu", "Alhaji K. Frimpong"),
            ("Sunshine Day", "Osibisa"),
            ("Woyaya", "Osibisa"),
        ],
    ),
]

STEM = "ssa_west_music_5_AFROBEAT_AFROFUNK"


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
