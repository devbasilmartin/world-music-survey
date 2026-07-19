#!/usr/bin/env python3
"""Build Sub-Saharan Africa: West, installment 6: The 80s/90s Mande Superstars & the World-Music Era.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1980-2000.
Dedup note: #1 used Toumani Diabate "Jarabi"/"Cantelowes"/"Alla l'a ke" and Ballake "Bafoulabe" -- avoided here.
"""

TITLE = ("The Story of West African Music — Installment 6: "
         "The Mande Superstars & the World-Music Era (c. 1980-2000)")

FRAMING = (
    "In the 1980s and 90s West Africa conquers the global stage. The griot tradition of Installment 1, "
    "the dance bands of Installment 3, and cheap electric amplification meet the new international "
    "'world music' industry (headquartered in Paris and London), and a generation of Malian and "
    "Senegalese stars becomes globally famous without leaving their languages behind. Mali's SALIF "
    "KEITA -- a nobleman and an albino who broke caste taboo to sing -- carries 'the golden voice' "
    "worldwide; MORY KANTE electrifies the kora and scores the first African million-seller in Europe "
    "('Ye Ke Ye Ke'); Senegal's YOUSSOU N'DOUR turns Wolof MBALAX into a world language and lands a "
    "global No. 1 with '7 Seconds'; ALI FARKA TOURE reveals the deep kinship between Malian song and "
    "American blues; and OUMOU SANGARE gives the Wassoulou women's tradition a fierce modern voice. "
    "Cross-links run everywhere: Ali Farka to John Lee Hooker and the whole US blues story (the blues "
    "was always partly Malian); the world-music business to Paris and London; and Mande melody back "
    "toward the Caribbean and Latin surveys. Region: named artists are Malian, Senegalese, Guinean, or "
    "Beninese; foreign duet partners (Neneh Cherry, Cesaria Evora, Ry Cooder) are noted, with the West "
    "African lead credited. Scope calls flagged."
)

