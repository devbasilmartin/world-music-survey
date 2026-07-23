#!/usr/bin/env python3
"""Build Southeast Asia, installment 2: Mainland Classical & Folk Traditions.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Southeast Asian Music — Installment 2: "
         "Mainland Classical & Folk Traditions (Thai, Khmer, Burmese, Vietnamese & Lao)")

FRAMING = (
    "Mainland Southeast Asia -- Thailand, Cambodia, Myanmar, Vietnam, Laos -- carries some of the "
    "world's most refined court and folk musics, shaped by Indian and Chinese contact yet wholly its "
    "own. The Thai and Khmer share a family of gong-and-xylophone ensembles (the PIPHAT and PINPEAT) "
    "born to accompany masked dance and the Ramayana; Myanmar's astonishing SAING WAING tunes whole "
    "circles of drums and gongs, and its arched SAUNG-GAUK harp is one of the oldest continuously played "
    "on Earth; Vietnam's Sinicized court music (NHA NHAC) and the exquisite sung poetry of CA TRU stand "
    "beside the haunting one-string DAN BAU; and across Laos and Thailand's Isan northeast, the "
    "free-reed KHAEN mouth-organ drives the witty sung poetry of MOR LAM. This installment covers the "
    "classical and folk roots before the 20th-century pop era. Cross-links: the Indian Ramayana "
    "(Ramakien/Reamker); Chinese court music and the sheng (kin to the khaen); the island gamelan world "
    "(#1). Content note: the Khmer Rouge's near-annihilation of Cambodian music and its revival are kept "
    "factual and with care. Names transliterated. Region: mainland Southeast Asia."
)

SECTIONS = [
    (
        "THAI CLASSICAL: PIPHAT, MAHORI & THE COURT",
        "Thai classical music centers on the PIPHAT -- a percussion-and-oboe ensemble for ritual and "
        "theater -- and the gentler string ensembles MAHORI and khruang sai for the court and chamber. "
        "Built on a distinctive seven-tone, nearly equidistant tuning, its interlocking layers of "
        "elaboration around a core melody are cousins to the gamelan idea.",
        [
            ("Thai classical music (the piphat & the court)", None),
            ("Piphat (the percussion-and-oboe ensemble)", None),
            ("Mahori & khruang sai (the Thai string ensembles)", None),
            ("The seven-tone equidistant Thai tuning", None),
            ("Layered elaboration around a core melody (Thai style)", None),
        ],
    ),
    (
        "THE THAI INSTRUMENTS, THE KHON & THE RAMAKIEN",
        "The Thai ensemble sparkles with the ranat ek and ranat thum xylophones, the khong wong "
        "gong-circles, the pi oboe, and the taphon and klong drums. It comes alive in the KHON masked "
        "dance-drama, staging the Ramakien -- Thailand's Ramayana. The sepha narrative and the film "
        "'The Overture' celebrate the ranat master's art. Cross-link: the Indian Ramayana.",
        [
            ("Ranat ek & ranat thum (the Thai xylophones)", None),
            ("Khong wong (the Thai gong-circles)", None),
            ("Pi & the Thai drums (oboe, taphon, klong)", None),
            ("The khon masked dance & the Ramakien (Thai Ramayana)", None),
            ("The ranat virtuoso (the sepha & 'The Overture')", None),
        ],
    ),
    (
        "CAMBODIA: PINPEAT & THE KHMER COURT",
        "Cambodia's classical music, the PINPEAT ensemble, is kin to the Thai piphat and reaches back to "
        "the glory of Angkor, whose bas-reliefs depict its instruments. It accompanies the sublime Royal "
        "Ballet -- the robam / Apsara dance -- and the sacred smot chant, an art of exquisite courtly "
        "refinement carved in stone a thousand years ago.",
        [
            ("Pinpeat (the Khmer classical ensemble)", None),
            ("The Khmer Royal Ballet (robam & the Apsara dance)", None),
            ("Roneat & korng (the Khmer xylophone & gong-circle)", None),
            ("Angkor & its musicians (the bas-relief heritage)", None),
            ("Smot (the Khmer sacred chant)", None),
        ],
    ),
    (
        "THE KHMER ROUGE & THE MUSIC'S REBIRTH",
        "Cambodia's music nearly died. Content note: under the Khmer Rouge (1975-1979), an estimated "
        "nine in ten of the country's musicians, dancers, and master artists were murdered or perished, "
        "almost severing a thousand-year tradition. The survivors and a new generation have painstakingly "
        "revived it (Cambodian Living Arts) -- a story of loss and extraordinary resilience.",
        [
            ("The Khmer Rouge & the near-death of Khmer music (content note)", None),
            ("A thousand-year tradition almost severed", None),
            ("The masters who survived (the fragile thread)", None),
            ("The revival (Cambodian Living Arts & the new generation)", None),
            ("Music as resilience (rebuilding after genocide)", None),
        ],
    ),
    (
        "MYANMAR: THE SAING WAING & THE SAUNG-GAUK HARP",
        "Burmese classical music is unlike any other. The SAING WAING ensemble tunes entire circles of "
        "instruments -- the pat waing (a ring of 21 drums played by one seated musician), the kyi waing "
        "gong-circle, and the hne oboe -- around the pattala bamboo xylophone. And the arched SAUNG-GAUK "
        "harp, Myanmar's national instrument, sings the Mahagita, the great classical songbook.",
        [
            ("Saing waing (the Burmese tuned-ensemble)", None),
            ("Pat waing (the circle of 21 tuned drums)", None),
            ("Saung-gauk (the Burmese arched harp)", None),
            ("The Mahagita (the great Burmese song repertoire)", None),
            ("Pattala & sandaya (the Burmese xylophone & piano)", None),
        ],
    ),
    (
        "VIETNAM: THE COURT & CA TRU",
        "Vietnam's classical music leans toward its Chinese neighbor yet keeps a distinct grace. The "
        "royal court music of Hue -- NHA NHAC (nhac cung dinh) -- is a UNESCO treasure, and CA TRU, an "
        "ancient chamber art of a female singer with the dan day lute and the phach clapper setting "
        "sung poetry, is one of the world's most refined vocal traditions. Cross-link: Chinese court "
        "music.",
        [
            ("Nha nhac (the Vietnamese royal court music of Hue)", None),
            ("Ca tru (the ancient sung-poetry chamber art)", None),
            ("The dan day & phach (the ca tru instruments)", None),
            ("Vietnamese court & ceremonial music", None),
            ("Quan ho (the northern folk love-duets)", None),
        ],
    ),
    (
        "THE VIETNAMESE INSTRUMENTS & CAI LUONG",
        "Vietnam's instruments are singular: the DAN BAU, a one-string monochord whose flexed harmonics "
        "bend like a human voice; the dan tranh 16-string zither; and the dan nguyet moon-lute. In the "
        "south, 'Da Co Hoai Lang' (1919) seeded the vong co and the reformed opera CAI LUONG, the "
        "popular musical theater of the Mekong delta.",
        [
            ("Da Co Hoai Lang (the ancestor of vong co)", "Cao Van Lau"),
            ("Dan bau (the one-string monochord)", None),
            ("Dan tranh & dan nguyet (the zither & moon-lute)", None),
            ("Vong co & cai luong (the southern reformed opera)", None),
            ("Nhac tai tu (the southern chamber music)", None),
        ],
    ),
    (
        "LAOS & ISAN: THE KHAEN & MOR LAM",
        "Across Laos and Thailand's Isan northeast sounds the KHAEN -- a free-reed bamboo mouth-organ, "
        "kin to the Chinese sheng, whose buzzing drone and dancing melody is the soul of the region. "
        "Over it flies MOR LAM, a fast, witty, half-sung half-spoken poetry of courtship and everyday "
        "life -- the beating heart of Lao and Isan folk music. Cross-link: the sheng of the China survey.",
        [
            ("Khaen (the Lao free-reed mouth-organ)", None),
            ("Mor lam (the Lao/Isan sung poetry)", None),
            ("The khaen drone & dancing melody", None),
            ("Lam styles (the mor lam repertoire)", None),
            ("The khaen & the Chinese sheng (cross-link)", None),
        ],
    ),
    (
        "THE MAINLAND AESTHETIC & THE ROAD AHEAD",
        "Mainland Southeast Asia's music grew from a shared Theravada-Buddhist and Hindu court heritage, "
        "Indianized in the Thai-Khmer-Burmese west and Sinicized in Vietnam, yet everywhere distinct. "
        "Cross-links: the island gamelan world (#1); India and China on either side. From these roots "
        "grew the 20th-century crooner and pop eras -- luk thung, cai luong pop, and more (Installment "
        "3).",
        [
            ("The Theravada-Buddhist & Hindu court heritage", None),
            ("Indianized west, Sinicized east (the mainland split)", None),
            ("Shared gong-and-xylophone family (Thai-Khmer-Lao)", None),
            ("Toward the 20th-century pop era (roads ahead)", None),
        ],
    ),
]

STEM = "sea_music_2_MAINLAND_CLASSICAL_FOLK"


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
