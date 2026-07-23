#!/usr/bin/env python3
"""Build East Asia: Korea, installment 1: Classical & Folk Roots (gugak).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/romanized only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Korean Music — Installment 1: "
         "Classical & Folk Roots (gugak, the deep tradition)")

FRAMING = (
    "Korean traditional music (gugak) is unmistakably its own -- deeper in emotion and looser in pulse "
    "than its Chinese and Japanese neighbors, built on a distinctive triple-meter swing and two great "
    "emotional poles: HAN (a deep, aching sorrow and longing) and HEUNG (irrepressible joyous energy), "
    "with MEOT (elegant, understated flair) as its grace. It splits into two worlds: the refined "
    "aristocratic JEONGAK (court and chamber music, including the solemn Confucian ritual aak and the "
    "UNESCO-listed jongmyo jeryeak) and the earthy folk MINSOGAK -- above all PANSORI, the astonishing "
    "hours-long epic story-singing of one raspy-voiced singer and one drummer, and SANJO, the great "
    "instrumental solo. Its instruments -- the gayageum and geomungo zithers, the haegeum fiddle, the "
    "daegeum flute -- and its thunderous farmers'-band percussion (pungmul, later samulnori) and "
    "shamanic gut rituals complete a tradition of enormous depth and feeling. This installment lays the "
    "pre-modern roots before the wrenching 20th century (occupation, war, and the rise of K-pop) to "
    "come. Cross-links: the shared-yet-distinct East Asian world of China and Japan; the shamanic layer "
    "beneath. Names romanized; (Traditional) marks forms, instruments, or pieces to seed listening. "
    "Region: Korea."
)

SECTIONS = [
    (
        "THE KOREAN MUSICAL WORLD & ITS AESTHETIC",
        "Korean music is shaped by feeling and by a loose, breathing sense of time. Its triple-meter "
        "swing sets it apart from China and Japan; its emotional heart is HAN (sorrowful longing) and "
        "its release is HEUNG (joyous energy). Music divided sharply between the aristocratic jeongak "
        "and the common people's minsogak.",
        [
            ("Han & heung (the Korean emotional poles)", None),
            ("Meot (the Korean aesthetic of understated flair)", None),
            ("The Korean triple-meter swing (jangdan rhythmic cycles)", None),
            ("Jeongak versus minsogak (court versus folk)", None),
            ("Jeong-gan-bo (the Korean mensural notation)", None),
        ],
    ),
    (
        "AAK & THE COURT / RITUAL MUSIC",
        "The court preserved solemn, slow, deeply dignified music. AAK, the Confucian ritual music "
        "imported from China, survives in Korea more completely than in China itself; the jongmyo "
        "jeryeak -- music for the royal ancestral shrine rites -- is a UNESCO treasure; and refined "
        "court pieces like 'Sujecheon' unfold with breathtaking slowness.",
        [
            ("Sujecheon (the classic slow court piece)", None),
            ("Jongmyo jeryeak (the royal ancestral shrine music, UNESCO)", None),
            ("Aak (the Confucian ritual court music)", None),
            ("Jeongak (the refined court & chamber music)", None),
            ("Yeongsan hoesang (the classic court suite)", None),
        ],
    ),
    (
        "PANSORI: THE EPIC STORY-SINGING",
        "Pansori is one of the world's great vocal arts: a single singer (sorikkun), armed only with a "
        "fan, performs an hours-long dramatic story -- sung, spoken (aniri), and acted -- accompanied by "
        "one barrel-drummer (gosu) who cries encouragements (chuimsae), as does the audience. Five "
        "stories survive. Content note: its powerful raspy voice is won through brutal training. UNESCO-"
        "listed.",
        [
            ("Pansori (the epic solo story-singing, UNESCO)", None),
            ("Chunhyangga (the love-story pansori)", None),
            ("Simcheongga & Heungbuga (pansori tales of virtue)", None),
            ("The gosu & chuimsae (the drummer and the shouts)", None),
            ("The raspy pansori voice (won through hard training)", None),
            ("Aniri (the spoken narration of pansori)", None),
        ],
    ),
    (
        "SANJO & THE INSTRUMENTAL SOLO",
        "SANJO -- 'scattered melodies' -- is the great instrumental solo form, developed in the late "
        "19th century: a virtuoso journey through a suite of rhythmic cycles (jangdan) that build from "
        "meditative slowness to dazzling speed, over a drummer's pulse. It grew from the shamanic "
        "improvisation sinawi, and Kim Chang-jo is credited with founding the gayageum sanjo.",
        [
            ("Sanjo (the virtuoso instrumental solo)", None),
            ("Sinawi (the shamanic ensemble improvisation)", None),
            ("Kim Chang-jo (father of gayageum sanjo, seed)", None),
            ("The jangdan cycles (slow-to-fast, the sanjo journey)", None),
            ("Improvisation in Korean music (sanjo & sinawi)", None),
        ],
    ),
    (
        "THE STRING INSTRUMENTS: GAYAGEUM & GEOMUNGO",
        "Two zithers anchor Korean melody. The bright, 12-string GAYAGEUM -- plucked with the bare "
        "fingers -- is the most beloved Korean instrument; the deep, six-string GEOMUNGO, struck with a "
        "bamboo stick, was the scholar's noble instrument. The bowed ajaeng adds a raw, growling bass. "
        "Their expressive left-hand bends carry han itself.",
        [
            ("Gayageum (the 12-string plucked zither)", None),
            ("Geomungo (the six-string scholar's zither)", None),
            ("Ajaeng (the bowed zither's growling bass)", None),
            ("The expressive left-hand bend (nonghyeon, the soul of the string)", None),
            ("The plucked-and-bowed Korean string world", None),
        ],
    ),
    (
        "THE WINDS & THE FIDDLE: DAEGEUM, PIRI & HAEGEUM",
        "Korean wind and bowed instruments have unforgettable voices. The large bamboo DAEGEUM flute "
        "buzzes with a reed membrane that gives it a haunting rasp; the PIRI is a piercing double-reed; "
        "the two-string vertical fiddle HAEGEUM wails and slides like a human voice; and the loud "
        "taepyeongso shawm leads outdoor processions.",
        [
            ("Daegeum (the large buzzing bamboo flute)", None),
            ("Piri (the piercing double-reed)", None),
            ("Haegeum (the two-string vertical fiddle)", None),
            ("Taepyeongso (the loud shawm of processions)", None),
            ("The voice-like Korean winds & fiddle", None),
        ],
    ),
    (
        "PUNGMUL, NONGAK & SAMULNORI",
        "Korea's most exhilarating music is its percussion. Farmers' bands (pungmul / nongak) filled "
        "villages with the interlocking clang and thunder of the kkwaenggwari gong, jing, janggu "
        "hourglass-drum, and buk barrel-drum, in outdoor communal dance-music. In 1978 this was "
        "distilled into SAMULNORI, a staged four-player quartet that took Korean rhythm to the world.",
        [
            ("Pungmul / nongak (the farmers'-band percussion)", None),
            ("Samulnori (the 1978 staged percussion quartet)", None),
            ("The kkwaenggwari, jing, janggu & buk (the four drums)", None),
            ("Interlocking jangdan percussion (the Korean groove)", None),
            ("Outdoor communal dance-music (the pungmul tradition)", None),
        ],
    ),
    (
        "SHAMANIC MUSIC (GUT) & THE DEEP ROOTS",
        "Beneath court and Confucian order lies Korea's oldest layer: the SHAMAN (mudang) and the gut, a "
        "ritual of music, dance, and trance to summon and appease spirits. Its ecstatic drumming and "
        "sinawi wailing fed directly into sanjo and pansori. This is the pre-Buddhist, pre-Confucian "
        "substratum of Korean sound. Content note: kept as living spiritual tradition.",
        [
            ("Gut (the Korean shamanic ritual music)", None),
            ("The mudang (the Korean shaman & the trance)", None),
            ("Shamanic drumming & ecstasy (the deep root)", None),
            ("Gut into sanjo & pansori (the folk-art connection)", None),
            ("The pre-Buddhist substratum of Korean music", None),
        ],
    ),
    (
        "MINYO: THE FOLK SONG & THE ROADS AHEAD",
        "The people's MINYO -- regional folk songs of work, love, and festival -- vary by province "
        "(the lyrical gyeonggi, the deep namdo, the plaintive seodo). Above them all floats 'Arirang', "
        "the beloved song that stands for Korea itself (UNESCO). Cross-link: this deep tradition would "
        "be suppressed under Japanese rule and then reborn beside a world-conquering pop (installments "
        "ahead).",
        [
            ("Arirang (the beloved national folk song, UNESCO)", None),
            ("Minyo (the regional Korean folk songs)", None),
            ("Gyeonggi, namdo & seodo minyo (the regional styles)", None),
            ("Korean work & festival songs", None),
            ("Toward the 20th century (occupation & modern pop ahead)", None),
        ],
    ),
]

STEM = "korea_music_1_CLASSICAL_FOLK_ROOTS_GUGAK"


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
