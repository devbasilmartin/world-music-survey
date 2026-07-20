#!/usr/bin/env python3
"""Build East Asia: China, installment 1: Classical & Folk Roots.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/Latin (pinyin) only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Chinese Music — Installment 1: "
         "Classical & Folk Roots (the deep tradition)")

FRAMING = (
    "Chinese music is one of the oldest and most philosophically weighted traditions on Earth -- a "
    "3,000-year continuity in which music was never mere entertainment but a mirror of cosmic and "
    "social order. Its foundation is the PENTATONIC scale (gong, shang, jue, zhi, yu) and a Confucian "
    "conviction that correct music makes a well-governed world. At its meditative summit sits the "
    "GUQIN, the scholar's seven-string zither; around it a family of iconic instruments -- the PIPA "
    "lute, the GUZHENG zither, the ERHU fiddle, the DIZI flute, the ancient SHENG mouth-organ, and the "
    "piercing SUONA shawm; a vast world of regional OPERA led by Peking opera; solemn ritual and court "
    "music; and the boundless FOLK song of the Han and the 55 recognized minorities, from Mongolian "
    "throat-singing to Uyghur muqam. This installment lays the deep pre-modern tradition before the "
    "20th-century upheavals (Shanghai, revolution, Cantopop) to come. Cross-links: the pentatonic and "
    "silk-string world shared with Japan and Korea (the East Asia surveys); the Silk Road link to "
    "Central Asian and Persian music. Content note: the music of Xinjiang, Tibet, and Inner Mongolia is "
    "kept with care as living tradition under cultural-political pressure. Names are transliterated "
    "(pinyin); (Traditional) marks forms, instruments, or pieces to seed listening. Region: China."
)

SECTIONS = [
    (
        "THE PENTATONIC FOUNDATION & THE PHILOSOPHY OF SOUND",
        "Chinese music theory is ancient and cosmological: the five-note pentatonic scale mapped to the "
        "five elements and directions, the twelve lu (pitch-pipes) fixing the tuning of the empire, and "
        "the Confucian belief that 'correct' music (yayue) orders society. The Book of Songs (Shijing) "
        "preserves the oldest lyrics. Music was statecraft and philosophy.",
        [
            ("The Chinese pentatonic scale (gong shang jue zhi yu)", None),
            ("The twelve lu (the pitch-pipe tuning system)", None),
            ("Yayue (elegant/ritual music & Confucian order)", None),
            ("Music as cosmic & social harmony (the philosophy)", None),
            ("The Shijing / Book of Songs (the ancient lyrics)", None),
        ],
    ),
    (
        "THE GUQIN & THE SCHOLAR'S TRADITION",
        "The guqin -- a fretless seven-string zither -- is the instrument of the literati (wenren), "
        "played for oneself in meditative solitude, not for an audience. Its subtle slides and "
        "harmonics carry a whole philosophy; 'Flowing Water' was chosen for the Voyager Golden Record, "
        "and the legend of Boya and Ziqi gave the world the phrase 'the one who understands the music'.",
        [
            ("Flowing Water", "Guan Pinghu"),
            ("Guqin (the scholar's seven-string zither)", None),
            ("High Mountains and Flowing Water (the zhiyin friendship legend)", None),
            ("The literati/wenren solo tradition (music for oneself)", None),
            ("Guqin tablature & the art of the slide", None),
        ],
    ),
    (
        "THE PLUCKED STRINGS: PIPA & GUZHENG",
        "Two plucked instruments carry much of the classical repertoire. The pear-shaped four-string "
        "PIPA blazes through martial epics like 'Ambush from Ten Sides' and sighs through lyrical "
        "pieces; the long GUZHENG zither shimmers with cascading glissandi. Both divide their repertoire "
        "into 'civil' (wen, lyrical) and 'martial' (wu, vigorous) styles.",
        [
            ("Pipa (the four-string pear-shaped lute)", None),
            ("Ambush from Ten Sides (Shimian Maifu, the martial pipa epic)", None),
            ("Guzheng (the long plucked zither)", None),
            ("Spring River Flower Moon Night (the lyrical classic)", None),
            ("Wen & wu (the civil & martial styles)", None),
            ("Autumn Moon over the Han Palace (a guzheng favorite)", None),
        ],
    ),
    (
        "THE BOWED & BLOWN: ERHU, DIZI, SHENG & SUONA",
        "The melodic soul of Chinese music runs through the two-string ERHU fiddle -- whose most famous "
        "piece, the blind musician Abing's 'Erquan Yingyue', is heartbreak itself -- the bamboo DIZI "
        "flute, the ancient mouth-organ SHENG (ancestor of the Western harmonica and accordion reed), "
        "and the blaring SUONA shawm of weddings and funerals. Together they form the silk-and-bamboo "
        "(sizhu) ensemble.",
        [
            ("Erquan Yingyue", "Abing"),
            ("Erhu (the two-string bowed fiddle)", None),
            ("Dizi (the bamboo transverse flute)", None),
            ("Sheng (the ancient mouth-organ, free-reed ancestor)", None),
            ("Suona (the piercing shawm of rites & festivals)", None),
            ("Jiangnan sizhu (the silk-and-bamboo ensemble)", None),
        ],
    ),
    (
        "CHINESE OPERA: PEKING OPERA & THE REGIONAL FORMS",
        "Opera was China's great popular entertainment -- a total art of song, stylized speech, "
        "acrobatics, and symbolic makeup. Peking opera (jingju) crystallized in the 19th century with "
        "its role types (sheng, dan, jing, chou) and its high, piercing vocal style; Mei Lanfang made "
        "the female-role dan world-famous. Older Kunqu and hundreds of regional operas flourish beside "
        "it.",
        [
            ("Peking opera / jingju (the total-theater art)", None),
            ("The role types (sheng, dan, jing, chou)", None),
            ("Mei Lanfang (the great dan/female-role master)", None),
            ("Kunqu (the oldest surviving opera, UNESCO)", None),
            ("Cantonese opera (the Yue/southern tradition)", None),
            ("Opera percussion & the piercing vocal style", None),
        ],
    ),
    (
        "RITUAL, COURT & TEMPLE MUSIC",
        "Solemn music served the state and the gods. Confucian ritual music accompanied ancestral and "
        "state rites; Buddhist and Daoist chant filled the temples; and the ancient court orchestras "
        "boasted astonishing instruments -- the 2,400-year-old bronze bell set (bianzhong) of the "
        "Marquis Yi of Zeng is a wonder of the ancient world.",
        [
            ("Confucian ritual music (the state rites)", None),
            ("Bianzhong (the ancient bronze bell-chimes, Marquis Yi of Zeng)", None),
            ("Buddhist temple chant (the Chinese sangha)", None),
            ("Daoist ritual music (the temple ceremonies)", None),
            ("The ancient court orchestra (bells, chimes & stones)", None),
        ],
    ),
    (
        "THE VAST HAN REGIONAL FOLK",
        "Beneath the classical arts lies an ocean of Han folk song -- work songs and love songs, the "
        "high mountain shan'ge of the north and the flower-songs (hua'er) of the northwest, narrative "
        "singing (shuochang), and the beloved 'Mo Li Hua' (Jasmine Flower), so lovely that Puccini put "
        "it in Turandot. Every province has its own voice.",
        [
            ("Mo Li Hua (Jasmine Flower, the beloved folk song)", None),
            ("Han folk song (work songs & love songs)", None),
            ("Shan'ge (the northern mountain songs)", None),
            ("Hua'er (the flower-songs of the northwest)", None),
            ("Shuochang (Chinese narrative sung storytelling)", None),
        ],
    ),
    (
        "THE 55 MINORITIES & THE BORDERLANDS",
        "China is not only Han. Mongolian long-song (urtiin duu) and khoomei throat-singing soar across "
        "the grasslands; the Uyghur Twelve Muqam of Xinjiang is a Silk Road classical treasure; Tibetan "
        "chant and folk, the Naxi ancient orchestra, and the Dong ethnic groups' shimmering unaccompanied "
        "grand choirs enrich the whole. Content note: the borderland traditions of Xinjiang, Tibet, and "
        "Inner Mongolia are living cultures under political pressure -- kept with care.",
        [
            ("Mongolian long-song (urtiin duu) & khoomei throat-singing", None),
            ("Uyghur Twelve Muqam (the Xinjiang Silk Road classical suite)", None),
            ("Tibetan chant & folk song (the plateau traditions)", None),
            ("Dong grand choir (the unaccompanied polyphony)", None),
            ("Naxi ancient music (the Lijiang orchestra)", None),
            ("The music of the 55 minorities (China beyond the Han)", None),
        ],
    ),
    (
        "THE INSTRUMENTS, NOTATION & THE ROAD AHEAD",
        "Binding it all is a shared aesthetic: the pentatonic soul, the silk string, the breath of "
        "bamboo, and old notation systems (gongche, jianzipu) that record gesture as much as pitch. "
        "Cross-link: this pentatonic, silk-string world is shared with Japan and Korea; and it was about "
        "to collide with the West, revolution, and pop in the tumultuous 20th century (installments "
        "ahead).",
        [
            ("Gongche & jianzipu (the old Chinese notations)", None),
            ("The silk-string & bamboo aesthetic (the Chinese sound)", None),
            ("The pentatonic soul (shared across East Asia)", None),
            ("Silk Road exchange (China, Central Asia & Persia)", None),
            ("Toward the 20th century (Western contact & upheaval, roads ahead)", None),
        ],
    ),
]

STEM = "china_music_1_CLASSICAL_FOLK_ROOTS"


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
