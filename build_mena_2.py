#!/usr/bin/env python3
"""Build MENA, installment 2: The Egyptian Golden Age & the Great Divas.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Middle Eastern & North African Music — Installment 2: "
         "The Egyptian Golden Age & the Great Divas (c. 1920-1975)")

FRAMING = (
    "For half a century Cairo was the Hollywood of the Arab world -- its radio, records, and musical "
    "cinema broadcasting a shared golden age from Morocco to Iraq. At its center stood UMM KULTHUM, the "
    "'Star of the East', whose monthly Thursday-night concerts, carried live across the Arab world, "
    "held entire nations rapt through hour-long songs of overwhelming emotional power; she is the most "
    "revered Arab musician who ever lived. Around her shone a constellation: MOHAMMED ABDEL WAHAB, the "
    "modernizer who married Western orchestration to Arab melody; ABDEL HALIM HAFEZ, the romantic film "
    "idol and voice of Nasser's generation; the King of the Oud FARID AL-ATRASH and his tragic sister "
    "ASMAHAN; and, in Lebanon, the crystalline FAIRUZ with the Rahbani Brothers, a more folk-and-"
    "European-tinged alternative to Cairo's tarab. This is the classic songbook the whole Arab world "
    "still knows by heart. Cross-links: the maqam and tarab roots (#1) scaled up to the grand orchestra; "
    "the Nasserist pan-Arab moment; the modern pop to come. Content note: the era intertwines with "
    "Nasser-era politics -- kept in view. Names transliterated. Region: Egypt & Lebanon (the Mashriq "
    "golden age)."
)

SECTIONS = [
    (
        "CAIRO: THE HOLLYWOOD OF THE ARAB WORLD",
        "Egyptian radio (from 1934), a booming musical-film industry, and the record labels made Cairo "
        "the cultural capital of the entire Arabic-speaking world. Its stars became household names from "
        "Casablanca to Baghdad, and the Egyptian dialect became the shared language of Arab song and "
        "cinema.",
        [
            ("Cairo, capital of Arab music & cinema", None),
            ("Egyptian radio & the pan-Arab broadcast (1934 on)", None),
            ("The Egyptian musical film (the singing-star cinema)", None),
            ("The Arab star system (Cairo's golden age)", None),
        ],
    ),
    (
        "UMM KULTHUM: THE VOICE OF THE ARAB WORLD (c. 1930-1975)",
        "Umm Kulthum -- 'Kawkab al-Sharq', the Star of the East -- is the towering figure of Arab music. "
        "Her live Thursday-night concerts, broadcast across the Arab world, built hour-long songs like "
        "'Enta Omri', 'Alf Leila wa Leila', and 'Al Atlal' into overwhelming communal experiences. Her "
        "1975 funeral drew millions. No one has ever meant more to a people's music.",
        [
            ("Enta Omri", "Umm Kulthum"),
            ("Alf Leila wa Leila (A Thousand and One Nights)", "Umm Kulthum"),
            ("Al Atlal (The Ruins)", "Umm Kulthum"),
            ("Umm Kulthum (Kawkab al-Sharq, the Star of the East)", None),
            ("The Thursday-night concerts (the pan-Arab ritual)", None),
            ("The hour-long tarab song (the Umm Kulthum experience)", None),
        ],
    ),
    (
        "THE UMM KULTHUM SONGBOOK & HER COMPOSERS",
        "Behind the voice stood the era's greatest craftsmen. Riyad al-Sunbati composed her most "
        "profound songs (including 'Al Atlal'); Zakaria Ahmed and Mohammed al-Qasabgi shaped her early "
        "art; Baligh Hamdi modernized her late sound; and the poet Ahmad Rami wrote her words. 'Amal "
        "Hayati' is another jewel of this peerless songbook.",
        [
            ("Amal Hayati (The Hope of My Life)", "Umm Kulthum"),
            ("Riyad al-Sunbati (Umm Kulthum's great composer)", None),
            ("Zakaria Ahmed & Mohammed al-Qasabgi (the early composers)", None),
            ("Baligh Hamdi (the modernizing composer)", None),
            ("Ahmad Rami (the poet of Umm Kulthum's songs)", None),
        ],
    ),
    (
        "MOHAMMED ABDEL WAHAB: THE MODERNIZER (c. 1920-1975)",
        "Mohammed Abdel Wahab -- the 'musician of the generations' -- transformed Arab music, folding in "
        "Western orchestration, tango and rumba rhythms, and film scoring while keeping its maqam soul. "
        "His 'El Gondool' is a classic, and his late-career composition of 'Enta Omri' for Umm Kulthum "
        "was hailed as 'the meeting of the giants'.",
        [
            ("El Gondool (The Gondola)", "Mohammed Abdel Wahab"),
            ("Mohammed Abdel Wahab (the musician of the generations)", None),
            ("Western orchestration meets Arab melody (Abdel Wahab's reform)", None),
            ("The meeting of the giants (Abdel Wahab & Umm Kulthum)", None),
        ],
    ),
    (
        "ABDEL HALIM HAFEZ: THE DARK NIGHTINGALE (c. 1953-1977)",
        "Abdel Halim Hafez -- 'al-Andaleeb al-Asmar', the Dark Nightingale -- was the romantic idol of "
        "the Nasser generation: a film star and heartthrob whose tender, aching voice on 'Ahwak' and "
        "'Zay El Hawa' defined young love, alongside nationalist anthems of the pan-Arab dream. Content "
        "note: he died in 1977, mourned as a national symbol.",
        [
            ("Ahwak (I Love You)", "Abdel Halim Hafez"),
            ("Zay El Hawa (Like Love)", "Abdel Halim Hafez"),
            ("Abdel Halim Hafez (the Dark Nightingale)", None),
            ("Qariat al-Fingan (The Fortune Teller)", "Abdel Halim Hafez"),
            ("The romantic film idol & the Nasser generation", None),
        ],
    ),
    (
        "FARID AL-ATRASH & ASMAHAN",
        "The Druze-Syrian siblings lit up Egyptian cinema. Farid al-Atrash -- the 'King of the Oud' -- "
        "was a virtuoso, composer, singer, and film star of aching romantic songs ('Ya Zahra'); his "
        "sister Asmahan possessed one of the greatest voices in Arab history ('Ya Toyour') before her "
        "mysterious death in 1944 at just 31. Content note: her early death is kept in view.",
        [
            ("Ya Zahra (Ya Zahratan fi Khayali)", "Farid al-Atrash"),
            ("Ya Toyour (O Birds)", "Asmahan"),
            ("Farid al-Atrash (the King of the Oud)", None),
            ("Asmahan (the great voice lost young)", None),
            ("The singing siblings in Egyptian cinema", None),
        ],
    ),
    (
        "LEBANON: FAIRUZ & THE RAHBANI BROTHERS (c. 1955-1975)",
        "Beirut offered a luminous alternative. Fairuz -- the 'soul of Lebanon' -- sang the songs of the "
        "Rahbani Brothers (Assi and Mansour), who fused Arab melody with folk and European classical "
        "into something crystalline and modern. Their Baalbeck-festival musical plays and songs like "
        "'Li Beirut' and 'Nassam Alayna El Hawa' are beloved across the Arab world.",
        [
            ("Li Beirut (To Beirut)", "Fairuz"),
            ("Nassam Alayna El Hawa (The Breeze Blew Upon Us)", "Fairuz"),
            ("Fairuz (the soul of Lebanon)", None),
            ("The Rahbani Brothers (Assi & Mansour, the composers)", None),
            ("The Baalbeck festival & the Rahbani musical plays", None),
            ("Wadih El Safi (the Lebanese classical giant)", None),
        ],
    ),
    (
        "THE ORCHESTRA, THE OTHER DIVAS & THE ROAD AHEAD (c. 1950-1975)",
        "The golden age scaled the intimate takht up into the grand firqa orchestra of massed violins "
        "and the electric qanun, and a wider firmament shone -- the Algerian-Egyptian Warda, the "
        "Lebanese Sabah, and the Egyptian Nagat and Shadia. The era closed with Umm Kulthum's death in "
        "1975. Cross-link: toward pan-Arab pop and the modern era.",
        [
            ("The firqa (the grand Arab orchestra)", None),
            ("Warda al-Jazairia (the Algerian-Egyptian diva)", None),
            ("Sabah, Nagat & Shadia (the other golden-age divas)", None),
            ("The end of the golden age (Umm Kulthum's death, 1975)", None),
            ("Toward pan-Arab pop (roads ahead)", None),
        ],
    ),
]

STEM = "mena_music_2_EGYPTIAN_GOLDEN_AGE_DIVAS"


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
