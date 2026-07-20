#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Southern, installment 7: Amapiano & the Global Present.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
Covers c. 2000-present. Final installment of the Southern Africa region.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of Southern African Music — Installment 7: "
         "Amapiano & the Global Present (c. 2000-present)")

FRAMING = (
    "The story ends with Southern Africa, once again, exporting a sound to the planet. Kwaito's "
    "house-music parent grew into a world-class SA HOUSE scene led by Black Coffee, who took the deep, "
    "soulful Johannesburg sound to Ibiza and a 2022 Grammy. Durban answered with GQOM -- dark, "
    "stripped, pounding -- and then, around 2019, the whole continent was swept by AMAPIANO: a "
    "jazzy, mid-tempo house built on a hypnotic bass 'log-drum', made by a young Pretoria and "
    "Johannesburg generation (Kabza De Small, DJ Maphorisa, Focalistic, DBN Gogo, Uncle Waffles) and "
    "spreading to Nigeria and the world. Meanwhile Master KG's 'Jerusalema' became a global lockdown "
    "dance challenge, and in 2024 Tyla's 'Water' won the first-ever Grammy for Best African Music "
    "Performance -- a South African teenager topping the world charts. Zimbabwe's Zim dancehall (Winky "
    "D) and a rich new SA jazz round out a region as musically alive as anywhere on Earth. Cross-links: "
    "SA house <-> US/Chicago house; amapiano <-> West African Afrobeats and UK dance; 'Jerusalema' and "
    "'Water' <-> the global pop mainstream. Region: artists are South African, Zimbabwean, Zambian, or "
    "Eswatini-born SA-based; scope calls flagged."
)

