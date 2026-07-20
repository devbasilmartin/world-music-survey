#!/usr/bin/env python3
"""Build India / South Asia, installment 6: Modern Filmi & the Indipop Boom.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/Latin only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Indian & South Asian Music — Installment 6: "
         "Modern Filmi & the Indipop Boom (c. 1970-2010)")

FRAMING = (
    "After the golden age, Indian popular music reinvented itself again and again. In the 1970s R.D. "
    "BURMAN ('Pancham') electrified film music with rock, funk, Latin, and psychedelia; the 1980s went "
    "DISCO with Bappi Lahiri's gold chains; a parallel non-film GHAZAL revival (Jagjit Singh, and the "
    "Pakistani masters Mehdi Hassan and Ghulam Ali) sold millions of cassettes. In the south, the "
    "prodigious ILAIYARAAJA reinvented Tamil film music, and then, in 1992, A.R. RAHMAN's 'Roja' "
    "detonated a sonic revolution that carried Indian film music to the Oscars ('Jai Ho'). Meanwhile "
    "cable TV and MTV India sparked the 1990s INDIPOP boom -- the first real non-film pop scene "
    "(Alisha Chinai, Daler Mehndi's bhangra-pop, Lucky Ali) -- before the film song reabsorbed it. "
    "Cross-links: the golden-age songbook (#5) it grew from; bhangra's global diaspora pop; qawwali/"
    "ghazal (#4) and the Pakistani masters (flagged wider-South-Asia); the streaming/global era (#7). "
    "Content notes: the cassette-piracy economy and Gulshan Kumar's 1997 murder are kept in view. Names "
    "are SONG - singer; bare titles are composers, scenes, or concepts. Region: India (with flagged "
    "Pakistani ghazal masters)."
)

SECTIONS = [
    (
        "R.D. BURMAN'S REVOLUTION (c. 1970-1985)",
        "Rahul Dev Burman -- 'Pancham', S.D.'s son -- blew up film music with rock rhythms, funk bass, "
        "Latin percussion, and sheer invention, most magically in partnership with singer (and wife) "
        "Asha Bhosle. 'Dum Maro Dum' and 'Chura Liya Hai Tumne' redefined cool, while Kishore Kumar "
        "reigned as his golden voice.",
        [
            ("Dum Maro Dum", "Asha Bhosle"),
            ("Chura Liya Hai Tumne", "Asha Bhosle"),
            ("Mehbooba Mehbooba", "R.D. Burman"),
            ("O Mere Dil Ke Chain", "Kishore Kumar"),
            ("R.D. Burman (Pancham, the 1970s revolutionary)", None),
            ("Rock, funk & Latin in the film song (Pancham's palette)", None),
        ],
    ),
    (
        "THE DISCO ERA & BAPPI LAHIRI (c. 1980-1988)",
        "When disco hit, Bappi Lahiri -- India's gold-draped 'Disco King' -- answered with pulsing "
        "synth-and-strings hits. 'Disco Dancer' (1982) became a global phenomenon from the USSR to "
        "Africa, and 'Jimmy Jimmy Aaja' an international earworm. Content note: much of it borrowed "
        "liberally from Western disco -- part of the era's story.",
        [
            ("I Am a Disco Dancer", "Vijay Benedict"),
            ("Jimmy Jimmy Aaja", "Parvati Khan"),
            ("Bappi Lahiri (India's Disco King)", None),
            ("Disco Dancer conquers the USSR & Africa", None),
            ("Synth-disco filmi (the 1980s sound)", None),
        ],
    ),
    (
        "THE GHAZAL REVIVAL (c. 1975-1995)",
        "Away from the movies, a golden non-film ghazal revival sold millions of LPs and cassettes. "
        "Jagjit Singh made the ghazal accessible and huge ('Tum Itna Jo Muskura Rahe Ho'); across the "
        "border the Pakistani masters Mehdi Hassan ('the king of ghazal') and Ghulam Ali reigned; and "
        "Pankaj Udhas brought the ghazal to film. Region note: the Pakistani greats flagged.",
        [
            ("Tum Itna Jo Muskura Rahe Ho", "Jagjit Singh"),
            ("Ranjish Hi Sahi", "Mehdi Hassan"),
            ("Chitthi Aayi Hai", "Pankaj Udhas"),
            ("Jagjit Singh (who made the ghazal a mass love)", None),
            ("Mehdi Hassan & Ghulam Ali (the Pakistani ghazal masters, flagged)", None),
            ("The non-film ghazal cassette boom", None),
        ],
    ),
    (
        "THE SOUTHERN MAESTRO: ILAIYARAAJA (c. 1976-1995)",
        "India's film music is not only Bollywood: the southern industries (Tamil, Telugu, Malayalam, "
        "Kannada) are vast. Their titan was Ilaiyaraaja -- 'the Maestro' -- who scored over a thousand "
        "films, fusing Tamil folk, Carnatic classical, and Western orchestration (even full symphonies) "
        "with astonishing range. Cross-link: the folk (#3) and classical (#2) roots, reborn in cinema.",
        [
            ("Ilaiyaraaja (the Maestro of Tamil film music)", None),
            ("The southern film industries (Tamil, Telugu & beyond)", None),
            ("Folk-Carnatic-Western fusion (Ilaiyaraaja's synthesis)", None),
            ("The prolific film composer (a thousand scores)", None),
            ("Regional cinema song (India beyond Bollywood)", None),
        ],
    ),
    (
        "A.R. RAHMAN & THE TRANSFORMATION (c. 1992-2010)",
        "In 1992 A.R. Rahman's debut score for 'Roja' changed everything -- a lush, digital, genre-"
        "melting sound rooted in Sufi devotion and global pop. He became India's most celebrated "
        "composer, took film music worldwide (the West End's Bombay Dreams), and won two Oscars for "
        "'Jai Ho' (Slumdog Millionaire, 2008). 'Chaiyya Chaiyya' is a modern classic.",
        [
            ("Chaiyya Chaiyya", "Sukhwinder Singh"),
            ("Jai Ho", "A.R. Rahman"),
            ("A.R. Rahman (the composer who remade film music)", None),
            ("Roja (the 1992 sonic revolution)", None),
            ("Rahman goes global (Bombay Dreams & the Oscars)", None),
            ("Sufi-pop & digital orchestration (the Rahman sound)", None),
        ],
    ),
    (
        "THE INDIPOP BOOM (c. 1995-2005)",
        "Cable TV and MTV India briefly birthed India's first true non-film pop scene: INDIPOP. Alisha "
        "Chinai's 'Made in India' was its anthem, Daler Mehndi turned bhangra into pan-Indian pop "
        "('Tunak Tunak Tun'), and Lucky Ali's soulful 'O Sanam' defined its cooler edge, alongside "
        "Colonial Cousins and Shubha Mudgal. Cross-link: bhangra's global diaspora explosion.",
        [
            ("Made in India", "Alisha Chinai"),
            ("Tunak Tunak Tun", "Daler Mehndi"),
            ("O Sanam", "Lucky Ali"),
            ("Indipop (the 1990s non-film pop scene)", None),
            ("Daler Mehndi & the bhangra-pop explosion", None),
            ("Colonial Cousins & Shubha Mudgal (Indipop's range)", None),
            ("MTV India & the music-video boom", None),
        ],
    ),
    (
        "THE NEW PLAYBACK & THE 2000s COMPOSERS (c. 2000-2010)",
        "A new generation of playback stars and composer teams took over as Indipop faded back into "
        "film. Sonu Nigam ('Kal Ho Naa Ho'), Shreya Ghoshal, Sunidhi Chauhan, and KK led the voices, "
        "while Shankar-Ehsaan-Loy (Dil Chahta Hai), Vishal-Shekhar, and Pritam brought a slick, "
        "genre-hopping multi-composer soundtrack.",
        [
            ("Kal Ho Naa Ho", "Sonu Nigam"),
            ("Shreya Ghoshal & Sunidhi Chauhan (the new playback queens)", None),
            ("Shankar-Ehsaan-Loy (the Dil Chahta Hai sound)", None),
            ("Vishal-Shekhar & Pritam (the 2000s hit machines)", None),
            ("The multi-composer soundtrack (the modern film album)", None),
        ],
    ),
    (
        "THE INDUSTRY, THE ITEM SONG & THE ROAD AHEAD (c. 1985-2010)",
        "Behind the hits ran a ferocious economy: T-Series and the cassette revolution democratized "
        "music but drowned it in piracy; the 'item number' became a marketing engine; and remix culture "
        "recycled the golden age. Content note: T-Series founder Gulshan Kumar was murdered by the "
        "underworld in 1997. Cross-link: the streaming/global era ahead (#7).",
        [
            ("T-Series & the cassette revolution (music democratized)", None),
            ("Gulshan Kumar's murder (1997, music & the underworld)", None),
            ("The item number (the marketing song)", None),
            ("Remix culture (the golden age recycled)", None),
            ("Toward streaming & the global 2010s (roads ahead)", None),
        ],
    ),
]

STEM = "south_asia_music_6_MODERN_FILMI_INDIPOP"


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
