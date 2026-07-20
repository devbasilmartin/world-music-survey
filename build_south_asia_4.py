#!/usr/bin/env python3
"""Build India / South Asia, installment 4: Devotional Traditions (Bhajan, Qawwali & the Sacred Voice).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/Latin only. Dedup is by TITLE only.
NOTE: do NOT reuse a bare "Amir Khusrau (...)" or "Bhakti (...)" title (they collide with #1).
"""

TITLE = ("The Story of Indian & South Asian Music — Installment 4: "
         "Devotional Traditions — Bhajan, Qawwali & the Sacred Voice")

FRAMING = (
    "Devotion is South Asia's deepest musical current -- older, wider, and more beloved than any "
    "concert art. This installment gathers the sacred song of the subcontinent's great faiths. From the "
    "medieval BHAKTI movement flowed a flood of poet-saints -- Mirabai, Kabir, Surdas, Tukaram -- whose "
    "BHAJANS and congregational KIRTAN put God within reach of every villager, beyond priest and caste. "
    "From Sufi Islam came QAWWALI -- the ecstatic shrine music born with the 13th-century genius Amir "
    "Khusrau and raised to world fame by NUSRAT FATEH ALI KHAN, the Sabri Brothers, and Abida Parveen. "
    "The Sikh tradition sings its scripture as SHABAD KIRTAN in the ragas themselves. And temple, "
    "mantra, and aarti thread through daily life everywhere. Cross-links: qawwali and Sufi song bridge "
    "into Pakistan and the wider Islamic/MENA world (Pakistani artists flagged as wider-South-Asia); "
    "the Baul mysticism of #3; devotion's later fusion with film song (#5) and the global yoga/kirtan "
    "scene (flagged Western). Names given as (Traditional) are forms, poets, or hymns to seed listening; "
    "canonical works/performers are named. Region: India & the wider South Asia (shared Sufi/qawwali "
    "world)."
)

