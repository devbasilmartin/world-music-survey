#!/usr/bin/env python3
"""Build East Asia: Korea, installment 4: The Birth of K-pop & the Hallyu Wave.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/romanized only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Korean Music — Installment 4: "
         "The Birth of K-pop & the Hallyu Wave (c. 1992-2009)")

FRAMING = (
    "Modern K-pop begins with a single earthquake: in 1992 SEO TAIJI AND BOYS performed 'I Know' on a "
    "TV talent show, fusing American hip-hop, new jack swing, and rock with Korean pop -- the judges "
    "scored them last, and the nation's youth made them gods. From that break grew the K-pop machine: "
    "the great entertainment AGENCIES (SM, YG, JYP) built a trainee-and-idol-factory system that "
    "manufactured the first idol generation (H.O.T., S.E.S., g.o.d, Shinhwa) alongside a golden age of "
    "ballad and R&B (Kim Gun-mo, Shin Seung-hun). Then Korean pop went regional and global: BoA and "
    "TVXQ conquered Japan, Korean TV dramas swept Asia in the early HALLYU (Korean Wave), and a polished "
    "second generation -- Big Bang, Girls' Generation, Wonder Girls, Super Junior, 2NE1 -- perfected the "
    "hook-driven, dance-heavy template that would soon take the whole planet. Cross-links: American "
    "hip-hop/R&B and Japanese idol pop feeding K-pop; the coming global BTS/BLACKPINK explosion (#5). "
    "Content notes: censorship battles and idol-industry labor controversies are kept factual and brief. "
    "Names romanized. Region: South Korea."
)

SECTIONS = [
    (
        "SEO TAIJI AND BOYS: THE 1992 REVOLUTION",
        "Seo Taiji and Boys detonated Korean pop. Their 1992 debut 'I Know' -- rap and new jack swing "
        "over a rock backbone -- was dismissed by the old-guard TV judges and adored by the young, "
        "changing everything overnight. 'Come Back Home' (1995) brought gangsta rap to Korea. Content "
        "note: they clashed with the state censorship board. This is the Big Bang of K-pop.",
        [
            ("Nan Arayo (I Know)", "Seo Taiji and Boys"),
            ("Come Back Home", "Seo Taiji and Boys"),
            ("Seo Taiji and Boys (the 1992 pop revolution)", None),
            ("Hip-hop & new jack swing enter Korean pop", None),
            ("The youth-culture earthquake (the Big Bang of K-pop)", None),
        ],
    ),
    (
        "THE AGENCY SYSTEM: THE IDOL FACTORY (c. 1995-present)",
        "K-pop's engine is the entertainment agency. Lee Soo-man's SM (1995), Yang Hyun-suk's YG, and "
        "Park Jin-young's JYP built a system of long trainee apprenticeships, manufactured groups, and "
        "total career management -- the 'idol factory' that would define Korean pop and, eventually, "
        "reshape global music production.",
        [
            ("The K-pop agency system (SM, YG, JYP)", None),
            ("Lee Soo-man & SM Entertainment (the blueprint)", None),
            ("The trainee system (the idol apprenticeship)", None),
            ("The manufactured idol group (total management)", None),
            ("The K-pop production model is born", None),
        ],
    ),
    (
        "THE FIRST IDOL GENERATION (c. 1996-2003)",
        "The first idols built the template and the fandoms. H.O.T. ('Candy') became the first "
        "megagroup, sparking a rivalry with Sechs Kies; the girl groups S.E.S. ('Dreams Come True') and "
        "Fin.K.L reigned; g.o.d and the enduring Shinhwa completed the '1st gen'. Organized, color-coded "
        "fandoms arrived with them.",
        [
            ("Candy", "H.O.T."),
            ("Dreams Come True", "S.E.S."),
            ("One Candle (Chotbulhana)", "g.o.d"),
            ("H.O.T. versus Sechs Kies (the first idol rivalry)", None),
            ("Fin.K.L & Shinhwa (the 1st-gen idols)", None),
            ("The birth of K-pop fandom culture", None),
        ],
    ),
    (
        "THE 90s BALLAD & R&B STARS",
        "Beside the idols, a golden age of solo pop thrived. Kim Gun-mo's 'Wrongful Meeting' sold a "
        "record-shattering number of copies; Shin Seung-hun ('I Believe') was the 'emperor of ballads'; "
        "and Solid and others imported a smooth Korean R&B. This was the adult, non-idol heart of 90s "
        "gayo.",
        [
            ("Jalmot-doen Mannam (Wrongful Meeting)", "Kim Gun-mo"),
            ("I Believe", "Shin Seung-hun"),
            ("The Korean ballad's 90s peak", None),
            ("Solid & the Korean R&B wave", None),
            ("Lee Soo-young & the ballad divas", None),
        ],
    ),
    (
        "BoA, TVXQ & THE CONQUEST OF JAPAN (c. 2000-2009)",
        "K-pop went regional. SM's teenage prodigy BoA, trilingual and superbly trained, broke Japan in "
        "2002 ('No.1') to become a star in both countries; and the five-member TVXQ (DBSK) grew into "
        "Korea-and-Japan superstars whose 'Mirotic' (2008) is a K-pop classic. The Japan market was "
        "cracked open.",
        [
            ("No.1", "BoA"),
            ("Mirotic", "TVXQ"),
            ("BoA breaks Japan (the first crossover, 2002)", None),
            ("TVXQ / DBSK (the Korea-Japan superstars)", None),
            ("SM's Japan strategy (K-pop goes regional)", None),
        ],
    ),
    (
        "THE HALLYU WAVE BEGINS (c. 2002-2009)",
        "The 'Korean Wave' (Hallyu) swept Asia -- above all through TV dramas like Winter Sonata, whose "
        "lush OSTs made Korean romance a pan-Asian obsession, and through the singer-actor Rain's "
        "global-facing pop ('It's Raining'). Korean pop culture had become a soft-power export. "
        "Cross-link: music, drama, and stardom moving together.",
        [
            ("It's Raining", "Rain"),
            ("The Hallyu wave (the Korean pop-culture export)", None),
            ("Winter Sonata & the K-drama OST (Hallyu in Asia)", None),
            ("Rain / Bi (the global-facing K-pop star)", None),
            ("Korean soft power (music, drama & stardom)", None),
        ],
    ),
    (
        "THE 2ND-GEN IDOLS ARRIVE (c. 2006-2009)",
        "A slicker, self-aware second generation took over. Big Bang -- with the young auteur G-Dragon "
        "writing their hits ('Lies') -- broke the manufactured mold; Super Junior's 'Sorry Sorry' became "
        "a pan-Asian anthem; and Wonder Girls' retro 'Tell Me' and 'Nobody' launched a craze (and a bold "
        "US attempt). SHINee and 2PM rounded out the boys.",
        [
            ("Lies (Geojitmal)", "Big Bang"),
            ("Tell Me", "Wonder Girls"),
            ("Sorry Sorry", "Super Junior"),
            ("G-Dragon & the self-producing idol (Big Bang)", None),
            ("SHINee & 2PM (the 2nd-gen boy groups)", None),
        ],
    ),
    (
        "THE GIRL-GROUP EXPLOSION (c. 2007-2009)",
        "The girl groups perfected the modern K-pop hit. Girls' Generation (SNSD) became a national "
        "phenomenon with the impossibly catchy 'Gee' (2009); 2NE1's 'Fire' brought edge and hip-hop "
        "cool; and KARA and others filled the charts. The bright, hook-laden, precisely choreographed "
        "template was now perfected.",
        [
            ("Gee", "Girls' Generation"),
            ("Fire", "2NE1"),
            ("The girl-group boom (SNSD, 2NE1, KARA)", None),
            ("The hook-and-choreography K-pop template (perfected)", None),
            ("Girls' Generation becomes a national phenomenon", None),
        ],
    ),
    (
        "THE K-POP MACHINE & THE ROAD AHEAD (c. 2009)",
        "By 2009 the K-pop system was fully built -- weekly music shows, comeback cycles, color-coded "
        "fandoms, and the idol as a total export product. Content note: the era also exposed the "
        "industry's darker side, from trainee pressures to the 'slave contract' disputes that split "
        "TVXQ. Cross-link: the coming global explosion of BTS and BLACKPINK (Installment 5).",
        [
            ("The consolidated K-pop system (music shows & comebacks)", None),
            ("The idol as export product", None),
            ("Idol-industry labor controversies (the slave-contract disputes)", None),
            ("Toward the global era (BTS & BLACKPINK ahead)", None),
        ],
    ),
]

STEM = "korea_music_4_KPOP_BIRTH_HALLYU"


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
