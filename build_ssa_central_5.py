#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Central, installment 5: Soukous Goes Global & the Birth of Ndombolo.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1980-2000.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of Central African Music — Installment 5: "
         "Soukous Goes Global & the Birth of Ndombolo (c. 1980-2000)")

FRAMING = (
    "In these two decades Congolese music conquered the world's dancefloors and then reinvented itself "
    "at home. As Zaire's economy collapsed, a wave of musicians relocated to PARIS, where cleaner "
    "studios and the booming 'world music' market sped soukous up into a gleaming, guitar-drenched "
    "dance machine: Kanda Bongo Man launched the KWASSA KWASSA craze, and Diblo Dibala's 'machine-gun' "
    "guitar with Loketo and the Soukous Stars made the Paris sound a global export. Back in Kinshasa, "
    "a new generation of giants took over -- Koffi Olomide's lush 'tcha tcha' ballads, and the youth "
    "supergroup Wenge Musica, whose split into JB Mpiana's and Werrason's rival camps birthed NDOMBOLO, "
    "the hip-swinging late-90s dance that swept the whole continent (Awilo Longomba's 'Coupe Bibamba' "
    "its global anthem). The era also closed the golden age: Franco died in 1989, and the old giants "
    "passed as Mobutu himself fell in 1997 and the country -- renamed DR Congo -- slid into catastrophic "
    "war. Cross-links: Paris soukous -> the world-music industry; ndombolo -> West and Southern African "
    "pop. Content note: the AIDS epidemic (which took Franco), Mobutu's fall, and the Congo wars are "
    "kept with context. Region: DR Congo / Zaire & Congo-Brazzaville (with the Paris diaspora flagged)."
)

SECTIONS = [
    (
        "THE PARIS SOUKOUS SCENE (c. 1982-1995)",
        "As Zaire crumbled, Kinshasa's musicians decamped to Paris, where studios were better and the "
        "'world music' boom was hungry. They stripped soukous down to its dance essence -- fast, bright, "
        "all sparkling guitars and driving sebene -- and sold it to Europe and back to Africa. Cross-"
        "link: this is the moment Congolese music enters the global world-music market.",
        [
            ("Paris soukous (the exile studios, 1980s)", None),
            ("Fast dance-floor soukous (for the world market)", None),
            ("The Congolese diaspora in Paris", None),
            ("Studio soukous production (cleaner and quicker)", None),
            ("Soukous conquers European world-music", None),
        ],
    ),
    (
        "KANDA BONGO MAN & KWASSA KWASSA (c. 1981-1990)",
        "Kanda Bongo Man broke soukous open for the world: he cut the long sung intros and got straight "
        "to the guitar dance, and his choreographer's KWASSA KWASSA became a continent-wide dance "
        "craze. With Diblo Dibala's dazzling lead lines, his records were the sound of 1980s African "
        "discos everywhere.",
        [
            ("Sai", "Kanda Bongo Man"),
            ("Zing Zong", "Kanda Bongo Man"),
            ("Yesu Kristu", "Kanda Bongo Man"),
            ("Kwassa kwassa (the dance craze)", None),
            ("Kanda Bongo Man (soukous for the world)", None),
        ],
    ),
    (
        "DIBLO DIBALA, LOKETO & THE SOUKOUS STARS (c. 1986-1995)",
        "Diblo Dibala's 'machine-gun' guitar was the era's most thrilling sound. With the Congolese-"
        "Brazzaville singer Aurlus Mabele -- 'the King of Soukous' -- he led Loketo and then the "
        "Soukous Stars, a Paris session collective that churned out relentlessly danceable hits and "
        "took the fast Paris style to its dizzying peak.",
        [
            ("Diblo Dibala (the Machine Gun guitar)", None),
            ("Loketo (Diblo & Aurlus Mabele)", None),
            ("Aurlus Mabele (the King of Soukous, Brazzaville)", None),
            ("Soukous Stars (the Paris session collective)", None),
            ("Lightning-fast sebene (the Paris style)", None),
        ],
    ),
    (
        "KOFFI OLOMIDE & THE 1990s KINSHASA GIANTS",
        "Back home, Koffi Olomide became the biggest star of the decade, inventing 'tcha tcha' -- a "
        "slow, lush, romantic soukous ballad style -- and fronting the star-packed Quartier Latin "
        "International. He was the flamboyant king of a rich Kinshasa scene. (Content note: his later "
        "career was clouded by legal controversy -- noted, not dwelt on.)",
        [
            ("Loi", "Koffi Olomide"),
            ("Papa Ngwasuma", "Koffi Olomide"),
            ("Andrada", "Koffi Olomide"),
            ("Quartier Latin International (Koffi's band)", None),
            ("Tcha tcha (the slow-sweet soukous ballad)", None),
            ("Koffi Olomide (the Kinshasa superstar)", None),
        ],
    ),
    (
        "WENGE MUSICA & THE BIRTH OF NDOMBOLO (c. 1992-2000)",
        "The youth supergroup Wenge Musica dominated the early 90s and then famously split into two "
        "warring camps -- JB Mpiana's Wenge BCBG and Werrason's Wenge Maison Mere -- whose rivalry "
        "birthed NDOMBOLO, a fast, hip-and-waist-swinging dance that scandalized moralists and "
        "conquered every dancefloor in Africa. The atalaku shout was now central.",
        [
            ("Wenge Musica (the 1990s youth supergroup)", None),
            ("JB Mpiana & Wenge BCBG", None),
            ("Werrason & Wenge Maison Mere", None),
            ("Ndombolo (the hip-swinging dance, late 1990s)", None),
            ("The Wenge split (Mpiana versus Werrason)", None),
            ("Feux de l'Amour (a Wenge-era anthem)", None),
        ],
    ),
    (
        "AWILO LONGOMBA & NDOMBOLO GOES CONTINENTAL (c. 1996-2000)",
        "Ndombolo became the pan-African sound of the turn of the millennium, and Awilo Longomba's "
        "'Coupe Bibamba' (1998) was its global anthem, a hit from Lagos to Nairobi to Johannesburg. "
        "Cross-link: ndombolo's beat and dance fed directly into West and Southern African pop of the "
        "era.",
        [
            ("Coupe Bibamba", "Awilo Longomba"),
            ("Karolina", "Awilo Longomba"),
            ("Ndombolo sweeps Africa (the pan-African craze)", None),
            ("Ndombolo in West and Southern Africa", None),
            ("Fast ndombolo dance (the sebene shout)", None),
        ],
    ),
    (
        "THE END OF AN ERA: THE GIANTS PASS (c. 1989-2000)",
        "The founding age closed. Franco died in 1989 and was given a state funeral; Tabu Ley turned to "
        "politics and exile; and Papa Wemba built a parallel world-music career (recording for Peter "
        "Gabriel's Real World). Content note: this unfolded as the AIDS epidemic took its toll, Mobutu "
        "fell in 1997 (Zaire becoming DR Congo), and the country plunged into the deadliest wars since "
        "1945 -- the music kept going through all of it.",
        [
            ("Yolele", "Papa Wemba"),
            ("Maria Valencia", "Papa Wemba"),
            ("Franco's death (1989, the state funeral)", None),
            ("Tabu Ley into politics & exile", None),
            ("Mobutu falls & Zaire becomes DR Congo (1997)", None),
            ("The Congo wars & the music's resilience", None),
        ],
    ),
]

STEM = "ssa_central_music_5_SOUKOUS_GLOBAL_NDOMBOLO"


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
