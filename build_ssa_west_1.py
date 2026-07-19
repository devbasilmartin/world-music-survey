#!/usr/bin/env python3
"""Build Sub-Saharan Africa: West, installment 1: Griot / Mande Roots (deep-traditional layer).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file (living tradition / no single definitive recording).
First installment of the West Africa region.
"""

TITLE = ("The Story of West African Music — Installment 1: "
         "Griot / Mande Roots (the deep-traditional layer)")

FRAMING = (
    "This is the taproot -- not only of West African music, but, through the transatlantic slave "
    "trade, of much of the music in the United States and Latin American surveys as well. West Africa "
    "has no single ancient 'classical' notation like Europe's; its deepest layer is an ORAL art of "
    "extraordinary sophistication, carried by hereditary professional musicians. Chief among them is "
    "the MANDE JELI (in French, GRIOT): a caste of historian-praise-singer-instrumentalists who have "
    "kept the memory of the empire of Mali since the days of Sundiata Keita (c. 1235). Their harp-lute "
    "the KORA, their xylophone the BALAFON, and their lute the NGONI (the banjo's ancestor) are among "
    "the world's great instruments. Because this layer is oral and living, we represent it honestly "
    "through modern recordings by master tradition-bearers -- and many entries are '(Traditional)' "
    "bare titles you will need to search for a version you like. This installment also reaches beyond "
    "the Mande to the Wolof, Fula, Hausa, Yoruba, and Akan traditions, and closes on the Atlantic "
    "cross-links -- the akonting that becomes the banjo, the Mande pentatonic behind the blues, and "
    "the Yoruba orisha drums that become Cuban batá and Brazilian candomblé. Content note: that "
    "transmission is inseparable from slavery, and is kept with its context. Region: all artists are "
    "West African (Mali, Guinea, Gambia, Senegal, Nigeria, Ghana); judgment calls are flagged."
)

