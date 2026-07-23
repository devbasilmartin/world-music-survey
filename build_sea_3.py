#!/usr/bin/env python3
"""Build Southeast Asia, installment 3: The 20th-Century Crooner & Film Era.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Southeast Asian Music — Installment 3: "
         "The 20th-Century Crooner & Film Era (Kroncong, Luk Thung, Nhac Vang, Kundiman & the Golden-Age Pop)")

FRAMING = (
    "Before the age of dangdut and K-pop-style idols, Southeast Asia had its own golden age of the "
    "POPULAR SONG -- a mid-century world of crooners, film playback singers, and radio stars who fused "
    "local melody with the guitar, the string orchestra, and the microphone. Indonesia's KRONCONG, born "
    "of a Portuguese ukulele-like instrument in the old port quarters, became the sweet national "
    "sentimental song ('Bengawan Solo'). Thailand split into the urban LUK KRUNG and the rural, "
    "heart-on-sleeve LUK THUNG of Suraphon and Pumpuang. In Saigon, the pre-1975 crooners of NHAC VANG "
    "('yellow music') and the songs of Trinh Cong Son gave Vietnam its most beloved ballads. The "
    "Philippines refined the KUNDIMAN art-song and then built early OPM around Pilita Corrales and the "
    "young Nora Aunor. And across the region, film was king: Malaya's P. RAMLEE was a one-man golden age, "
    "and Cambodia's astonishing 1960s-70s rock-and-pop scene -- Sinn Sisamouth, Ros Serey Sothea, Pan Ron "
    "-- blazed brilliantly before the Khmer Rouge. Content note: nearly all of Cambodia's golden-age "
    "stars were murdered in 1975-1979; their surviving recordings are treasured. Names transliterated. "
    "Cross-links: mainland classical (#2); the island gamelan world (#1); the modern pop era ahead (#4). "
    "Region: 20th-century Southeast Asia."
)

SECTIONS = [
    (
        "INDONESIA: KRONCONG, THE SWEET NATIONAL SONG",
        "Kroncong grew from a small ukulele-like instrument brought by the Portuguese to the port "
        "quarters of Batavia centuries ago, becoming Indonesia's gentle, nostalgic popular song of "
        "interlocking plucked strings and a crooned melody. Gesang's 'Bengawan Solo' (1940) is its "
        "immortal anthem, beloved across Asia; Waldjinah reigned as its queen.",
        [
            ("Bengawan Solo", "Gesang"),
            ("Walang Kekek", "Waldjinah"),
            ("Kroncong (the Indonesian sentimental song)", None),
            ("The kroncong ensemble (the ukulele-born strings)", None),
            ("Langgam Jawa (the Javanese kroncong style)", None),
        ],
    ),
    (
        "THAILAND: LUK KRUNG & THE CITY SONG",
        "As Thailand modernized, the urbane LUK KRUNG ('child of the capital') set romantic Thai lyrics "
        "to Western-style light orchestras and jazz-tinged arrangements -- the polished sound of Bangkok "
        "radio and the ballroom. The composer-king Bhumibol Adulyadej wrote jazz standards, and Suntharaporn's "
        "band defined the elegant mid-century Thai pop.",
        [
            ("Luk krung (the Thai city song)", None),
            ("Suntharaporn (the classic Thai big band)", None),
            ("Falling Rain (H.M. Bhumibol's jazz)", "Bhumibol Adulyadej"),
            ("The Thai light orchestra (radio & ballroom)", None),
        ],
    ),
    (
        "THAILAND: LUK THUNG, THE SONG OF THE FIELDS",
        "LUK THUNG ('child of the fields') is the soul music of rural Thailand -- slow, deeply emotive, "
        "ornamented singing about hardship, love, and the countryside, with a distinctive quavering vibrato. "
        "Suraphon Sombatcharoen was its founding king, and Pumpuang Duangjan its beloved queen, whose "
        "'electronic luk thung' made her a legend mourned by the nation.",
        [
            ("Mae Kha Song Rome (the luk thung classic)", "Suraphon Sombatcharoen"),
            ("Krasab Sung (Pumpuang's signature)", "Pumpuang Duangjan"),
            ("Luk thung (the Thai country song of the fields)", None),
            ("Suraphon Sombatcharoen (the king of luk thung)", None),
            ("Pumpuang Duangjan (the queen of luk thung)", None),
        ],
    ),
    (
        "VIETNAM: NHAC VANG & THE SAIGON CROONERS",
        "In the Saigon of the 1950s-1970s, NHAC VANG ('yellow music') -- sentimental, bolero-tinged "
        "ballads of love and longing -- and the pre-1975 crooners ruled. Content note: after 1975 the "
        "style was long banned in the north as decadent, surviving in the diaspora before its revival. "
        "Its stars, from Thai Thanh to Che Linh, remain deeply beloved.",
        [
            ("Nhac vang (the Vietnamese 'yellow music' ballad)", None),
            ("The Vietnamese bolero (the Saigon sentimental song)", None),
            ("Thai Thanh (the pre-1975 Saigon voice)", None),
            ("Che Linh (the nhac vang crooner)", None),
            ("Pham Duy (the great Vietnamese songwriter)", None),
        ],
    ),
    (
        "VIETNAM: TRINH CONG SON & THE POET-SONGWRITER",
        "Trinh Cong Son was Vietnam's Dylan and its most profound songwriter -- his spare, philosophical "
        "songs of love, peace, and the sorrow of war became the conscience of a generation, immortalized "
        "by the singer Khanh Ly. Content note: his anti-war 'yellow-skinned mother' songs stand as some "
        "of the most moving music of the Vietnam War era.",
        [
            ("Diem Xua (Faded Memories)", "Trinh Cong Son"),
            ("Ha Trang (White Summer)", "Khanh Ly"),
            ("Trinh Cong Son (the poet of Vietnamese song)", None),
            ("Khanh Ly (the voice of Trinh's songs)", None),
            ("Ca khuc da vang (the anti-war song cycle)", None),
        ],
    ),
    (
        "THE PHILIPPINES: KUNDIMAN & EARLY OPM",
        "The Philippines refined the KUNDIMAN -- a lyrical Tagalog art-song of yearning, its love often a "
        "veiled love of country -- perfected by composers like Nicanor Abelardo and Francisco Santiago. "
        "From it grew mid-century Filipino popular music: the Kapampangan-Spanish glamour of Pilita "
        "Corrales and the meteoric rise of the young 'superstar' Nora Aunor.",
        [
            ("Mutya ng Pasig", "Nicanor Abelardo"),
            ("Kundiman (the Filipino art-song of yearning)", None),
            ("Dahil Sa Iyo (Because of You)", "Pilita Corrales"),
            ("Pilita Corrales (Asia's Queen of Songs)", None),
            ("Nora Aunor (the Filipino superstar)", None),
        ],
    ),
    (
        "MALAYA & THE FILM SONG: P. RAMLEE",
        "In the Malay world, the golden age of Singapore-Malay cinema produced a one-man legend: P. "
        "RAMLEE -- actor, director, composer, and singer -- whose warm, sophisticated film songs blending "
        "Malay melody, Latin, and jazz remain the beloved standard across Malaysia, Singapore, and "
        "Indonesia. The keroncong-tinged and asli styles filled the silver screen.",
        [
            ("Getaran Jiwa", "P. Ramlee"),
            ("Di Mana Kan Ku Cari Ganti", "P. Ramlee"),
            ("P. Ramlee (the Malay film-song legend)", None),
            ("Malay film music (the golden age of Malay cinema)", None),
            ("Lagu asli & the Malay sentimental song", None),
        ],
    ),
    (
        "CAMBODIA'S GOLDEN AGE: THE 1960s-70s ROCK & POP",
        "For a brilliant decade, Phnom Penh had one of Asia's most thrilling pop scenes -- Cambodian rock, "
        "surf, soul, and psychedelia fused with Khmer melody. Sinn Sisamouth, the 'King', Ros Serey Sothea, "
        "the 'Golden Voice', and the wild Pan Ron made unforgettable records. Content note: nearly all of "
        "them were murdered under the Khmer Rouge (1975-1979); their surviving songs are treasured relics.",
        [
            ("Champa Battambang", "Sinn Sisamouth"),
            ("Chnam Oun 16 (I'm 16)", "Ros Serey Sothea"),
            ("Cambodian rock & pop (the 1960s-70s golden age)", None),
            ("Sinn Sisamouth (the King of Khmer music)", None),
            ("Ros Serey Sothea (the Golden Voice of the capital)", None),
            ("Pan Ron (the wild Khmer pop voice)", None),
            ("The golden age lost to the Khmer Rouge (content note)", None),
        ],
    ),
    (
        "THE CROONER ERA & THE ROAD AHEAD",
        "Across the region, the mid-century popular song fused local melody with the guitar, the string "
        "orchestra, film, and radio -- a golden age of crooners and playback stars beloved to this day. "
        "From here the sound would electrify into dangdut, and the modern pop, hip-hop, and idol worlds "
        "of the present (#4, the SE Asia finale). Cross-links: mainland classical (#2); the island "
        "gamelan world (#1).",
        [
            ("The Southeast Asian crooner era (the shared golden age)", None),
            ("Film, radio & the popular song (the mid-century sound)", None),
            ("Local melody meets the guitar & the orchestra", None),
            ("Toward dangdut & the modern pop present (roads ahead)", None),
        ],
    ),
]

STEM = "sea_music_3_CROONER_FILM_ERA"


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
