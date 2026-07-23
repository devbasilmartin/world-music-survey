#!/usr/bin/env python3
"""Build the Caribbean, installment 1: Cuban Roots & the Afro-Caribbean Foundation.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Caribbean Music — Installment 1: "
         "Cuban Roots & the Afro-Caribbean Foundation (Son, Rumba, Danzon, Mambo & the Afro-Cuban Sacred)")

FRAMING = (
    "The Caribbean is where Africa and Europe met in the cane fields and the ports, and no island poured "
    "out more music than CUBA. From the marriage of African rhythm and Spanish melody came the SON -- the "
    "guitar-and-tres, clave-driven root of nearly all later Cuban and salsa music -- and the drum-and-voice "
    "RUMBA of the solares (the yard rumba, in its guaguanco, yambu, and columbia forms). Beneath them "
    "beats the sacred: the bata drums and chants of Santeria (the Lucumi/Yoruba religion of the enslaved). "
    "The refined salons gave the DANZON and the charanga; the heart gave the BOLERO; and the mid-century "
    "gave the world the MAMBO and the CHA-CHA-CHA, and Beny More, the 'Barbaro del Ritmo'. Afro-Cuban jazz "
    "(Machito, Chano Pozo) carried the clave to New York. This installment lays the Afro-Cuban foundation "
    "of the whole Caribbean and Latin dance world. Content note: the Afro-Cuban sacred traditions and "
    "their roots in slavery are treated factually and with respect. Cross-links: SALSA and its New York "
    "story live in the Latin America survey -- here we stay on the ISLAND's own roots; West/Central "
    "African rhythm; the wider Caribbean (#2-4). Names transliterated. Region: Cuba & the Afro-Caribbean."
)

SECTIONS = [
    (
        "THE AFRICAN-AND-SPANISH FUSION",
        "Cuban music was born of two worlds: the rhythms and drums of enslaved West and Central Africans "
        "and the melodies, guitars, and song forms of Spain, fused over centuries into something wholly "
        "new. At its center lies the CLAVE -- a two-bar rhythmic key, tapped on two hardwood sticks -- "
        "the organizing pulse of nearly all Cuban music.",
        [
            ("Clave (the rhythmic key of Cuban music)", None),
            ("The African-Spanish fusion (the roots of Cuban music)", None),
            ("The clave sticks & the Cuban pulse", None),
            ("Cuba, the crossroads of the Caribbean", None),
        ],
    ),
    (
        "THE SON: THE ROOT OF IT ALL",
        "The SON, born in the eastern hills of Oriente, married the Spanish guitar and the Cuban tres to "
        "African call-and-response and clave, becoming the fountainhead of Cuban popular music and the "
        "direct ancestor of salsa. The Trio Matamoros and Ignacio Pineiro's Septeto Nacional made it a "
        "national art. Cross-link: salsa in the Latin America survey.",
        [
            ("Son de la Loma", "Trio Matamoros"),
            ("Echale Salsita", "Ignacio Pineiro"),
            ("Son cubano (the root of Cuban popular music)", None),
            ("The tres & the son ensemble (guitar, tres, bongo)", None),
            ("The Septeto & the son montuno (the call-and-response)", None),
        ],
    ),
    (
        "THE BUENA VISTA REVIVAL",
        "In 1997, a group of veteran Cuban musicians -- many long retired -- recorded the Buena Vista "
        "Social Club, a worldwide sensation that reintroduced the classic son and bolero to a new global "
        "generation. Ibrahim Ferrer's velvet voice, Compay Segundo's songs, and Ruben Gonzalez's piano "
        "became beloved the world over.",
        [
            ("Chan Chan", "Compay Segundo"),
            ("Dos Gardenias", "Ibrahim Ferrer"),
            ("Candela", "Buena Vista Social Club"),
            ("El Cuarto de Tula", "Buena Vista Social Club"),
            ("The Buena Vista Social Club (the global son revival)", None),
        ],
    ),
    (
        "RUMBA: THE DRUM & THE YARD",
        "The true Afro-Cuban RUMBA is not ballroom dance but a secular drum-and-voice tradition of the "
        "solares (tenement yards) -- conga drums, claves, and call-and-response singing in three forms: "
        "the flirtatious GUAGUANCO, the slow YAMBU, and the fast, acrobatic male COLUMBIA. Los Munequitos "
        "de Matanzas are its masters.",
        [
            ("Rumba guaguanco (the flirtation dance-song)", None),
            ("Yambu & columbia (the slow & the acrobatic rumba)", None),
            ("Los Munequitos de Matanzas (the rumba masters)", None),
            ("The rumba yard (conga, clave & the coro)", None),
            ("The quinto (the lead rumba drum)", None),
        ],
    ),
    (
        "THE AFRO-CUBAN SACRED: SANTERIA & THE BATA",
        "Beneath the popular music lies the sacred. SANTERIA (Regla de Ocha / Lucumi) -- the Yoruba "
        "religion carried by the enslaved and veiled in Catholic saints -- is served by the sacred BATA, "
        "a set of three double-headed hourglass drums, and by chants (orisha songs) to deities like Chango "
        "and Yemaya. Content note: a living religion, treated with respect.",
        [
            ("Bata drums (the sacred Afro-Cuban drums)", None),
            ("Santeria & the orisha songs (the Lucumi tradition)", None),
            ("Chants to Chango & Yemaya (the orisha praise-songs)", None),
            ("The Yoruba root in Cuba (the sacred inheritance)", None),
            ("Abakua & the Afro-Cuban brotherhoods", None),
        ],
    ),
    (
        "THE SALON: DANZON, CHARANGA & THE BOLERO",
        "The refined side of Cuban music gave the DANZON -- the elegant national dance played by the "
        "flute-and-strings CHARANGA -- and, from the trova tradition, the CUBAN BOLERO, a slow, romantic "
        "song of the guitar that spread across all of Latin America. 'Las Alturas de Simpson' launched the "
        "danzon in 1879.",
        [
            ("Las Alturas de Simpson (the first danzon)", "Miguel Failde"),
            ("Danzon (the elegant Cuban national dance)", None),
            ("The charanga (the flute-and-strings ensemble)", None),
            ("Cuban bolero (the romantic guitar song)", None),
            ("La trova (the Cuban song tradition)", None),
        ],
    ),
    (
        "THE MAMBO & THE CHA-CHA-CHA",
        "From the danzon and son came the mid-century dance crazes that swept the world: the MAMBO, its "
        "big-band fire crystallized by Perez Prado, and the CHA-CHA-CHA, invented by Enrique Jorrin for "
        "the charanga. Beny More, the 'Barbaro del Ritmo', reigned as the greatest Cuban voice of the "
        "age. The mambo conquered New York and the globe.",
        [
            ("Mambo No. 5", "Perez Prado"),
            ("La Enganadora (the first cha-cha-cha)", "Enrique Jorrin"),
            ("Que Rico El Mambo", "Perez Prado"),
            ("Bonito y Sabroso", "Beny More"),
            ("Beny More (the Barbaro del Ritmo)", None),
            ("The mambo & cha-cha-cha craze (the global dance)", None),
        ],
    ),
    (
        "AFRO-CUBAN JAZZ & THE CLAVE GOES NORTH",
        "Cuban rhythm remade American music. In 1940s New York, Machito and his Afro-Cubans, with Mario "
        "Bauza, fused the clave with jazz, and Dizzy Gillespie's collaboration with the conguero Chano "
        "Pozo ('Manteca') created Cubop -- Afro-Cuban jazz. This clave-and-jazz marriage would soon seed "
        "salsa. Cross-link: salsa's New York story in the Latin America survey.",
        [
            ("Manteca", "Chano Pozo"),
            ("Tanga", "Machito"),
            ("Afro-Cuban jazz / Cubop (the clave meets jazz)", None),
            ("Machito & Mario Bauza (the Afro-Cubans)", None),
            ("The conga & bongo in jazz (the Latin tinge)", None),
        ],
    ),
    (
        "THE AFRO-CUBAN FOUNDATION & THE ROAD AHEAD",
        "Cuba gave the Caribbean and the world its deepest dance foundation: clave, son, rumba, and the "
        "sacred bata, from which flowed mambo, cha-cha-cha, Latin jazz, and salsa. From this Afro-Cuban "
        "root the survey turns to the other great island engines -- Jamaica's reggae, Trinidad's calypso, "
        "and the modern Caribbean. Cross-links: salsa (Latin America); Africa; the wider isles (#2-4).",
        [
            ("The Afro-Cuban foundation (clave, son & rumba)", None),
            ("Cuba seeds the Latin dance world (the shared root)", None),
            ("From son to salsa (the cross-link ahead)", None),
            ("Toward Jamaica & the wider Caribbean (roads ahead)", None),
        ],
    ),
]

STEM = "carib_music_1_CUBAN_AFRO_ROOTS"


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
