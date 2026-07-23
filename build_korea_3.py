#!/usr/bin/env python3
"""Build East Asia: Korea, installment 3: The Developmental Decades -- Folk, Rock, Trot & the Ballad.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/romanized only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Korean Music — Installment 3: "
         "The Developmental Decades — Folk, Rock, Trot & the Ballad (c. 1960-1987)")

FRAMING = (
    "Across three decades of breakneck growth and harsh military rule, South Korean popular music grew "
    "into its own -- and repeatedly collided with the state. Musicians trained in the US Army base "
    "clubs became the first stars (Patti Kim, the Kim Sisters, who reached American TV), and SHIN "
    "JOONG-HYUN, the 'godfather of Korean rock', plugged in the electric guitar (his 'Beauty' a 1974 "
    "landmark). A folk boom and TONGGITA (acoustic-guitar) youth counterculture found its anthem in Kim "
    "Min-gi's 'Morning Dew'; TROT reached a golden age with Lee Mi-ja and the Nam Jin / Na Hoon-a "
    "rivalry; and CHO YONG-PIL emerged as the first true superstar with 'Come Back to Busan Port'. But "
    "all of it played out under the Park Chung-hee and Chun Doo-hwan dictatorships, whose censorship "
    "banned hundreds of songs and whose 1975 marijuana crackdown jailed and blacklisted the rock and "
    "folk scene. By 1987, democratization and the coming Seoul Olympics were about to open everything "
    "up. Cross-links: American pop/rock (US survey) via the bases; Japanese trot ties; the Seo Taiji "
    "revolution & K-pop ahead (#4). Content notes: dictatorship, censorship, and the 1975 crackdown are "
    "kept factual and with care. Names romanized. Region: South Korea."
)

SECTIONS = [
    (
        "THE EIGHTH-ARMY GENERATION & THE FIRST STARS (c. 1958-1968)",
        "The US base-club circuit produced Korea's first modern pop stars. Patti Kim became the "
        "nation's first great diva; the Kim Sisters took Korean pop onto American television (the Ed "
        "Sullivan Show); and a polished, Western-facing showbiz emerged, fluent in jazz standards and "
        "American pop.",
        [
            ("Patti Kim (Korea's first diva)", None),
            ("The Kim Sisters (Korean pop on US television)", None),
            ("The base-club showbiz generation", None),
            ("Jazz standards & American pop, Koreanized", None),
        ],
    ),
    (
        "SHIN JOONG-HYUN & THE BIRTH OF KOREAN ROCK (c. 1964-1975)",
        "Shin Joong-hyun -- the 'godfather of Korean rock' -- electrified Korean music. His band the "
        "Add4 cut 'The Woman in the Rain' (1964), often called the first Korean rock song, and his "
        "psychedelic guitar peaked with 'Beauty' (1974). Content note: he refused to write a song "
        "praising the president and was later blacklisted and jailed.",
        [
            ("Bitsokui Yeoin (The Woman in the Rain)", "The Add4"),
            ("Miin (Beauty)", "Shin Joong-hyun"),
            ("Shin Joong-hyun (the godfather of Korean rock)", None),
            ("Korean psychedelic rock (the Yeopjeons era)", None),
            ("The electric guitar comes to Korea", None),
        ],
    ),
    (
        "THE FOLK BOOM & THE TONGGITA COUNTERCULTURE (c. 1968-1978)",
        "A folk boom gave restless youth its voice. Around the tonggita (acoustic-guitar) cafes, Kim "
        "Min-gi's 'Morning Dew' became an unofficial protest anthem, the wild Han Dae-soo sang of a "
        "'Land of Happiness', and Yang Hee-eun and Song Chang-sik led a jeans-and-long-hair generation. "
        "Content note: many of these songs were banned.",
        [
            ("Achim Isul (Morning Dew)", "Kim Min-gi"),
            ("Haengbokui Nara-ro (To a Land of Happiness)", "Han Dae-soo"),
            ("The tonggita folk-cafe scene (guitar & youth)", None),
            ("Yang Hee-eun & Song Chang-sik (the folk voices)", None),
            ("The jeans-and-guitar counterculture", None),
        ],
    ),
    (
        "TROT'S GOLDEN AGE (c. 1964-1980)",
        "Trot reached its golden age as the music of the people. Lee Mi-ja, the 'queen of elegy', ruled "
        "with 'Camellia Lady' (1964, later banned for sounding too Japanese); and the great rivalry of "
        "Nam Jin ('Together With You') and Na Hoon-a divided the nation's affections. Trot was Korea's "
        "beating popular heart.",
        [
            ("Dongbaek Agassi (Camellia Lady)", "Lee Mi-ja"),
            ("Nimgwa Hamkke (Together With You)", "Nam Jin"),
            ("Lee Mi-ja (the queen of elegy)", None),
            ("Na Hoon-a & the Nam Jin rivalry (the trot titans)", None),
            ("Trot as the people's music (the golden age)", None),
        ],
    ),
    (
        "CHO YONG-PIL & THE SUPERSTAR ERA (c. 1976-1987)",
        "Cho Yong-pil became Korea's first true superstar and its 'King of Pop'. 'Come Back to Busan "
        "Port' (1976) was a national and pan-Asian sensation (huge in Japan too), and across the 1980s "
        "he dominated every chart, spanning trot, rock, ballad, and folk with a peerless voice.",
        [
            ("Dol-awayo Busanhang-e (Come Back to Busan Port)", "Cho Yong-pil"),
            ("Cho Yong-pil (the King of Korean pop)", None),
            ("A superstar across every genre (Cho's range)", None),
            ("Korean pop reaches Japan (Cho's pan-Asian fame)", None),
        ],
    ),
    (
        "MUSIC UNDER DICTATORSHIP: CENSORSHIP & THE 1975 CRACKDOWN",
        "All of this unfolded under military rule. Park Chung-hee's Yushin regime ran a strict "
        "censorship board that banned hundreds of songs (for being 'decadent', pessimistic, or too "
        "Japanese) and mandated wholesome 'healthy songs'. Content note: the 1975 marijuana (daemacho) "
        "crackdown jailed and blacklisted much of the rock and folk scene, including Shin Joong-hyun.",
        [
            ("The censorship board & the banned-song lists", None),
            ("The 1975 marijuana crackdown (daemacho, content note)", None),
            ("Geonjeon gayo (the mandated 'healthy songs')", None),
            ("Music under the Yushin regime (content note)", None),
            ("Blacklists & the silencing of rock (1975)", None),
        ],
    ),
    (
        "THE BALLAD & THE 1980s SOUND (c. 1980-1987)",
        "The 1980s brought the polished Korean BALLAD to the fore. Yoo Jae-ha's landmark 1987 album "
        "redefined the form (before his tragic early death), Lee Sun-hee arrived with 'To J' (1984), "
        "and group-sound bands like Deul Gukhwa rocked on. Content note: this played out under Chun "
        "Doo-hwan's rule, in the shadow of the 1980 Gwangju uprising -- kept brief and factual.",
        [
            ("J-ege (To J)", "Lee Sun-hee"),
            ("Yoo Jae-ha & the modern Korean ballad (the 1987 landmark)", None),
            ("Deul Gukhwa (the group-sound rock band)", None),
            ("The gayo TV-chart era (1980s)", None),
            ("The polished Korean ballad emerges", None),
        ],
    ),
    (
        "TOWARD LIBERALIZATION & THE ROAD AHEAD (c. 1985-1988)",
        "By the late 1980s the tide turned. The 1987 democratization movement loosened the state's grip "
        "on culture, censorship eased, and the 1988 Seoul Olympics flung Korea open to the world -- "
        "setting the stage for the Seo Taiji revolution that would ignite modern K-pop. Cross-link: the "
        "birth of K-pop & the Hallyu wave (Installment 4).",
        [
            ("Democratization (1987) & the easing of censorship", None),
            ("The 1988 Seoul Olympics (Korea opens up)", None),
            ("A freer music culture (the late-80s turn)", None),
            ("Toward Seo Taiji & modern K-pop (roads ahead)", None),
        ],
    ),
]

STEM = "korea_music_3_FOLK_ROCK_TROT_BALLAD"


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
