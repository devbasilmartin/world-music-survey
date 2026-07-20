#!/usr/bin/env python3
"""Build East Asia: China, installment 3: Shanghai Shidaiqu & the Mao Era.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/pinyin only. Dedup is by TITLE only.
NOTE: do NOT reuse "Li Jinhui", "Mao Mao Yu", "The birth of shidaiqu", or "Yellow River Cantata"
(they collide with #2).
"""

TITLE = ("The Story of Chinese Music — Installment 3: "
         "Shanghai Shidaiqu & the Mao Era (c. 1927-1978)")

FRAMING = (
    "Few musical stories swing so violently. In 1930s-40s SHANGHAI -- 'the Paris of the East' -- a "
    "glittering pop music called SHIDAIQU fused Chinese folk melody with Hollywood jazz and cabaret, "
    "and ZHOU XUAN's 'Golden Voice' made her the biggest star in China. The 'seven great singing stars' "
    "ruled the dance halls and the silver screen; Yao Lee's 'Rose, Rose, I Love You' even became an "
    "American hit. Then, in 1949, the Communist victory branded shidaiqu decadent 'YELLOW MUSIC' and "
    "banned it; the industry and its stars fled to Hong Kong (seeding Mandopop, #4), while on the "
    "mainland a new music of the masses arose -- 'The East Is Red', revolutionary choirs, and a "
    "'national style' concert music (the beloved 'Butterfly Lovers' concerto). The CULTURAL REVOLUTION "
    "(1966-76) then narrowed the nation's entire soundtrack to eight state-approved 'model works', while "
    "traditional music was smashed and musicians persecuted. Cross-links: shidaiqu fleeing to Hong "
    "Kong/Taiwan (Cantopop & Mandopop, #4); Soviet mass-song models; the reform-era thaw and rock (#5). "
    "Content notes: the ban, the Cultural Revolution, and the persecution and deaths of musicians are "
    "kept with care. Names transliterated (pinyin). Region: China (mainland, with the Hong Kong exodus)."
)

