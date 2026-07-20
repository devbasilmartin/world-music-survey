#!/usr/bin/env python3
"""Build East Asia: China, installment 2: Opera's Golden Age & the Road to the Republic.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/pinyin only. Dedup is by TITLE only.
NOTE: do NOT reuse a bare "Mei Lanfang (...)" title (collides with #1).
"""

TITLE = ("The Story of Chinese Music — Installment 2: "
         "Opera's Golden Age & the Road to the Republic (c. 1850-1949)")

FRAMING = (
    "As the Qing empire crumbled and a modern nation struggled to be born, Chinese music lived a double "
    "life. On one hand, traditional PEKING OPERA reached its dazzling golden age -- the 'four great "
    "dan', led by MEI LANFANG, became superstars, and Mei carried the art to America and the USSR, "
    "astonishing Brecht and Stanislavski. On the other, revolution and the NEW CULTURE MOVEMENT (May "
    "Fourth, 1919) drove reformers to modernize and Westernize: the SCHOOL-SONG movement (Li Shutong's "
    "immortal 'Song Bie') taught a new kind of song, the first conservatories and modern composers "
    "(Xiao Youmei, Zhao Yuanren, Huang Zi) arrived, Liu Tianhua dragged the erhu into the concert hall, "
    "and as war with Japan loomed, NIE ER and XIAN XINGHAI forged patriotic anthems -- Nie Er's 'March "
    "of the Volunteers' would become the national anthem. Beneath it all, Li Jinhui was inventing "
    "Chinese pop in Shanghai (the story of #3). Cross-links: Western classical music entering China; "
    "Japanese school-song models; the coming Shanghai jazz age. Content notes: the fall of the Qing, "
    "the warlord era, and the Japanese invasion (1937-45) are kept in view. Names transliterated "
    "(pinyin). Region: China."
)

