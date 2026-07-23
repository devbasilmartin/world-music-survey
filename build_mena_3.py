#!/usr/bin/env python3
"""Build MENA, installment 3: Persian (Iranian) Classical & Pop.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
NOTE: do NOT reuse a bare "Ney (...)" title (collides with #1's ney line).
"""

TITLE = ("The Story of Middle Eastern & North African Music — Installment 3: "
         "Persian (Iranian) Classical & Pop")

FRAMING = (
    "Persian music is a world unto itself -- related to the Arab maqam but built on its own DASTGAH "
    "system and its own soul. Its classical art rests on the RADIF, a vast memorized canon of melodic "
    "units (gushe) organized into twelve modal systems, realized above all in the AVAZ: a non-metric, "
    "improvised vocal art of breathtaking ornament (tahrir) wedded to the greatest classical poetry on "
    "Earth -- Hafez, Rumi, Saadi. Its supreme voice was MOHAMMAD-REZA SHAJARIAN. In the 20th century a "
    "modern pop was born (Vigen, the 'father of Persian pop') and flowered into a golden age of "
    "superstars -- GOOGOOSH, Dariush, Hayedeh -- until the 1979 Islamic Revolution banned pop music and "
    "silenced the female solo voice, scattering artists into exile. From Los Angeles the diaspora "
    "rebuilt a whole pop industry ('Tehrangeles'), beamed back home; and inside Iran, an underground of "
    "rock and rap, and protest anthems like 'Baraye', kept a defiant music alive. Cross-links: the "
    "shared-yet-distinct maqam/dastgah family (#1, #4); Persian mystic poetry & Sufism; the diaspora "
    "reaching the US. Content notes: the revolution, censorship, and the ban on women's solo singing are "
    "kept factual and with care. Names transliterated. Region: Iran & the Persian diaspora."
)

