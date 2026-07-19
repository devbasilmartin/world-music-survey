#!/usr/bin/env python3
"""Build Latin America installment 4: The Mid-Century Golden Age (c. 1940-1960).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file.
"""

TITLE = ("The Story of Latin American Music — Installment 4: "
         "The Mid-Century Golden Age (c. 1940-1960)")

FRAMING = (
    "This is the era of stars and studios. Radio, the jukebox, and above all the golden-age film "
    "industries of Mexico City, Havana, and Rio turn the forms of Installment 3 into a continent-wide "
    "star system. Cuba's son goes big-band and detonates the MAMBO and the CHA-CHA-CHA, sweeping New "
    "York and the world; the BOLERO refines into the guitar-trio romance of Los Panchos; Mexican "
    "RANCHERA becomes the soundtrack of a national cinema mythology sung by Negrete and Infante; "
    "Colombia's coastal CUMBIA is orchestrated and goes national; and in Rio, samba-cancao thins and "
    "cools until, in 1958-59, Joao Gilberto's whisper announces BOSSA NOVA -- the doorway to "
    "Installment 5. The nationalist ART-MUSIC composers keep working in parallel. Cross-links run hot "
    "to the US survey: mambo and cha-cha-cha are already half-American (Machito and Tito Puente work "
    "out of New York), and Latin jazz is being invented on the same bandstands. Scope calls are "
    "flagged, not buried."
)

