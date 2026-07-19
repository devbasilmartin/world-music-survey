#!/usr/bin/env python3
"""Build Latin America installment 5: The Boom (c. 1960-1975).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file.
"""

TITLE = ("The Story of Latin American Music — Installment 5: "
         "The Boom (c. 1960-1975)")

FRAMING = (
    "This is the explosion. In fifteen years Latin American music stops following the world and starts "
    "leading it. Installment 4 ended on Joao Gilberto's whisper; here BOSSA NOVA conquers the planet, "
    "then turns inward into MPB and detonates into the art-rock riot of TROPICALIA. In the Southern "
    "Cone and the Andes, Violeta Parra's rediscovered folk becomes NUEVA CANCION -- song as conscience "
    "and, soon, as resistance under the dictatorships closing in. In revolutionary Cuba the same impulse "
    "becomes the NUEVA TROVA of Silvio Rodriguez and Pablo Milanes. And in the barrios of New York, "
    "Cuban son plus Puerto Rican energy plus the Fania machine is renamed SALSA and becomes the sound of "
    "Latin New York -- the loudest cross-link yet to the US survey. Behind it all the avant-garde art "
    "composers push into the international vanguard. This is the era when 'protest', 'pop', and 'art' "
    "stop being separable. Content note: several artists in this chapter were exiled, jailed, or "
    "murdered by the military regimes of the 1970s -- that history is kept, not sanded off. Scope calls "
    "are flagged, not buried."
)

