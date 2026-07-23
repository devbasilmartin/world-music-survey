#!/usr/bin/env python3
"""Build Oceania / the Pacific, installment 1: Aboriginal Australia & Melanesia.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Pacific & Oceanian Music — Installment 1: "
         "Aboriginal Australia & Melanesia (The Oldest Continuous Music on Earth)")

FRAMING = (
    "Oceania holds humanity's oldest living music. The ABORIGINAL peoples of Australia have sung their "
    "country for more than forty thousand years -- the longest continuous musical culture on Earth -- in "
    "the SONGLINES (dreaming tracks) that map the land in song, sung to the click of CLAPSTICKS and, in "
    "the north, the deep buzzing drone of the DIDGERIDOO (yidaki), sounded by circular breathing. To the "
    "north and east, MELANESIA -- New Guinea, the Solomons, Vanuatu, Fiji -- is one of the most musically "
    "diverse regions anywhere: Papua New Guinea alone has hundreds of languages and a wealth of kundu "
    "hand-drums, garamut slit-gongs, sacred flutes, and vast SING-SING festival gatherings; the Solomon "
    "Islands answer with shimmering bamboo PANPIPE orchestras; and Vanuatu women play the water itself as "
    "a drum. This installment lays Oceania's deepest foundation before Polynesia (#2). Content notes: much "
    "of this music is sacred or secret-sacred, was gravely disrupted by colonization, and raises real "
    "questions about the ethics of recording and sampling Indigenous music -- all treated factually and "
    "with deep respect. Names as commonly romanized. Region: Aboriginal Australia & Melanesia."
)

SECTIONS = [
    (
        "THE OLDEST LIVING MUSIC: ABORIGINAL AUSTRALIA",
        "Aboriginal Australians have maintained an unbroken musical tradition for over forty thousand "
        "years -- the oldest continuous culture on Earth. Their music is inseparable from the Dreaming "
        "(the Tjukurpa), the land, and ceremony; song is law, map, and history at once. Content note: "
        "this is a living sacred tradition, treated with deep respect.",
        [
            ("The oldest continuous music on Earth (Aboriginal Australia)", None),
            ("Song, land & the Dreaming (the Tjukurpa)", None),
            ("Aboriginal ceremony & the sacred song", None),
            ("Forty thousand years of song (the unbroken tradition)", None),
        ],
    ),
    (
        "THE DIDGERIDOO / YIDAKI",
        "The DIDGERIDOO -- properly the YIDAKI of Arnhem Land -- is a wooden drone pipe, often a "
        "termite-hollowed eucalyptus branch, sounded through continuous CIRCULAR BREATHING so the deep, "
        "buzzing drone never stops, shaped by the player's voice and mouth into rhythmic textures. It is "
        "one of the world's oldest wind instruments.",
        [
            ("The didgeridoo / yidaki (the Aboriginal drone pipe)", None),
            ("Circular breathing (the unbroken drone)", None),
            ("The yidaki of Arnhem Land (the northern tradition)", None),
            ("The voice inside the drone (didgeridoo technique)", None),
            ("Djalu Gurruwiwi (the yidaki master & keeper)", None),
        ],
    ),
    (
        "THE SONGLINES, CLAPSTICKS & CORROBOREE",
        "Aboriginal song is carried by the SONGLINES -- sung paths that map the country across vast "
        "distances -- and marked by the CLAPSTICKS (bilma) that set the rhythm beneath the voice. Public "
        "ceremonies (corroboree) gather song, dance, and body-paint into performance, while deeper songs "
        "remain restricted. Content note: many songs are secret-sacred and not for outside performance.",
        [
            ("The songlines (the sung map of country)", None),
            ("Clapsticks / bilma (the Aboriginal rhythm sticks)", None),
            ("Corroboree (the Aboriginal ceremonial gathering)", None),
            ("Manikay (the song-cycles of Arnhem Land)", None),
            ("The restricted & the public song (secret-sacred, content note)", None),
        ],
    ),
    (
        "THE TORRES STRAIT & THE CENTRE",
        "Between Australia and New Guinea, the TORRES STRAIT Islanders -- a Melanesian people -- have their "
        "own vibrant song and dance (the island dance, the warup drum) and rich Christian hymn-singing. "
        "Across the desert Centre, women's and men's ceremonial song-cycles (the inma, the awelye) carry "
        "the Dreaming of the great song-countries.",
        [
            ("Torres Strait Islander song & dance (the warup drum)", None),
            ("The island dance of the Torres Strait", None),
            ("Inma & awelye (the desert ceremonial song-cycles)", None),
            ("Aboriginal women's ceremony & song", None),
        ],
    ),
    (
        "MELANESIA: PAPUA NEW GUINEA'S DIVERSITY",
        "Papua New Guinea is one of the most culturally diverse places on Earth -- over eight hundred "
        "languages -- and its music is correspondingly vast. The KUNDU hourglass hand-drum and the great "
        "GARAMUT slit-gong drive song and dance across the highlands and coasts, each people with its own "
        "traditions of ceremony, mask, and voice.",
        [
            ("Kundu (the New Guinea hourglass hand-drum)", None),
            ("Garamut (the New Guinea slit-gong)", None),
            ("Papua New Guinea's musical diversity (800 languages)", None),
            ("Highland song & dance (the PNG ceremony)", None),
            ("The bilas & the dance (the PNG body-adornment)", None),
        ],
    ),
    (
        "THE SING-SING & THE SACRED FLUTES",
        "The great SING-SING festivals gather many tribes for spectacular massed song and dance in full "
        "feather and paint (the Goroka and Mount Hagen shows are famous). Deeper still are the sacred "
        "bamboo FLUTES and BULLROARERS, whose sounds -- often forbidden to the uninitiated -- voice "
        "ancestral spirits. Content note: much of this is initiatory and restricted.",
        [
            ("The sing-sing (the PNG festival gathering)", None),
            ("Massed song & dance (the sing-sing spectacle)", None),
            ("The sacred bamboo flutes of New Guinea", None),
            ("The bullroarer (the ancestral voice, content note)", None),
            ("The Goroka & Mount Hagen shows (the great gatherings)", None),
        ],
    ),
    (
        "THE SOLOMON ISLANDS: BAMBOO PANPIPES & VOICE",
        "The Solomon Islands are famous for shimmering bamboo PANPIPE orchestras -- interlocking players "
        "and 'bamboo band' (the stamped bamboo tubes) -- and for the exquisite panpipe polyphony of the "
        "'Are'are people. The lullaby 'Rorogwela' became world-famous through a controversial sample. "
        "Content note: that sampling raised lasting questions of consent and appropriation.",
        [
            ("Solomon Islands bamboo panpipes (the panpipe orchestra)", None),
            ("The 'Are'are panpipe polyphony", None),
            ("Rorogwela (the Baegu lullaby)", "Afunakwa"),
            ("The bamboo band (the stamped-tube sound)", None),
            ("Sampling & consent (the Rorogwela question, content note)", None),
        ],
    ),
    (
        "VANUATU, FIJI & THE WIDER MELANESIA",
        "Across Vanuatu, the women play the sea itself in WATER-DRUMMING (ETETUNG), slapping the lagoon "
        "into rhythm, alongside the tamtam slit-drums and string bands. Fiji sings rich vocal harmony in "
        "the meke song-dance and the church, and New Caledonia's Kanak people keep their own ceremony and "
        "the modern kaneka. Cross-link: Pacific string bands (#3).",
        [
            ("Vanuatu water-drumming (etetung, the women's water music)", None),
            ("The tamtam & the Vanuatu slit-drums", None),
            ("Fijian meke (the song-and-dance)", None),
            ("Fijian vocal harmony & the church song", None),
            ("Kanak music of New Caledonia (ceremony & kaneka)", None),
        ],
    ),
    (
        "THE OCEANIC FOUNDATION & THE ROAD AHEAD",
        "From the forty-thousand-year songlines and the yidaki drone to New Guinea's sing-sings and the "
        "Solomon panpipes, Aboriginal Australia and Melanesia hold the deepest musical roots in the "
        "Pacific -- a world of ceremony, drone, drum, and voice. From here the survey sails east to "
        "Polynesia (#2) and the island-pop present. Cross-links: Southeast Asia (the Austronesian voyage); "
        "the Pacific string bands & modern pop (#3-4).",
        [
            ("The Oceanic musical foundation (drone, drum & ceremony)", None),
            ("The world's oldest & most diverse (Australia & Melanesia)", None),
            ("Song as land, law & memory (the Oceanic through-line)", None),
            ("Toward Polynesia & the island present (roads ahead)", None),
        ],
    ),
]

STEM = "pacific_music_1_ABORIGINAL_MELANESIA"


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