SECTIONS = [
    (
        "PEKING OPERA'S GOLDEN AGE (c. 1850-1937)",
        "Peking opera reached its peak as China's great popular art. Early masters like Tan Xinpei "
        "(among the first Chinese ever recorded) set the standard, and the 'four great dan' -- Mei "
        "Lanfang, Cheng Yanqiu, Shang Xiaoyun, and Xun Huisheng -- became national idols. Signature "
        "operas like 'Farewell My Concubine' defined the era's glamour.",
        [
            ("The four great dan (Mei Lanfang, Cheng Yanqiu, Shang Xiaoyun, Xun Huisheng)", None),
            ("Farewell My Concubine (Bawang Bie Ji, the signature opera)", None),
            ("Tan Xinpei (early laosheng master, among the first recorded)", None),
            ("The Mei Lanfang world tours (US 1930, USSR 1935)", None),
            ("The Peking opera star system (idols of the age)", None),
            ("The Drunken Beauty (Guifei Zui Jiu, a famous dan role)", None),
        ],
    ),
    (
        "THE REGIONAL OPERA WORLD MATURES",
        "Beside Peking opera, hundreds of local operas flourished. Yue opera from Shaoxing became a "
        "lyrical, largely all-female form; Yu opera boomed in Henan; Sichuan opera dazzled with its "
        "face-changing (bianlian) magic; and the gentle Huangmei opera spread from Anhui. Each region "
        "sang its own dialect and melody.",
        [
            ("Yue opera (Shaoxing, the lyrical women's opera)", None),
            ("Yu opera (the Henan regional form)", None),
            ("Sichuan opera & face-changing (bianlian)", None),
            ("Huangmei opera (the gentle Anhui form)", None),
            ("The hundreds of regional operas (dialect & melody)", None),
        ],
    ),
    (
        "THE FALL OF THE QING & THE NEW CULTURE MOVEMENT (c. 1911-1925)",
        "The 1911 revolution ended two millennia of empire, and the New Culture and May Fourth (1919) "
        "movements demanded a modern China of 'science and democracy'. Reformers attacked the old arts "
        "as feudal and looked to the West -- setting music, like everything, on a course of radical, "
        "sometimes painful, modernization.",
        [
            ("The fall of the Qing & the Republic (1911-12)", None),
            ("The May Fourth / New Culture Movement (1919)", None),
            ("Science, democracy & the call to modernize music", None),
            ("Western music enters China (missionaries & military bands)", None),
            ("The debate over tradition versus reform", None),
        ],
    ),
    (
        "THE SCHOOL-SONG MOVEMENT & LI SHUTONG (c. 1900-1920)",
        "Modernizers borrowed the Japanese model of xuetang yuege -- 'school songs' -- setting new "
        "Chinese lyrics (patriotism, science, nature) to Western or Japanese melodies for a new "
        "generation. Its masterpiece is Li Shutong's 'Song Bie' (Farewell), a melody of aching beauty "
        "that remains one of China's most beloved songs.",
        [
            ("Song Bie (Farewell)", "Li Shutong"),
            ("The school-song movement (xuetang yuege)", None),
            ("Li Shutong (the monk-artist behind Farewell)", None),
            ("Shen Xingong (a school-song pioneer)", None),
            ("Western melodies with Chinese lyrics (the new song)", None),
        ],
    ),
    (
        "THE FIRST MODERN COMPOSERS & THE CONSERVATORY (c. 1920-1937)",
        "China built a Western-style art-music world almost from scratch. Xiao Youmei founded the "
        "Shanghai Conservatory (1927); Zhao Yuanren (the linguist Y.R. Chao) wrote the first great "
        "Chinese art song, 'How Could I Not Miss Her'; and Huang Zi composed refined art songs and the "
        "first Chinese cantata. A national concert music was born.",
        [
            ("Jiao Wo Ru He Bu Xiang Ta (How Could I Not Miss Her)", "Zhao Yuanren"),
            ("Xiao Youmei (founder of the Shanghai Conservatory, 1927)", None),
            ("Huang Zi (the refined art-song composer)", None),
            ("The birth of Chinese art song (Western form, Chinese voice)", None),
            ("Western classical music takes root in China", None),
        ],
    ),
    (
        "NATIONAL MUSIC (GUOYUE) & THE MODERN ERHU (c. 1920-1940)",
        "A parallel movement modernized the traditional instruments themselves. Liu Tianhua reformed the "
        "erhu -- standardizing it, writing concert pieces, and bringing it into the conservatory -- and "
        "the guoyue ('national music') movement built the first modern Chinese orchestras. In the south, "
        "Cantonese music (Guangdong yinyue) charmed with pieces like Lu Wencheng's 'Autumn Moon on Calm "
        "Lake'.",
        [
            ("Ping Hu Qiu Yue (Autumn Moon on Calm Lake)", "Lu Wencheng"),
            ("Liu Tianhua (the erhu reformer)", None),
            ("The guoyue / national-music movement", None),
            ("The first modern Chinese orchestra", None),
            ("Cantonese music (Guangdong yinyue, the southern light style)", None),
        ],
    ),
    (
        "MUSIC & NATIONAL SALVATION: NIE ER & XIAN XINGHAI (c. 1930-1945)",
        "As Japan invaded, music became a weapon of resistance. Nie Er wrote fierce mass songs before "
        "his early death, including 'March of the Volunteers' -- later the national anthem; and Xian "
        "Xinghai composed the mighty 'Yellow River Cantata', a symbol of wartime defiance. Content note: "
        "the Japanese invasion (1937-45) and its horrors frame this music.",
        [
            ("March of the Volunteers (Yiyongjun Jinxingqu)", "Nie Er"),
            ("Yellow River Cantata (Huang He Da Hechang)", "Xian Xinghai"),
            ("The mass-song movement (music for resistance)", None),
            ("Nie Er (the anthem composer, dead at 23)", None),
            ("Music against the Japanese invasion (national salvation song)", None),
        ],
    ),
    (
        "TOWARD SHANGHAI & THE ROADS AHEAD (c. 1927-1949)",
        "Even as anthems rang out, a very different sound was rising in cosmopolitan Shanghai: Li "
        "Jinhui, the 'father of Chinese popular music', fused folk melody with jazz to create shidaiqu, "
        "and his 'Drizzle' (Mao Mao Yu) is often called China's first pop song. The Shanghai jazz age, "
        "and the 1949 revolution that would sweep it away, are the story of Installment 3.",
        [
            ("Mao Mao Yu (Drizzle, often called China's first pop song)", None),
            ("Li Jinhui (the father of Chinese popular music)", None),
            ("The birth of shidaiqu (folk melody meets jazz)", None),
            ("Cosmopolitan Shanghai (the coming jazz age)", None),
            ("The 1949 divide (revolution & the roads ahead)", None),
        ],
    ),
]

STEM = "china_music_2_OPERA_GOLDEN_AGE_REPUBLIC"


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
