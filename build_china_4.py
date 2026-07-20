#!/usr/bin/env python3
"""Build East Asia: China, installment 4: Cantopop & Mandopop (HK/Taiwan).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/pinyin only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Chinese Music — Installment 4: "
         "Cantopop & Mandopop — the Gangtai Golden Age (c. 1970-2000)")

FRAMING = (
    "While the mainland fell silent, Chinese pop bloomed spectacularly in Hong Kong and Taiwan -- the "
    "'gangtai' world that inherited exiled Shanghai shidaiqu and remade it for a new era. Its queen was "
    "TERESA TENG (Deng Lijun) of Taiwan, whose impossibly tender voice became, via smuggled cassettes, "
    "the sound the whole mainland secretly loved -- 'by day Deng Xiaoping rules China, by night Deng "
    "Lijun rules China'. In Hong Kong, Sam Hui made Cantonese vernacular pop -- CANTOPOP -- and a golden "
    "age followed: Leslie Cheung and Anita Mui, the manufactured-idol 'Four Heavenly Kings', and the "
    "great rock band Beyond. In Taiwan, a campus-folk movement bred singer-songwriters like Lo Ta-yu "
    "and a line of ballad divas, culminating in the genre-bending Faye Wong. Bound by Mandarin and "
    "Cantonese, karaoke and TV, this pan-Chinese pop reunited a scattered culture in song. Cross-links: "
    "the shidaiqu it descends from (#3); the mainland's own scene & rock (#5); the Japanese idol/enka "
    "influence (Japan survey). Content note: Leslie Cheung, Anita Mui, Teresa Teng, and Beyond's Wong Ka "
    "Kui all died young -- kept in view. Names transliterated (pinyin); HK/Taiwan flagged. Region: China "
    "(Hong Kong & Taiwan)."
)

SECTIONS = [
    (
        "TERESA TENG: THE VOICE THAT CONQUERED CHINA (c. 1970-1995)",
        "Teresa Teng of Taiwan was the most beloved Chinese singer of the century. Her gentle, intimate "
        "voice on 'The Moon Represents My Heart' and 'Sweet Honey' spread across every Chinese "
        "community -- and, on smuggled cassettes, into a mainland starved of soft feeling. Content note: "
        "she died suddenly in 1995, at 42, and was mourned across the Chinese-speaking world.",
        [
            ("Yueliang Daibiao Wo De Xin (The Moon Represents My Heart)", "Teresa Teng"),
            ("Tian Mi Mi (Sweet Honey)", "Teresa Teng"),
            ("Teresa Teng (the pan-Chinese queen of song, Taiwan)", None),
            ("The smuggled cassettes (Teng reaches the mainland)", None),
            ("The two Dengs (by day Xiaoping, by night Lijun)", None),
        ],
    ),
    (
        "THE BIRTH OF CANTOPOP: SAM HUI & THE 1970s",
        "Hong Kong pop had sung in Mandarin and English until Sam Hui began writing witty, streetwise "
        "songs in everyday CANTONESE around 1974 -- inventing modern Cantopop. Roman Tam, the 'godfather "
        "of Cantopop', and the booming TVB television theme songs cemented Cantonese as the language of "
        "Hong Kong's own pop. Region flag: Hong Kong.",
        [
            ("Sam Hui (the father of Cantopop)", None),
            ("Cantopop is born (Cantonese vernacular pop, 1974)", None),
            ("Roman Tam (the godfather of Cantopop)", None),
            ("The TVB theme song (television & Cantopop)", None),
            ("Cantonese becomes Hong Kong's pop language", None),
        ],
    ),
    (
        "THE 1980s CANTOPOP GOLDEN AGE",
        "Hong Kong's 1980s were a pop-and-film golden age. Leslie Cheung ('Monica') and Anita Mui -- the "
        "ever-transforming 'Madonna of Asia' -- were its dazzling idols, locked with Alan Tam in fierce "
        "chart rivalry, and inseparable from the Hong Kong cinema boom. Content note: both Leslie and "
        "Anita died in 2003, a devastating year for Cantopop.",
        [
            ("Monica", "Leslie Cheung"),
            ("Anita Mui (the Madonna of Asia)", None),
            ("Leslie Cheung (the Cantopop-and-film idol)", None),
            ("Alan Tam (the 80s chart rival)", None),
            ("Cantopop & the Hong Kong cinema boom", None),
        ],
    ),
    (
        "THE FOUR HEAVENLY KINGS (1990s)",
        "1990s Cantopop crowned the 'Four Heavenly Kings' (Sei Dai Tin Wong): Jacky Cheung, the 'God of "
        "Songs', whose 'Goodbye Kiss' is a karaoke eternal; the film-star Andy Lau; and the idols Leon "
        "Lai and Aaron Kwok. Manufactured, adored, and everywhere, they were the commercial peak of "
        "Hong Kong pop. Region flag: Hong Kong.",
        [
            ("Wen Bie (Goodbye Kiss)", "Jacky Cheung"),
            ("The Four Heavenly Kings (Sei Dai Tin Wong, 1990s)", None),
            ("Jacky Cheung (the God of Songs)", None),
            ("Andy Lau (the film-star idol)", None),
            ("Leon Lai & Aaron Kwok (the pop idols)", None),
        ],
    ),
    (
        "BEYOND & HONG KONG ROCK",
        "Against the manufactured idols stood Beyond -- Hong Kong's greatest rock band -- whose anthem "
        "'Boundless Oceans, Vast Skies' carried real social conscience and a longing for freedom. Their "
        "leader Wong Ka Kui died in an accident in 1993, but their songs remain protest and comfort "
        "across the Chinese world. Region flag: Hong Kong.",
        [
            ("Hai Kuo Tian Kong (Boundless Oceans, Vast Skies)", "Beyond"),
            ("Beyond (Hong Kong's greatest rock band)", None),
            ("Wong Ka Kui (Beyond's leader, d. 1993)", None),
            ("Cantopop rock & social conscience", None),
            ("Songs of freedom & idealism (the Beyond legacy)", None),
        ],
    ),
    (
        "TAIWAN: CAMPUS FOLK & THE SINGER-SONGWRITERS (c. 1975-1995)",
        "Taiwan took a different road. The 1970s 'sing our own songs' campus-folk movement rejected "
        "imported pop for homegrown acoustic songs, breeding singer-songwriters -- above all Lo Ta-yu, "
        "the sharp-tongued 'godfather' whose 'Childhood' and social-critique anthems defined a "
        "generation, plus the poetic Chyi Yu ('The Olive Tree') and producer Jonathan Lee. Region flag: "
        "Taiwan.",
        [
            ("Tong Nian (Childhood)", "Lo Ta-yu"),
            ("Ganlanshu (The Olive Tree)", "Chyi Yu"),
            ("The campus folk movement (sing our own songs, Taiwan)", None),
            ("Lo Ta-yu (the godfather of Mandopop)", None),
            ("Jonathan Lee (the singer-songwriter-producer)", None),
        ],
    ),
    (
        "THE MANDOPOP DIVAS & FAYE WONG (c. 1985-2000)",
        "Mandopop matured into a diva's art -- the ballad queens Tsai Chin and Sarah Chen, the "
        "aboriginal Taiwanese superstar A-Mei, and, transcending all categories, Faye Wong: a "
        "Beijing-born, Hong Kong-based, dream-pop-influenced original whose 'Red Bean' and her turn in "
        "Chungking Express made her Asia's coolest voice.",
        [
            ("Hong Dou (Red Bean)", "Faye Wong"),
            ("Faye Wong (the genre-bending pan-Chinese diva)", None),
            ("A-Mei (the aboriginal Taiwanese superstar)", None),
            ("Tsai Chin & Sarah Chen (the Mandopop ballad divas)", None),
            ("The pan-Chinese diva (HK-Taiwan-mainland)", None),
        ],
    ),
    (
        "THE KARAOKE ERA & THE PAN-CHINESE MARKET (c. 1985-2000)",
        "KTV (karaoke) turned every hit into a communal ritual and bound the whole Chinese-speaking "
        "world -- Hong Kong, Taiwan, the reopening mainland, and the Southeast Asian diaspora -- into a "
        "single gangtai market. Cross-link: this pop flooded back into the mainland as it opened up, "
        "setting the stage for China's own scene and rock (Installment 5).",
        [
            ("KTV / karaoke culture (the communal hit)", None),
            ("The gangtai market (HK-Taiwan-mainland-diaspora)", None),
            ("The music video & the TV pop era", None),
            ("Gangtai pop floods the reopening mainland", None),
            ("Toward the mainland's own pop & rock (roads ahead)", None),
        ],
    ),
]

STEM = "china_music_4_CANTOPOP_MANDOPOP"


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
