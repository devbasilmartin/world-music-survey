#!/usr/bin/env python3
"""Build East Asia: Korea, installment 2: The 20th Century -- Occupation, Trot & Early Pop.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/romanized only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Korean Music — Installment 2: "
         "Occupation, Trot & Early Pop (c. 1900-1960)")

FRAMING = (
    "Korea's early modern music was forged under occupation and war. Japanese colonial rule (1910-1945) "
    "suppressed Korean culture and marginalized the old court music, even as it opened the door to "
    "Western song (the hymn-and-school-song CHANGGA) and to the gramophone. From that collision came "
    "TROT (teuroteu, or 'ppongjjak') -- Korea's first pop, a sentimental two-beat song blending "
    "Japanese enka, Western foxtrot, and deep Korean HAN. Its first stars, above all LEE NAN-YOUNG "
    "('Tears of Mokpo', 1935), sang a sorrow that doubled as veiled national feeling. Then came "
    "liberation (1945), the tragic division of the peninsula, and the catastrophic KOREAN WAR (1950-53), "
    "whose songs of separation ('Farewell at Busan Station') still ache. Finally the US military "
    "presence and AFKN radio poured American jazz, pop, and rock into the South via the 'Eighth Army "
    "show' circuit -- the seedbed of the modern Korean pop and rock to come. Cross-links: Japanese enka "
    "(the Japan survey) shaping trot; American pop (US survey) via the army bases; the gugak roots (#1) "
    "pushed underground. Content notes: colonial suppression and the Korean War are kept with care. "
    "Names romanized. Region: Korea (primarily the South after 1945)."
)

SECTIONS = [
    (
        "COLONIAL RULE & THE SUPPRESSION OF GUGAK (1910-1945)",
        "Under Japanese rule, Korean court music lost its royal patronage, the language and culture were "
        "increasingly suppressed (harshly so by the late 1930s), and the old traditions were pushed to "
        "the margins. Yet music also modernized fast, on Japanese and Western terms. Content note: this "
        "is culture under colonial domination -- kept with care.",
        [
            ("Japanese colonial rule & Korean music (1910-1945)", None),
            ("The court music loses its patronage (gugak marginalized)", None),
            ("Cultural suppression under occupation (content note)", None),
            ("Modernization on colonial terms (Japanese & Western)", None),
        ],
    ),
    (
        "CHANGGA & THE COMING OF WESTERN SONG (c. 1900-1930)",
        "Western music entered Korea through churches and modern schools as CHANGGA -- new songs set to "
        "Western hymn and school-song melodies, teaching modern ideas (and, quietly, national feeling). "
        "It reshaped the Korean musical ear and paved the way for a Western-style popular song.",
        [
            ("Changga (the early Western-style Korean songs)", None),
            ("Western music via church & school (the missionary route)", None),
            ("The Korean ear meets Western melody", None),
            ("Modern ideas & quiet nationalism in changga", None),
        ],
    ),
    (
        "THE BIRTH OF TROT (teuroteu) (c. 1925-1945)",
        "TROT -- 'teuroteu', nicknamed 'ppongjjak' for its two-beat lilt -- became Korea's first true "
        "popular music: a sentimental ballad fusing Japanese enka's minor-key melancholy, the Western "
        "foxtrot rhythm, and Korean han. Recorded by Columbia, Victor, and OKeh, it filled the gramophone "
        "age. Cross-link: Japanese enka (the Japan survey), remade in Korean.",
        [
            ("Trot / teuroteu (the birth of Korean pop)", None),
            ("Ppongjjak (the two-beat trot lilt)", None),
            ("Enka, foxtrot & han (the trot fusion)", None),
            ("The colonial-era record industry (Columbia, Victor, OKeh)", None),
            ("The gramophone age in Korea", None),
        ],
    ),
    (
        "THE FIRST RECORDING STARS (c. 1930-1945)",
        "Trot minted Korea's first pop celebrities. Lee Nan-young's 'Tears of Mokpo' (1935) became a "
        "defining hit whose sorrow read as veiled national longing; Nam In-su, Chae Gyu-yeop, and Wang "
        "Su-bok were gramophone idols. The star system had arrived. Content note: overt patriotism was "
        "censored, so feeling went coded.",
        [
            ("Mokpo-ui Nunmul (Tears of Mokpo)", "Lee Nan-young"),
            ("Lee Nan-young (the first great trot star)", None),
            ("Nam In-su (the gramophone-age idol)", None),
            ("Chae Gyu-yeop & Wang Su-bok (early recording stars)", None),
            ("Veiled national feeling in colonial pop (coded han)", None),
        ],
    ),
    (
        "LIBERATION & DIVISION (1945-1950)",
        "Liberation in 1945 brought euphoria -- and then the tragic division of the peninsula at the "
        "38th parallel. New 'liberation songs' rang out, Hyun In's 'Silla Moonlit Night' charmed the "
        "recovering South, and a battered entertainment industry began to rebuild before catastrophe "
        "struck again.",
        [
            ("Sinla-ui Dalbam (Silla Moonlit Night)", "Hyun In"),
            ("Liberation (1945) & the songs of freedom", None),
            ("The division of the peninsula (the 38th parallel)", None),
            ("Rebuilding the entertainment scene (post-liberation)", None),
        ],
    ),
    (
        "THE KOREAN WAR & ITS SONGS (1950-1953)",
        "The Korean War devastated the peninsula and tore millions of families apart across the new "
        "border. Its songs are among the most wrenching in Korean music -- 'Farewell at Busan Station' "
        "and 'Heartbreaking Miari Hill' voice the refugee's grief and the pain of separation. Content "
        "note: the war's catastrophe and its divided families are kept with care.",
        [
            ("Ibyeol-ui Busan Jeonggeojang (Farewell at Busan Station)", "Nam In-su"),
            ("Danjang-ui Miari Gogae (Heartbreaking Miari Hill)", "Lee Hae-yeon"),
            ("Songs of the refugee & the separated family", None),
            ("The Korean War (1950-53) in song (content note)", None),
            ("The pain of division (the wartime ballad)", None),
        ],
    ),
    (
        "THE US BASES, AFKN & THE AMERICAN INVASION (c. 1953-1960)",
        "After the armistice, the American military presence transformed Southern music. AFKN radio "
        "broadcast US pop, jazz, and rock-and-roll; and the 'Eighth Army show' circuit -- entertaining "
        "GIs on the bases -- became the school where a generation of Korean musicians learned American "
        "styles. Cross-link: American pop (US survey) enters Korea wholesale.",
        [
            ("AFKN radio (American pop reaches Korea)", None),
            ("The Eighth Army show circuit (the base-club school)", None),
            ("American jazz, pop & rock invade the South", None),
            ("Korean musicians learn the American songbook", None),
        ],
    ),
    (
        "THE POSTWAR SCENE & THE ROAD AHEAD (c. 1953-1960)",
        "From the ruins a lively postwar entertainment world revived -- trot roared back, cabaret and "
        "radio flourished, and the collision of Korean sentiment with American sound set the stage for "
        "the folk, rock, and pop explosion of the 1960s-70s (Shin Joong-hyun, Patti Kim). Cross-link: "
        "toward the developmental-decade pop of Installment 3.",
        [
            ("The postwar trot revival", None),
            ("Cabaret & radio in 1950s Korea", None),
            ("Korean sentiment meets American sound", None),
            ("Toward the 1960s folk-rock-pop explosion (roads ahead)", None),
        ],
    ),
]

STEM = "korea_music_2_OCCUPATION_TROT_EARLY_POP"


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
