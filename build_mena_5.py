#!/usr/bin/env python3
"""Build MENA, installment 5: The Maghreb -- Andalusian, Chaabi, Rai, Gnawa & Amazigh.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Middle Eastern & North African Music — Installment 5: "
         "The Maghreb — Andalusian, Chaabi, Rai, Gnawa & Amazigh")

FRAMING = (
    "The Maghreb -- Morocco, Algeria, Tunisia -- braids together Andalusian refinement, Arab and Berber "
    "roots, and a deep sub-Saharan African undertow. It preserved the ANDALUSIAN classical music lost "
    "when Muslim Spain fell (the malouf, gharnati, and al-ala nuba suites); it built the poetic urban "
    "CHAABI of the Algiers Casbah (El Anka; Dahmane El Harrachi's emigrant anthem 'Ya Rayah'); and out "
    "of Oran it forged RAI -- from Cheikha Rimitti's raw Bedouin roots to a synth-driven global "
    "explosion with Cheb Khaled's 'Didi' and 'Aicha'. Morocco gave the world GNAWA, the hypnotic "
    "sub-Saharan-descended trance music of the guembri, and the poetic folk-fusion of Nass El Ghiwane; "
    "and the BERBER/Amazigh peoples their own proud song, from Idir's global 'A Vava Inouva' to the "
    "Kabyle protest tradition. Cross-links: al-Andalus (#1) & flamenco (Europe survey); Gnawa's roots in "
    "the Sahel/West Africa surveys; the huge Maghrebi diaspora in France. Content note: the Algerian "
    "civil war of the 1990s, in which rai singers (Cheb Hasni) and the Kabyle voice Matoub Lounes were "
    "assassinated, is kept factual and with care. Names transliterated. Region: North Africa (the "
    "Maghreb) & its French diaspora."
)

SECTIONS = [
    (
        "THE ANDALUSIAN LEGACY IN NORTH AFRICA",
        "When Muslim Spain fell, its sophisticated court music migrated south and survived in the "
        "Maghreb as living classical traditions: the malouf of Tunisia, the gharnati and sanaa of "
        "Algeria, and the al-ala of Morocco -- all performing the great Andalusian NUBA suite. It is a "
        "direct inheritance of the world Ziryab built. Cross-link: al-Andalus (#1) & flamenco.",
        [
            ("The Andalusian nuba in the Maghreb (the surviving suite)", None),
            ("Malouf (the Tunisian Andalusian tradition)", None),
            ("Gharnati & sanaa (the Algerian Andalusian schools)", None),
            ("Al-ala (the Moroccan Andalusian classical music)", None),
            ("Andalusian music preserved after 1492 (the Maghreb inheritance)", None),
        ],
    ),
    (
        "ALGERIAN CHAABI",
        "In the Casbah of Algiers, El Hadj M'Hamed El Anka forged CHAABI ('popular') -- a poetic urban "
        "song built from Andalusian and folk roots on the mandole and banjo. Dahmane El Harrachi's 'Ya "
        "Rayah', an aching anthem of emigration, became one of the most beloved and widely covered songs "
        "of the whole Maghreb.",
        [
            ("Ya Rayah (O Emigrant)", "Dahmane El Harrachi"),
            ("El Hadj M'Hamed El Anka (the father of chaabi)", None),
            ("Chaabi (the poetic urban song of Algiers)", None),
            ("The mandole & banjo in chaabi", None),
            ("The Casbah of Algiers (the chaabi world)", None),
        ],
    ),
    (
        "THE ROOTS OF RAI",
        "RAI was born in the fields and dive bars around Oran, sung by the cheikhs and, scandalously, "
        "the cheikhas -- women like the legendary CHEIKHA RIMITTI, the 'mother of rai', whose raw, frank "
        "songs of love, drink, and hardship defied every taboo. This is rai's earthy, rebellious "
        "bedrock. Content note: its frank subject matter long drew censure.",
        [
            ("Cheikha Rimitti (the mother of rai)", None),
            ("Rai (the rebellious song of Oran)", None),
            ("The cheikhas (the women singers of rai)", None),
            ("Bedouin & meddahat roots of rai", None),
            ("Frank, defiant lyrics (rai's earthy bedrock)", None),
        ],
    ),
    (
        "POP-RAI GOES GLOBAL (c. 1980-2000)",
        "In the 1980s rai plugged in -- synths, drum machines, and pop production turned it into a "
        "youth phenomenon. Chaba Fadela & Cheb Sahraoui's 'N'sel Fik' launched pop-rai; then Cheb "
        "Khaled, the 'King of Rai', broke worldwide with 'Didi' (1992) and the gorgeous 'Aicha'; and "
        "Cheb Mami, the 'Prince of Rai', took it further still. Cross-link: rai on the world charts.",
        [
            ("N'sel Fik (You Are Mine)", "Chaba Fadela"),
            ("Didi", "Cheb Khaled"),
            ("Aicha", "Cheb Khaled"),
            ("Cheb Khaled (the King of Rai)", None),
            ("Cheb Mami (the Prince of Rai)", None),
            ("Pop-rai (the electric global sound)", None),
        ],
    ),
    (
        "RAI & THE ALGERIAN TRAGEDY (c. 1990-2000)",
        "Rai's rise collided with catastrophe. During Algeria's civil war, Islamist extremists targeted "
        "its stars: the beloved sentimental singer Cheb Hasni -- 'the martyr of rai' -- was assassinated "
        "in Oran in 1994, and the producer Rachid Baba-Ahmed in 1995. Many artists fled to France. "
        "Content note: this violence is kept factual and with care.",
        [
            ("Cheb Hasni (the martyr of rai, d. 1994)", None),
            ("The Algerian civil war & the targeting of musicians", None),
            ("Rachid Baba-Ahmed (the rai producer, d. 1995)", None),
            ("Rai in exile (the flight to France)", None),
            ("Sentimental love-rai (the Cheb Hasni style)", None),
        ],
    ),
    (
        "MOROCCAN GNAWA: TRANCE & THE GUEMBRI",
        "GNAWA music descends from sub-Saharan Africans brought to Morocco -- a hypnotic ritual music of "
        "healing and trance (the all-night lila / derdeba) built on the deep three-string guembri bass "
        "lute and clashing qraqeb castanets, led by a maalem (master) who summons the mluk (spirits). "
        "Maalem Mahmoud Guinia was its great figure. Cross-link: sub-Saharan roots (the Sahel/West "
        "Africa surveys); the Essaouira festival & jazz fusion.",
        [
            ("Gnawa (the Moroccan trance music)", None),
            ("The guembri & qraqeb (the Gnawa instruments)", None),
            ("The lila / derdeba (the all-night trance ceremony)", None),
            ("Maalem Mahmoud Guinia (the Gnawa master)", None),
            ("Gnawa's sub-Saharan roots (cross-link)", None),
            ("Gnawa meets jazz & the Essaouira festival", None),
        ],
    ),
    (
        "MOROCCAN CHAABI & THE GHIWANE GENERATION",
        "Morocco's popular music surged in the 1970s with Nass El Ghiwane -- the 'Rolling Stones of "
        "Africa' -- who fused Gnawa, Sufi, and Amazigh roots with poetic, socially charged lyrics into a "
        "new folk-protest sound, followed by Jil Jilala. The older aita and malhun song traditions "
        "endured beneath them.",
        [
            ("Nass El Ghiwane (the Rolling Stones of Africa)", None),
            ("Jil Jilala (the Moroccan folk-fusion band)", None),
            ("Moroccan chaabi (the popular song)", None),
            ("Aita & malhun (the older Moroccan traditions)", None),
            ("Poetic protest folk (the Ghiwane generation)", None),
        ],
    ),
    (
        "BERBER / AMAZIGH MUSIC",
        "The Berbers (Amazigh) -- North Africa's indigenous peoples -- carry their own proud musical "
        "world. The Kabyle singer Idir made 'A Vava Inouva' (1976) a global Berber anthem; the Kabyle "
        "song became a vehicle of identity and protest (its hero Matoub Lounes assassinated in 1998); "
        "and the Chleuh of the Souss sing their own. Cross-link: the Tuareg-Amazigh thread of the Sahel "
        "survey.",
        [
            ("A Vava Inouva", "Idir"),
            ("Kabyle song (the Amazigh music of identity)", None),
            ("Matoub Lounes (the Kabyle protest singer, d. 1998)", None),
            ("Chleuh / Souss music (the southern Amazigh)", None),
            ("The Amazigh-Tuareg thread (cross-link to the Sahel)", None),
        ],
    ),
    (
        "THE MAGHREB IN FRANCE & THE ROAD AHEAD",
        "France became the Maghreb's second home. Rai stars settled in Paris, the 'beur' (French-Arab) "
        "generation grew up between worlds, and Rachid Taha fused rock and chaabi (his blazing cover of "
        "'Ya Rayah'), opening a path to today's French-Maghreb rap. Cross-link: toward modern pan-Arab "
        "pop and the region today (#6).",
        [
            ("Rachid Taha (the Franco-Algerian rocker)", None),
            ("The Maghrebi diaspora in France (the beur generation)", None),
            ("Rai & chaabi in Paris (the second home)", None),
            ("Toward French-Maghreb rap (roads ahead)", None),
            ("The Maghreb's global reach (the diaspora sound)", None),
        ],
    ),
]

STEM = "mena_music_5_MAGHREB_RAI_GNAWA_AMAZIGH"


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
