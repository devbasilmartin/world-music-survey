#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Central, installment 3: Soukous & the Second Generation.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1965-1975.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of Central African Music — Installment 3: "
         "Soukous & the Second Generation (c. 1965-1975)")

FRAMING = (
    "The golden-age bands splintered into a second generation that made Congolese music faster, "
    "flashier, and truly continental. In 1963 the star vocalist Tabu Ley Rochereau and the guitar "
    "genius Dr Nico left Le Grand Kalle to form AFRICAN FIESTA, and when that too split (1965) each "
    "led his own band -- Tabu Ley refining a suave, cosmopolitan rumba (and becoming, in 1970, the "
    "first African artist to headline the Paris Olympia), Dr Nico canonizing the crystalline Congolese "
    "lead-guitar style. Meanwhile Franco's OK JAZZ swelled into the mighty TP OK Jazz, the people's "
    "heavyweight. Across all of it, the dance section -- the SEBENE -- grew longer and faster, and the "
    "guitar-driven style earned a new name: SOUKOUS (from the French secouer, 'to shake'). This all "
    "unfolded under Mobutu Sese Seko, whose 1971 'authenticite' campaign renamed the country Zaire and "
    "enlisted music for the state. Cross-links: Congolese emigres carried soukous to Nairobi and Dar es "
    "Salaam, seeding East African pop (the East Africa survey to come); and the Congo guitar remained "
    "the template for the whole continent. Content note: Mobutu's dictatorship and its "
    "cultural-nationalist machinery -- kept with context. Region: DR Congo / Zaire & Congo-Brazzaville."
)

SECTIONS = [
    (
        "TABU LEY ROCHEREAU & AFRICAN FIESTA (c. 1963-1975)",
        "Tabu Ley Rochereau had one of the great voices of African music, and after leaving Kabasele he "
        "built a sophisticated, endlessly melodic rumba with African Fiesta and then his own Afrisa "
        "International. His 1970 concert at the Paris Olympia announced Congolese music to Europe. He "
        "wrote thousands of songs; these are touchstones.",
        [
            ("Mokolo Nakokufa", "Tabu Ley Rochereau"),
            ("Kelya", "Tabu Ley Rochereau"),
            ("Pitie", "Tabu Ley Rochereau"),
            ("Sorozo", "Tabu Ley Rochereau"),
            ("African Fiesta (Rochereau & Dr Nico, post-Kalle)", None),
            ("Rochereau at the Olympia (1970, first African star in Paris)", None),
        ],
    ),
    (
        "DR NICO & AFRICAN FIESTA SUKISA (c. 1965-1975)",
        "Nicolas 'Dr Nico' Kasanda was called 'the God of the Guitar' -- his liquid, singing lead lines "
        "defined what a Congolese guitar could do, and every soukous player since has studied him. "
        "After the African Fiesta split he led African Fiesta Sukisa. His influence is the invisible "
        "spine of everything that follows.",
        [
            ("Aji Special", "Dr Nico"),
            ("Dorothea", "Dr Nico"),
            ("African Fiesta Sukisa (Dr Nico's band)", None),
            ("Dr Nico (the God of the Guitar)", None),
            ("The Congo lead-guitar standard (Nico's legacy)", None),
        ],
    ),
    (
        "FRANCO & OK JAZZ MATURE INTO A HEAVYWEIGHT (c. 1965-1975)",
        "While the Fiesta men dazzled, Franco's OK Jazz grew into the vast TP OK Jazz (Tout Puissant, "
        "'all-powerful') -- a rumba institution of biting Lingala storytelling and Franco's endlessly "
        "inventive rhythm guitar. He was now the towering figure of Zairean music, as much a social "
        "commentator as a bandleader.",
        [
            ("AZDA", "Franco"),
            ("Infidelite Mado", "Franco"),
            ("Course au Pouvoir", "Franco"),
            ("TP OK Jazz (Tout Puissant, the heavyweight)", None),
            ("Franco's mi-solo guitar (maturing)", None),
            ("Lingala social-commentary rumba (Franco)", None),
        ],
    ),
    (
        "THE BIRTH OF SOUKOUS & THE FAST SEBENE",
        "As the dance-floor demanded more, the sebene -- the up-tempo, guitar-led second half of a "
        "rumba -- lengthened and accelerated until it became the whole point, and the style got a new "
        "name: SOUKOUS. Its engine is the interlock of three or more guitars (lead, mi-solo, rhythm) "
        "over a driving bass. This is the sound that conquers the 1980s (Installment 5).",
        [
            ("Soukous (from secouer, the shake)", None),
            ("The fast sebene (the guitar dance section accelerates)", None),
            ("Guitar-led dance rumba (the soukous turn)", None),
            ("Three-guitar interlock (Congo style perfected)", None),
            ("Rumba-to-soukous transition (mid-1960s)", None),
        ],
    ),
    (
        "SAM MANGWANA & THE PAN-AFRICAN VOICE",
        "Sam Mangwana embodied the era's mobility -- a superb vocalist who sang with both OK Jazz and "
        "African Fiesta and roamed the continent, earning the nickname 'the travelling pigeon'. The "
        "musicians moved fluidly between rival bands, and the Congolese star system became a "
        "pan-African institution.",
        [
            ("Georgette Eckins", "Sam Mangwana"),
            ("Sam Mangwana (the pan-African travelling pigeon)", None),
            ("The Congo crooner tradition (vocalist rumba)", None),
            ("Cross-band Congo star system (musicians move between bands)", None),
        ],
    ),
    (
        "AUTHENTICITÉ & ZAIRIANIZATION (Mobutu, c. 1971-1975)",
        "In 1971 Mobutu Sese Seko renamed the Congo 'Zaire' and launched AUTHENTICITE -- a "
        "cultural-nationalist campaign that banned Christian names and Western suits (replaced by the "
        "abacost) and enlisted musicians in state 'animation politique'. Franco and the great bands "
        "navigated a wary, sometimes lucrative bargain with the dictatorship. Content note: this is "
        "music under an authoritarian personality cult -- kept with context.",
        [
            ("Authenticite (Mobutu's cultural nationalism, 1971)", None),
            ("Zaire (the renamed nation, 1971)", None),
            ("Animation politique (state-sponsored music)", None),
            ("Franco and Mobutu (the ambivalent bargain)", None),
            ("Abacost-era Kinshasa nightlife", None),
        ],
    ),
    (
        "SOUKOUS SPREADS: EAST AFRICA & THE CONTINENT",
        "Congolese musicians emigrated and toured relentlessly, and the sound went everywhere: to "
        "Nairobi and Dar es Salaam, where it reshaped Kenyan and Tanzanian pop, and across West and "
        "Southern Africa via radio. Congo rumba/soukous was now the single most influential popular "
        "music in Africa. Cross-link: this seeds the East Africa survey to come.",
        [
            ("Congo rumba in Nairobi (Congolese emigres)", None),
            ("Congo rumba in Dar es Salaam (Tanzania)", None),
            ("Congo guitar seeds East African benga", None),
            ("Franco and Tabu Ley tour the continent", None),
        ],
    ),
]

STEM = "ssa_central_music_3_SOUKOUS_SECOND_GENERATION"


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
