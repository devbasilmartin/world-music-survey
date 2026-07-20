#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Southern, installment 3: Kwela, Sax Jive & Township Jazz.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1950-1962.
Note: dedup key is TITLE-only (norm() drops artist), so every title string must be unique region-wide.
"""

TITLE = ("The Story of Southern African Music — Installment 3: "
         "Kwela, Sax Jive & Township Jazz (c. 1950-1962)")

FRAMING = (
    "The 1950s are Black South Africa's dazzling, doomed golden age -- the Sophiatown and District Six "
    "years, when the marabi and mission music of Installment 2 flowered into a world-class urban "
    "culture just as apartheid moved to destroy it. On the street corners, boys turned a cheap tin "
    "pennywhistle into KWELA -- Spokes Mashiyane its virtuoso -- and 'Tom Hark' became a British hit. "
    "Kwela grew up into SAX JIVE, and the shebeens and dance halls rang with a sophisticated TOWNSHIP "
    "JAZZ: the close-harmony Manhattan Brothers, the young Miriam Makeba and the Skylarks, Dorothy "
    "Masuka, and the bebop of the Jazz Epistles (Dollar Brand/Abdullah Ibrahim, Hugh Masekela, Kippie "
    "Moeketsi). The 1959 jazz musical 'King Kong' launched a generation onto the world stage. Then the "
    "bulldozers came: the 1955 destruction of Sophiatown and the tightening pass laws scattered this "
    "world, and by the early 1960s Makeba, Masekela, Ibrahim, Masuka, and Gwangwa were all in exile -- "
    "a direct bridge into the US survey. Cross-links: township jazz <-> American swing and bebop; "
    "kwela's pennywhistle <-> UK skiffle. Content note: this chapter ends in forced removal and exile, "
    "kept with full weight. Region: all artists are South African. Because dedup is by song title, "
    "every title here is unique across the survey."
)

SECTIONS = [
    (
        "KWELA: THE PENNYWHISTLE OF THE STREETS (c. 1950-1958)",
        "A sixpenny tin flute became a national craze. Spokes Mashiyane was the undisputed king of "
        "KWELA -- bright, skipping pennywhistle jive played on street corners, one lookout watching for "
        "police (kwela means 'climb on/jump up', also slang for the police van). In 1956 'Tom Hark' "
        "reached the UK charts. Cross-link: the pennywhistle craze paralleled British skiffle.",
        [
            ("Ace Blues", "Spokes Mashiyane"),
            ("Kwela Spokes", "Spokes Mashiyane"),
            ("Big Joe Special", "Spokes Mashiyane"),
            ("Tom Hark", "Elias and his Zig-Zag Jive Flutes"),
            ("Lemmy Special", "Lemmy Special Mabaso"),
            ("Jackpot (Spokes goes to sax)", "Spokes Mashiyane"),
            ("Kwela pennywhistle street jive (Johannesburg)", None),
        ],
    ),
    (
        "SOPHIATOWN & THE VOCAL-JAZZ GROUPS (c. 1950-1959)",
        "Sophiatown -- the one Johannesburg suburb where Black people could own property -- was a "
        "cosmopolitan melting pot of jazz, gangsters, writers (Drum magazine), and close-harmony "
        "groups. The Manhattan Brothers, modelled on American vocal quartets, scored a landmark with "
        "'Lovely Lies', and the young Miriam Makeba sang with them and with her own female group the "
        "Skylarks. Cross-link: the harmony model is the US survey's (the Mills Brothers, the Ink Spots).",
        [
            ("Lovely Lies (Lakutshona Ilanga)", "Manhattan Brothers"),
            ("Kilimanjaro", "Manhattan Brothers"),
            ("Miriam Makeba and the Skylarks (Sophiatown close-harmony)", None),
            ("African Inkspots close-harmony jive", None),
            ("Sophiatown shebeen jazz (Drum-era)", None),
        ],
    ),
    (
        "THE GREAT VOICES: MAKEBA, MASUKA & RATHEBE (c. 1953-1961)",
        "The era's women became its immortals. Miriam Makeba cut the original 'Pata Pata' and the "
        "'Click Song' before exile made her a global icon; Dorothy Masuka wrote and sang sharp, topical "
        "hits until the apartheid state banned and hounded her out; and Dolly Rathebe was the glamorous "
        "face of Black film and song. Content note: nearly all of them were forced into exile by the "
        "early 1960s.",
        [
            ("Pata Pata (1957 original)", "Miriam Makeba"),
            ("Qongqothwane (The Click Song)", "Miriam Makeba"),
            ("Sophiatown Is Gone", "Miriam Makeba"),
            ("Hamba Nontsokolo", "Dorothy Masuka"),
            ("Into Yam", "Dorothy Masuka"),
            ("Dolly Rathebe (Sophiatown film diva)", None),
        ],
    ),
    (
        "THE JAZZ EPISTLES & MODERN JAZZ (c. 1959-1962)",
        "South Africa's modernists absorbed bebop and made it their own. In 1960 the Jazz Epistles -- "
        "Dollar Brand (Abdullah Ibrahim) on piano, Hugh Masekela on trumpet, Jonas Gwangwa on trombone, "
        "and the visionary alto Kippie Moeketsi -- cut the first LP by Black South African jazz "
        "musicians. Cross-link: this is Parker and Gillespie (US survey) re-voiced with a township "
        "accent, and its players would soon carry it to New York.",
        [
            ("Jazz Epistle, Verse 1", "The Jazz Epistles"),
            ("Scullery Department", "The Jazz Epistles"),
            ("Kippie Moeketsi (the township Charlie Parker)", None),
            ("Dollar Brand trio (early Abdullah Ibrahim)", None),
            ("Jonas Gwangwa & Hugh Masekela (pre-exile brass)", None),
        ],
    ),
    (
        "'KING KONG' & THE MUSICAL STAGE (1959)",
        "The all-Black jazz musical 'King Kong' (music by Todd Matshikiza, the story of boxer Ezekiel "
        "Dlamini) was a sensation in Johannesburg and then London, and it catapulted Makeba, Masekela, "
        "and their peers onto the international stage. It is the sound of township jazz at its peak, "
        "just before the diaspora.",
        [
            ("Back of the Moon", "Todd Matshikiza"),
            ("King Kong (1959 jazz musical, title theme)", None),
            ("Sad Times, Bad Times (from King Kong)", None),
            ("The Ballad of King Kong", None),
        ],
    ),
    (
        "REMOVALS & EXILE: THE END OF SOPHIATOWN (c. 1955-1962)",
        "The golden age was bulldozed. From 1955 the state demolished Sophiatown and forced its people "
        "to the barren township of Meadowlands; the ironic hit 'Meadowlands' masked its protest in a "
        "cheerful tune. Pass laws, bans, and the post-Sharpeville crackdown drove the music's greatest "
        "names abroad. Content note: this exile seeds the US and world careers of Makeba and Masekela "
        "(US survey) and sets up the defiant home-grown mbaqanga of Installment 4.",
        [
            ("Meadowlands", "Nancy Jacobs and her Sisters"),
            ("Bye Bye Sophiatown (forced-removal lament)", None),
            ("Township jazz in exile (the diaspora begins)", None),
            ("Sax jive after the removals (early 1960s)", None),
        ],
    ),
]

STEM = "ssa_south_music_3_KWELA_TOWNSHIP_JAZZ"


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
