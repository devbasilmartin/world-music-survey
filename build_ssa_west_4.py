#!/usr/bin/env python3
"""Build Sub-Saharan Africa: West, installment 4: Juju & Fuji Explode (c. 1965-1980).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file.
"""

TITLE = ("The Story of West African Music — Installment 4: "
         "Juju & Fuji Explode + Congo-Inflected Guitar Pop (c. 1965-1980)")

FRAMING = (
    "As highlife's horn-driven dance bands fade after the Biafran war, southwestern Nigeria's Yoruba "
    "country becomes the engine room of West African pop. JUJU -- the guitar-and-talking-drum praise "
    "music seeded back in Installment 2 -- is modernized by I.K. Dairo, then blown up into a stadium "
    "spectacle by King Sunny Ade (armies of guitars, pedal steel, synthesizer) and given a "
    "philosopher's voice by Chief Commander Ebenezer Obey. Out of Yoruba Muslim WERE (Ramadan "
    "wake-up drumming) a wholly percussion-and-voice music, FUJI, is born and named by Sikiru Ayinde "
    "Barrister, with Ayinla Kollington as his great rival -- while the older APALA and SAKARA masters "
    "(Haruna Ishola, Ayinla Omowura) still command huge audiences. Meanwhile a Congo-inflected "
    "GUITAR POP sweeps the coast, and in 1976 a half-Cameroonian bandleader in eastern Nigeria cuts "
    "'Sweet Mother', reputedly the best-selling African single of all time. Cross-links: juju's pedal "
    "steel comes from American country and Hawaiian guitar (US survey); the soukous tide points to the "
    "coming Central Africa survey. Region: named artists are Nigerian (one Nigerian-Cameroonian, "
    "flagged); content notes are kept."
)

SECTIONS = [
    (
        "I.K. DAIRO: THE FATHER OF MODERN JUJU (c. 1957-1972)",
        "I.K. Dairo remade juju for the independence era, adding the accordion and pushing the Yoruba "
        "talking drum to the front, and became the first African musician appointed MBE by the Queen. "
        "His Blue Spots' warm, devotional sound is the template every later juju star built on. Search "
        "his classic 1960s sides.",
        [
            ("Salome", "I.K. Dairo"),
            ("Mo Sorire", "I.K. Dairo"),
            ("Ka Sora", "I.K. Dairo"),
            ("I.K. Dairo & his Blue Spots (accordion-and-talking-drum juju)", None),
            ("Juju modernized (late-1950s Yoruba, Dairo era)", None),
        ],
    ),
    (
        "KING SUNNY ADÉ: SYNCRO-SYSTEM JUJU (c. 1967-1983)",
        "King Sunny Ade turned juju into a vast, hypnotic orchestra -- a dozen guitars, banks of "
        "talking drums, and the shimmering pedal-steel and synthesizer that became his signature. By "
        "the early 1980s Island Records was marketing him as 'the African Bob Marley'. Cross-link: the "
        "pedal-steel guitar he adopted came from American country and Hawaiian music. (Scope note: "
        "'Ja Funmi' and 'Synchro System' are 1982-83, just past this window, but define the sound built "
        "in the 1970s -- kept here, and flagged.)",
        [
            ("Sunny Ti De", "King Sunny Ade"),
            ("Challenge Cup", "King Sunny Ade"),
            ("E Kilo F'omo Ode", "King Sunny Ade"),
            ("Ja Funmi", "King Sunny Ade"),
            ("Synchro System", "King Sunny Ade"),
        ],
    ),
    (
        "EBENEZER OBEY: PHILOSOPHICAL JUJU & THE MILIKI SOUND (c. 1968-1980)",
        "Chief Commander Ebenezer Obey was Sunny Ade's great rival and opposite: where Ade dazzled, "
        "Obey preached, weaving Yoruba proverbs, Christian faith, and gentle social counsel into his "
        "flowing 'miliki' juju with the Inter-Reformers Band. Search his long medley sides.",
        [
            ("Board Members", "Ebenezer Obey"),
            ("Ketekete", "Ebenezer Obey"),
            ("Aimasiko", "Ebenezer Obey"),
            ("Miliki juju (Obey's Inter-Reformers style)", None),
        ],
    ),
    (
        "FUJI IS BORN: WERE, BARRISTER & KOLLINGTON (c. 1965-1980)",
        "A new, guitar-less music rose from the mosque: WERE (also ajiwere/ajisari), the percussion and "
        "chant used to wake the faithful during Ramadan, was secularized and named FUJI by Sikiru "
        "Ayinde Barrister, with Ayinla Kollington as his fierce rival. All voice, talking drums, and "
        "sakara -- fuji becomes the dominant Yoruba street music for decades. Search Barrister's 'Fuji "
        "Garbage' series.",
        [
            ("Fuji Garbage", "Sikiru Ayinde Barrister"),
            ("Barrister fuji (Ajisari/were roots)", None),
            ("Ayinla Kollington fuji (the great rivalry)", None),
            ("Were (Ramadan wake-up music, Yoruba Muslim)", None),
            ("Ajiwere / Ajisari (dawn Ramadan drumming)", None),
        ],
    ),
    (
        "THE YORUBA ROOTS STARS: APALA & SAKARA (c. 1965-1980)",
        "The older Yoruba genres were still commercial giants. Haruna Ishola made APALA -- talking "
        "drums, agidigbo, and dense proverb-lyrics -- a national sound; Ayinla Omowura's raw Abeokuta "
        "apala had a vast working-class following; and Yusuf Olatunji kept SAKARA alive. Content note: "
        "Ayinla Omowura was murdered in 1980 at the height of his fame.",
        [
            ("Oroki Social Club", "Haruna Ishola"),
            ("Apala rhythm (Ishola/Omowura era)", None),
            ("Ayinla Omowura (Abeokuta apala)", None),
            ("Yusuf Olatunji (Yoruba sakara)", None),
            ("Goje fiddle in sakara (Yoruba)", None),
        ],
    ),
    (
        "GUITAR-POP, THE CONGO TIDE & THE BIGGEST SONG IN AFRICA (c. 1965-1980)",
        "Outside the Yoruba heartland, a Congo-inflected GUITAR POP swept the coast. Sir Victor Uwaifo "
        "scored Nigeria's first gold record with the Edo-highlife 'Joromi'; Ghana's C.K. Mann renewed "
        "guitar highlife; and in 1976 Prince Nico Mbarga's 'Sweet Mother' -- highlife with a "
        "Congolese-style guitar lilt -- became reputedly the best-selling single in African history. "
        "(Scope note: Prince Nico Mbarga was Nigerian-Cameroonian and Nigeria-based -- kept as West "
        "African, and flagged.) Cross-link: the soukous guitar tide leads to the Central Africa survey.",
        [
            ("Joromi", "Sir Victor Uwaifo"),
            ("Guitar Boy", "Sir Victor Uwaifo"),
            ("Sweet Mother", "Prince Nico Mbarga"),
            ("Congo soukous crossing west (the guitar-band tide)", None),
            ("C.K. Mann (Ghanaian guitar highlife)", None),
            ("Edo / Bendel guitar highlife (Nigeria)", None),
        ],
    ),
]

STEM = "ssa_west_music_4_JUJU_FUJI_GUITARPOP"


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
