#!/usr/bin/env python3
"""Build East Asia: Korea, installment 5 (FINAL): Modern & Global K-pop.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/romanized only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Korean Music — Installment 5 (Finale): "
         "Modern & Global K-pop (c. 2010-present)")

FRAMING = (
    "In little more than a decade, K-pop went from a regional industry to a planet-conquering "
    "phenomenon. PSY's 'Gangnam Style' (2012) was the crack in the dam -- the first Korean song to go "
    "truly global viral. Then BTS broke it wide open: a self-aware, self-producing group whose "
    "'Dynamite' topped the US Billboard chart and whose ARMY fandom became a global force, making them "
    "the biggest band in the world. BLACKPINK headlined Coachella; a 3rd-generation constellation (EXO, "
    "TWICE, Red Velvet, Seventeen) and a global-native 4th generation (Stray Kids, aespa, LE SSERAFIM, "
    "and the retro-resetting NEWJEANS) filled the world's charts. Beneath the idols runs a rich "
    "K-HIP-HOP scene (Epik High, Jay Park, Zico), a K-R&B and INDIE world, and the artistry of IU. K-pop "
    "is now a soft-power juggernaut, riding the same Hallyu 2.0 wave that carried Parasite and Squid "
    "Game. This installment closes the Korea survey -- and ALL of East Asia. Cross-links: US hip-hop/"
    "pop and global streaming; the whole Korean arc from han to the algorithm. Content notes: the "
    "industry's labor pressures and the mental-health toll on idols are kept brief, factual, and with "
    "care. Names romanized. Region: South Korea (global)."
)

SECTIONS = [
    (
        "PSY & 'GANGNAM STYLE': THE GLOBAL BREAK (2012)",
        "Psy's 'Gangnam Style' -- a comic satire of Seoul's flashy Gangnam district -- became the first "
        "Korean song to conquer the world, and the first YouTube video ever to pass a billion views. It "
        "was many Westerners' first taste of K-pop, and it flung the door wide open. Cross-link: the "
        "internet as K-pop's global stage.",
        [
            ("Gangnam Style", "Psy"),
            ("Psy (the global viral breakthrough, 2012)", None),
            ("The first billion-view YouTube video", None),
            ("K-pop's viral global stage (the door opens)", None),
        ],
    ),
    (
        "BTS & THE GLOBAL EXPLOSION (c. 2013-present)",
        "BTS remade what a Korean group could be: seven members who wrote and spoke for themselves, "
        "building a bond with a colossal global fandom (ARMY). 'Dynamite' (2020) topped the US Billboard "
        "Hot 100, and 'Spring Day' became a modern classic. They became the biggest band in the world. "
        "Content note: the members' openness about mental health broke K-pop taboos.",
        [
            ("Dynamite", "BTS"),
            ("Spring Day (Bom Nal)", "BTS"),
            ("BTS & the ARMY (the global fandom)", None),
            ("The self-producing idol group (BTS's authenticity)", None),
            ("The biggest band in the world (K-pop conquers the US)", None),
        ],
    ),
    (
        "BLACKPINK & THE GIRL-GROUP GOES GLOBAL (c. 2016-present)",
        "BLACKPINK became the biggest girl group in the world -- the first K-pop act to headline "
        "Coachella, with global smashes like 'DDU-DU DDU-DU' and members (Lisa, Jennie, Rose, Jisoo) who "
        "crossed into global fashion and solo stardom. They made K-pop girl-group glamour a worldwide "
        "language.",
        [
            ("DDU-DU DDU-DU", "BLACKPINK"),
            ("BLACKPINK (the biggest girl group in the world)", None),
            ("K-pop headlines Coachella (the global stage)", None),
            ("The BLACKPINK members go solo & global (fashion & pop)", None),
        ],
    ),
    (
        "THE 3RD-GEN CONSTELLATION (c. 2012-2019)",
        "A dazzling third generation built the mature K-pop machine. EXO's 'Growl' set the boy-group "
        "standard; TWICE's 'TT' and its bright J-line reach ruled the girl-group charts; Red Velvet "
        "balanced sweet and experimental; and Seventeen, NCT, and Mamamoo widened the field. K-pop was "
        "now a deep, self-renewing industry.",
        [
            ("Growl", "EXO"),
            ("TT", "TWICE"),
            ("Red Flavor", "Red Velvet"),
            ("Seventeen & NCT (the large-group era)", None),
            ("Mamamoo & the vocal girl groups", None),
        ],
    ),
    (
        "THE 4TH GENERATION (c. 2018-present)",
        "A global-native fourth generation arrived, born straight into worldwide fame. Stray Kids' "
        "'God's Menu' brought noise-rap muscle; aespa's 'Next Level' built a metaverse concept; ITZY, "
        "IVE, and LE SSERAFIM ruled; and NewJeans' 'Ditto' reset the sound toward retro, easy, "
        "Y2K-tinged pop, a phenomenon in itself.",
        [
            ("God's Menu", "Stray Kids"),
            ("Next Level", "aespa"),
            ("Ditto", "NewJeans"),
            ("Antifragile", "LE SSERAFIM"),
            ("ITZY & IVE (the 4th-gen girl groups)", None),
        ],
    ),
    (
        "K-HIP-HOP (c. 2010-present)",
        "Beneath the idols runs a serious hip-hop scene. Epik High pioneered Korean rap's crossover; the "
        "TV competition Show Me the Money made rappers stars; Jay Park built the AOMG label empire; and "
        "Zico's 'Any Song' (2020) topped every chart. K-hip-hop is now central to Korean youth culture.",
        [
            ("Any Song", "Zico"),
            ("Epik High (the K-hip-hop pioneers)", None),
            ("Show Me the Money (the rap-competition boom)", None),
            ("Jay Park & AOMG (the K-hip-hop label empire)", None),
            ("Dynamic Duo & the Korean rap scene", None),
        ],
    ),
    (
        "K-INDIE, K-R&B & THE ARTISTS (c. 2010-present)",
        "Away from the idol machine thrives a world of auteurs. IU grew from 'nation's little sister' "
        "into a revered singer-songwriter ('Good Day', 'Palette'); Hyukoh led a cool indie-band scene; "
        "and Dean, Crush, and Zion.T built a smooth K-R&B. This is the artist's side of Korean pop.",
        [
            ("Good Day (Gooeun Nal)", "IU"),
            ("Palette", "IU"),
            ("Hyukoh & the K-indie band scene", None),
            ("Dean, Crush & Zion.T (the K-R&B wave)", None),
            ("AKMU & 10cm (the indie-pop artists)", None),
        ],
    ),
    (
        "THE FANDOM, SOFT POWER & THE DARK SIDE (c. 2012-present)",
        "K-pop became a national industry and a soft-power juggernaut -- global streaming dominance, "
        "vast organized fandoms (ARMY, BLINK), and the Hallyu 2.0 halo of Parasite's Oscar and Squid "
        "Game. Content note: the era also exposed the industry's costs -- brutal idol schedules, the "
        "mental-health toll and tragic losses, and major scandals -- kept brief and with care.",
        [
            ("K-pop as soft power (the national industry)", None),
            ("The global fandom machine (ARMY, BLINK & streaming)", None),
            ("Hallyu 2.0 (Parasite & Squid Game halo)", None),
            ("The cost of the idol system (mental health, content note)", None),
        ],
    ),
    (
        "THE THROUGH-LINE: KOREA'S MUSICAL CENTURY",
        "Five installments trace an extraordinary arc: from the han and heung of pansori and gugak, "
        "through occupation, war, and dictatorship, to a pop that conquered the planet. From 'Arirang' "
        "to the algorithm, Korean music turned deep feeling into a global language. This closes the "
        "Korea survey -- and all of East Asia. Cross-links: the shared East Asian world (China & Japan); "
        "the worldwide Hallyu audience.",
        [
            ("From Arirang to the algorithm (the Korean arc)", None),
            ("Han & heung, from pansori to K-pop (the emotional thread)", None),
            ("Korea's soft-power century (the global turn)", None),
            ("Korea & the East Asian musical family (cross-link)", None),
            ("All of East Asia, complete (the milestone)", None),
        ],
    ),
]

STEM = "korea_music_5_MODERN_GLOBAL_KPOP"


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
