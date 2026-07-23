#!/usr/bin/env python3
"""Build Oceania / the Pacific, installment 3: Micronesia & the Island-Pop / String-Band / Hymnody Era.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Pacific & Oceanian Music — Installment 3: "
         "Micronesia & the Island-Pop, String-Band & Hymnody Era")

FRAMING = (
    "This installment covers MICRONESIA -- the thousands of small islands of the northwest Pacific -- and "
    "the great 20th-century POPULAR sound that came to bind the whole ocean. Micronesia (the Marshalls, "
    "Kiribati, Chuuk, Pohnpei, Palau, Yap, Chamorro Guam) keeps its own stick dances, chant, and "
    "navigation songs, and, like all the Pacific, an overwhelming tradition of church HYMNODY. Over the "
    "century, three things spread across every island group and fused into a shared 'ISLAND MUSIC': the "
    "UKULELE and guitar STRING-BAND sound (born of Hawaiian influence and the wartime meeting of peoples), "
    "the glorious missionary-seeded close-harmony HIMENE/hymn singing, and -- from the 1970s -- ISLAND "
    "REGGAE, the Pacific's embrace of Jamaican reggae into its own laid-back, harmony-rich style. Together "
    "these made the sweet, guitar-and-voice 'Pasifika' sound heard from Papua to Tahiti. Content notes: "
    "the nuclear testing that devastated the Marshall Islands (and the songs of exile it produced) and the "
    "colonial/missionary history are treated factually and with respect. Names romanized to ASCII. Region: "
    "Micronesia & the pan-Pacific popular sound."
)

SECTIONS = [
    (
        "MICRONESIA: CHANT, STICK-DANCE & NAVIGATION",
        "Micronesia's island cultures keep vibrant traditions of group chant and the STICK DANCE (the "
        "Marshallese and Yapese stick dances, the beating sticks marking intricate rhythm), alongside the "
        "chants that once encoded the astonishing wayfinding knowledge of the Pacific navigators who "
        "settled these tiny, scattered atolls.",
        [
            ("Micronesian chant & group song", None),
            ("The stick dance (the Marshallese & Yapese bwebwenato)", None),
            ("Navigation chant (the wayfinders' songs)", None),
            ("The atoll cultures of Micronesia (chant & dance)", None),
        ],
    ),
    (
        "THE ISLAND GROUPS & THE CHAMORRO",
        "Each Micronesian nation has its own voice: Kiribati's powerful seated song and the te kaimatoa; "
        "Palau and Pohnpei's chant and dance; and the CHAMORRO people of Guam and the Marianas, whose "
        "music blends Pacific, Spanish (from centuries of colonization), and American strands into the "
        "belembaotuyan gourd-bow and the Chamorro song.",
        [
            ("Kiribati song & dance (the seated te kaimatoa)", None),
            ("Chamorro music of Guam & the Marianas", None),
            ("The belembaotuyan (the Chamorro musical bow)", None),
            ("Palauan & Pohnpeian chant (the island voices)", None),
            ("The Spanish-Pacific blend (the Chamorro heritage)", None),
        ],
    ),
    (
        "THE MARSHALL ISLANDS & THE SONGS OF EXILE",
        "The Marshall Islands sing rich hymn-harmony and traditional chant -- and carry a hard modern "
        "history. Content note: US nuclear testing at Bikini and Enewetak (1946-1958) displaced whole "
        "communities and poisoned islands; the exile and loss are remembered in Marshallese song, kept "
        "factual and with care.",
        [
            ("Marshallese hymn harmony (the roro & the church song)", None),
            ("Songs of the nuclear exile (Bikini & Enewetak, content note)", None),
            ("Traditional Marshallese chant", None),
            ("The Marshall Islands & the bomb (music of memory)", None),
        ],
    ),
    (
        "THE UKULELE & THE STRING BAND",
        "The single most transforming sound in the modern Pacific was the STRING BAND -- ukuleles, "
        "guitars, and voices in sweet harmony -- spread by Hawaiian influence, traders, and the vast "
        "meeting of peoples in the Second World War. From PNG to the Solomons to Polynesia, the string "
        "band became the everyday music of the islands.",
        [
            ("The Pacific string band (ukulele, guitar & voice)", None),
            ("The ukulele across the Pacific (the island four-string)", None),
            ("Papua New Guinea string bands (the PNG sound)", None),
            ("Solomon Islands & Vanuatu string bands", None),
            ("The wartime spread of island music (the WWII meeting)", None),
        ],
    ),
    (
        "THE HYMNODY THAT BINDS THE OCEAN",
        "No sound is more pan-Pacific than the church HYMN, sung in soaring, richly harmonized "
        "congregational voices. Seeded by 19th-century missionaries and utterly transformed by island "
        "singers, the HIMENE and hymn harmony became a central, beloved music from Micronesia to Melanesia "
        "to Polynesia -- often a community's proudest musical art.",
        [
            ("Pacific hymn harmony (the pan-island church song)", None),
            ("The himene / hymn tradition across Oceania", None),
            ("Congregational close harmony (the island choir)", None),
            ("The missionary hymn transformed (the island voice)", None),
        ],
    ),
    (
        "ISLAND REGGAE IS BORN",
        "From the 1970s, Jamaican reggae swept the Pacific and was remade in its own image: ISLAND REGGAE "
        "(and Hawaii's 'Jawaiian'), a laid-back, harmony-rich, ukulele-and-guitar reggae that became the "
        "definitive modern island sound. The Fijian and Hawaiian scenes led, and it spread to every "
        "shore. Cross-link: Jamaican reggae (the Caribbean survey).",
        [
            ("Island reggae (the Pacific's own reggae)", None),
            ("Jawaiian (the Hawaiian reggae sound)", None),
            ("The birth of Pacific reggae (the 1970s embrace)", None),
            ("Reggae remade for the islands (the laid-back harmony)", None),
            ("Reggae comes to the Pacific (cross-link)", None),
        ],
    ),
    (
        "THE HAWAIIAN RENAISSANCE & THE ISLAND SOUND",
        "In 1970s Hawaii, a cultural RENAISSANCE revived the language, hula, and slack-key -- and fused "
        "them with contemporary sounds. The Sunday Manoa and the Brothers Cazimero renewed Hawaiian "
        "music, and the sweet 'contemporary Hawaiian' style set the template for a modern island-pop that "
        "spread across the ocean. Cross-link: Hawaiian roots (#2).",
        [
            ("Guava Jam (the Hawaiian renaissance sound)", "The Sunday Manoa"),
            ("The Hawaiian renaissance (the 1970s revival)", None),
            ("The Brothers Cazimero (contemporary Hawaiian music)", None),
            ("Contemporary Hawaiian (the modern island template)", None),
            ("Language & music revived (the Hawaiian renewal)", None),
        ],
    ),
    (
        "THE SHARED 'ISLAND MUSIC'",
        "By the late 20th century, a shared Pacific popular music had emerged -- guitars, ukuleles, sweet "
        "layered harmony, gentle reggae and hymn influence, sung in island languages and English -- that "
        "everyone from Fiji to Samoa to PNG recognized as 'island music'. It is the warm, communal sound "
        "of the modern Pacific, and the foundation of the pop present (#4).",
        [
            ("Island music (the shared modern Pacific sound)", None),
            ("Sweet harmony & the island guitar (the Pasifika style)", None),
            ("The pan-Pacific popular song (many isles, one sound)", None),
            ("Sung in island tongues (the language of island music)", None),
        ],
    ),
    (
        "THE ISLAND-POP FOUNDATION & THE ROAD AHEAD",
        "From Micronesian chant and the songs of nuclear exile to the ukulele string band, the pan-Pacific "
        "hymn, and the birth of island reggae, the 20th century wove the Pacific into a shared popular "
        "music. From this foundation the survey turns to the modern Pacific and Aboriginal/Maori pop of "
        "today (#4, the finale). Cross-links: the deep roots (#1-2); Caribbean reggae; the global present.",
        [
            ("The island-pop foundation (string band, hymn & reggae)", None),
            ("A shared ocean of song (the pan-Pacific sound)", None),
            ("Tradition meets the guitar & reggae (the island fusion)", None),
            ("Toward modern Pacific & Maori pop (roads ahead)", None),
        ],
    ),
]

STEM = "pacific_music_3_MICRONESIA_ISLAND_POP"


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
