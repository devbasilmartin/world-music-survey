#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Southern, installment 2: Marabi, Early Recording & Mission Choralism.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1900-1948.
"""

TITLE = ("The Story of Southern African Music — Installment 2: "
         "Marabi, Early Recording & Mission Choralism (c. 1900-1948)")

FRAMING = (
    "As the mines pull hundreds of thousands of workers into Johannesburg and Kimberley, the "
    "deep-traditional layer of Installment 1 collides with the pedal organ, the guitar, the concertina, "
    "and imported American 78s -- and Black urban South Africa invents its first modern popular music. "
    "In the illegal-liquor slumyards, MARABI is born: a hypnotic, endlessly-cycling I-IV-V keyboard "
    "dance music, the exact cousin of American ragtime and blues, and the seedbed of South African "
    "jazz. In the mission schools, Reuben Caluza and John Knox Bokwe forge a modern Black CHORAL music "
    "(makwaya) that carries political weight -- Caluza's songs protest the 1913 Land Act. In the mine "
    "hostels, Zulu men perfect the a cappella competition style that becomes isicathamiya, and in 1939 "
    "Solomon Linda records 'Mbube' -- a song later stolen into 'Wimoweh' and 'The Lion Sleeps "
    "Tonight', earning millions for others while Linda died poor. Cross-links run straight to the US "
    "survey (marabi <-> ragtime/jazz; Mbube -> The Weavers and Disney's Lion King) and to West Africa "
    "(the same colonial guitar-and-record economy). Content note: this is music of segregation, the "
    "compound, and one of pop history's great injustices -- kept with full context. Many pre-1948 "
    "forms survive only as living tradition or scarce 78s, so descriptor/'(Traditional)' bare titles "
    "sit beside the handful of named landmarks. Region: all artists are Southern African."
)

SECTIONS = [
    (
        "MARABI: THE SHEBEEN KEYBOARD & THE ENDLESS CYCLE (c. 1920-1945)",
        "Marabi was the sound of the slumyard shebeen: a pedal organ or piano (later with pennywhistle "
        "and banjo) grinding a three-chord cycle for hours while dancers drank illegal skokiaan. "
        "Disreputable, working-class, and deeply African-American in feel, it fused Khoisan and Sotho "
        "melody with ragtime and blues. Cross-link: this is South Africa's ragtime -- the same I-IV-V "
        "engine driving the US survey's early jazz.",
        [
            ("Marabi (shebeen pedal-organ dance music)", None),
            ("Marabi piano cycle (I-IV-V, Doornfontein slumyards)", None),
            ("Ndunduma (early marabi-jazz)", None),
            ("Tickey-draai / vastrap (highveld & Cape dance)", None),
            ("Famo (Sotho shebeen accordion dance)", None),
            ("Marabi shebeen party (Johannesburg 1930s)", None),
        ],
    ),
    (
        "SOLOMON LINDA & 'MBUBE' (1939)",
        "In 1939 the Zulu migrant worker Solomon Linda and his Evening Birds recorded 'Mbube' ('lion'), "
        "improvising the soaring falsetto line that would circle the globe. Content note: sold outright "
        "for a pittance, the melody became Pete Seeger/The Weavers' 'Wimoweh' and then 'The Lion Sleeps "
        "Tonight' -- earning millions while Linda died in poverty in 1962; his heirs only won a "
        "settlement in 2006. The song also names a whole genre: MBUBE, the mine-hostel a cappella style.",
        [
            ("Mbube", "Solomon Linda's Original Evening Birds"),
            ("Zulu a cappella mine-hostel singing (cothoza mfana)", None),
            ("Evening Birds & the roots of isicathamiya", None),
        ],
    ),
    (
        "REUBEN CALUZA & THE MISSION-MODERN CHORAL SONG (c. 1910-1940)",
        "In the mission schools a modern Black choral art arose. Reuben Caluza fused Zulu melody with "
        "four-part hymnody and ragtime step, and recorded in London in 1930; his 'iLand Act' protests "
        "the 1913 Natives Land Act that dispossessed Black South Africans. John Knox Bokwe's Xhosa hymns "
        "and the Ohlange choir tradition (John Dube's school) made makwaya a vehicle of dignity and, "
        "quietly, of politics.",
        [
            ("iLand Act (uMteto we Land Act)", "Reuben Caluza"),
            ("Silusapho Lwase Afrika", "Reuben Caluza"),
            ("Plea for Africa", "John Knox Bokwe"),
            ("Zulu makwaya choral songs (ragtime-inflected)", None),
            ("Ohlange choir tradition (John Dube's school)", None),
            ("Amakwaya competition (mission schools)", None),
        ],
    ),
    (
        "MASKANDI, MIGRANT STRING & CONCERTINA MUSIC (c. 1930-1948)",
        "The migrant troubadour picked up the guitar and concertina and adapted the bow-and-voice "
        "tradition to strings, birthing Zulu MASKANDI and its cousins. The Zimbabwean George Sibanda's "
        "'Guabi Guabi' became one of Africa's most influential guitar records; Basotho famo accordion "
        "and tin-guitar songs filled the mine hostels. (Scope note: Sibanda's key sides are c. 1950, "
        "just past this window, but belong to this migrant-guitar story -- flagged.)",
        [
            ("Guabi Guabi", "George Sibanda"),
            ("Zulu maskandi guitar (migrant troubadour roots)", None),
            ("Basotho famo accordion (early recordings)", None),
            ("Concertina & tin-guitar migrant song", None),
            ("Josaya Hadebe / early Zulu solo guitar", None),
        ],
    ),
    (
        "THE MARABI-TO-JAZZ BRIDGE: THE DANCE BANDS (c. 1935-1948)",
        "American swing 78s met marabi to create 'African jazz'. The Jazz Maniacs of Solomon 'Zuluboy' "
        "Cele took marabi uptown; the Merry Blackbirds of Peter Rezant were the elegant society "
        "orchestra of the Black elite; and the tsaba-tsaba dance craze swept the late 1940s. This band "
        "culture becomes the kwela and mbaqanga of the next installments. Cross-link: the swing is the "
        "US survey's, re-Africanized.",
        [
            ("Jazz Maniacs (Zuluboy Cele, marabi-swing)", None),
            ("Merry Blackbirds (Peter Rezant society jazz)", None),
            ("Tsaba-tsaba (late-1940s dance craze)", None),
            ("African Swingsters (marabi big-band)", None),
            ("Johannesburg marabi-jazz orchestra (1940s)", None),
        ],
    ),
    (
        "THE RECORDING INDUSTRY & THE WIDER REGION (context)",
        "A record business took shape around the music: Eric Gallo's label and the pioneer artist-"
        "producer Griffiths Motsieloa cut the first Black South African discs, while ethnographers like "
        "Hugh Tracey (ILAM) archived traditions across the whole region -- the Copperbelt of Northern "
        "Rhodesia (Zambia) and Southern Rhodesia (Zimbabwe) included. Content note: much of it was "
        "marketed under a segregationist 'tribal' framing.",
        [
            ("Griffiths Motsieloa (first Black SA recording artist-producer)", None),
            ("Gallo & the first Black South African 78s", None),
            ("Copperbelt guitar (Northern Rhodesia / Zambia)", None),
            ("Southern Rhodesia early recordings (Zimbabwe)", None),
            ("Hugh Tracey / ILAM field recordings (regional archive)", None),
        ],
    ),
]

STEM = "ssa_south_music_2_MARABI_MISSION_EARLY_RECORDING"


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
