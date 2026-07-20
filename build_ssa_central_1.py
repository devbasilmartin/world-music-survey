#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Central, installment 1: Congolese Rumba's Roots & Birth.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1930s-1957.
First installment of the Central Africa region. Dedup is by TITLE only.
"""

TITLE = ("The Story of Central African Music — Installment 1: "
         "Congolese Rumba's Roots & Birth (c. 1930-1957)")

FRAMING = (
    "No African music has travelled further or shaped more of the continent than CONGOLESE RUMBA -- "
    "and this installment tells how it was born. The deep layer is the folkloric music of the Congo "
    "basin: the LIKEMBE (thumb-piano), the interlocking forest polyphony of the BaAka, and the Kongo, "
    "Luba, and Mongo traditions whose rhythmic and cosmological DNA had already crossed the Atlantic "
    "with the slave trade to seed Cuban and Haitian music. Then, in one of history's great musical "
    "round-trips, that DNA came home: in the 1930s-40s, His Master's Voice 'GV' 78s of Cuban SON "
    "flooded Leopoldville, and Congolese musicians -- hearing a familiar clave -- localized it as "
    "'rumba'. Fused with coastal palm-wine guitar and the accordion, and cut on the new Greek-owned "
    "labels (Ngoma, Opika, Loningisa), it produced its first star in 1948: Wendo Kolosoy, whose "
    "'Marie-Louise' was so hypnotic it was rumoured to raise the dead. By the mid-1950s Joseph "
    "Kabasele's African Jazz and a young guitarist named Franco were assembling the bands that would "
    "detonate the golden age (Installment 2). Cross-links: Cuban son (Latin survey) -> Congo rumba -> "
    "back out across West, East, and Southern Africa (it is the Congo guitar that seeds them all). "
    "Content note: this is music made under the brutal Belgian colonial Congo, heir to Leopold II's "
    "atrocities -- kept with context. Region: DR Congo & Congo-Brazzaville. Many roots-era entries are "
    "'(Traditional)' or descriptor bare titles to search."
)

SECTIONS = [
    (
        "THE DEEP CONGO: FOLKLORIC ROOTS",
        "Beneath everything lies the vast folkloric music of the Congo basin: the LIKEMBE lamellophone, "
        "the astonishing hocketed forest polyphony of the BaAka ('Pygmy') communities, Kongo and Luba "
        "drumming and song, and the lokole slit-drum. Cross-link: Kongo religious and rhythmic "
        "structures crossed the Atlantic centuries earlier to shape Cuban, Haitian, and Brazilian "
        "sacred music (Latin survey) -- so the son that returns here is, in a sense, a distant cousin "
        "coming home.",
        [
            ("Likembe / sanza (Congo thumb-piano)", None),
            ("BaAka forest polyphony (Aka hocketing)", None),
            ("Kongo ngoma drumming and song", None),
            ("Luba and Mongo traditional song", None),
            ("Kongo cosmology song (slave-trade diaspora root)", None),
            ("Lokole (Congo talking slit-drum)", None),
        ],
    ),
    (
        "THE CUBAN SPARK: THE 'GV' SON RECORDS ARRIVE (c. 1930-1948)",
        "The catalyst came on shellac. His Master's Voice sold its 'GV' series of Cuban SON records "
        "across the Congo, and their clave, guitars, and call-and-response felt instantly familiar to "
        "Congolese ears. Musicians adopted the sound and called it 'rumba' (after the label term), "
        "learning the son template that would underpin everything after. Cross-link: this is the son "
        "cubano of the Latin America survey, boomeranging back to Africa.",
        [
            ("Cuban son 78s (HMV 'GV' series in Congo)", None),
            ("Rumba (the Congolese name for the son-derived dance)", None),
            ("Maracas and clave enter Congo", None),
            ("Cuban son craze reaches Leopoldville", None),
        ],
    ),
    (
        "THE COASTAL GUITAR, MARINGA & THE ACCORDION (c. 1930-1948)",
        "Alongside the records came instruments and styles from the coast: the palm-wine/maringa guitar "
        "drifting down the Atlantic seaboard, the 'Hawaiian' slide guitar, and the accordion of the "
        "early rumba dance (associated with the pioneer Feruzi). These fused with likembe melody to "
        "make the first Congolese urban pop. Cross-link: the same coastal guitar economy as the West "
        "Africa survey's palm-wine chapter.",
        [
            ("Maringa (coastal palm-wine guitar reaches Congo)", None),
            ("Hawaiian-style guitar (early Congo pop)", None),
            ("Accordion rumba (Feruzi's dance)", None),
            ("Likembe-and-guitar transition", None),
            ("Congo bar music (1940s Leopoldville)", None),
        ],
    ),
    (
        "WENDO KOLOSOY & THE BIRTH OF RUMBA (Leopoldville, 1948-1957)",
        "In 1948 Antoine 'Wendo' Kolosoy cut 'Marie-Louise' with guitarist Henri Bowane -- the first "
        "great Congolese rumba hit, so bewitching that rumour said playing it could raise the dead, and "
        "the Catholic church briefly had Wendo jailed. Adou Elenga's 'Ata Ndele' ('sooner or later') "
        "smuggled in a note of anti-colonial hope, and across the river in Brazzaville Paul Kamba was a "
        "pioneer too. Content note: made under Belgian colonial rule.",
        [
            ("Marie-Louise", "Wendo Kolosoy"),
            ("Ata Ndele", "Adou Elenga"),
            ("Paul Kamba (Brazzaville rumba pioneer)", None),
            ("Antoine Moundanda (likembe rumba)", None),
            ("Wendo Kolosoy & Victoria Bakolo Miziki", None),
            ("Congo rumba (the Leopoldville sound is born)", None),
        ],
    ),
    (
        "THE LABELS & THE STUDIO SCENE (Ngoma, Opika, Loningisa)",
        "A recording industry sprang up almost overnight, built by Greek and Portuguese traders: Ngoma "
        "(Nicolas Jeronimidis), Opika, Loningisa, and CEFA cut thousands of rumba sides and employed "
        "house bands that trained a generation. Manuel d'Oliveira and others were early stars. Content "
        "note: the musicians who made these hits were typically paid flat fees while the labels kept the "
        "profits -- the same exploitation seen across the African surveys.",
        [
            ("Ngoma label rumba (Leopoldville)", None),
            ("Opika label rumba", None),
            ("Loningisa studio house band", None),
            ("Manuel d'Oliveira (Ngoma pioneer)", None),
            ("CEFA and the Greek-owned record labels", None),
            ("Leopoldville session-guitarist scene (1950s)", None),
        ],
    ),
    (
        "THE NEXT GENERATION EMERGES (early Kalle & Franco, c. 1953-1957)",
        "The pieces of the golden age were falling into place. In 1953 Joseph Kabasele -- 'Le Grand "
        "Kalle' -- founded African Jazz, the first modern Congolese band; and a teenage guitar prodigy, "
        "Franco Luambo, was cutting his first sides at Loningisa. The electric guitar arrived (via "
        "players like Bill Alexandre), and the classic rumba template -- with its accelerating dance "
        "section -- was set. This is the launch pad for Installment 2.",
        [
            ("Para Fifi", "Joseph Kabasele"),
            ("African Jazz forms (Kabasele, 1953)", None),
            ("Young Franco at Loningisa (pre-OK Jazz)", None),
            ("Bill Alexandre and the electric guitar arrives", None),
            ("Toward the rumba golden age (the odemba template)", None),
        ],
    ),
]

STEM = "ssa_central_music_1_RUMBA_ROOTS_BIRTH"


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