SECTIONS = [
    (
        "BOSSA NOVA CONQUERS THE WORLD (c. 1960-1967)",
        "Joao Gilberto's threshold sound of 1959 became, within five years, a global language. Antonio "
        "Carlos Jobim's harmonies and Vinicius de Moraes's poetry, carried by the 1964 'Getz/Gilberto' "
        "sessions, put Portuguese on jukeboxes worldwide; 'Garota de Ipanema' became the second most "
        "recorded pop song on Earth. Baden Powell and Vinicius mined the Afro-Bahian side in the "
        "'Afro-Sambas'. (Prior installment 4 already listed 'Chega de Saudade' and 'Desafinado'; this "
        "picks up after.)",
        [
            ("Garota de Ipanema (The Girl from Ipanema)", "Joao Gilberto"),
            ("Corcovado", "Antonio Carlos Jobim"),
            ("Insensatez (How Insensitive)", "Antonio Carlos Jobim"),
            ("Wave", "Antonio Carlos Jobim"),
            ("Samba de Uma Nota So (One Note Samba)", "Joao Gilberto"),
            ("Berimbau", "Baden Powell"),
            ("Canto de Ossanha", "Baden Powell"),
            ("Arrastao", "Elis Regina"),
        ],
    ),
    (
        "MPB & THE FESTIVAL ERA: SONG AS THE NATIONAL DEBATE (c. 1965-1972)",
        "The televised song festivals turned MUSICA POPULAR BRASILEIRA into a national arena where a "
        "generation argued about Brazil in three-minute songs -- often in coded protest against the "
        "1964-85 military dictatorship. Chico Buarque, Geraldo Vandre, Edu Lobo, and the Minas circle "
        "around Milton Nascimento made MPB the country's literary conscience. Content note: Vandre's "
        "'Caminhando' became a banned protest anthem and forced him into exile.",
        [
            ("Disparada", "Geraldo Vandre"),
            ("Pra Nao Dizer Que Nao Falei das Flores (Caminhando)", "Geraldo Vandre"),
            ("Roda Viva", "Chico Buarque"),
            ("A Banda", "Chico Buarque"),
            ("Construcao", "Chico Buarque"),
            ("Ponteio", "Edu Lobo"),
            ("Travessia", "Milton Nascimento"),
            ("Cancao do Sal", "Milton Nascimento"),
        ],
    ),
    (
        "TROPICALIA: THE ART-ROCK RIOT (c. 1967-1972)",
        "In 1967-68 Caetano Veloso and Gilberto Gil detonated TROPICALIA -- bossa and MPB smashed "
        "together with electric rock, avant-garde poetry, and pop-art irreverence, 'cannibalizing' "
        "global culture in the spirit of Oswald de Andrade. Os Mutantes supplied the fuzz, Gal Costa "
        "and Tom Ze the edges. Content note: the regime jailed Caetano and Gil in 1968 and forced them "
        "into London exile -- the movement was crushed at its peak but rewired Brazilian music forever.",
        [
            ("Alegria, Alegria", "Caetano Veloso"),
            ("Tropicalia", "Caetano Veloso"),
            ("Domingo no Parque", "Gilberto Gil"),
            ("Aquele Abraco", "Gilberto Gil"),
            ("Panis et Circenses", "Os Mutantes"),
            ("Baby", "Gal Costa"),
            ("Parque Industrial", "Tom Ze"),
        ],
    ),
    (
        "NUEVA CANCION: VIOLETA, VICTOR & THE SONG OF THE PEOPLE (Chile/Argentina, c. 1960-1973)",
        "Violeta Parra's decade of collecting Chilean folk flowered into original song that launched "
        "NUEVA CANCION -- rooted, political, continent-spanning. Victor Jara, Quilapayun, and "
        "Inti-Illimani made it the soundtrack of Allende's Chile, while Mercedes Sosa gave the "
        "movement its towering voice across the Andes. Content note: Victor Jara was tortured and "
        "murdered in the September 1973 coup; Sosa and Inti-Illimani were driven into exile. 'El "
        "Pueblo Unido' became the global anthem of the resistance that followed.",
        [
            ("Gracias a la Vida", "Violeta Parra"),
            ("Volver a los 17", "Violeta Parra"),
            ("Te Recuerdo Amanda", "Victor Jara"),
            ("El Derecho de Vivir en Paz", "Victor Jara"),
            ("Plegaria a un Labrador", "Victor Jara"),
            ("El Pueblo Unido Jamas Sera Vencido", "Quilapayun"),
            ("Venceremos", "Inti-Illimani"),
            ("Cancion con Todos", "Mercedes Sosa"),
            ("Alfonsina y el Mar", "Mercedes Sosa"),
        ],
    ),
    (
        "NUEVA TROVA & THE MEXICAN SONG MOVEMENT (c. 1967-1975)",
        "Revolutionary Cuba grew its own committed song: the NUEVA TROVA of Silvio Rodriguez and Pablo "
        "Milanes, poetic and guitar-borne, threading the same needle as nueva cancion from inside the "
        "Revolution. In Mexico a parallel canto nuevo -- Oscar Chavez, Amparo Ochoa, and the "
        "collective Los Folkloristas -- recovered folk and Indigenous memory as protest. Cross-link: "
        "this whole continental network shared songs, tours, and a politics.",
        [
            ("Ojala", "Silvio Rodriguez"),
            ("Playa Giron", "Silvio Rodriguez"),
            ("Yolanda", "Pablo Milanes"),
            ("Yo Pisare las Calles Nuevamente", "Pablo Milanes"),
            ("La Maldicion de Malinche", "Amparo Ochoa"),
            ("Por Ti", "Oscar Chavez"),
            ("La Iguana (son, Los Folkloristas)", "Los Folkloristas"),
        ],
    ),
    (
        "THE BIRTH OF SALSA: FANIA & LATIN NEW YORK (c. 1962-1975)",
        "Cuban son, guaguanco, and the mambo/cha-cha-cha machine of Installment 4 -- cut off from the "
        "island by the embargo -- were reforged in the New York barrio by mostly Puerto Rican "
        "musicians, passed through the boogaloo craze, and rebranded by the Fania label as SALSA. "
        "Eddie Palmieri, Willie Colon and Hector Lavoe, Ray Barretto, and Celia Cruz made it the "
        "voice of a diaspora. (Scope call: this music is New York-made and pan-Caribbean -- it also "
        "lives in the US survey and the still-open Caribbean survey; kept here as the direct continuation "
        "of the Cuban/Latin dance lineage this survey has tracked since Installment 2, and flagged.)",
        [
            ("Azucar Pa' Ti", "Eddie Palmieri"),
            ("Bang Bang", "Joe Cuba"),
            ("Che Che Cole", "Willie Colon"),
            ("Mi Gente", "Hector Lavoe"),
            ("Indestructible", "Ray Barretto"),
            ("Anacaona", "Cheo Feliciano"),
            ("Quimbara", "Celia Cruz"),
            ("Abran Paso", "Ismael Rivera"),
        ],
    ),
    (
        "THE ANDEAN & FOLK-ROOTS CURRENT DEEPENS (c. 1960-1975)",
        "Underneath the movements, the traditional roots kept feeding the boom. The Andean pan-flute "
        "ensembles and Argentine folk had a revival; Simon Diaz codified Venezuela's tonada llanera; "
        "and in Peru the Afro-Peruvian renaissance that Nicomedes Santa Cruz began now surfaced fully "
        "on record in the young Susana Baca's tradition and the group Peru Negro. Living tradition "
        "stays '(Traditional)'.",
        [
            ("Caballo Viejo", "Simon Diaz"),
            ("Tonada de Luna Llena", "Simon Diaz"),
            ("Zamba de Mi Esperanza", "Jorge Cafrune"),
            ("Virgen India", "Jorge Cafrune"),
            ("Toro Mata (Afro-Peruvian revival)", "Peru Negro"),
            ("Carnavalito / Sikuris (Andean ensemble revival)", None),
        ],
    ),
    (
        "THE VANGUARD: ART MUSIC GOES INTERNATIONAL (c. 1960-1975)",
        "Latin American art music now sat at the world's cutting edge. Alberto Ginastera's expressionist "
        "operas scandalized and dazzled; Leo Brouwer pushed the guitar into the avant-garde; the "
        "Argentine Mauricio Kagel became a leader of European experimental theatre-music; and "
        "Villa-Lobos's final grand canvas closed the nationalist age. Name the work, not the performer.",
        [
            ("Bomarzo (opera): excerpts", "Alberto Ginastera"),
            ("Piano Concerto No. 1", "Alberto Ginastera"),
            ("La Espiral Eterna", "Leo Brouwer"),
            ("A Floresta do Amazonas", "Heitor Villa-Lobos"),
            ("Sonata for Guitar", "Alberto Ginastera"),
        ],
    ),
]

STEM = "latam_music_5_THE_BOOM"


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
