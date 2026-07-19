#!/usr/bin/env python3
"""Build Latin America installment 3: The Recording Era & the Golden Age (c. 1900-1940).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file.
"""

TITLE = ("The Story of Latin American Music — Installment 3: "
         "The Recording Era & the Golden Age (c. 1900-1940)")

FRAMING = (
    "The needle drops. Between roughly 1900 and 1940, the phonograph, radio, and the film musical "
    "turn the regional forms of Installment 2 into national -- and then international -- popular "
    "music. The loaded spring releases: the Rio de la Plata's proto-tango becomes the TANGO-CANCION "
    "and a global craze the moment Carlos Gardel opens his mouth; Rio's maxixe and lundu crystallize "
    "into SAMBA with the first recorded side in 1917; Cuba's son sweeps out of Oriente to conquer "
    "Havana and then the world as 'rumba'; Mexico's canción hardens into RANCHERA while Agustin Lara "
    "makes the BOLERO the continent's shared love-language. In parallel, a generation of nationalist "
    "ART-MUSIC composers -- Villa-Lobos, Chavez, Revueltas, Ginastera -- carry the folk material into "
    "the concert hall. Cross-links run everywhere now: Cuban son and the 1930 'Peanut Vendor' feed the "
    "US 'rumba craze' and the mambo to come; the bolero threads through every Spanish-speaking country; "
    "Villa-Lobos answers Bach across the Atlantic. Scope note: Puerto Rican figures (Rafael Hernandez) "
    "appear here because the bolero/cancion story is pan-Latin and inseparable from the mainland -- the "
    "Caribbean-as-its-own-survey question is still open in the roadmap, and is flagged, not buried."
)

