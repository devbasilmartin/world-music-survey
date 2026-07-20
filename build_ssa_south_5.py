#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Southern, installment 5: Mbira, Chimurenga & the Liberation Era.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1970-1989.
Dedup is by TITLE only -- every title unique region-wide (avoid #1's "Kasahwa"/"Chapfudza").
"""

TITLE = ("The Story of Southern African Music — Installment 5: "
         "Mbira, Chimurenga & the Liberation Era (c. 1970-1989)")

FRAMING = (
    "As the liberation wars burned across the region, its music became a weapon and a witness. In "
    "Rhodesia, Thomas Mapfumo transposed the ancient mbira melodies of Installment 1 onto electric "
    "guitars and sang in Shona about the war for majority rule -- CHIMURENGA ('struggle') music -- and "
    "the white regime detained him without charge in 1979; a year later the country was independent "
    "Zimbabwe. Around him grew a whole Zimbabwean guitar pop: Oliver Mtukudzi's soulful Tuku music, "
    "the Bhundu Boys' effervescent JIT (a sensation in 1980s Britain), and the sungura dance bands. To "
    "the north, on the Zambian Copperbelt, President Kaunda's 'Zambianization' and a flood of Hendrix "
    "and Black Sabbath records produced the fuzzed-out psychedelia of ZAMROCK (WITCH, Amanaz, Ngozi "
    "Family). In Mozambique the urban dance of MARRABENTA held on through war. And in South Africa, "
    "Juluka -- the white Johnny Clegg and the Zulu Sipho Mchunu -- crossed the colour line in open "
    "defiance of apartheid. Cross-links: chimurenga's mbira-to-guitar transfer ties straight back to "
    "Installment 1; Zamrock <-> US/UK psych and funk; and this whole liberation soundtrack rhymes with "
    "the protest music of the US and West Africa surveys. Content note: liberation war, detention, "
    "censorship, and the AIDS epidemic that later devastated these scenes -- kept with full context. "
    "Region: Zimbabwe, Zambia, Mozambique, South Africa. Scope call (Johnny Clegg) flagged."
)

SECTIONS = [
    (
        "THOMAS MAPFUMO & CHIMURENGA (Zimbabwe, c. 1973-1989)",
        "Thomas Mapfumo, 'the Lion of Zimbabwe', took the sacred mbira patterns of the Shona and "
        "arranged them for electric guitar, bass, and drums, singing coded Shona lyrics that rallied "
        "the guerrilla struggle against Ian Smith's regime. Content note: his music was banned and he "
        "was detained without trial in 1979; after independence he became, just as fearlessly, a critic "
        "of the new government's 'Corruption'.",
        [
            ("Hokoyo!", "Thomas Mapfumo"),
            ("Pfumvu Paruzevha", "Thomas Mapfumo"),
            ("Nyarai", "Thomas Mapfumo"),
            ("Chitima Ndikature", "Thomas Mapfumo"),
            ("Corruption", "Thomas Mapfumo"),
            ("Chimurenga (electric-mbira liberation song)", None),
        ],
    ),
    (
        "THE MBIRA GOES ELECTRIC & THE ZIMBABWEAN SOUND (c. 1975-1989)",
        "Chimurenga was one node in a booming Zimbabwean guitar pop. Stella Chiweshe (Installment 1) "
        "electrified the mbira for the stage; Zexie Manatsa scored a national sensation with a wedding "
        "song performed live at his own wedding; and the sungura dance bands packed the beer halls. "
        "Cross-link: the guitar lines are literally mbira patterns retuned for strings.",
        [
            ("Njuzu", "Stella Chiweshe"),
            ("Chipo Chiroorwa", "Zexie Manatsa"),
            ("Mbira-to-guitar (Shona chimurenga style)", None),
            ("Sungura (Zimbabwean guitar-band dance pop)", None),
            ("Devera Ngwena Jazz Band (mine-town pop)", None),
        ],
    ),
    (
        "OLIVER MTUKUDZI: TUKU MUSIC (Zimbabwe, c. 1977-1989)",
        "Oliver 'Tuku' Mtukudzi built a warm, gospel-tinged sound of his own -- 'Tuku music' -- from "
        "Korekore mbira feel, township jit, and South African mbaqanga, with a husky voice and gentle "
        "moral authority. Over a vast catalogue he became, with Mapfumo, one of the two pillars of "
        "Zimbabwean music. (Some signature titles like 'Todii' and 'Neria' peaked in the 1990s but grow "
        "from the 1970s roots traced here.)",
        [
            ("Neria", "Oliver Mtukudzi"),
            ("Todii", "Oliver Mtukudzi"),
            ("Dzoka Uyamwe", "Oliver Mtukudzi"),
            ("Nhava", "Oliver Mtukudzi"),
            ("Tuku music (Korekore-mbaqanga groove)", None),
        ],
    ),
    (
        "THE BHUNDU BOYS & JIT (Zimbabwe, c. 1980-1989)",
        "Post-independence Harare's brightest export was JIT (or jiti) -- fast, sunny, chiming "
        "guitar-pop. The Bhundu Boys became a genuine 1980s phenomenon in Britain, opening for Madonna "
        "at Wembley; the Four Brothers and others rode the same wave. Content note: the Bhundu Boys' "
        "story ended in tragedy, several members lost to AIDS and frontman Biggie Tembo's suicide in "
        "1995 -- the epidemic that would gut the whole region's music.",
        [
            ("Shabini", "Bhundu Boys"),
            ("Hupenyu Hwangu", "Bhundu Boys"),
            ("Manhenga", "Bhundu Boys"),
            ("Makorokoto", "Four Brothers"),
            ("Jit (Zimbabwean sunshine guitar-pop)", None),
            ("Jiti (fast Shona dance rhythm)", None),
        ],
    ),
    (
        "ZAMBIAN ZAMROCK: THE COPPERBELT PSYCH (Zambia, c. 1972-1980)",
        "On the Zambian Copperbelt, President Kaunda's rule that radio play 95% Zambian music collided "
        "with imported Hendrix, Cream, and James Brown to produce ZAMROCK -- raw, fuzzed psychedelic "
        "rock-funk sung in English and Bemba. WITCH ('We Intend To Cause Havoc'), Amanaz, and the Ngozi "
        "Family were its stars. Content note: the scene was almost entirely wiped out by the AIDS "
        "epidemic; it was rediscovered by crate-diggers decades later. Cross-link: US/UK psych and funk.",
        [
            ("Lazy Bones", "WITCH"),
            ("Introduction", "WITCH"),
            ("Khala My Friend", "Amanaz"),
            ("Nizakupanga Ngozi", "Ngozi Family"),
            ("Zamrock (Copperbelt psych-funk under Kaunda)", None),
            ("Musi-O-Tunya (Zambian rock)", None),
        ],
    ),
    (
        "MARRABENTA & THE LUSOPHONE SOUTH (Mozambique, c. 1970-1989)",
        "In Portuguese-colonial and then war-torn Mozambique, the urban dance music MARRABENTA -- built "
        "on a home-made tin guitar and the majika beat -- carried the cities. Fany Mpfumo was its "
        "pioneer voice and the Orchestra Marrabenta Star de Mocambique its great band, playing through "
        "independence (1975) and the long civil war. Cross-link: marrabenta's roots touch the Chopi "
        "timbila of Installment 1.",
        [
            ("Marrabenta (Mozambican urban dance music)", None),
            ("Fany Mpfumo (marrabenta pioneer)", None),
            ("Orchestra Marrabenta Star de Mocambique", None),
            ("Majika beat (Mozambican dance rhythm)", None),
        ],
    ),
    (
        "CROSSING THE COLOUR LINE: ANTI-APARTHEID & JULUKA (South Africa, c. 1979-1989)",
        "In South Africa the music turned openly defiant. Juluka -- the white 'White Zulu' Johnny Clegg "
        "and the Zulu migrant Sipho Mchunu -- fused Celtic folk-rock with Zulu maskandi and dance, the "
        "first prominent mixed-race band under apartheid, harassed and banned for it. Sipho 'Hotstix' "
        "Mabuse and the jazz-fusion band Sakhile carried the same spirit. (Scope note: Johnny Clegg is "
        "a white South African -- kept as South African, and flagged.)",
        [
            ("Scatterlings of Africa", "Juluka"),
            ("Impi", "Juluka"),
            ("December African Rain", "Juluka"),
            ("Burn Out", "Sipho Mabuse"),
            ("Sakhile (South African jazz-fusion)", None),
            ("Anti-apartheid protest & exile song", None),
        ],
    ),
]

STEM = "ssa_south_music_5_MBIRA_CHIMURENGA_LIBERATION"


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
