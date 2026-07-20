#!/usr/bin/env python3
"""Build Sub-Saharan Africa: East, installment 4: The Modern Era -- Bongo Flava, Genge & Hip-Hop.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1995-2010.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of East African Music — Installment 4: "
         "The Modern Era — Bongo Flava, Genge & Hip-Hop (c. 1995-2010)")

FRAMING = (
    "In the 1990s a hip-hop generation took the mic, and East African pop was reborn in Sheng and "
    "Swahili slang. In Tanzania, imported rap fused with R&B and local melody into BONGO FLAVA -- named "
    "for Dar es Salaam ('Bongo', the city of brains) -- which grew from underground crews (Kwanza Unit) "
    "into the region's dominant pop, with Professor Jay's biting political satire, Mr Nice's sunny "
    "hits, and Lady Jaydee's R&B. In Kenya, conscious hip-hop rose from the Dandora slums (Kalamashaka, "
    "Ukoo Flani) rapping in SHENG, then split into the party-pop of GENGE and KAPUKA (Nonini, Jua Cali, "
    "the Ogopa DJs and Calif/Clemo sound) and radio stars like Nameless and the beloved E-Sir (lost in "
    "a 2003 crash). Gidi Gidi Maji Maji's 'Unbwogable' became a 2002 political anthem. And in Uganda, "
    "the 'Big Three' -- Jose Chameleone, Bebe Cool, and Bobi Wine -- built a booming kidandali pop "
    "scene. Cross-links: US hip-hop and R&B (the American survey) localized into Sheng and Swahili; the "
    "coming Afrobeats/amapiano/singeli waves. Content notes: E-Sir's death and, in Uganda, Bobi Wine's "
    "later political persecution are kept in view. Region: Tanzania, Kenya & Uganda."
)

SECTIONS = [
    (
        "THE BIRTH OF BONGO FLAVA (Dar es Salaam, c. 1995-2000)",
        "Tanzanian youth took American rap and made it their own -- rhyming in Swahili over beats that "
        "soon absorbed R&B, taarab, and dansi melody. Pioneering crews like Kwanza Unit and rappers "
        "like Saleh J and Mr II (Sugu) built the underground that would become BONGO FLAVA, the sound "
        "of a liberalized, media-hungry Dar es Salaam.",
        [
            ("Bongo flava (Swahili hip-hop & R&B, Dar es Salaam)", None),
            ("Kwanza Unit (pioneering Tanzanian hip-hop crew)", None),
            ("Saleh J & the first Swahili rappers", None),
            ("Mr II / Sugu (early bongo flava, conscious rap)", None),
            ("Rhyming in Swahili (localizing American hip-hop)", None),
            ("The Dar es Salaam radio & studio boom", None),
        ],
    ),
    (
        "BONGO FLAVA GOES MAINSTREAM (c. 2000-2008)",
        "Bongo flava became Tanzania's dominant pop. Professor Jay turned rap into sharp political "
        "satire ('Ndio Mzee', a mock politician's promises), Mr Nice scored breezy continental hits "
        "('Kunguru'), and TID, Juma Nature, AY, and Mwana FA filled the charts. It was youthful, "
        "Swahili, and unstoppable.",
        [
            ("Ndio Mzee", "Professor Jay"),
            ("Kunguru", "Mr Nice"),
            ("Professor Jay (bongo flava's political satirist)", None),
            ("TID (Top In Dar, bongo flava hitmaker)", None),
            ("Juma Nature (Temeke's conscious voice)", None),
            ("AY & Mwana FA (the bongo flava charts)", None),
        ],
    ),
    (
        "THE QUEENS & THE R&B SIDE OF BONGO (c. 2000-2008)",
        "Bongo flava's softer half was a lush Swahili R&B, and its queen was Lady Jaydee, whose "
        "'Wanaonizunguka' made her a superstar. Ray C and others carried the love-song banner, and "
        "smooth crooners like Dully Sykes kept the slow jams coming -- proof the genre was as much "
        "romance as rap.",
        [
            ("Wanaonizunguka", "Lady Jaydee"),
            ("Lady Jaydee (the queen of bongo flava R&B)", None),
            ("Ray C (bongo flava love songs)", None),
            ("Dully Sykes (the smooth bongo crooner)", None),
            ("Swahili R&B (the soft side of bongo flava)", None),
        ],
    ),
    (
        "KENYAN HIP-HOP: DANDORA & KALAMASHAKA (c. 1995-2003)",
        "Kenya's hip-hop grew hard and conscious out of Nairobi's Dandora estates. Kalamashaka's "
        "'Tafsiri Hii' was a landmark, and the Ukoo Flani Mau Mau collective and K-South rapped street "
        "reality in SHENG -- the Nairobi slang that became hip-hop's mother tongue. Cross-link: US "
        "conscious rap (the American survey), rewritten for Kenyan streets.",
        [
            ("Tafsiri Hii", "Kalamashaka"),
            ("Kalamashaka (pioneers of Kenyan conscious hip-hop)", None),
            ("Ukoo Flani Mau Mau (the Nairobi hip-hop collective)", None),
            ("Sheng (Nairobi slang as hip-hop's tongue)", None),
            ("K-South & the Dandora sound", None),
            ("Conscious rap from the Nairobi estates", None),
        ],
    ),
    (
        "GENGE & KAPUKA: THE NAIROBI POP SOUND (c. 2001-2008)",
        "Kenyan hip-hop split toward the party. GENGE -- coined by Nonini and the Calif label -- and "
        "the bouncy KAPUKA beat of the Ogopa DJs turned Sheng rap into pure dancefloor pop. Nonini's "
        "'Manzi wa Nairobi' and Jua Cali's 'Kiasi' defined a cheeky, club-ready Kenyan sound.",
        [
            ("Manzi wa Nairobi", "Nonini"),
            ("Kiasi", "Jua Cali"),
            ("Genge (Nonini & Calif Records' street pop)", None),
            ("Kapuka (the Ogopa DJs party beat)", None),
            ("Jua Cali (the face of genge)", None),
            ("The Nairobi club-pop explosion", None),
        ],
    ),
    (
        "E-SIR, NAMELESS & THE OGOPA STARS (c. 2001-2008)",
        "Radio-friendly pop crowned a golden run of Kenyan stars. E-Sir was the brilliant young "
        "lyricist whose 'Boomba Train' (with Nameless) topped every chart before his death in a 2003 "
        "car crash; Nameless ('Megarider') and Redsan became household names. Content note: E-Sir's "
        "death at 21 is kept in view.",
        [
            ("Boomba Train", "E-Sir"),
            ("Megarider", "Nameless"),
            ("E-Sir (the lost prince of Kenyan pop, d. 2003)", None),
            ("Nameless (Ogopa radio-pop star)", None),
            ("Redsan (Kenyan dancehall-pop)", None),
            ("The Ogopa DJs hit factory", None),
        ],
    ),
    (
        "\"UNBWOGABLE\", RAGGA & THE GOSPEL BOOM (c. 2002-2008)",
        "Music met politics head-on when Gidi Gidi Maji Maji's 'Unbwogable' ('unshakeable') became the "
        "anthem of Kenya's 2002 change election. Necessary Noize (Nazizi, the 'first lady' of Kenyan "
        "hip-hop, with Wyre) led a ragga wave, and a massive gospel scene (Esther Wahome's 'Kuna Dawa') "
        "ran alongside the secular pop. Content note: music as political force.",
        [
            ("Unbwogable", "Gidi Gidi Maji Maji"),
            ("Necessary Noize & Nazizi (Kenyan ragga, the first lady of hip-hop)", None),
            ("Wyre (the love child, Kenyan dancehall)", None),
            ("Kuna Dawa", "Esther Wahome"),
            ("The Kenyan gospel boom (Ohangla & choir pop)", None),
            ("Music & the 2002 election (Unbwogable's moment)", None),
        ],
    ),
    (
        "UGANDA'S BIG THREE & THE REGIONAL SCENE (c. 2000-2010)",
        "Uganda built its own boom. The 'Big Three' -- Jose Chameleone ('Mama Mia'), Bebe Cool, and "
        "Bobi Wine -- fronted a lively KIDANDALI pop, while the older KADONGO KAMU storytelling of "
        "Paulo Kafeero held the roots. Cross-link: these scenes feed straight into the Afrobeats, "
        "singeli, and amapiano waves of the 2010s. Content note: Bobi Wine's later political "
        "persecution is flagged forward.",
        [
            ("Mama Mia", "Jose Chameleone"),
            ("Jose Chameleone (Uganda's biggest pop star)", None),
            ("Bebe Cool & Bobi Wine (Uganda's Big Three)", None),
            ("Kidandali (modern Ugandan dance pop)", None),
            ("Kadongo Kamu & Paulo Kafeero (Ugandan storytelling song)", None),
            ("Toward the 2010s (Afrobeats, singeli & amapiano ahead)", None),
        ],
    ),
]

STEM = "ssa_east_music_4_BONGO_FLAVA_GENGE_HIPHOP"


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