SECTIONS = [
    (
        "SA DEEP & SOULFUL HOUSE: BLACK COFFEE & THE HOUSE NATION (c. 2005-present)",
        "South Africa became one of the world's great house-music countries. Black Coffee turned the "
        "deep, soulful, spiritual Johannesburg sound into a global brand -- Ibiza residencies, a "
        "Grammy-winning 2021 album -- while Zakes Bantwini, Culoe De Song, and a huge DJ culture kept "
        "the dancefloors full. Cross-link: the DNA is US/Chicago house, re-soulified with African "
        "vocals and swing.",
        [
            ("Superman", "Black Coffee"),
            ("We Dance Again", "Black Coffee"),
            ("Drive", "Black Coffee"),
            ("Turn Me On", "Black Coffee"),
            ("Osama", "Zakes Bantwini"),
            ("Bright Forest", "Culoe De Song"),
            ("South African deep house (the house nation)", None),
        ],
    ),
    (
        "THE DURBAN GQOM (c. 2012-2018)",
        "From Durban's townships came GQOM (the Zulu word for a drum hit) -- dark, minimal, broken-beat "
        "house with no melody and maximum menace. DJ Lag exported it; Babes Wodumo's 'Wololo' and "
        "Distruction Boyz' 'Omunye' made it national pop. It is the raw underground that fed straight "
        "into amapiano.",
        [
            ("Ice Drop", "DJ Lag"),
            ("Wololo", "Babes Wodumo"),
            ("Omunye", "Distruction Boyz"),
            ("Mercedes", "Rudeboyz"),
            ("Gqom (dark minimal Durban house)", None),
        ],
    ),
    (
        "THE AMAPIANO EXPLOSION: THE LOG-DRUM ERA (c. 2018-present)",
        "AMAPIANO ('the pianos') fused kwaito, deep house, jazz chords, and a deep, bouncing bass "
        "'LOG-DRUM' into the most infectious African sound of the era. Kabza De Small and DJ Maphorisa "
        "(the Scorpion Kings) are its architects; MFR Souls named it; and Busta 929, De Mthuda, and "
        "Vigro Deep filled the streets. It is the sound of a generation.",
        [
            ("Sponono", "Scorpion Kings"),
            ("Amantombazane", "MFR Souls"),
            ("Umsebenzi Wethu", "Busta 929 & Mr JazziQ"),
            ("Amapiano log-drum (the Pretoria/Jozi sound)", None),
            ("Vigro Deep (Baby Boy amapiano)", None),
            ("De Mthuda (soulful amapiano)", None),
            ("Kabza De Small & DJ Maphorisa (Scorpion Kings)", None),
        ],
    ),
    (
        "AMAPIANO GOES GLOBAL (c. 2020-present)",
        "Within two years amapiano was continental and then global. Focalistic's 'Ke Star' got a Davido "
        "remix (cross-link to West Africa); DBN Gogo and the Eswatini-born Uncle Waffles became "
        "international DJ stars; Young Stunna's 'Adiwele' was an anthem; and Nigerian and Ghanaian "
        "Afrobeats stars began building the log-drum into their own hits. (Scope note: Uncle Waffles is "
        "Eswatini-born and South Africa-based -- kept as Southern African, flagged.)",
        [
            ("Ke Star", "Focalistic"),
            ("Khuza Gogo", "DBN Gogo"),
            ("Tanzania", "Uncle Waffles"),
            ("Adiwele", "Young Stunna"),
            ("Emcimbini", "Kabza De Small"),
            ("Sha Sha (Zimbabwe's amapiano queen)", None),
            ("Amapiano-to-Afrobeats crossover (Nigeria/Ghana)", None),
        ],
    ),
    (
        "THE GLOBAL CROSSOVER: JERUSALEMA & TYLA (c. 2019-present)",
        "Two South African records conquered the actual world. Master KG and Nomcebo Zikode's "
        "'Jerusalema' (2019) became the defining global dance challenge of the 2020 lockdown; and in "
        "2024 the 21-year-old Tyla's amapiano-pop 'Water' hit the US Top 10 and won the first-ever "
        "Grammy for Best African Music Performance. Sho Madjozi's Tsonga-rap 'John Cena' and Nasty C's "
        "hip-hop show the range. Cross-link: this is South African music AS global pop.",
        [
            ("Jerusalema", "Master KG"),
            ("Xola Moya Wam", "Nomcebo Zikode"),
            ("Water", "Tyla"),
            ("John Cena", "Sho Madjozi"),
            ("Jerusalema dance challenge (2020 global phenomenon)", None),
            ("Nasty C (South African hip-hop)", None),
        ],
    ),
    (
        "ZIMBABWE & THE WIDER REGION NOW (c. 2000-present)",
        "Beyond South Africa the region pulses too. Zimbabwe's ZIM DANCEHALL -- Winky D above all, plus "
        "Killer T -- rules the ghetto, while Jah Prayzah blends mbira-pop and Afro-fusion; and the "
        "Zambian-born, Botswana-raised Sampa the Great carries Southern African hip-hop to the world. "
        "(Scope note: Sampa the Great is Zambian-born and Australia-based -- kept as Zambian/Southern "
        "African, flagged.)",
        [
            ("Disappear", "Winky D"),
            ("Kutonga Kwaro", "Jah Prayzah"),
            ("Final Form", "Sampa the Great"),
            ("Zim dancehall (Winky D & Killer T riddim culture)", None),
            ("Zambian pop now (Zamrock heirs to hip-hop)", None),
            ("Botswana & Namibia contemporary pop", None),
        ],
    ),
    (
        "THE 21ST-CENTURY JAZZ & ROOTS REVIVAL (c. 2000-present)",
        "Underneath the dancefloor, a serious new South African jazz and roots movement flourished: "
        "Thandiswa Mazwai carried Xhosa tradition and struggle memory into modern song, and a new "
        "generation of spiritual jazz players (Nduduzo Makhathini, Bokani Dyer) won global acclaim -- "
        "even as maskandi and the deep tradition of Installment 1 kept renewing themselves.",
        [
            ("Zabalaza", "Thandiswa Mazwai"),
            ("Nduduzo Makhathini (spiritual South African jazz)", None),
            ("Bokani Dyer & the new Cape jazz", None),
            ("Maskandi revival (Phuzekhemisi's heirs)", None),
            ("New South African roots (The Brother Moves On)", None),
        ],
    ),
]

STEM = "ssa_south_music_7_AMAPIANO_GLOBAL_PRESENT"


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
