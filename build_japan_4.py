#!/usr/bin/env python3
"""Build East Asia: Japan, installment 4: New Music, City Pop & the Idol Age.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/romaji only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Japanese Music — Installment 4: "
         "New Music, City Pop & the Idol Age (c. 1975-1995)")

FRAMING = (
    "Japan's bubble-era pop is having a second life -- decades on, the world is rediscovering it. In the "
    "late 1970s the folk boom matured into NEW MUSIC: sophisticated, self-written pop from Yumi "
    "Matsutoya ('Yuming') and Southern All Stars. From it grew CITY POP -- glossy, funk-and-AOR-inflected "
    "music of urban night and leisure (Tatsuro Yamashita, Mariya Takeuchi, Anri) whose 'Plastic Love' "
    "and 'Mayonaka no Door' became global YouTube and vaporwave sensations forty years later. Meanwhile "
    "YELLOW MAGIC ORCHESTRA pioneered synthpop and technopop, shaping electronic music worldwide, and "
    "Ryuichi Sakamoto became a global film composer. A vast IDOL boom (Pink Lady, Seiko Matsuda, Akina "
    "Nakamori, then the mass-group Onyanko Club) built the template for modern J-pop, while a late-80s "
    "BAND BOOM (Boowy, The Blue Hearts) put rock in the mainstream. Cross-links: American AOR/funk & "
    "disco feeding City Pop; YMO's global influence on electronic and hip-hop; the City Pop revival via "
    "the algorithm; the term 'J-pop' about to be coined (#5). Content note: the 1980s bubble economy and "
    "its 1991 burst frame this glittering era. Names transliterated (romaji). Region: Japan."
)

SECTIONS = [
    (
        "NEW MUSIC: THE SOPHISTICATED SINGER-SONGWRITERS (c. 1975-1985)",
        "The folk boom grew up into NEW MUSIC -- self-written, urbane, and apolitical, with lush "
        "arrangements. Yumi Matsutoya ('Yuming') became its poet laureate of young women's lives; "
        "Southern All Stars, led by Keisuke Kuwata, fused rock and pop with cheeky wit ('Ellie My Love' "
        "was covered by Ray Charles); and Off Course's 'Sayonara' defined the ballad.",
        [
            ("Rouge no Dengon (Message of Rouge)", "Yumi Matsutoya"),
            ("Itoshi no Ellie (Ellie My Love)", "Southern All Stars"),
            ("Sayonara", "Off Course"),
            ("Yumi Matsutoya / Yuming (the New Music poet laureate)", None),
            ("New Music (the sophisticated singer-songwriter pop)", None),
        ],
    ),
    (
        "CITY POP: THE SOUND OF THE BUBBLE (c. 1978-1988)",
        "City Pop was the glossy soundtrack of Japan's rising prosperity -- funk, boogie, and West-Coast "
        "AOR dressed in neon and cocktails, evoking a life of city nights, sports cars, and the sea. "
        "Tatsuro Yamashita's 'Ride on Time' is its sunlit archetype, with Taeko Onuki and Toshiki "
        "Kadomatsu close behind.",
        [
            ("Ride on Time", "Tatsuro Yamashita"),
            ("City Pop (the glossy urban AOR-funk sound)", None),
            ("Taeko Onuki (the City Pop sophisticate)", None),
            ("Toshiki Kadomatsu (the City Pop groove master)", None),
            ("Neon, leisure & the bubble optimism (City Pop's world)", None),
        ],
    ),
    (
        "THE CITY POP DIVAS & THE GLOBAL REVIVAL",
        "City Pop's afterlife is extraordinary. Mariya Takeuchi's 'Plastic Love' and Miki Matsubara's "
        "'Mayonaka no Door (Stay With Me)' -- modest hits in their day -- became viral global phenomena "
        "in the 2010s-20s via YouTube's algorithm, vaporwave, and future funk, winning millions of new "
        "fans worldwide. Cross-link: the internet rediscovers Japan.",
        [
            ("Plastic Love", "Mariya Takeuchi"),
            ("Mayonaka no Door (Stay With Me)", "Miki Matsubara"),
            ("Remember Summer Days", "Anri"),
            ("The global City Pop revival (YouTube & vaporwave)", None),
            ("Momoko Kikuchi & the City Pop divas", None),
        ],
    ),
    (
        "YMO & TECHNOPOP (c. 1978-1984)",
        "Yellow Magic Orchestra -- Ryuichi Sakamoto, Haruomi Hosono, and Yukihiro Takahashi -- pioneered "
        "synthpop and 'technopop', their crisp electronic hits ('Rydeen', 'Technopolis') influencing "
        "global electronic music, synthpop, and hip-hop. Sakamoto went on to a global film career, "
        "winning an Oscar and writing 'Merry Christmas Mr. Lawrence'. Cross-link: world electronic music.",
        [
            ("Rydeen", "Yellow Magic Orchestra"),
            ("Merry Christmas Mr. Lawrence", "Ryuichi Sakamoto"),
            ("Technopop (the YMO electronic revolution)", None),
            ("YMO's global influence (synthpop, electro & hip-hop)", None),
            ("Haruomi Hosono & Yukihiro Takahashi (the YMO core)", None),
        ],
    ),
    (
        "THE IDOL BOOM: SEIKO, AKINA & THE 80s (c. 1976-1988)",
        "The manufactured teen idol (aidoru) became a national industry. Pink Lady's dance smashes ('UFO') "
        "conquered the late 70s; then Seiko Matsuda, the eternal idol, reigned with bright hits like "
        "'Aoi Sangosho', locked in fabled rivalry with the cooler, huskier Akina Nakamori ('Desire'). "
        "The idol was now central to Japanese pop.",
        [
            ("UFO", "Pink Lady"),
            ("Aoi Sangosho (Blue Coral Reef)", "Seiko Matsuda"),
            ("Desire", "Akina Nakamori"),
            ("The aidoru system (the manufactured teen idol)", None),
            ("Momoe Yamaguchi (the 1970s idol queen)", None),
            ("Seiko versus Akina (the great idol rivalry)", None),
        ],
    ),
    (
        "ONYANKO CLUB & THE IDOL-GROUP TEMPLATE (c. 1985-1990)",
        "In the mid-80s Onyanko Club -- a large, rotating cast of ordinary-girl idols assembled on a TV "
        "show -- pioneered the mass idol group, the model that would later birth AKB48 and the whole "
        "J-pop idol machine. Kyoko Koizumi and Wink carried the solo/duo idol torch beside it.",
        [
            ("Onyanko Club (the mass idol-group template)", None),
            ("The idol-group model (precursor to AKB48)", None),
            ("Kyoko Koizumi (the 80s idol)", None),
            ("Wink (the idol duo)", None),
            ("The TV-made idol (manufacturing the star)", None),
        ],
    ),
    (
        "THE BAND BOOM (late 1980s)",
        "Rock bands surged into the mainstream in the late-80s 'Band Boom'. Boowy (Kyosuke Himuro and "
        "guitarist Tomoyasu Hotei) set an enduring template; The Blue Hearts' raw punk anthem 'Linda "
        "Linda' became a generational cry; and Princess Princess's 'Diamonds' topped the charts. Rock "
        "was now pop.",
        [
            ("Linda Linda", "The Blue Hearts"),
            ("Diamonds", "Princess Princess"),
            ("Boowy (the influential Band-Boom rock band)", None),
            ("Tomoyasu Hotei & the guitar-band template", None),
            ("Rebecca & The Checkers (the Band Boom)", None),
        ],
    ),
    (
        "THE BUBBLE, THE MACHINE & THE ROAD AHEAD (c. 1988-1995)",
        "As the industry professionalized, the TV-drama theme and ad tie-up became hit factories, and "
        "around 1988-90 the very term 'J-POP' was coined to brand it all. Content note: the bubble "
        "economy burst in 1991, shadowing the decade to come. Cross-link: the 90s J-pop explosion, the "
        "Komuro sound, and anime/Vocaloid (Installment 5).",
        [
            ("The term 'J-pop' is coined (c. 1988-1990)", None),
            ("The tie-up economy (TV drama & ad theme songs)", None),
            ("The bubble bursts (1991, content note)", None),
            ("Kayokyoku becomes J-pop (the transition)", None),
            ("Toward the 90s J-pop explosion (roads ahead)", None),
        ],
    ),
]

STEM = "japan_music_4_NEWMUSIC_CITYPOP_IDOLS"


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