SECTIONS = [
    (
        "SALIF KEITA: THE GOLDEN VOICE (Mali)",
        "Salif Keita rose through Bamako's Rail Band and Les Ambassadeurs before going solo and, with "
        "the 1987 album 'Soro', defining the lush, soaring Mande pop of the era. A descendant of "
        "Sundiata himself, singing was forbidden to his noble caste -- and being albino made him an "
        "outcast twice over; his career is an act of defiance. (Scope note: 'Yamore' is a duet with "
        "Cape Verde's Cesaria Evora, credited here to Keita.)",
        [
            ("Mandjou", "Salif Keita"),
            ("Soro (Afriki)", "Salif Keita"),
            ("Yamore", "Salif Keita"),
            ("Madan", "Salif Keita"),
            ("Nou Pas Bouger", "Salif Keita"),
            ("La Difference", "Salif Keita"),
            ("Tekere", "Salif Keita"),
        ],
    ),
    (
        "MORY KANTÉ & THE ELECTRIC KORA (Guinea/Mali)",
        "A Rail Band veteran from a Guinean griot family, Mory Kante plugged the kora into a dance "
        "floor and, in 1987, sent 'Ye Ke Ye Ke' to the top of European charts -- the first African "
        "single to sell a million there. He proved the deepest tradition could be a global disco hit "
        "without apology.",
        [
            ("Ye Ke Ye Ke", "Mory Kante"),
            ("Tama", "Mory Kante"),
            ("Akwaba Beach", "Mory Kante"),
        ],
    ),
    (
        "YOUSSOU N'DOUR & MBALAX (Senegal)",
        "Youssou N'Dour rebuilt Cuban-tinged Senegalese dance music around the frenetic sabar drumming "
        "of the Wolof to create MBALAX, and with his Super Etoile band and a voice of astonishing power "
        "became Africa's biggest star. His 1994 duet '7 Seconds' with Neneh Cherry was a worldwide No. 1. "
        "(Scope note: '7 Seconds' features the Swedish artist Neneh Cherry; credited here to N'Dour.)",
        [
            ("7 Seconds", "Youssou N'Dour"),
            ("Immigres", "Youssou N'Dour"),
            ("Birima", "Youssou N'Dour"),
            ("Set", "Youssou N'Dour"),
            ("Nelson Mandela", "Youssou N'Dour"),
        ],
    ),
    (
        "THE SENEGAMBIAN WAVE: BAABA MAAL, ISMAËL LÔ & ORCHESTRA BAOBAB (Senegal)",
        "Around N'Dour rose a whole Senegambian generation. Baaba Maal sang in Pulaar from the Fula "
        "north; Ismael Lo's harmonica-and-guitar songs earned him 'the African Bob Dylan'; Toure Kunda "
        "pioneered the Paris-African crossover; and the veteran Afro-Cuban Orchestra Baobab was "
        "gloriously revived. Cross-link: Baobab's sound loops straight back to the Cuban son of the "
        "Latin America survey.",
        [
            ("Djam Leelii", "Baaba Maal"),
            ("Yela", "Baaba Maal"),
            ("Tajabone", "Ismael Lo"),
            ("Jammu Africa", "Ismael Lo"),
            ("Emma", "Toure Kunda"),
            ("Utru Horas", "Orchestra Baobab"),
        ],
    ),
    (
        "ALI FARKA TOURÉ & DESERT BLUES (Mali)",
        "From Niafunke on the Niger bend, Ali Farka Toure played a hypnotic, one-chord guitar music "
        "that sounded uncannily like the Mississippi blues -- because, he argued, the blues had gone "
        "the other way, born of Malian roots carried across the Atlantic. His 1994 'Talking Timbuktu' "
        "with Ry Cooder won a Grammy. Cross-link: this is the single clearest musical proof of the "
        "West-Africa-to-US-blues thread (John Lee Hooker especially).",
        [
            ("Ai Du", "Ali Farka Toure"),
            ("Diaraby", "Ali Farka Toure"),
            ("Amandrai", "Ali Farka Toure"),
            ("Soukora", "Ali Farka Toure"),
            ("Debe (In the Heart of the Moon)", "Ali Farka Toure & Toumani Diabate"),
        ],
    ),
    (
        "THE WASSOULOU WOMEN: OUMOU SANGARÉ & THE FEMALE VOICE (Mali)",
        "South of Bamako, the Wassoulou region's hunter-song tradition -- sung largely by women, on the "
        "gourd harp kamele ngoni -- produced a superstar in Oumou Sangare, whose songs championed "
        "women's rights, denounced polygamy and forced marriage, and still filled dance floors. Nahawa "
        "Doumbia and others carried the same banner. This is West Africa's great feminist pop.",
        [
            ("Diaraby Nene", "Oumou Sangare"),
            ("Saa Magni", "Oumou Sangare"),
            ("Ah Ndiya", "Oumou Sangare"),
            ("Moussolou", "Oumou Sangare"),
            ("Yankaw", "Nahawa Doumbia"),
        ],
    ),
    (
        "THE WORLD STAGE: KIDJO, THE GLOBAL KORA & AMADOU & MARIAM (Benin/Mali)",
        "The era's final leap was fully global. Benin's Angelique Kidjo fused West African song with "
        "funk, rumba, and rock into an international pop career and a shelf of Grammys; Toumani Diabate "
        "took the kora onto the world's biggest stages with his Symmetric Orchestra; and the blind "
        "Malian couple Amadou & Mariam began the crossover that would soon make them festival "
        "headliners. Cross-link: Kidjo's Yoruba roots tie back to the batá/candomble thread of the "
        "Latin America survey.",
        [
            ("Agolo", "Angelique Kidjo"),
            ("Batonga", "Angelique Kidjo"),
            ("Wombo Lombo", "Angelique Kidjo"),
            ("Boulevard de l'Independance", "Toumani Diabate & the Symmetric Orchestra"),
            ("Je Pense a Toi", "Amadou & Mariam"),
        ],
    ),
    (
        "THE BAMAKO ORCHESTRA ROOTS (context, c. 1970-1985)",
        "All of the above grew from Mali's post-independence dance orchestras -- the state-sponsored "
        "big bands where Salif Keita and Mory Kante first sang, blending Cuban charanga, highlife, and "
        "Mande melody. These are the launchpads; search the reissued 1970s sides.",
        [
            ("Rail Band of Bamako (Salif & Mory's launchpad)", None),
            ("Les Ambassadeurs du Motel de Bamako", None),
            ("Kasse Mady Diabate (Malian golden voice)", None),
        ],
    ),
]

STEM = "ssa_west_music_6_MANDE_SUPERSTARS_WORLDMUSIC"


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
