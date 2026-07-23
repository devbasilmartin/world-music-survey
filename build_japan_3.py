#!/usr/bin/env python3
"""Build East Asia: Japan, installment 3: The Postwar Boom -- Kayokyoku, Enka, Group Sounds & Folk.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/romaji only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Japanese Music — Installment 3: "
         "The Postwar Boom — Kayokyoku, Enka, Group Sounds & Folk (c. 1945-1975)")

FRAMING = (
    "From the rubble of 1945, Japan built one of the world's great pop cultures with astonishing speed. "
    "American boogie and jazz fused with Japanese melody into a reborn KAYOKYOKU, and a child prodigy "
    "named HIBARI MISORA rose to become the queen of the entire Showa era. In 1963 Kyu Sakamoto's 'Ue o "
    "Muite Aruko' -- known abroad as 'Sukiyaki' -- topped the American Billboard chart, the only "
    "Japanese-language song ever to do so. The sentimental ENKA ballad reached its golden age (Saburo "
    "Kitajima, Keiko Fuji); sophisticated MOOD KAYO crooners ruled the cabarets; a Beatles-sparked "
    "GROUP SOUNDS boom (The Tigers, The Blue Comets) gave Japan its first mass rock wave; and a "
    "late-60s FOLK boom (Yosui Inoue, Kaguyahime, the Kansai scene) birthed the singer-songwriter. By "
    "1975 the Showa songbook was the beating heart of a pop-cultural superpower. Cross-links: American "
    "pop/rock and the Beatles reshaping Japan; 'Sukiyaki' on the US charts (US survey); the folk boom "
    "flowing into 'New Music', City Pop, and idols (#4). Names transliterated (romaji). Region: Japan."
)

SECTIONS = [
    (
        "FROM THE RUINS: POSTWAR KAYOKYOKU & THE BOOGIE (c. 1945-1952)",
        "Music helped a shattered nation recover. 'The Apple Song' (1945) was the first great postwar "
        "hit, a burst of hope amid the ruins, and Shizuko Kasagi's exuberant 'Tokyo Boogie-Woogie' "
        "(composed by Ryoichi Hattori) caught the American-inflected energy of the occupation years. "
        "Kayokyoku -- Japanese popular song -- was reborn.",
        [
            ("Ringo no Uta (Apple Song)", "Michiko Namiki"),
            ("Tokyo Boogie-Woogie", "Shizuko Kasagi"),
            ("Kayokyoku reborn (postwar Japanese popular song)", None),
            ("Ryoichi Hattori (the composer of the boogie era)", None),
            ("American jazz & boogie in occupied Japan", None),
        ],
    ),
    (
        "HIBARI MISORA: THE QUEEN OF SHOWA (c. 1949-1975)",
        "No star has ever dominated Japan like Hibari Misora. A child prodigy who debuted in 1949, she "
        "reigned for four decades across kayokyoku and enka, her rich, aching voice the very sound of "
        "postwar Japan. 'Ringo Oiwake' (1952) is one of her defining classics. She remains a national "
        "icon beyond category.",
        [
            ("Ringo Oiwake", "Hibari Misora"),
            ("Hibari Misora (the queen of the Showa era)", None),
            ("Kanashiki Kuchibue (Sad Whistle, her early hit)", None),
            ("The voice of postwar Japan (Hibari's reign)", None),
            ("Kayokyoku meets enka (Hibari's range)", None),
        ],
    ),
    (
        "'SUKIYAKI' & THE GLOBAL MOMENT (c. 1961-1963)",
        "In 1961 Kyu Sakamoto recorded 'Ue o Muite Aruko' ('I Look Up as I Walk') -- a bright song of "
        "hidden sadness. Retitled 'Sukiyaki' abroad, it hit number one on the US Billboard Hot 100 in "
        "1963, the only Japanese-language song ever to top the American chart. Cross-link: a rare "
        "East-to-West pop breakthrough.",
        [
            ("Ue o Muite Aruko (Sukiyaki)", "Kyu Sakamoto"),
            ("Kyu Sakamoto (the global Sukiyaki star)", None),
            ("Sukiyaki tops the US Billboard (1963, cross-link)", None),
            ("A Japanese song conquers America (the rare breakthrough)", None),
        ],
    ),
    (
        "ENKA'S GOLDEN AGE (c. 1950-1975)",
        "The sentimental, minor-key ENKA ballad -- of heartbreak, hometowns, sake, and stoic endurance "
        "-- reached its golden age. Saburo Kitajima's 'Kitaguni no Haru', Harumi Miyako, Hachiro Kasuga, "
        "and the tragic Keiko Fuji (mother of Utada Hikaru) with 'Yume wa Yoru Hiraku' defined a genre "
        "that still means 'the heart of Japan' to millions.",
        [
            ("Kitaguni no Haru (Spring in the Northern Country)", "Saburo Kitajima"),
            ("Keiko no Yume wa Yoru Hiraku (Dreams Open at Night)", "Keiko Fuji"),
            ("Enka's golden age (the sentimental ballad flowers)", None),
            ("Harumi Miyako & Hachiro Kasuga (the enka greats)", None),
            ("The kobushi vocal & the minor-key ballad (enka's soul)", None),
        ],
    ),
    (
        "MOOD KAYO & THE URBAN CROONERS (c. 1955-1970)",
        "A sophisticated adult pop -- 'mood kayo' -- filled the cabarets and lounges of a reviving "
        "Japan: smooth, jazzy, and romantic, with a whiff of the exotic. Frank Nagai's 'Let's Meet in "
        "Yurakucho' and the harmony group Mahina Stars gave the salaryman era its late-night soundtrack.",
        [
            ("Frank Nagai (the mood-kayo crooner)", None),
            ("Yurakucho de Aimasho (Let's Meet in Yurakucho)", None),
            ("Mood kayo (the sophisticated adult pop)", None),
            ("Mahina Stars (the harmony-group sound)", None),
            ("The cabaret & lounge kayokyoku", None),
        ],
    ),
    (
        "ROCKABILLY & THE GROUP SOUNDS BOOM (c. 1958-1970)",
        "Western rock hit hard. A late-50s rockabilly craze (the Nichigeki Western Carnival) gave way, "
        "after the Beatles' 1966 Tokyo concert, to the GROUP SOUNDS boom -- hundreds of Beatles-styled "
        "bands. The Blue Comets' 'Blue Chateau' and The Tigers (fronted by the idol Kenji 'Julie' "
        "Sawada) with 'Hana no Kubikazari' led Japan's first mass rock wave.",
        [
            ("Blue Chateau", "The Blue Comets"),
            ("Hana no Kubikazari (The Flower Necklace)", "The Tigers"),
            ("Group Sounds (the Beatles-era band boom)", None),
            ("The Nichigeki Western Carnival (the rockabilly craze)", None),
            ("The Spiders & The Tempters (Group Sounds bands)", None),
            ("Kenji Sawada / Julie (the Group Sounds idol)", None),
        ],
    ),
    (
        "THE FOLK BOOM & THE KANSAI SCENE (c. 1967-1975)",
        "As Group Sounds faded, a folk boom rose -- acoustic, personal, and often political. The Folk "
        "Crusaders' novelty smash 'Kaettekita Yopparai', the anti-war songs of the Kansai scene, and "
        "singer-songwriters like Yosui Inoue ('Yume no Naka e') and the group Kaguyahime ('Kanda-gawa') "
        "birthed the Japanese singer-songwriter. Cross-link: toward 'New Music' (#4).",
        [
            ("Kanda-gawa (The Kanda River)", "Kaguyahime"),
            ("Yume no Naka e (Into the Dream)", "Yosui Inoue"),
            ("Kaettekita Yopparai (The Drunkard Returns)", "The Folk Crusaders"),
            ("The Japanese folk boom (acoustic & political)", None),
            ("Takuro Yoshida & the Kansai folk scene", None),
            ("The singer-songwriter is born (Japan)", None),
        ],
    ),
    (
        "THE SHOWA SONGBOOK & THE ROAD AHEAD (c. 1960-1975)",
        "All these streams poured into the great Showa songbook, broadcast to the nation through records "
        "and TV -- above all NHK's year-end Kohaku Uta Gassen, where the whole country watched its stars "
        "sing. Cross-link: the folk boom would soon mutate into sophisticated 'New Music' and City Pop, "
        "and a manufactured idol industry (Installment 4).",
        [
            ("Kohaku Uta Gassen (NHK's year-end song contest)", None),
            ("The Showa songbook (records & TV)", None),
            ("The kayokyoku star machine (TV & the hit parade)", None),
            ("Toward New Music, City Pop & idols (roads ahead)", None),
        ],
    ),
]

STEM = "japan_music_3_POSTWAR_KAYOKYOKU_GS_FOLK"


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