SECTIONS = [
    (
        "THE BHAKTI POET-SAINTS & THEIR SONGS",
        "The bhakti (devotion) movement, sweeping India from the 7th century, replaced ritual and caste "
        "with direct, personal love of the divine -- and it sang. Mirabai poured out ecstatic songs to "
        "Krishna, Kabir wove piercing formless-God couplets, Surdas and Tulsidas hymned Krishna and Ram, "
        "and Narsinh Mehta wrote the bhajan Gandhi loved. Their verses are still sung daily.",
        [
            ("Mirabai bhajans (the ecstatic Krishna songs, seed)", None),
            ("Payoji Maine (the beloved Mira bhajan)", None),
            ("Kabir ke dohe (the formless-God couplets, seed)", None),
            ("Surdas & the Krishna bhajan tradition", None),
            ("Hanuman Chalisa (Tulsidas's hymn to Hanuman)", None),
            ("Vaishnava Jana To (Narsinh Mehta's bhajan, Gandhi's favorite)", None),
        ],
    ),
    (
        "BHAJAN & KIRTAN: HINDU CONGREGATIONAL SONG",
        "Beyond the poets, everyday Hindu worship sings. The BHAJAN (devotional song) and call-and-"
        "response KIRTAN -- driven by harmonium, dholak, and clashing manjira -- fill temples and homes; "
        "Chaitanya's Hare Krishna sankirtan turned chanting into ecstasy; and the aarti closes every "
        "ritual with communal song.",
        [
            ("Bhajan (the Hindu devotional song)", None),
            ("Kirtan (call-and-response congregational chant)", None),
            ("Hare Krishna sankirtan (Chaitanya's ecstatic chanting)", None),
            ("Om Jai Jagdish Hare (the universal aarti)", None),
            ("Harmonium, dholak & manjira (the bhajan ensemble)", None),
            ("Abhang & the Pandharpur warkari (Tukaram's Maharashtra)", None),
        ],
    ),
    (
        "THE SUFI SHRINE & THE BIRTH OF QAWWALI",
        "Qawwali is the devotional music of South Asian Sufism -- sung at the dargah (shrine) to induce "
        "sama, spiritual ecstasy. It was shaped in the 13th century by the poet-musician-genius Amir "
        "Khusrau at the shrine of Nizamuddin Auliya in Delhi; his 'Man Kunto Maula' and 'Chaap Tilak' "
        "remain its cornerstones. The party builds from praise (hamd, naat) toward rapture.",
        [
            ("Man Kunto Maula", "Amir Khusrau"),
            ("Chaap Tilak", "Amir Khusrau"),
            ("Qawwali (the Sufi shrine music)", None),
            ("The dargah & sama (shrine & ecstasy: Nizamuddin, Ajmer Sharif)", None),
            ("Hamd, naat & manqabat (the qawwali sequence)", None),
            ("The qawwali party (lead, chorus, handclaps & harmonium)", None),
        ],
    ),
    (
        "NUSRAT FATEH ALI KHAN: THE SHAHENSHAH-E-QAWWALI",
        "Nusrat Fateh Ali Khan -- the 'King of Kings of Qawwali' -- possessed one of the great voices of "
        "any tradition, capable of soaring improvisation and overwhelming power. He carried qawwali to "
        "the world through Peter Gabriel's Real World, film, and collaborations (Massive Attack, Eddie "
        "Vedder). Region note: Pakistani, flagged as wider-South-Asia. He is a titan of global music.",
        [
            ("Allah Hoo Allah Hoo", "Nusrat Fateh Ali Khan"),
            ("Mera Piya Ghar Aaya", "Nusrat Fateh Ali Khan"),
            ("Nusrat Fateh Ali Khan (the Shahenshah-e-Qawwali, flagged Pakistani)", None),
            ("Nusrat goes global (Real World, Peter Gabriel, film)", None),
            ("The sargam improvisation (Nusrat's vocal fireworks)", None),
        ],
    ),
    (
        "THE QAWWALI DYNASTIES & THE SUFI VOICE",
        "Qawwali runs in families and lineages. The Sabri Brothers' thunderous 'Bhar Do Jholi', Aziz "
        "Mian's marathon philosophical qawwalis, and the Warsi Brothers carried the men's tradition, "
        "while Abida Parveen became the peerless female voice of Sufi song. 'Dama Dam Mast Qalandar' is "
        "the shared anthem. Region note: several are Pakistani (flagged).",
        [
            ("Bhar Do Jholi", "Sabri Brothers"),
            ("Abida Parveen (the queen of Sufi song, flagged Pakistani)", None),
            ("Aziz Mian (the marathon philosophical qawwal)", None),
            ("Dama Dam Mast Qalandar (the great Sufi anthem)", None),
            ("The Warsi Brothers & the qawwali gharanas", None),
        ],
    ),
    (
        "THE SUFI POETS SUNG",
        "Qawwali and Sufi song are vehicles for mystic poetry across South Asia's languages. Bulleh "
        "Shah and Baba Farid in Punjabi, Shah Abdul Latif Bhittai in Sindhi, and Amir Khusrau's Hindavi "
        "verse turn longing for the divine into the language of love. Cross-links: the Baul mystics of "
        "Bengal (#3) and the wider Sufi/MENA world.",
        [
            ("Bulleh Shah (the Punjabi Sufi poet sung)", None),
            ("Baba Farid (the early Punjabi Sufi verse)", None),
            ("Shah Abdul Latif Bhittai (the Sindhi Sufi, Shah jo Risalo)", None),
            ("Kafi (the Sufi lyric form of Punjab & Sindh)", None),
            ("Mystic poetry as love song (the Sufi idiom)", None),
        ],
    ),
    (
        "SIKH GURBANI & SHABAD KIRTAN",
        "The Sikh tradition is sung scripture: the Guru Granth Sahib is set to and performed in specific "
        "ragas as SHABAD KIRTAN, led by ragis at the Golden Temple and every gurdwara. This Gurmat "
        "Sangeet -- founded by Guru Nanak with his companion Mardana on the rabab -- is among the most "
        "serene devotional music anywhere.",
        [
            ("Shabad Kirtan (the sung Sikh scripture)", None),
            ("Gurbani in raga (the Guru Granth Sahib set to music)", None),
            ("The ragis of the Golden Temple", None),
            ("Guru Nanak & Mardana's rabab (the tradition's root)", None),
            ("Gurmat Sangeet (the Sikh classical devotional style)", None),
        ],
    ),
    (
        "DEVOTION GOES ON: MANTRA, TEMPLE & THE GLOBAL KIRTAN",
        "Devotional music never stopped growing. Vedic mantra and Om chant, the cassette-and-TV bhajan "
        "empire (Gulshan Kumar's T-Series built on it), and a global kirtan scene (yoga studios, Krishna "
        "Das in the West -- flagged Western) all carry the sacred forward. Cross-link: film's devotional "
        "songs (#5), where bhajan meets Bollywood.",
        [
            ("Gayatri Mantra & Om chant (the Vedic sound, sung)", None),
            ("The cassette bhajan boom (Gulshan Kumar & T-Series)", None),
            ("Global kirtan (yoga-world chanting, flagged Western)", None),
            ("Temple bhajan & the aarti today", None),
            ("Devotion into film song (bhajan meets Bollywood, roads ahead)", None),
        ],
    ),
]

STEM = "south_asia_music_4_DEVOTIONAL_BHAJAN_QAWWALI"


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