SECTIONS = [
    (
        "THE JELI (GRIOT) & THE EPIC OF OLD MALI",
        "The jeli is a hereditary word-and-music specialist: genealogist, praise-singer, diplomat, and "
        "keeper of the SUNJATA epic -- the founding story of the Mali empire and its hero Sundiata "
        "Keita (c. 1235), still recited today. The core praise-pieces ('Sunjata', 'Lambang', 'Duga') "
        "are centuries old and belong to the whole tradition; the kora classic 'Kaira' was composed by "
        "Sidiki Diabate, 'the king of the kora'. Living oral tradition -- search a griot recording.",
        [
            ("Sunjata (the Mande epic of Sundiata Keita)", None),
            ("Lambang (jeli praise-piece for the Keita line)", None),
            ("Duga (the vulture -- praise song for heroes)", None),
            ("Tutu Jara (classic Mande praise song)", None),
            ("Kaira", "Sidiki Diabate"),
            ("Jarabi", "Toumani Diabate"),
        ],
    ),
    (
        "THE KORA: THE 21-STRING HARP OF THE MANDE",
        "The kora -- a 21-string harp-lute over a calabash -- is the sound most associated with the "
        "griot, spread across Mali, Guinea, Gambia, and Senegal in distinct family lineages. Toumani "
        "Diabate brought it to the world's concert halls; the Gambian Konte and Jobarteh dynasties "
        "keep the western style; and Sona Jobarteh became the first woman from a griot family to make "
        "the kora her profession. (Scope note: Sona Jobarteh was raised in Britain but is of the "
        "Gambian griot lineage -- kept as West African, and flagged.)",
        [
            ("Alla l'a ke", "Toumani Diabate & Ballake Sissoko"),
            ("Bafoulabe", "Ballake Sissoko"),
            ("Cantelowes", "Toumani Diabate"),
            ("Kelefaba (epic of Kelefa Saane)", "Alhaji Bai Konte"),
            ("Mamadou Bitiki", "Amadu Bansang Jobarteh"),
            ("Gambia", "Sona Jobarteh"),
        ],
    ),
    (
        "THE BALAFON & THE NGONI: VOICES OF WOOD AND STRING",
        "Older even than the kora are the balafon -- a gourd-resonated xylophone whose sacred ancestor, "
        "the SOSSO BALA of Nyagassola in Guinea, is said to date to Sundiata's own time (UNESCO lists "
        "it as a masterpiece of oral heritage) -- and the ngoni, the skin-covered lute that crossed "
        "the Atlantic to become the BANJO. Bassekou Kouyate made the ngoni a modern lead instrument; "
        "Neba Solo renewed the balafon. Cross-link: hold the ngoni next to an early banjo (US survey).",
        [
            ("Sosso Bala (the sacred balafon of Nyagassola)", None),
            ("Balani (Mande balafon dance)", None),
            ("Poyi", "Bassekou Kouyate"),
            ("Ngoni Fola", "Bassekou Kouyate"),
            ("Sinankun", "Neba Solo"),
            ("Ngoni (the Mande lute -- ancestor of the banjo)", None),
        ],
    ),
    (
        "THE JELIMUSO: THE GREAT GRIOT WOMEN",
        "In the jeli tradition the star vocalists are overwhelmingly women -- the jelimusolu -- whose "
        "soaring praise-singing is the tradition's most celebrated sound. Fanta Damba and Sira Mory "
        "Diabate were mid-century giants; Kandia Kouyate, Ami Koita, and Tata Bambo Kouyate ruled the "
        "cassette era; Hawa Kasse Mady Diabate carries it now. These are living artists; search a "
        "representative recording of each.",
        [
            ("Kita Kan", "Kandia Kouyate"),
            ("Tata Sira", "Ami Koita"),
            ("Djan Magni", "Tata Bambo Kouyate"),
            ("Fanta Bourama", "Fanta Damba"),
            ("Sara", "Sira Mory Diabate"),
            ("Kanuya", "Hawa Kasse Mady Diabate"),
        ],
    ),
    (
        "THE DRUM: DJEMBE, DUNDUN & THE MANDE PERCUSSION ENSEMBLE",
        "The djembe -- a goblet drum from the Mande heartland of Guinea and Mali -- and its bass "
        "companions the dunun form one of Earth's most powerful drum languages, each rhythm tied to a "
        "specific dance, festival, or rite. The national ballets exported it worldwide through masters "
        "like Mamady Keita and Famoudou Konate. Most rhythms are communal property -- '(Traditional)'.",
        [
            ("Djole", "Mamady Keita"),
            ("Kuku", "Mamady Keita"),
            ("Rhythms of the Malinke", "Famoudou Konate"),
            ("Dununba (dance of the strong men)", None),
            ("Soli (initiation rhythm)", None),
            ("Sunun (Mande djembe rhythm)", None),
        ],
    ),
    (
        "BEYOND THE MANDE: WOLOF, FULA, HAUSA, YORUBA & AKAN DEEP TRADITIONS",
        "West Africa is far more than the Mande. Senegal's Wolof have the thunderous SABAR drum choir "
        "and the xalam lute; the Fula (Fulani) have pastoral flute and song across the Sahel; the "
        "Hausa north of Nigeria and Niger keep an Islamic court music of kakaki trumpets and goge "
        "fiddle; the Yoruba of southwest Nigeria have the DUNDUN talking drum and the sacred BATA; and "
        "the Akan of Ghana keep royal drum orchestras. All living tradition -- search a version.",
        [
            ("Sabar (Wolof drum ensemble, Senegal)", None),
            ("Xalam / Khalam (Wolof lute)", None),
            ("Fula flute (Fulani pastoral song)", None),
            ("Kakaki & Goge (Hausa court music, northern Nigeria)", None),
            ("Dundun: Yoruba talking drum (SW Nigeria)", None),
            ("Bata drums (Yoruba, for the orisha)", None),
            ("Fontomfrom (Akan royal drums, Ghana)", None),
            ("Agbekor (Ewe war dance, Ghana/Togo)", None),
        ],
    ),
    (
        "THE ROOT OF THE AMERICAS: WEST AFRICA'S RHYTHM CROSSES THE ATLANTIC",
        "This is the loudest cross-link in the entire World Music Survey. Through the transatlantic "
        "slave trade, West African music became the rhythmic engine of the Americas: the Senegambian "
        "AKONTING gives rise to the banjo; the Mande pentatonic griot song underlies the modal, "
        "'one-chord' feel of the BLUES (US survey); the Yoruba BATA and orisha rhythms become Cuban "
        "Santeria batá and Brazilian candomblé (Latin survey); and the West African bell timeline "
        "becomes the clave. Content note: this transmission is the sound of enslavement's survival -- "
        "kept with its full context, not romanticized.",
        [
            ("Akonting (Jola lute, Senegambia -- ancestor of the banjo)", None),
            ("Griot blues / Mande pentatonic (proto-blues modal song)", None),
            ("Bata for Shango (Yoruba orisha rhythm -> Cuban/Brazilian)", None),
            ("Standard bell pattern (West African timeline -> clave)", None),
            ("Sabar rhythm (Wolof -> the diaspora)", None),
        ],
    ),
]

STEM = "ssa_west_music_1_GRIOT_MANDE_ROOTS"


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