SECTIONS = [
    (
        "THE MAMBO EXPLOSION & THE AFRO-CUBAN BIG BAND (c. 1940-1958)",
        "Arsenio Rodriguez's son montuno went big-band, and Damaso Perez Prado weaponized it into the "
        "MAMBO -- a global craze by 1950. Beny More, 'el Barbaro del Ritmo', was its greatest voice, "
        "while Machito and the descarga (jam) pioneers like Cachao were, in the same years, inventing "
        "Latin jazz. Cross-link: this bandstand is shared with the US survey -- Machito worked out of "
        "Harlem.",
        [
            ("Mambo No. 5", "Perez Prado"),
            ("Cerezo Rosa (Cherry Pink and Apple Blossom White)", "Perez Prado"),
            ("Que Rico el Mambo", "Perez Prado"),
            ("Como Fue", "Beny More"),
            ("Bonito y Sabroso", "Beny More"),
            ("Tanga", "Machito"),
            ("Dundunbanza", "Arsenio Rodriguez"),
            ("Descarga Cubana", "Israel Cachao Lopez"),
        ],
    ),
    (
        "THE BOLERO TRIO ERA: LOS PANCHOS & THE ROMANTIC VOICE (c. 1944-1960)",
        "The bolero found its classic form in the guitar trio -- three voices, requinto lead, and pure "
        "romance -- perfected by Trio Los Panchos and carried by a generation of great interpreters "
        "across every border. It was the continent's shared love-language on record. (Scope note: "
        "'Historia de un Amor' is Panamanian, by Carlos Eleta Almaran -- kept as pan-Latin repertoire.)",
        [
            ("Sin Ti", "Trio Los Panchos"),
            ("Rayito de Luna", "Trio Los Panchos"),
            ("Contigo en la Distancia", "Lucho Gatica"),
            ("La Barca", "Lucho Gatica"),
            ("Noche de Ronda", "Tona la Negra"),
            ("Sabor a Mi", "Los Tres Ases"),
            ("Historia de un Amor", "Carlos Eleta Almaran"),
        ],
    ),
    (
        "RANCHERA & THE GOLDEN AGE OF MEXICAN CINEMA (c. 1941-1960)",
        "The Epoca de Oro of Mexican film made the singing charro a national myth: Jorge Negrete and "
        "Pedro Infante were matinee idols whose rancheras defined mexicanidad, while Jose Alfredo "
        "Jimenez wrote the era's aching poetry from the cantina and Lola Beltran gave the genre its "
        "queen. Name the performer for these popular songs.",
        [
            ("Ay Jalisco No Te Rajes", "Jorge Negrete"),
            ("Mexico Lindo y Querido", "Jorge Negrete"),
            ("Amorcito Corazon", "Pedro Infante"),
            ("Cien Anos", "Pedro Infante"),
            ("Ella", "Jose Alfredo Jimenez"),
            ("La Que Se Fue", "Jose Alfredo Jimenez"),
            ("Cucurrucucu Paloma", "Lola Beltran"),
        ],
    ),
    (
        "BRAZIL: SAMBA-CANCAO, RADIO STARS & THE THRESHOLD OF BOSSA NOVA (c. 1940-1959)",
        "Postwar Rio cooled samba into the introspective SAMBA-CANCAO of the radio crooners, and a "
        "small circle of harmonically adventurous musicians -- Johnny Alf, Dick Farney -- pointed the "
        "way. In 1958-59 Joao Gilberto's understated guitar and voice, with Jobim's harmony, crystallized "
        "BOSSA NOVA. This section ends exactly on that threshold; the movement itself opens Installment 5.",
        [
            ("Chega de Saudade (1959)", "Joao Gilberto"),
            ("Desafinado", "Joao Gilberto"),
            ("Cancao do Amor Demais", "Elizeth Cardoso"),
            ("Copacabana", "Dick Farney"),
            ("Rapaz de Bem", "Johnny Alf"),
            ("Marina", "Dorival Caymmi"),
            ("Ave Maria no Morro", "Herivelto Martins"),
        ],
    ),
    (
        "THE ANDES, THE CRIOLLO REVIVAL & THE ROOTS OF NUEVA CANCION (c. 1945-1960)",
        "Away from the film capitals, a rooted song movement matured: Atahualpa Yupanqui gave Argentine "
        "folklore a poet and a conscience that would seed nueva cancion; Chabuca Granda elevated the "
        "Peruvian vals criollo; Yma Sumac took Andean melody to Hollywood exotica; and Nicomedes Santa "
        "Cruz launched the Afro-Peruvian revival. Living folk stays '(Traditional)'.",
        [
            ("Luna Tucumana", "Atahualpa Yupanqui"),
            ("Los Ejes de Mi Carreta", "Atahualpa Yupanqui"),
            ("La Flor de la Canela", "Chabuca Granda"),
            ("Fina Estampa", "Chabuca Granda"),
            ("Gopher (Taita Inty)", "Yma Sumac"),
            ("Ritmos Negros del Peru", "Nicomedes Santa Cruz"),
        ],
    ),
    (
        "COLOMBIA & THE TROPICAL EXPLOSION: CUMBIA AND VALLENATO GO NATIONAL (c. 1946-1960)",
        "The coastal seeds of Installment 3 burst into the national mainstream: Lucho Bermudez and "
        "Pacho Galan orchestrated cumbia and porro into sophisticated big-band 'musica tropical' that "
        "conquered the whole country and much of the continent, while Rafael Escalona gave the "
        "accordion VALLENATO its songbook. This is the launch pad for cumbia's later conquest of all "
        "Latin America.",
        [
            ("Colombia Tierra Querida", "Lucho Bermudez"),
            ("Salsipuedes", "Lucho Bermudez"),
            ("Ay Cosita Linda", "Pacho Galan"),
            ("La Pollera Colora", "Wilson Choperena"),
            ("La Casa en el Aire", "Rafael Escalona"),
            ("La Mucura (Colombian coastal)", None),
            ("Micaela (porro)", None),
        ],
    ),
    (
        "THE CONCERT HALL CONTINUES: MID-CENTURY ART MUSIC (c. 1940-1960)",
        "The nationalist project deepened: Villa-Lobos painted a train crossing the Brazilian "
        "backlands, Ginastera distilled the pampa, Guastavino wrote art songs of aching lyricism, and "
        "Mexico's Ponce gave the guitar a landmark concerto. Latin American art music was now fully "
        "itself. Name the work.",
        [
            ("O Trenzinho do Caipira (Bachianas Brasileiras No. 2)", "Heitor Villa-Lobos"),
            ("Danzas Argentinas", "Alberto Ginastera"),
            ("Se Equivoco la Paloma", "Carlos Guastavino"),
            ("La Rosa y el Sauce", "Carlos Guastavino"),
            ("Concierto del Sur", "Manuel M. Ponce"),
            ("Estudios Sencillos", "Leo Brouwer"),
        ],
    ),
    (
        "CHA-CHA-CHA & THE DANCE-FLOOR CROSSOVER (c. 1951-1960)",
        "Enrique Jorrin slowed the mambo into the easy-to-dance CHA-CHA-CHA, and the charangas -- "
        "Orquesta Aragon above all -- made it a worldwide ballroom staple. In New York the same "
        "Cuban DNA powered the Palladium. (Scope note: Tito Puente was Nuyorican, New York-born to "
        "Puerto Rican parents -- kept here as central to the Cuban-derived mambo/Latin-jazz axis he "
        "shares with the US survey.)",
        [
            ("La Enganadora (first cha-cha-cha, 1953)", "Enrique Jorrin"),
            ("El Bodeguero", "Orquesta Aragon"),
            ("Rico Vacilon", "Orquesta Aragon"),
            ("Guantanamera", "Joseito Fernandez"),
            ("Ran Kan Kan", "Tito Puente"),
        ],
    ),
]

STEM = "latam_music_4_MIDCENTURY_GOLDEN_AGE"


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