SECTIONS = [
    (
        "THE TANGO GOLDEN AGE: BUENOS AIRES & CARLOS GARDEL (c. 1917-1940)",
        "Recording made the tango a singer's art. In 1917 Carlos Gardel cut 'Mi Noche Triste' and "
        "invented the tango-cancion; by the 1930s he was the most famous voice in the Spanish-"
        "speaking world, and Buenos Aires and Montevideo orchestras had refined the genre into a "
        "sophisticated concert music. This is the hinge from the arrabal tangos of Installment 2 to "
        "a global phenomenon.",
        [
            ("Mi Noche Triste (first tango-cancion, 1917)", "Carlos Gardel"),
            ("Mi Buenos Aires Querido", "Carlos Gardel"),
            ("El Dia Que Me Quieras", "Carlos Gardel"),
            ("Volver", "Carlos Gardel"),
            ("Por una Cabeza", "Carlos Gardel"),
            ("La Cumparsita", "Gerardo Matos Rodriguez"),
            ("Caminito", "Juan de Dios Filiberto"),
            ("Tiempos Viejos", "Francisco Canaro"),
        ],
    ),
    (
        "BRAZIL: THE BIRTH OF SAMBA & THE CHORO MASTERS (c. 1917-1940)",
        "In 1917 'Pelo Telefone' became the first recorded samba, and within two decades samba was "
        "Brazil's national sound, codified in the Rio hills and broadcast nationwide. Alongside it, "
        "choro reached its peak in Pixinguinha, and the radio-era songbook of Noel Rosa, Ary "
        "Barroso, and Dorival Caymmi was born. (Scope note: Carmen Miranda was Portuguese-born but "
        "wholly a creation of Rio's samba scene -- kept as Brazilian.)",
        [
            ("Pelo Telefone (first recorded samba, 1917)", "Donga"),
            ("Carinhoso", "Pixinguinha"),
            ("Aquarela do Brasil (1939)", "Ary Barroso"),
            ("Com Que Roupa?", "Noel Rosa"),
            ("O Que E Que a Baiana Tem?", "Dorival Caymmi"),
            ("Tai (Pra Voce Gostar de Mim)", "Carmen Miranda"),
            ("Cidade Maravilhosa", "Andre Filho"),
        ],
    ),
    (
        "CUBA: SON CUBANO CONQUERS THE WORLD (c. 1920-1940)",
        "The son travelled from the mountains of Oriente to Havana and, via record and radio, to the "
        "world. The septetos codified it; Ignacio Pineiro and the Trio Matamoros made it art; and in "
        "1930 'El Manisero' set off an international 'rumba craze' that seeded the American mambo and "
        "salsa to come. Arsenio Rodriguez was already pushing son toward the montuno that would power "
        "everything after.",
        [
            ("Son de la Loma", "Trio Matamoros"),
            ("Lagrimas Negras", "Trio Matamoros"),
            ("Echale Salsita", "Septeto Nacional (Ignacio Pineiro)"),
            ("El Manisero (The Peanut Vendor, 1930)", "Moises Simons"),
            ("Veinte Anos", "Maria Teresa Vera"),
            ("Aquellos Ojos Verdes", "Nilo Menendez"),
            ("Bruca Manigua", "Arsenio Rodriguez"),
        ],
    ),
    (
        "MEXICO: REVOLUTION CORRIDOS, RANCHERA & AGUSTIN LARA (c. 1910-1940)",
        "The Revolution (1910-1920) generated a flood of narrative CORRIDOS that are the era's living "
        "newspaper. Out of the cantina came the canción RANCHERA, and in the salons and on the radio "
        "Agustin Lara reinvented the bolero as sophisticated, cosmopolitan song. Corridos stay "
        "'(Traditional)'; the composed songs name their author.",
        [
            ("La Cucaracha (Revolution corrido)", None),
            ("La Adelita (Revolution corrido)", None),
            ("La Valentina", None),
            ("Alla en el Rancho Grande", "Silvano R. Ramos"),
            ("Granada", "Agustin Lara"),
            ("Solamente Una Vez", "Agustin Lara"),
            ("Maria Bonita", "Agustin Lara"),
            ("Nunca (Yucatecan trova)", "Guty Cardenas"),
        ],
    ),
    (
        "THE BOLERO & THE PAN-LATIN SONGBOOK SPREAD (c. 1925-1940)",
        "The bolero became the shared romantic idiom of every Spanish-speaking country, carried on "
        "record and radio across borders. Puerto Rico's Rafael Hernandez wrote anthems of longing and "
        "island pride that belong to the whole continent, and Mexican composers gave the world "
        "standards that jazz and Hollywood would adopt wholesale.",
        [
            ("Lamento Borincano (1930)", "Rafael Hernandez"),
            ("El Cumbanchero", "Rafael Hernandez"),
            ("Preciosa", "Rafael Hernandez"),
            ("Perfidia", "Alberto Dominguez"),
            ("Frenesi", "Alberto Dominguez"),
            ("Besame Mucho (1940)", "Consuelo Velazquez"),
        ],
    ),
    (
        "THE ANDES & THE CRIOLLO SONG ON RECORD (c. 1910-1940)",
        "Recording reached the Andean republics too, capturing the mestizo vals criollo and the "
        "highland huayno as composed, authored songs for the first time. Felipe Pinglo Alva gave the "
        "Peruvian vals its poet; Daniel Alomia Robles set Andean melody into concert form. Living "
        "folk forms stay '(Traditional)'.",
        [
            ("El Plebeyo (1930)", "Felipe Pinglo Alva"),
            ("Virgenes del Sol", "Daniel Alomia Robles"),
            ("Valicha (Cuzco huayno)", None),
            ("La Lopez Pereyra (Argentine zamba)", None),
            ("El Humahuaqueno / El Carnavalito", None),
        ],
    ),
    (
        "THE CONCERT HALL: NATIONALIST ART MUSIC (c. 1915-1945)",
        "A generation of composers did for Latin America what Bartok and Dvorak did for Europe: they "
        "carried folk and Afro-Indigenous material into symphonic and chamber form, creating a "
        "self-consciously American art music. Villa-Lobos answered Bach through a Brazilian lens; "
        "Chavez and Revueltas mined Mexico's Indigenous and mestizo roots; Ginastera did the same for "
        "the Argentine pampa. Name the work.",
        [
            ("Bachianas Brasileiras No. 5: Aria (Cantilena)", "Heitor Villa-Lobos"),
            ("Choros No. 10", "Heitor Villa-Lobos"),
            ("Sinfonia India (Symphony No. 2)", "Carlos Chavez"),
            ("Sensemaya", "Silvestre Revueltas"),
            ("La Noche de los Mayas", "Silvestre Revueltas"),
            ("Estancia: Malambo", "Alberto Ginastera"),
            ("La Rebambaramba", "Amadeo Roldan"),
        ],
    ),
    (
        "THE CARIBBEAN COAST: THE SEEDS OF CUMBIA & VALLENATO (Colombia/Venezuela, c. 1920-1940)",
        "On Colombia's Caribbean coast, the accordion-and-drum forms that become CUMBIA and VALLENATO "
        "began reaching wax, and Venezuela's plains and Maracaibo traditions followed. This current is "
        "only just being recorded here; it explodes into a continental force in the next installment "
        "-- watch this space.",
        [
            ("Cumbia (Colombian Caribbean coast)", None),
            ("Porro (Colombian coastal big-band)", None),
            ("Gaita Zuliana (Venezuelan, Maracaibo)", None),
            ("Se Va el Caiman", "Jose Maria Penaranda"),
            ("Grito Vagabundo (early vallenato)", "Guillermo Buitrago"),
        ],
    ),
]

STEM = "latam_music_3_RECORDING_GOLDEN_AGE"


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
