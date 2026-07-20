#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Sahel, installment 1: Desert & Savanna Roots.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers the deep roots, c. pre-1970.
Dedup is by TITLE only -- every title unique region-wide. Roots-heavy: mostly traditions & seeds.
"""

TITLE = ("The Story of Sahelian Music — Installment 1: "
         "Desert & Savanna Roots (the deep tradition, c. pre-1970)")

FRAMING = (
    "The Sahel is the great belt where the Sahara's edge meets the savanna -- a corridor of caravan "
    "routes, empires (Ghana, Mali, Songhai, Kanem-Bornu), and Islam running from Mauritania across "
    "Mali, Niger, and Chad to northern Nigeria. Its music is the SOUTH's meeting with the NORTH: the "
    "pentatonic, modal, often melancholy sound of desert and river peoples, shaped by Berber and Arab "
    "currents and by centuries of Islam, and carried by hereditary praise-musicians. This installment "
    "lays the deep tradition BEFORE the electric age: the MOORISH art music of Mauritania (tidinit and "
    "ardin); TUAREG imzad and tende and the poetry of longing (assouf) that would become 'desert "
    "blues'; the SONGHAI takamba of the Niger bend; FULANI herders' flutes; HAUSA court trumpets and "
    "goje fiddles; and the family of Sahelian lutes -- the ngoni and tehardent -- whose pentatonic, "
    "call-and-response spirit is a documented ancestor of the American blues (the 'Mali-to-Mississippi' "
    "thread). Scope note: this Sahel survey is the DESERT-EDGE thread (Mauritania, northern & eastern "
    "Mali, Niger, Chad, northern Nigeria); the coastal Mande griot/kora world is covered in the "
    "separate, COMPLETE West Africa survey -- overlaps are flagged. Cross-links: US blues (American "
    "survey); Berber/Arab North Africa (MENA survey to come); Mande griot (West Africa survey). "
    "Region: the Sahel belt. Names given as (Traditional) are living traditions or search seeds."
)

SECTIONS = [
    (
        "THE SAHEL: WHERE DESERT MEETS SAVANNA",
        "Sahelian music is defined by its geography -- the meeting of Saharan and sub-Saharan worlds "
        "along the old trans-Saharan trade and pilgrimage routes. It tends to the pentatonic, the modal, "
        "and the deeply melodic, and it is saturated with Islam, from the muezzin's call to Sufi "
        "praise. Empire and caravan made it a crossroads music.",
        [
            ("Sahelian music (where the Sahara meets the savanna)", None),
            ("The trans-Saharan crossroads (caravan-route music)", None),
            ("The pentatonic, modal north (Sahel tonality)", None),
            ("Islam & Sahelian music (muezzin, Sufi praise, Quranic cantillation)", None),
            ("Empires of the Sahel (Mali, Songhai, Kanem-Bornu in song)", None),
        ],
    ),
    (
        "THE MOORISH TRADITION OF MAURITANIA",
        "In Mauritania, the Moorish (Bidhan) art music is one of Africa's most sophisticated modal "
        "systems, performed by hereditary iggawin griots. The men play the lute-like TIDINIT, the women "
        "the harp-like ARDIN, moving through an ordered sequence of 'ways' (modes) from 'black' to "
        "'white'. Its great voices (Dimi Mint Abba the most famous) command the whole azawan.",
        [
            ("Moorish azawan (the Mauritanian modal suite)", None),
            ("Tidinit (the Moorish men's lute)", None),
            ("Ardin (the Moorish women's harp)", None),
            ("Iggawin (the Moorish griot caste)", None),
            ("Dimi Mint Abba (Mauritania's great voice, seed)", None),
            ("The black-and-white modes (Moorish musical order)", None),
        ],
    ),
    (
        "TUAREG MUSIC OF THE DESERT (Kel Tamashek)",
        "The Tuareg (Kel Tamashek) of the central Sahara carry a music of vast melancholy. The women's "
        "one-string IMZAD fiddle accompanies epic poetry; the TENDE mortar-drum drives communal song "
        "and camel festivals; and the mood of ASSOUF -- longing, nostalgia, exile -- runs through it "
        "all. This is the pre-electric taproot of 'desert blues'. Cross-link: the guitar ishumar to "
        "come.",
        [
            ("Imzad (the Tuareg women's one-string fiddle)", None),
            ("Tende (the Tuareg mortar-drum song)", None),
            ("Assouf (the Tuareg music of longing & exile)", None),
            ("Tuareg poetry & sung verse (tisiway)", None),
            ("The pre-guitar roots of desert blues (Tuareg tradition)", None),
            ("Camel-festival & caravan song (Kel Tamashek)", None),
        ],
    ),
    (
        "SONGHAI & THE NIGER BEND",
        "Along the great bend of the Niger -- Gao, Timbuktu, the river towns -- the Songhai and their "
        "neighbors built a river culture with its own dances and spirit rites. The lilting TAKAMBA "
        "rhythm (guitar-and-calabash today, lute-and-drum in its roots) is the Niger bend's signature, "
        "and the holey possession ceremonies carry an older layer still.",
        [
            ("Takamba (the Niger-bend groove of Gao & Timbuktu)", None),
            ("Songhai river music (the Niger bend)", None),
            ("Holey / spirit-possession music (Songhai-Zarma rites)", None),
            ("Timbuktu & the manuscript cities in song", None),
            ("Calabash percussion of the river towns", None),
        ],
    ),
    (
        "FULANI (PEUL) & THE HERDERS' MUSIC",
        "The Fulani (Fulɓe, Peul) -- cattle-herding pastoralists spread across the entire Sahel -- carry "
        "a distinctive music of solo FLUTE and herders' song, and among the Wodaabe the astonishing "
        "GEREWOL courtship festival, where men sing and dance to be judged the most beautiful. Their "
        "sound threads through every Sahelian nation.",
        [
            ("Fulani flute (the herder's solo)", None),
            ("Wodaabe gerewol (the male-beauty courtship song)", None),
            ("Fulɓe pastoral song (across the Sahel)", None),
            ("Peul praise & cattle songs", None),
            ("The one-string molo & Fulani lute", None),
        ],
    ),
    (
        "HAUSA MUSIC & THE COURTS OF THE NORTH",
        "In the Hausa lands (northern Nigeria and southern Niger), music is bound to the emirs' courts "
        "and to praise. Long metal KAKAKI trumpets and drums announce royalty (rok'o), the bowed GOJE "
        "fiddle and kalangu talking-drum accompany singers, and hereditary praise-poets wield "
        "reputations like weapons. Islam shapes it all. Content note: the praise-singer's power to "
        "flatter or shame is real.",
        [
            ("Kakaki (the Hausa royal long-trumpet)", None),
            ("Goje (the Hausa bowed fiddle)", None),
            ("Hausa court & praise music (rok'o)", None),
            ("Kalangu (the Hausa talking-drum)", None),
            ("Hausa hereditary praise-poets (maroka)", None),
            ("Islamic song & Sufi brotherhoods of the north", None),
        ],
    ),
    (
        "THE SAHELIAN LUTES & THE ROOTS OF THE BLUES",
        "At the heart of Sahelian sound is a family of plucked lutes -- the Mande NGONI, the Tuareg/"
        "Songhai TEHARDENT (tahardent), the Wolof xalam -- whose skin-headed, gut-strung twang and "
        "pentatonic, call-and-response phrasing are a documented ancestor of the American banjo and "
        "the blues. Cross-link: the 'Mali-to-Mississippi' thread of the US survey.",
        [
            ("Ngoni (the Sahelian skin-covered lute)", None),
            ("Tehardent / tahardent (the Tuareg-Songhai lute)", None),
            ("Xalam / molo (the Wolof-Fulani lute)", None),
            ("Pentatonic call-and-response (the blues taproot)", None),
            ("Ngoni to banjo (the Mali-to-Mississippi thread)", None),
            ("The griot's lute across the Sahel", None),
        ],
    ),
    (
        "ISLAM, THE GRIOT & THE ROADS AHEAD",
        "Two forces bind Sahelian music: Islam (praise, Sufi dhikr, and the manuscript learning of the "
        "desert cities) and the hereditary GRIOT / praise-musician, keeper of genealogy and history. "
        "From these roots grew everything ahead -- Ali Farka Touré's river blues, the Tuareg guitar of "
        "Tinariwen, wassoulou, and Sahelian pop. Cross-links: West Africa's Mande griot; MENA's "
        "Arab-Berber north.",
        [
            ("The Sahelian griot (keeper of history & genealogy)", None),
            ("Sufi dhikr & devotional song (the Sahel's Islam)", None),
            ("Ali Farka Touré (the river blues to come, seed)", None),
            ("Toward the electric desert blues (Tinariwen ahead)", None),
            ("Desert-city learning & the sung word (Timbuktu, Chinguetti)", None),
        ],
    ),
]

STEM = "ssa_sahel_music_1_DESERT_SAVANNA_ROOTS"


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