SECTIONS = [
    (
        "THE DASTGAH SYSTEM & THE RADIF",
        "Persian classical music is organized into twelve DASTGAH and avaz -- modal systems, each a "
        "collection of melodic figures (gushe) drawn from the RADIF, the great memorized repertoire "
        "passed master to student. Related to the Arab maqam but distinct in its intervals and feeling, "
        "it is among the most refined modal systems in the world. Cross-link: the maqam/makam/dastgah "
        "family.",
        [
            ("Dastgah (the Persian modal system)", None),
            ("The radif (the memorized classical canon)", None),
            ("Gushe (the melodic units of the radif)", None),
            ("Dastgah-e Shur, Mahur & Homayun (the core systems)", None),
            ("Segah, Chahargah & the avaz modes", None),
        ],
    ),
    (
        "THE AVAZ & THE POETRY",
        "The heart of Persian classical music is the AVAZ -- a free, non-metric vocal improvisation "
        "adorned with tahrir, a rippling nightingale-like ornament -- set to the immortal classical "
        "poets. To sing avaz is to interpret Hafez, Rumi, Saadi, and Khayyam; music and mystic poetry "
        "are inseparable here.",
        [
            ("Avaz (the non-metric vocal improvisation)", None),
            ("Tahrir (the nightingale vocal ornament)", None),
            ("Poetry & song (Hafez, Rumi, Saadi in the avaz)", None),
            ("Music as sung Persian mysticism", None),
        ],
    ),
    (
        "THE PERSIAN INSTRUMENTS",
        "The classical ensemble is intimate and silvery: the long-necked TAR and SETAR lutes, the "
        "hammered-dulcimer SANTUR, the spike-fiddle KAMANCHEH, and the winds and percussion (ney, "
        "tombak, daf). Each has a delicate, deeply expressive voice suited to the avaz and the radif.",
        [
            ("Tar & setar (the Persian long-necked lutes)", None),
            ("Santur (the Persian hammered dulcimer)", None),
            ("Kamancheh (the Persian spike-fiddle)", None),
            ("Ney, tombak & daf (the Persian winds & percussion)", None),
            ("The intimate Persian classical ensemble", None),
        ],
    ),
    (
        "THE CLASSICAL MASTERS (c. 1960-present)",
        "The 20th century brought a great classical revival. Mohammad-Reza Shajarian, the supreme "
        "vocalist, made 'Morgh-e Sahar' (Bird of Dawn) an anthem of freedom; Hossein Alizadeh (tar) and "
        "Kayhan Kalhor (kamancheh) renewed the instrumental art, and Parisa and Mohammad Reza Lotfi "
        "carried the tradition. Content note: Shajarian was banned from state media after 2009.",
        [
            ("Morgh-e Sahar (Bird of Dawn)", "Mohammad-Reza Shajarian"),
            ("Mohammad-Reza Shajarian (the supreme Persian vocalist)", None),
            ("Hossein Alizadeh & Kayhan Kalhor (the instrumental masters)", None),
            ("Parisa & Mohammad Reza Lotfi (the classical revival)", None),
            ("The Persian classical revival (the radif preserved)", None),
        ],
    ),
    (
        "VIGEN & THE BIRTH OF PERSIAN POP (c. 1950-1965)",
        "Modern Persian pop began with Vigen -- an Armenian-Iranian crooner, the 'Sultan of Jazz', who "
        "brought the guitar and Western song forms to Persian music in the 1950s. He is remembered as "
        "the father of Persian pop, opening the door to the golden age that followed.",
        [
            ("Vigen (the father of Persian pop)", None),
            ("Western guitar & song enter Persian music (the 1950s)", None),
            ("Mahtab (a Vigen classic)", None),
            ("The birth of the modern Persian pop song", None),
        ],
    ),
    (
        "THE GOLDEN-AGE POP & THE DIVAS (c. 1965-1979)",
        "Pre-revolution Tehran roared with pop. Googoosh became a superstar and style icon ('Talagh'); "
        "Dariush sang the social conscience of a generation ('Booye Gandom'); and the great voices of "
        "Hayedeh ('Soghati'), Ebi, Mahasti, and Sattar filled the airwaves. It was a cosmopolitan, "
        "confident, and glamorous pop era.",
        [
            ("Talagh (Divorce)", "Googoosh"),
            ("Booye Gandom (Scent of Wheat)", "Dariush"),
            ("Soghati", "Hayedeh"),
            ("Googoosh (the superstar diva & style icon)", None),
            ("Ebi, Mahasti & Sattar (the golden-age pop stars)", None),
            ("Cosmopolitan Tehran pop (the pre-revolution boom)", None),
        ],
    ),
    (
        "THE 1979 REVOLUTION & THE RUPTURE",
        "The 1979 Islamic Revolution transformed everything. Pop music was banned as decadent, and women "
        "were prohibited from singing solo before mixed or male audiences -- silencing an entire "
        "generation of divas overnight. Many artists fled abroad; classical music was more tolerated as "
        "'authentic'. Content note: this is one of modern music's starkest ruptures, kept factual and "
        "with care.",
        [
            ("Pop music banned (the 1979 revolution)", None),
            ("The female solo voice silenced (content note)", None),
            ("Artists into exile (the great scattering)", None),
            ("Classical music semi-tolerated (the surviving tradition)", None),
            ("The rupture of 1979 (a generation silenced)", None),
        ],
    ),
    (
        "TEHRANGELES: THE DIASPORA POP (c. 1980-present)",
        "In exile the Persian pop industry was reborn in Los Angeles -- 'Tehrangeles' -- and beamed back "
        "into Iran on smuggled cassettes and satellite TV. Googoosh returned to the stage in 2000 after "
        "two decades of silence; Andy, Shahram Shabpareh, and a glossy LA pop kept the diaspora dancing "
        "and homesick at once. Cross-link: the Iranian diaspora in America.",
        [
            ("Tehrangeles (the Los Angeles Persian pop industry)", None),
            ("Googoosh returns (the 2000 comeback from silence)", None),
            ("Satellite TV & smuggled cassettes (diaspora pop reaches Iran)", None),
            ("Andy & Shahram Shabpareh (the LA-Persian pop sound)", None),
            ("Exile & homesickness in the diaspora song", None),
        ],
    ),
    (
        "INSIDE IRAN: UNDERGROUND & PROTEST (c. 1998-present)",
        "Inside Iran a defiant music persists. An underground of rock, rap, and metal (Hichkas, the "
        "'father of Persian rap'; Kiosk; O-Hum) records outside the state, beside an 'authorized' "
        "permitted pop. And in 2022 Shervin Hajipour's 'Baraye' became the anthem of the "
        "'Woman, Life, Freedom' protests, winning a Grammy. Content note: he was detained; kept factual "
        "and with care.",
        [
            ("Baraye", "Shervin Hajipour"),
            ("Hichkas (the father of Persian rap, underground)", None),
            ("Kiosk & O-Hum (the Iranian underground rock)", None),
            ("Authorized pop versus the underground (inside Iran)", None),
            ("Music as protest (Woman, Life, Freedom, 2022)", None),
        ],
    ),
]

STEM = "mena_music_3_PERSIAN_CLASSICAL_POP"


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
