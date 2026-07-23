#!/usr/bin/env python3
"""Build East Asia: Japan, installment 5 (FINAL): Modern & Global -- J-pop, Anime, Vocaloid & the Wave.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/romaji only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Japanese Music — Installment 5 (Finale): "
         "Modern & Global — J-pop, Anime, Vocaloid & the Wave (c. 1995-present)")

FRAMING = (
    "The final chapter is Japan's most globally connected. The 1990s brought a J-POP explosion of "
    "million-sellers -- Tetsuya Komuro's production empire, the mega-bands B'z and Mr. Children, and, "
    "resetting everything, HIKARU UTADA, whose 'First Love' remains the best-selling album in Japanese "
    "history. Two homegrown worlds then carried Japanese music across the planet: ANIME and GAME music "
    "-- Joe Hisaishi's Studio Ghibli scores, the anisong industry, and video-game soundtracks that a "
    "generation everywhere grew up on -- and a fierce J-ROCK and VISUAL KEI scene (X Japan, L'Arc, "
    "Babymetal). Japan also invented a new kind of pop entirely with VOCALOID and the virtual idol "
    "Hatsune Miku, and industrialized the idol into the AKB48 era. Today Kenshi Yonezu, Yoasobi, and Ado "
    "top global charts on the back of anime and streaming, while the City Pop of the 1980s enjoys a "
    "worldwide second life. Cross-links: Western R&B/rock/metal in J-pop; anime and games as Japan's "
    "great cultural export; the City Pop revival. This installment also builds the Japan region master. "
    "Content note: the Johnny's agency abuse revelations (2023) are kept factual and brief. Names "
    "transliterated (romaji). Region: Japan."
)

SECTIONS = [
    (
        "THE 90s J-POP EXPLOSION & THE KOMURO EMPIRE (c. 1994-1999)",
        "The 1990s were J-pop's commercial peak, and producer Tetsuya Komuro was its king -- his "
        "electronic dance-pop for globe ('Departures'), TRF, and especially Namie Amuro ('Can You "
        "Celebrate?') sold in the millions. The CD single became a national obsession and the term "
        "'J-pop' triumphed.",
        [
            ("Departures", "globe"),
            ("Can You Celebrate?", "Namie Amuro"),
            ("Tetsuya Komuro (the 90s hit-machine producer)", None),
            ("TRF & the Komuro dance-pop sound", None),
            ("The million-selling CD era (90s J-pop peak)", None),
        ],
    ),
    (
        "HIKARU UTADA & THE R&B REVOLUTION (c. 1998-2005)",
        "In 1998 the teenage Hikaru Utada's 'Automatic' arrived -- a sophisticated, bilingual R&B unlike "
        "anything in J-pop -- and the album 'First Love' (1999) became the best-selling record in "
        "Japanese history. Utada reset the sound and standard of Japanese pop, later reaching global "
        "gamers through Kingdom Hearts.",
        [
            ("Automatic", "Hikaru Utada"),
            ("First Love", "Hikaru Utada"),
            ("The R&B revolution in J-pop (Utada's reset)", None),
            ("Hikari (the Kingdom Hearts theme, global reach)", None),
            ("Bilingual, self-written pop (the Utada standard)", None),
        ],
    ),
    (
        "THE MEGA-BANDS OF THE 90s",
        "Rock and pop bands sold on a colossal scale. B'z became the best-selling act in Japanese "
        "history with hard-rock anthems like 'Ultra Soul'; Mr. Children ('Tomorrow Never Knows') were "
        "the thoughtful giants; Spitz's 'Robinson' was a gentle classic; and Glay, L'Arc-en-Ciel, and "
        "ZARD filled stadiums during the CD boom's peak.",
        [
            ("Ultra Soul", "B'z"),
            ("Tomorrow Never Knows", "Mr. Children"),
            ("Robinson", "Spitz"),
            ("Glay & ZARD (the 90s band-pop giants)", None),
            ("The CD-boom stadium bands", None),
        ],
    ),
    (
        "STUDIO GHIBLI & JOE HISAISHI",
        "Few sounds are more globally beloved than Joe Hisaishi's scores for Studio Ghibli. His warm, "
        "wistful orchestral melodies -- from 'My Neighbor Totoro' to 'One Summer's Day' (Spirited Away) "
        "and Howl's 'Merry-Go-Round of Life' -- carried Japanese music to every corner of the world. "
        "Cross-link: anime as Japan's great cultural ambassador.",
        [
            ("One Summer's Day (Spirited Away)", "Joe Hisaishi"),
            ("Joe Hisaishi (the Studio Ghibli composer)", None),
            ("Merry-Go-Round of Life (Howl's Moving Castle)", None),
            ("The emotional-orchestral anime film sound", None),
            ("Ghibli music goes global (the world sings along)", None),
        ],
    ),
    (
        "ANISONG & GAME MUSIC",
        "Two industries made Japanese music globally native. ANISONG -- anime theme songs -- became a "
        "juggernaut (Yoko Kanno's jazzy 'Tank!' for Cowboy Bebop; LiSA's 'Gurenge' for Demon Slayer), "
        "and video-game composers Koji Kondo (Mario, Zelda) and Nobuo Uematsu (Final Fantasy) wrote "
        "melodies a whole planet knows by heart. Cross-link: games & anime as a global soundtrack.",
        [
            ("Tank!", "Yoko Kanno"),
            ("Gurenge", "LiSA"),
            ("Anisong (the anime theme-song industry)", None),
            ("Koji Kondo (the Super Mario & Zelda themes)", None),
            ("Nobuo Uematsu (the Final Fantasy composer)", None),
        ],
    ),
    (
        "J-ROCK & VISUAL KEI",
        "Japan built a fierce rock world. X Japan (led by Yoshiki) invented VISUAL KEI -- theatrical, "
        "androgynous, and heavy -- with anthems like 'Kurenai', followed by Luna Sea, L'Arc-en-Ciel, "
        "and Dir En Grey; and modern acts went global, from One Ok Rock's stadium rock to Babymetal's "
        "metal-idol fusion ('Gimme Chocolate!!'). Cross-link: Western metal and rock, remade.",
        [
            ("Kurenai", "X Japan"),
            ("Gimme Chocolate!!", "Babymetal"),
            ("Visual Kei (the theatrical rock movement)", None),
            ("Luna Sea & Dir En Grey (the Visual Kei wave)", None),
            ("One Ok Rock (modern J-rock goes global)", None),
        ],
    ),
    (
        "VOCALOID & HATSUNE MIKU (c. 2007-present)",
        "Japan invented a new pop paradigm: VOCALOID, singing-synthesizer software whose turquoise-"
        "haired avatar HATSUNE MIKU became a virtual idol with sold-out holographic concerts. A vast "
        "crowdsourced producer culture arose (supercell's 'Melt'; the producer 'Hachi' who became "
        "Kenshi Yonezu), redefining who makes pop and how. Cross-link: a wholly new music culture.",
        [
            ("Melt", "supercell"),
            ("Hatsune Miku (the Vocaloid virtual idol)", None),
            ("Vocaloid (the singing-synthesizer pop culture)", None),
            ("The Vocaloid producer scene (crowdsourced pop)", None),
            ("Hatsune Miku's holographic concerts", None),
        ],
    ),
    (
        "THE MODERN IDOL ERA",
        "The idol became a mass industry. AKB48 built a huge rotating-cast empire of handshake events "
        "and fan elections ('Heavy Rotation'), with Nogizaka46 and Momoiro Clover Z beside it, while the "
        "Johnny's agency ruled male idols for decades (SMAP's near-national-anthem 'Sekai ni Hitotsu "
        "Dake no Hana', Arashi). Content note: Johnny's decades of abuse were exposed in 2023 -- kept "
        "factual and brief.",
        [
            ("Heavy Rotation", "AKB48"),
            ("Sekai ni Hitotsu Dake no Hana (The One and Only Flower)", "SMAP"),
            ("AKB48 & the mega-idol-group empire", None),
            ("Nogizaka46 & Momoiro Clover Z (the modern idols)", None),
            ("The Johnny's boy-band machine (Arashi; the 2023 reckoning)", None),
        ],
    ),
    (
        "THE GLOBAL WAVE & THE THROUGH-LINE (c. 2016-present)",
        "Today Japanese music tops global charts on its own terms: Kenshi Yonezu's 'Lemon', Yoasobi's "
        "'Idol', and Ado's 'New Genesis' ride anime and streaming worldwide, and 1980s City Pop enjoys "
        "a viral second life. Five installments span gagaku to the algorithm -- an art of ma and timbre "
        "become a global pop powerhouse. Cross-links: the East Asia family (Korea ahead); the worldwide "
        "anime audience.",
        [
            ("Lemon", "Kenshi Yonezu"),
            ("Idol", "Yoasobi"),
            ("New Genesis (Shinjidai)", "Ado"),
            ("Anime & streaming drive J-music global", None),
            ("From gagaku to the algorithm (the Japanese arc closes)", None),
        ],
    ),
]

STEM = "japan_music_5_JPOP_ANIME_VOCALOID_GLOBAL"


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
