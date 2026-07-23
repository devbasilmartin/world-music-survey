#!/usr/bin/env python3
"""Build Oceania / the Pacific, installment 4 (FINALE): Modern Pacific & Aboriginal/Maori Pop.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Pacific & Oceanian Music — Installment 4 (Finale): "
         "Modern Pacific & Aboriginal/Maori Pop")

FRAMING = (
    "The final Pacific chapter carries the oldest music on Earth into the global present. In Australia, "
    "ABORIGINAL musicians fused their heritage with rock, country, and hip-hop: Yothu Yindi's 'Treaty' "
    "put the didgeridoo on the world's dancefloors, Archie Roach sang the Stolen Generations, the sublime "
    "blind Yolngu singer GURRUMUL became a national treasure, and Baker Boy now raps in Yolngu Matha. In "
    "Aotearoa, MAORI and PASIFIKA artists built a world-class scene -- Herbs' Pacific reggae, OMC's global "
    "hit 'How Bizarre', Che Fu, Six60 (one of the biggest bands in the hemisphere), Stan Walker, and a "
    "flowering of te reo Maori song. Across the islands, ISLAND REGGAE reigns (Katchafire, J Boog, Fiji, "
    "Common Kings), and a huge Pacific DIASPORA shapes the music of New Zealand and Australia. This closes "
    "the Pacific survey and ties its whole arc -- from the songlines to the global stage -- together. "
    "Content notes: the Stolen Generations, colonization, and Indigenous struggle are treated factually, "
    "respectfully, and as the substance of much of this music. Cross-links: Caribbean reggae; the deep "
    "roots (#1-3); global pop. Names romanized to ASCII. Region: the modern Pacific & its diaspora."
)

SECTIONS = [
    (
        "ABORIGINAL ROCK & YOTHU YINDI",
        "Aboriginal Australia found a powerful modern voice in rock. Yothu Yindi's 'Treaty' (1991) fused "
        "Yolngu song and the didgeridoo with dance-rock into an international hit and a landmark of "
        "Indigenous political music, and the Warumpi Band ('Blackfella/Whitefella') brought desert rock to "
        "the nation. Cross-link: the yidaki (#1).",
        [
            ("Treaty", "Yothu Yindi"),
            ("Blackfella Whitefella", "Warumpi Band"),
            ("Yothu Yindi (the Yolngu rock pioneers)", None),
            ("Aboriginal rock (the didgeridoo meets the band)", None),
            ("Indigenous political song (music & land rights)", None),
        ],
    ),
    (
        "ARCHIE ROACH & THE STOLEN GENERATIONS",
        "Archie Roach's 'Took the Children Away' (1990) gave unforgettable voice to the Stolen Generations "
        "-- the Aboriginal children forcibly removed from their families. Content note: this history is "
        "painful and real, and Roach, himself taken as a child, sang it with grace and without hatred, "
        "making it one of the most important Australian songs ever written.",
        [
            ("Took the Children Away", "Archie Roach"),
            ("Archie Roach (the voice of the Stolen Generations)", None),
            ("The Stolen Generations in song (content note)", None),
            ("Aboriginal country & folk (the storytelling tradition)", None),
            ("Kev Carmody (the Aboriginal singer-songwriter)", None),
        ],
    ),
    (
        "GURRUMUL & THE NEW ABORIGINAL VOICES",
        "Geoffrey Gurrumul Yunupingu -- blind from birth, singing in Yolngu Matha in a voice of "
        "heart-stopping beauty -- became one of Australia's most beloved artists. A new generation "
        "followed: Christine Anu's 'My Island Home', Jessica Mauboy's pop, and Baker Boy, who raps in "
        "Yolngu Matha and English. The oldest culture speaks in the newest forms.",
        [
            ("Wiyathul", "Gurrumul"),
            ("My Island Home", "Christine Anu"),
            ("Marryuna", "Baker Boy"),
            ("Gurrumul (the sublime Yolngu voice)", None),
            ("Jessica Mauboy & modern Aboriginal pop", None),
        ],
    ),
    (
        "MAORI MODERN MUSIC & TE REO POP",
        "Maori artists built a vibrant modern scene and a flowering of te reo Maori (language) song. Herbs "
        "pioneered Aotearoa's Pacific reggae; the Patea Maori Club's 'Poi E' became a beloved landmark; "
        "and today Maisey Rika, Rob Ruha, and the te reo charts carry the language into contemporary pop. "
        "Cross-link: the haka & waiata (#2).",
        [
            ("Poi E", "Patea Maori Club"),
            ("E Papa (the modern te reo song)", "Maisey Rika"),
            ("Herbs (the Aotearoa Pacific-reggae pioneers)", None),
            ("Te reo Maori pop (the language revival in song)", None),
            ("Modern Maori music (the contemporary scene)", None),
        ],
    ),
    (
        "PASIFIKA & THE AOTEAROA SOUND",
        "New Zealand's Pacific and Maori artists produced global and national hits: OMC's 'How Bizarre' "
        "became a worldwide smash, Che Fu blended soul and reggae, Bic Runga sang exquisite pop, and Six60 "
        "grew into one of the biggest bands in the Southern Hemisphere. Stan Walker carries a powerful "
        "Maori-Pasifika voice.",
        [
            ("How Bizarre", "OMC"),
            ("Sweet Disposition (the Aotearoa pop era)", "Bic Runga"),
            ("Don't Forget Your Roots", "Six60"),
            ("Che Fu (the NZ soul-reggae voice)", None),
            ("Stan Walker (the Maori-Pasifika star)", None),
        ],
    ),
    (
        "ISLAND REGGAE TODAY",
        "Island reggae is the dominant modern Pacific sound. New Zealand's Katchafire, the Samoan-American "
        "J Boog ('Let's Do It Again'), Fiji (the artist), the Green from Hawaii, and Common Kings fill "
        "arenas across the Pacific and its diaspora with laid-back, harmony-rich roots reggae. Cross-link: "
        "Jamaican reggae (the Caribbean survey).",
        [
            ("Let's Do It Again", "J Boog"),
            ("Island reggae today (the dominant Pacific sound)", None),
            ("Katchafire (the Aotearoa roots-reggae band)", None),
            ("Common Kings & the Green (the island-reggae wave)", None),
            ("Fiji (the island-reggae star)", None),
        ],
    ),
    (
        "THE PACIFIC ISLANDS & PNG MODERN POP",
        "Across the islands, modern pop, hip-hop, and reggae thrive in local languages: Papua New Guinea's "
        "booming pop and string-band-descended music, Samoan and Tongan hip-hop, Tahitian and Fijian pop, "
        "and the reggae and R&B of the wider Pacific. The island sound of #3 grew into a full contemporary "
        "industry.",
        [
            ("Papua New Guinea modern pop (the PNG scene)", None),
            ("Samoan & Tongan hip-hop (the Pasifika rap)", None),
            ("Tahitian & Fijian modern pop", None),
            ("Pacific R&B & reggae (the island contemporary sound)", None),
            ("The modern island-language pop (the local charts)", None),
        ],
    ),
    (
        "THE PASIFIKA DIASPORA & THE GLOBAL STAGE",
        "The vast Pacific diaspora -- Maori and Pasifika communities in New Zealand, Australia, Hawaii, and "
        "the US -- became a powerhouse of Southern Hemisphere music, shaping hip-hop, R&B, reggae, gospel, "
        "and pop far beyond the islands. From church choirs to global charts, the Pacific voice travels. "
        "Cross-links: the US and global pop worlds.",
        [
            ("The Pasifika diaspora sound (NZ, Australia & beyond)", None),
            ("Pacific hip-hop & R&B (the diaspora scene)", None),
            ("Pasifika gospel & church music (the diaspora choir)", None),
            ("The Pacific voice goes global (the wider stage)", None),
        ],
    ),
    (
        "THE PACIFIC ARC: A FINALE",
        "Four installments span the widest ocean: the forty-thousand-year songlines and the yidaki, the "
        "Polynesian chant and hula, the ukulele string band and the island hymn, and now a modern pop that "
        "carries the oldest music on Earth to the global stage. From the songline to the global chart, the "
        "Pacific sings its country still. This closes the Pacific survey. Cross-links: Southeast Asia; the "
        "Caribbean; the Americas; the world.",
        [
            ("The Pacific arc (from the songlines to the global stage)", None),
            ("The oldest music meets the newest (the Pacific genius)", None),
            ("Song as country, memory & survival (the Oceanic soul)", None),
            ("Toward the surveys ahead (roads onward)", None),
        ],
    ),
]

STEM = "pacific_music_4_MODERN_POP"


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