SECTIONS = [
    (
        "THE SHANGHAI JAZZ AGE & SHIDAIQU (c. 1927-1940)",
        "Cosmopolitan Shanghai's ballrooms and film studios birthed China's first true pop: shidaiqu "
        "('songs of the era'), a sophisticated blend of Chinese pentatonic melody, Hollywood jazz "
        "orchestration, and cabaret glamour, cut on Pathe and EMI records. It was the sound of a "
        "modern, decadent, doomed metropolis.",
        [
            ("The Shanghai shidaiqu sound (cabaret jazz + Chinese melody)", None),
            ("The Shanghai jazz age (the Paramount & the ballrooms)", None),
            ("Pathe & EMI Shanghai (the record industry)", None),
            ("The sing-song girls & the cabaret world", None),
            ("Film & pop song intertwined (Shanghai cinema)", None),
        ],
    ),
    (
        "ZHOU XUAN & THE GOLDEN VOICE (c. 1934-1949)",
        "Zhou Xuan was the era's supreme star -- 'the Golden Voice' -- an actress-singer whose delicate "
        "tone defined shidaiqu. 'Shanghai Nights', the 'Song of a Wandering Songstress' from the film "
        "Street Angel (1937), and 'When Will You Return' are eternal classics. Content note: her life "
        "ended tragically, in mental illness, at 39.",
        [
            ("Ye Shanghai (Shanghai Nights)", "Zhou Xuan"),
            ("Tian Ya Ge Nu (Song of a Wandering Songstress)", "Zhou Xuan"),
            ("He Ri Jun Zai Lai (When Will You Return)", "Zhou Xuan"),
            ("Zhou Xuan (the Golden Voice of Shanghai)", None),
            ("Street Angel (1937, the classic film & its songs)", None),
        ],
    ),
    (
        "THE SEVEN GREAT SINGING STARS (c. 1930-1949)",
        "A galaxy of divas ruled shidaiqu. Yao Lee's 'Rose, Rose, I Love You' crossed the Pacific to "
        "become a 1951 American pop hit; Bai Guang purred in a sultry contralto; Bai Hong, Wu Yingyin, "
        "and Gong Qiuxia each had their fans. Li Xianglan sang 'Ye Lai Xiang' -- content note: she was "
        "the Japanese actress Yoshiko Yamaguchi, passing as Chinese in occupied China.",
        [
            ("Mei Gui Mei Gui Wo Ai Ni (Rose Rose I Love You)", "Yao Lee"),
            ("Ye Lai Xiang (Fragrance of the Night)", "Li Xianglan"),
            ("Bai Guang (the sultry contralto of shidaiqu)", None),
            ("The seven great singing stars (the shidaiqu divas)", None),
            ("Wu Yingyin & Gong Qiuxia (more of the golden voices)", None),
        ],
    ),
    (
        "THE 1949 DIVIDE: 'YELLOW MUSIC' BANNED",
        "The Communist victory in 1949 condemned shidaiqu as bourgeois, pornographic 'yellow music' and "
        "banned it outright. The Shanghai record industry and its stars fled to British Hong Kong, "
        "carrying Mandarin pop with them -- where it would flourish and seed Mandopop and Cantopop "
        "(Installment 4). On the mainland, an entire musical world went silent overnight.",
        [
            ("Yellow music banned (huangse yinyue, 1949)", None),
            ("The exodus to Hong Kong (shidaiqu flees south)", None),
            ("Mandarin pop's Hong Kong refuge (seeding Mandopop)", None),
            ("A pop world silenced on the mainland", None),
            ("The two Chinas of song (mainland vs the emigres)", None),
        ],
    ),
    (
        "THE MASS SONG & 'THE EAST IS RED' (c. 1949-1966)",
        "New China built a new soundtrack: revolutionary MASS SONGS, huge amateur choirs, and "
        "Soviet-influenced orchestral works celebrating the Party and the people. 'The East Is Red' -- a "
        "folk tune reworked into a hymn to Mao -- became a national anthem in all but name, alongside "
        "'Ode to the Motherland' and the Yan'an-era 'Nanniwan'.",
        [
            ("Dong Fang Hong (The East Is Red, the Mao hymn)", None),
            ("Ge Chang Zuguo (Ode to the Motherland)", None),
            ("Nanniwan (the beloved Yan'an-era song)", None),
            ("Revolutionary choirs of New China (the mass-singing culture)", None),
            ("Soviet influence on Chinese music (the 1950s)", None),
        ],
    ),
    (
        "THE NATIONAL STYLE: CONCERT MUSIC OF THE 1950s",
        "Conservatory composers forged a 'national style', fusing Western classical form with Chinese "
        "melody, opera, and folk. Its masterpiece is the 'Butterfly Lovers Violin Concerto' (1959) -- "
        "based on the tragic Liang Zhu legend and Yue opera -- still the most beloved Chinese orchestral "
        "work, alongside new virtuoso pieces for the traditional instruments.",
        [
            ("The Butterfly Lovers Violin Concerto (Liang Zhu)", "He Zhanhao & Chen Gang"),
            ("The national style (Western form, Chinese melody)", None),
            ("New concert works for erhu, pipa & guzheng", None),
            ("The conservatories of New China", None),
            ("Chinese orchestral music (the 1950s flowering)", None),
        ],
    ),
    (
        "THE CULTURAL REVOLUTION & THE MODEL WORKS (1966-1976)",
        "During the Cultural Revolution, Jiang Qing narrowed the nation's entire permitted music to "
        "eight 'model works' (yangbanxi) -- revolutionary operas and ballets like 'The Red Detachment "
        "of Women', 'Taking Tiger Mountain by Strategy', and 'The Red Lantern' -- plus the 'Yellow "
        "River Piano Concerto'. Content note: nearly all other music was banned, traditional culture "
        "smashed, and countless musicians persecuted, imprisoned, or driven to death.",
        [
            ("Yellow River Piano Concerto", "Yin Chengzong"),
            ("The Red Detachment of Women (Hongse Niangzijun, the model ballet)", None),
            ("Taking Tiger Mountain by Strategy (the model opera)", None),
            ("The Red Lantern (Hong Deng Ji, the model opera)", None),
            ("The eight model works (yangbanxi)", None),
            ("Music smashed & musicians persecuted (content note)", None),
        ],
    ),
    (
        "THE THAW & THE ROADS AHEAD (1976-1978)",
        "Mao's death in 1976 and the fall of the Gang of Four ended the Cultural Revolution. The bans "
        "lifted, old recordings crept back, and the reform era dawned -- setting the stage for "
        "Taiwan/Hong Kong pop to flood in and, soon, for Chinese rock to erupt (Cui Jian, Installment "
        "5). Cross-links: the returning shidaiqu; Cantopop/Mandopop (#4); mainland rock (#5).",
        [
            ("The end of the Cultural Revolution (1976)", None),
            ("The bans lift & old songs return (the thaw)", None),
            ("The reform era dawns (music reopens)", None),
            ("Taiwan & Hong Kong pop seep in (roads ahead)", None),
            ("Toward Chinese rock (Cui Jian ahead)", None),
        ],
    ),
]

STEM = "china_music_3_SHIDAIQU_MAO_ERA"


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
