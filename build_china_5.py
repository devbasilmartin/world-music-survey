#!/usr/bin/env python3
"""Build East Asia: China, installment 5 (FINAL): The Mainland Finds Its Voice & Today.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/pinyin only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Chinese Music — Installment 5 (Finale): "
         "The Mainland Finds Its Voice & Today (c. 1986-present)")

FRAMING = (
    "As China opened after the Cultural Revolution, the mainland grew a pop and rock scene of its own. "
    "In 1986 CUI JIAN roared 'Nothing to My Name' -- the first Chinese rock song and the anthem of a "
    "restless reform-era generation. A gritty 1990s Beijing underground followed (Tang Dynasty, Dou "
    "Wei, He Yong), even as rock stayed marginal and watched. Then, from Taiwan, JAY CHOU reinvented "
    "Mandopop around the millennium -- blending R&B and hip-hop with a proud 'Chinese style' "
    "(zhongguofeng) -- and led a glittering pan-Chinese C-POP industry (Jolin Tsai, Wang Leehom, "
    "Stefanie Sun, Mayday). The 2010s brought a folk-and-indie revival (Zhao Lei's 'Chengdu'), a "
    "hip-hop explosion via the show 'The Rap of China' (Higher Brothers, GAI), and a streaming/short-"
    "video age ruled by Douyin. From guqin to algorithm, China's musical century comes full circle. "
    "Cross-links: HK/Taiwan gangtai pop (#4); Western rock/R&B/hip-hop (US survey); the East Asia "
    "neighbors (Japan/Korea). This installment also builds the China region master. Content notes: the "
    "1989 context around Cui Jian, censorship, and banned artists are kept factual and brief. Names "
    "transliterated (pinyin). Region: China (mainland, with pan-Chinese C-pop)."
)

SECTIONS = [
    (
        "CUI JIAN & THE BIRTH OF CHINESE ROCK (1986-1990)",
        "In 1986 Cui Jian took the stage in a Beijing concert and sang 'Nothing to My Name' -- raw, "
        "electric, and full of a longing the reform generation had never heard voiced. It became the "
        "first Chinese rock song and an anthem of the era. Content note: it echoed powerfully in the "
        "spring of 1989; the context is kept factual and brief.",
        [
            ("Yi Wu Suo You (Nothing to My Name)", "Cui Jian"),
            ("Cui Jian (the father of Chinese rock)", None),
            ("A Piece of Red Cloth (Yi Kuai Hong Bu, a Cui Jian anthem)", None),
            ("The reform-era youth find a voice (mainland rock is born)", None),
            ("The raw Beijing rock sound (1980s)", None),
        ],
    ),
    (
        "THE 1990s BEIJING ROCK UNDERGROUND",
        "A gritty rock underground grew in 1990s Beijing, gathered around the Magic Stone / Rock Records "
        "labels. Tang Dynasty forged Chinese heavy metal; Dou Wei made moody art-rock; He Yong provoked "
        "with 'Garbage Dump'; and Zheng Jun's 'Return to Lhasa' soared. Content note: rock remained "
        "commercially marginal and closely watched.",
        [
            ("Meng Hui Tang Chao (A Dream Return to Tang Dynasty)", "Tang Dynasty"),
            ("Hui Dao Lasa (Return to Lhasa)", "Zheng Jun"),
            ("Dou Wei (the art-rock innovator)", None),
            ("He Yong & Garbage Dump (the provocateur)", None),
            ("Black Panther (Hei Bao, the rock band)", None),
            ("The Magic Stone / Rock Records scene", None),
        ],
    ),
    (
        "JAY CHOU & THE MANDOPOP REVOLUTION (c. 2000-2010)",
        "Around the millennium, Taiwan's Jay Chou remade Mandopop. Fusing R&B, hip-hop, and classical "
        "flourishes with a proud 'Chinese style' (zhongguofeng) and his famously mumbled delivery, hits "
        "like 'Blue and White Porcelain' and 'Dong Feng Po' made him the defining star of the whole "
        "Chinese-speaking world. Region flag: Taiwan (pan-Chinese reach).",
        [
            ("Qing Hua Ci (Blue and White Porcelain)", "Jay Chou"),
            ("Dong Feng Po", "Jay Chou"),
            ("Jay Chou (the Mandopop revolutionary)", None),
            ("Zhongguofeng (the Chinese-style pop wave)", None),
            ("R&B & hip-hop enter Mandopop (the Jay Chou sound)", None),
        ],
    ),
    (
        "THE 2000s C-POP CONSTELLATION",
        "Jay Chou led a glittering pan-Chinese Mandopop industry. Jolin Tsai reigned as dance-pop queen, "
        "Wang Leehom and David Tao pioneered Chinese R&B and fusion, Singapore's Stefanie Sun and JJ Lin "
        "became superstars, and the Taiwanese band Mayday grew into the biggest rock act in the "
        "Chinese-speaking world. C-pop was now a vast, unified market.",
        [
            ("Jolin Tsai (the queen of C-pop dance)", None),
            ("Wang Leehom (the Chinese R&B/fusion pioneer)", None),
            ("David Tao (the mainland-Taiwan R&B pioneer)", None),
            ("Stefanie Sun & JJ Lin (the Singapore Mandopop stars)", None),
            ("Mayday / Wu Yue Tian (the biggest Chinese rock band, Taiwan)", None),
        ],
    ),
    (
        "THE FOLK REVIVAL & INDIE (c. 2010-present)",
        "A new folk and indie scene rose from the livehouses and the internet. Zhao Lei's wistful "
        "'Chengdu' became a national phenomenon, the singer-songwriters Li Zhi, Song Dongye, and Ma Di "
        "won devoted followings, and Second Hand Rose fused northeastern errenzhuan folk with rock. "
        "Content note: some independent artists (Li Zhi) vanished from platforms amid censorship.",
        [
            ("Chengdu", "Zhao Lei"),
            ("The new folk singer-songwriters (Li Zhi, Song Dongye, Ma Di)", None),
            ("Second Hand Rose (errenzhuan-folk rock)", None),
            ("The indie & livehouse scene (2010s China)", None),
            ("Folk revival & the internet audience", None),
        ],
    ),
    (
        "CHINESE HIP-HOP & 'THE RAP OF CHINA' (c. 2017-present)",
        "Hip-hop had bubbled underground for years, but the 2017 streaming show 'The Rap of China' blew "
        "it into the mainstream overnight. The Chengdu crew Higher Brothers went global with 'Made in "
        "China' (via 88rising), and GAI brought a trap-meets-Chinese-style flow. Content note: a swift "
        "official backlash then curbed hip-hop's visibility.",
        [
            ("Made in China", "Higher Brothers"),
            ("The Rap of China (the 2017 hip-hop explosion)", None),
            ("Higher Brothers (the Chengdu crew goes global)", None),
            ("GAI & the trap-guofeng flow", None),
            ("Chinese hip-hop & the official backlash", None),
        ],
    ),
    (
        "THE STREAMING & SHORT-VIDEO AGE (c. 2015-present)",
        "Today Chinese music lives on the phone: Douyin (TikTok) mints viral hits overnight, QQ Music "
        "and NetEase Cloud stream to hundreds of millions, idol-survival shows manufacture stars, and a "
        "'national style' (guofeng) revival dresses pop in classical Chinese imagery. It is one of the "
        "world's largest and most self-contained music markets.",
        [
            ("Douyin (TikTok) viral songs (the short-video hit)", None),
            ("QQ Music & NetEase Cloud (the streaming giants)", None),
            ("The idol-survival show era (manufactured C-pop)", None),
            ("The guofeng revival (classical imagery in pop)", None),
            ("China's vast self-contained music market", None),
        ],
    ),
    (
        "THE THROUGH-LINE: CHINA'S MUSICAL CENTURY",
        "Five installments span an astonishing arc: from the guqin and the pentatonic ideal, through "
        "opera and revolution, shidaiqu and its silencing, the gangtai golden age, and the mainland's "
        "own rock-to-streaming rise. Through every upheaval the pentatonic soul persists. Cross-links: "
        "the shared East Asian world of Japan and Korea (the surveys ahead) and the global Chinese "
        "diaspora.",
        [
            ("From guqin to streaming (the Chinese arc)", None),
            ("The pentatonic soul persists (through every upheaval)", None),
            ("Tradition, revolution & global pop (China's swings)", None),
            ("The Chinese-speaking world reunited in song", None),
            ("China & the East Asian musical family (cross-link)", None),
        ],
    ),
]

STEM = "china_music_5_MAINLAND_ROCK_CPOP_TODAY"


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
