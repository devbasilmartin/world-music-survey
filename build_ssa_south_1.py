#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Southern, installment 1: the deep-traditional layer.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file (living tradition / no single definitive recording).
First installment of the Southern Africa region.
"""

TITLE = ("The Story of Southern African Music — Installment 1: "
         "The Deep-Traditional Layer (bow, voice, mbira & the oldest song on Earth)")

FRAMING = (
    "Southern Africa holds some of the oldest and most sophisticated music on the planet -- and, like "
    "West Africa, it is mostly an ORAL tradition we represent through recordings of living "
    "tradition-bearers. Its signatures are unmistakable: the MUSICAL BOW (Zulu ugubhu, Xhosa uhadi) "
    "whose natural harmonics generate whole melodies; the astonishing Xhosa OVERTONE and split-tone "
    "singing (umngqokolo), where one throat sounds two or three notes at once; the trance-inducing "
    "SHONA MBIRA of Zimbabwe, whose interlocking thumb-piano cycles summon the ancestors; and, oldest "
    "of all, the healing-dance music of the SAN (Bushmen), whose click-language songs may be the "
    "deepest continuous musical layer humanity has. Around these run the Sotho highveld bow-and-voice "
    "traditions, the Venda reed-pipe dances, and the Chopi xylophone orchestras of Mozambique. Two "
    "outside forces -- the Christian MISSION HYMN and the MIGRANT-LABOUR COMPOUND -- are already "
    "reshaping everything, and set up the marabi and Mbube of Installment 2. Cross-links: the mbira and "
    "bow tie back to the pan-African roots of the West Africa and US surveys; isicathamiya's choral "
    "roots here lead straight to Paul Simon's Graceland decades later. Content note: this is music made "
    "under colonial dispossession, the mines, and the coming shadow of apartheid -- kept with context. "
    "Because the layer is oral, many entries are '(Traditional)' bare titles to search; canonical "
    "tradition-bearers are named where they exist. Region: South Africa, Zimbabwe, Mozambique, Lesotho, "
    "Namibia, Botswana, Eswatini."
)

SECTIONS = [
    (
        "ZULU & SWAZI: THE BOW, THE VOICE & THE NGOMA",
        "Zulu music is built on the musical bow and the massed voice. Princess Magogo kaDinuzulu, a "
        "royal composer, is the definitive recorded bearer of the ugubhu gourd-bow song; alongside it "
        "stand the amahubo ceremonial anthems and the thunderous ngoma dance. This is the root from "
        "which maskandi and Ladysmith-style choral music will later grow.",
        [
            ("Zulu ugubhu bow songs", "Princess Magogo kaDinuzulu"),
            ("Ugubhu / umakhweyana (Zulu musical bow)", None),
            ("Ngoma (Zulu drum & war dance)", None),
            ("Amahubo (Zulu ceremonial anthems)", None),
            ("Swazi sibhaca / royal ncwala song", None),
        ],
    ),
    (
        "XHOSA: OVERTONE SINGING, UHADI & THE SPLIT-TONE",
        "The Xhosa tradition is one of the wonders of world music: umngqokolo, a deep 'split-tone' "
        "throat singing that produces reinforced overtones, sung over the uhadi and umrhubhe bows. "
        "Nofinishi Dywili and Madosini (Latozi Mpahleni) are its great recorded voices, and the Ngqoko "
        "women's group preserves the overtone art. Cross-link: this is the same harmonic-series "
        "principle that governs the bow music across the whole region.",
        [
            ("Umngqokolo (Xhosa overtone/split-tone singing)", None),
            ("Xhosa uhadi bow songs", "Nofinishi Dywili"),
            ("Umrhubhe & uhadi bow music", "Madosini"),
            ("Ngqoko women's overtone singing", "Ngqoko Cultural Group"),
            ("Amagwijo (Xhosa call-and-response song)", None),
            ("Izibongo (Xhosa clan praise poetry)", None),
        ],
    ),
    (
        "SOTHO, TSWANA & THE HIGHVELD",
        "On the high interior plateau, the Basotho play the lesiba -- a mouth-resonated wind-bow unique "
        "to the region -- and the women dance the mokhibo; the Tswana and Pedi keep reed-pipe (dinaka) "
        "and kiba traditions. These highveld forms feed directly into the migrant-worker musics to "
        "come, especially Sotho famo.",
        [
            ("Lesiba (Basotho mouth-bow wind instrument)", None),
            ("Mokhibo (Basotho women's knee dance song)", None),
            ("Dithoko (Sotho praise poetry)", None),
            ("Kiba / dinaka reed-pipe dance (Pedi/Tswana)", None),
        ],
    ),
    (
        "THE SHONA MBIRA OF ZIMBABWE",
        "The mbira dzavadzimu ('mbira of the ancestors') is a 22-to-28-key thumb piano played in "
        "cross-rhythmic cycles for the all-night BIRA ceremony, where its shimmering, hocketed patterns "
        "call the spirits into the medium. Stella Chiweshe ('the queen of mbira'), Ephat Mujuru, "
        "Dumisani Maraire, and singer Hakurotwi Mude carried it to the world. Cross-link: the mbira's "
        "interlocking cycles are the Zimbabwean cousin of the West African balafon and kora patterns.",
        [
            ("Nhemamusasa (mbira dzavadzimu, ancestral piece)", None),
            ("Kasahwa", "Stella Chiweshe"),
            ("Chapfudza", "Stella Chiweshe"),
            ("Chemutengure", "Dumisani Maraire"),
            ("Nyamaropa (classic mbira cycle)", None),
            ("Chaminuka Ndimambo", "Ephat Mujuru"),
            ("Taireva", "Hakurotwi Mude"),
            ("Bira ceremony mbira & hosho (Shona ancestral rite)", None),
        ],
    ),
    (
        "THE SAN & KHOI: THE OLDEST LAYER",
        "The San (Bushmen) of the Kalahari and their Khoikhoi kin carry what may be the deepest "
        "continuous musical tradition on Earth: click-language songs, mouth-bow melodies, and the "
        "all-night HEALING or TRANCE dance in which singers and clappers send healers into altered "
        "states to cure the community. Content note: the San are among the most dispossessed peoples "
        "of the region; this music survives against enormous pressure.",
        [
            ("San (Bushmen) healing trance-dance songs", None),
            ("San hunting-bow and mouth-bow music", None),
            ("Ju/hoansi San song (Kalahari)", None),
            ("Khoikhoi / Nama stap dance song", None),
            ("San story-song (Namibia/Botswana)", None),
        ],
    ),
    (
        "VENDA, TSONGA & THE CHOPI TIMBILA",
        "The far north and the Mozambican coast hold their own marvels: the Venda tshikona reed-pipe "
        "'national dance' and the domba python initiation; the Tsonga xitende bow and muchongolo dance; "
        "and, greatest of all, the CHOPI TIMBILA -- vast tuned-xylophone orchestras of Mozambique whose "
        "composed, multi-movement suites (migodo) are a UNESCO Masterpiece of oral heritage.",
        [
            ("Tshikona (Venda reed-pipe national dance)", None),
            ("Domba (Venda python initiation dance)", None),
            ("Chopi Timbila (Mozambican xylophone orchestra)", None),
            ("Tsonga xitende bow & muchongolo dance", None),
            ("Malombo / Venda ngoma drums", None),
        ],
    ),
    (
        "THE BACKDROP: MIGRANT LABOUR & THE MISSION HYMN",
        "Two colonial forces reshaped everything that follows. Christian missions taught Tonic Sol-fa "
        "and four-part hymnody, birthing a huge Black CHORAL tradition (makwaya); and the diamond and "
        "gold mines drew men from across the region into single-sex COMPOUNDS that mixed languages and "
        "bred new urban musics. Content note: this is the machinery of dispossession that also, "
        "unintentionally, forged marabi, Mbube, and isicathamiya (Installment 2). Ntsikana's early "
        "Xhosa hymn is the tradition's fountainhead.",
        [
            ("Ntsikana's Great Hymn (Ulo Thixo Omkhulu, first Xhosa hymn, c.1820)", None),
            ("Makwaya (mission-derived four-part choral song)", None),
            ("Tonic Sol-fa mission hymnody (Zulu/Xhosa)", None),
            ("Migrant-labour compound song (mine hostels)", None),
            ("Sotho famo precursors (shebeen & migrant song)", None),
        ],
    ),
]

STEM = "ssa_south_music_1_DEEP_TRADITIONAL"


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
