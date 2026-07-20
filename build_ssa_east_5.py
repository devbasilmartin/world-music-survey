#!/usr/bin/env python3
"""Build Sub-Saharan Africa: East, installment 5 (FINAL): The Streaming Era & Global Crossover.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 2010-present.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of East African Music — Installment 5 (Finale): "
         "The Streaming Era & Global Crossover (c. 2010-present)")

FRAMING = (
    "In the streaming decade East Africa stopped being a receiver and became a global player. From Dar "
    "es Salaam, DIAMOND PLATNUMZ built a pan-African empire -- his WCB Wasafi label (Rayvanny, "
    "Harmonize, Mbosso, Zuchu) turned bongo flava into slick 'Bongo' afrobeats that charts from Lagos "
    "to London. Tanzania also birthed SINGELI, a dizzying 200-plus-bpm street sound that the Nyege "
    "Nyege scene carried to the world's clubs. In Kenya, GENGETONE revived raw Sheng street rap (Ethic, "
    "Sailors), while SAUTI SOL wore the afropop crown and a new wave of rappers and crooners "
    "(Nyashinski, Khaligraph Jones, Bien) went continental. Uganda's Eddy Kenzo scored a global viral "
    "smash ('Sitya Loss') and Nyege Nyege made Kampala a festival capital; Rwanda and the wider region "
    "joined in. And amapiano and afrobeats crossed in from South and West Africa, closing the circle. "
    "Cross-links: West African Afrobeats and South African amapiano (those surveys); US/global streaming "
    "pop; the Congo diaspora still in the mix. Content notes: gengetone's censorship battles and "
    "regional politics are kept. Region-integrity note: Sho Madjozi is South African (Tsonga), flagged "
    "as a cross-border collaborator. This installment also builds the SSA-East region master. Region: "
    "Tanzania, Kenya, Uganda & the wider East Africa (the Horn/Ethiopia is a separate survey)."
)

SECTIONS = [
    (
        "DIAMOND PLATNUMZ & THE WASAFI EMPIRE (c. 2010-present)",
        "Diamond Platnumz is East Africa's biggest star -- a Dar es Salaam kid who turned bongo flava "
        "into a glossy, Nigerian-facing 'Bongo' afrobeats and built the WCB Wasafi label, radio, and TV "
        "empire. 'Number One' (with Davido) announced him continentally, and a decade of collaborations "
        "made him the region's first true pan-African pop machine.",
        [
            ("Number One", "Diamond Platnumz"),
            ("Diamond Platnumz (East Africa's biggest pop star)", None),
            ("WCB Wasafi (Diamond's label & media empire)", None),
            ("Bongo flava goes continental (the afrobeats crossover)", None),
            ("Jeje & the Diamond hit machine", None),
            ("Pan-African collaborations (Lagos-Dar axis)", None),
        ],
    ),
    (
        "THE WASAFI & BONGO STARS (c. 2015-present)",
        "Around and beyond Diamond, a galaxy of Tanzanian stars ruled African streaming. Rayvanny's "
        "'Tetema' and Harmonize's 'Kwangwaru' were continental smashes; Mbosso crooned; Nandy reigned "
        "as the 'African princess'; and Zuchu's debut 'Sukari' shattered records for a female artist. "
        "Bongo was now a hit factory.",
        [
            ("Tetema", "Rayvanny"),
            ("Kwangwaru", "Harmonize"),
            ("Sukari", "Zuchu"),
            ("Mbosso (the Wasafi crooner)", None),
            ("Nandy (the African princess of bongo)", None),
            ("Bongo flava's streaming hit factory", None),
        ],
    ),
    (
        "SINGELI: TANZANIA'S HYPERSPEED SOUND (c. 2010-present)",
        "From the Manzese ghetto of Dar came SINGELI -- a frantic, 200-to-300-bpm dance music of "
        "breakneck beats and rapid-fire MCing, first a wedding-and-street sound, then a global club "
        "sensation via the Nyege Nyege / Sisso Studios scene. Sisso, Duke, Bamba Pana, and Msaga Sumu "
        "took it worldwide. Cross-link: global bass/electronic scenes.",
        [
            ("Singeli (Tanzania's 200-bpm street dance)", None),
            ("Sisso Studios & the Manzese singeli scene", None),
            ("Bamba Pana (singeli's global breakout)", None),
            ("Duke & Msaga Sumu (singeli MCs)", None),
            ("Nyege Nyege & the East African underground", None),
            ("Hyperspeed beats & rapid-fire MCing", None),
        ],
    ),
    (
        "KENYAN GENGETONE: THE SHENG STREET REVIVAL (c. 2018-present)",
        "A raw, rowdy revival of Sheng street rap swept Nairobi: GENGETONE, all shouted hooks and "
        "hard beats. Ethic's 'Lamba Lolo' kicked it off and Sailors' 'Wamlambez' became a nationwide "
        "chant (and a censorship flashpoint). Boondocks Gang, Mbogi Genje, and the Ochungulo Family "
        "carried the unfiltered energy. Content note: gengetone's lewd-lyric bans are kept in view.",
        [
            ("Lamba Lolo", "Ethic"),
            ("Wamlambez", "Sailors"),
            ("Gengetone (the raw Sheng street revival)", None),
            ("Boondocks Gang & Mbogi Genje", None),
            ("Ochungulo Family (gengetone crew)", None),
            ("Gengetone & the censorship battles", None),
        ],
    ),
    (
        "SAUTI SOL & THE KENYAN AFROPOP CROWN (c. 2011-present)",
        "Sauti Sol became Kenya's most beloved band and its biggest global ambassadors -- polished "
        "afropop harmonies with 'Sura Yako' (and its Lipala dance) and 'Suzanna' topping charts across "
        "the continent. They proved a Kenyan act could headline anywhere. Cross-link: West African "
        "Afrobeats, mirrored in Nairobi.",
        [
            ("Sura Yako", "Sauti Sol"),
            ("Suzanna", "Sauti Sol"),
            ("Sauti Sol (Kenya's afropop ambassadors)", None),
            ("The Lipala dance (Sura Yako's craze)", None),
            ("Kenyan band-pop goes continental", None),
            ("Bien & the Sauti Sol solo era", None),
        ],
    ),
    (
        "THE KENYAN NEW WAVE: RAP, R&B & CROSSOVER (c. 2015-present)",
        "A confident Kenyan mainstream matured: Nyashinski returned from the US to score with 'Mungu "
        "Pekee', Khaligraph Jones ('Mazishi') became the country's rap king and an African punchline "
        "heavyweight, and crooners like Otile Brown, Nviiri, and Nadia Mukami filled the airwaves. "
        "Kenyan pop finally had range.",
        [
            ("Mungu Pekee", "Nyashinski"),
            ("Mazishi", "Khaligraph Jones"),
            ("Nyashinski (the comeback king of Kenyan pop)", None),
            ("Khaligraph Jones (the OG, Kenyan rap heavyweight)", None),
            ("Otile Brown & the Kenyan R&B wave", None),
            ("Nadia Mukami & Nviiri (the new crooners)", None),
        ],
    ),
    (
        "UGANDA, RWANDA & THE WIDER REGION GO GLOBAL (c. 2014-present)",
        "Uganda's Eddy Kenzo turned 'Sitya Loss' into a worldwide viral hit (and a BET Award), Sheebah "
        "and Fik Fameica ruled Kampala, and the Nyege Nyege festival made Uganda an underground magnet. "
        "Rwanda's Bruce Melodie and The Ben joined the regional pop boom. Content note: Uganda's fraught "
        "music-and-politics (Bobi Wine) stays flagged.",
        [
            ("Sitya Loss", "Eddy Kenzo"),
            ("Eddy Kenzo (Uganda's global breakout)", None),
            ("Sheebah & Fik Fameica (Kampala pop)", None),
            ("Bruce Melodie & The Ben (Rwanda's pop wave)", None),
            ("Nyege Nyege festival (Kampala, the underground magnet)", None),
            ("Kidandali & the Ugandan streaming scene", None),
        ],
    ),
    (
        "CROSS-BORDER & THE GLOBAL EAST AFRICA (c. 2018-present)",
        "The region's music now flows both ways across Africa. Sho Madjozi's 'John Cena' (a South "
        "African Tsonga hit) swept East Africa, amapiano and Afrobeats crossed in from the south and "
        "west, and East African artists and their diaspora went fully global on streaming. Cross-links: "
        "the West African Afrobeats and South African amapiano surveys; the five-installment East "
        "African arc, from taarab to TikTok.",
        [
            ("John Cena", "Sho Madjozi"),
            ("Amapiano & Afrobeats cross into East Africa", None),
            ("Sho Madjozi's cross-border hit (flagged South African)", None),
            ("The East African diaspora goes global", None),
            ("Streaming, YouTube & TikTok (the new East African pop)", None),
            ("From taarab to the algorithm (the East African arc)", None),
        ],
    ),
]

STEM = "ssa_east_music_5_STREAMING_ERA_GLOBAL"


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
