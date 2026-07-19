#!/usr/bin/env python3
"""Build Latin America installment 2: Independence & the Criollo Century (c. 1800-1900).

Holds the data as (section_title, intro, [(title, artist_or_None), ...]) and emits both
latam_music_2_INDEPENDENCE_CRIOLLO.md (narrative) and ..._IMPORT.txt (clean Title - Artist).
Artist=None => traditional / no definitive recording => bare title in the import file.
"""

TITLE = "The Story of Latin American Music — Installment 2: Independence & the Criollo Century (c. 1800-1900)"

FRAMING = (
    "The three-way braid set in Installment 1 -- Indigenous + Iberian + African -- now becomes "
    "something new: as the colonies tear free of Spain and Portugal (roughly 1810-1825), the music "
    "stops being colonial and starts being *national*. Watch three things happen at once. (1) Each "
    "new republic writes itself an ANTHEM and grows a CREOLE SALON art music -- pianists and opera "
    "composers who are American-born and proud of it. (2) The Afro-Iberian dance forms crystallize "
    "into named genres -- Cuba's contradanza hardens into the first danzon, the Rio de la Plata's "
    "milonga edges toward TANGO, Brazil's lundu and polka fuse into CHORO, Mexico's salon waltz and "
    "cancion seed MARIACHI. (3) The folk republics -- Andean, Colombian, Venezuelan, Southern Cone "
    "-- mature their string-band forms. This is still largely pre-recording, so named composers and "
    "works anchor the art music while living-tradition folk stays '(Traditional)'. Everything here "
    "is the loaded spring; Installment 3 is the recording era it explodes into. Cross-links run "
    "hot to the US survey (the habanera bass under ragtime and 'the Spanish tinge' in jazz) and "
    "back to Europe (the habanera that becomes Bizet's 'Carmen')."
)

SECTIONS = [
    (
        "SONGS OF INDEPENDENCE: THE NEW NATIONS FIND A VOICE (c. 1810-1870)",
        "The wars of independence produced the region's first mass-shared music: battle hymns and "
        "national anthems, sung to weld strangers into citizens. Musically they are European in "
        "idiom -- Italianate marches and hymns -- but they are the first music consciously made to "
        "be *ours*. A note on scope: several anthem composers were Iberian-born but did the work in "
        "the Americas for the new nations (Blas Parera, a Catalan, wrote Argentina's in Buenos "
        "Aires); they are kept as national works, the nation's own.",
        [
            ("Himno Nacional Argentino (1813)", "Blas Parera"),
            ("Hino Nacional Brasileiro", "Francisco Manuel da Silva"),
            ("Himno Nacional del Peru (1821)", "Jose Bernardo Alcedo"),
            ("Gloria al Bravo Pueblo (Venezuelan anthem)", "Juan Jose Landaeta"),
            ("La Bayamesa / Himno de Bayamo (Cuban anthem, 1868)", "Perucho Figueredo"),
            ("Himno Nacional Mexicano (1854)", "Jaime Nuno"),
        ],
    ),
    (
        "THE CREOLE SALON: A NEW WORLD ART MUSIC COMES OF AGE (c. 1850-1900)",
        "With cathedrals no longer the only patron, art music moved into the bourgeois parlor and "
        "the opera house. American-born composers wrote piano danzas, salon waltzes, and full "
        "operas that were technically the equal of Europe's but rhythmically creole. (Scope call: "
        "Louis Moreau Gottschalk, the New Orleans pianist who toured and died in Latin America and "
        "wrote Latin-themed works, is CUT here -- he belongs to the US survey; his influence is "
        "noted instead.) Name the work, not the performer.",
        [
            ("Il Guarany: Overture", "Antonio Carlos Gomes"),
            ("Lo Schiavo: Alvorada", "Antonio Carlos Gomes"),
            ("Danzas Cubanas: Los Tres Golpes", "Ignacio Cervantes"),
            ("Danzas Cubanas: Adios a Cuba", "Ignacio Cervantes"),
            ("Contradanza: La Tedezco", "Manuel Saumell"),
            ("Mi Teresita (vals)", "Teresa Carreno"),
            ("El Rancho Abandonado", "Alberto Williams"),
        ],
    ),
    (
        "CUBA: CONTRADANZA -> HABANERA -> THE FIRST DANZON (c. 1800-1900)",
        "No island did more to shape global popular rhythm. The European contradanza, reworked over "
        "an African-derived bass, became the CONTRADANZA CUBANA, then the HABANERA (its 'tango' "
        "bass-figure travels the world), and in 1879 Miguel Failde codified the DANZON, Cuba's "
        "first true national dance. Cross-link: the habanera bass is 'the Spanish tinge' Jelly Roll "
        "Morton called essential to jazz, and it is the tune Bizet lifted for 'Carmen'.",
        [
            ("Las Alturas de Simpson (first danzon, 1879)", "Miguel Failde"),
            ("Tu (habanera)", "Eduardo Sanchez de Fuentes"),
            ("La Paloma (habanera)", "Sebastian Iradier"),
            ("Contradanza: La Suavecita", "Manuel Saumell"),
            ("Danza: Amelia", "Ignacio Cervantes"),
            ("Guajira (Cuban peasant song form)", None),
            ("Punto Guajiro (Cuban campesino tradition)", None),
        ],
    ),
    (
        "THE RIO DE LA PLATA: PAYADA, MILONGA & THE BIRTH OF TANGO (c. 1860-1900)",
        "On the docks of Buenos Aires and Montevideo, the gaucho's improvised PAYADA and the fast "
        "MILONGA met the habanera, the Andalusian tango, and Afro-Rioplatense candombe in the "
        "immigrant tenements -- and TANGO was born, first as danced music of the arrabal before it "
        "was ever sung or recorded. These are the primordial tangos, right at the 1900 threshold.",
        [
            ("Milonga (Rioplatense song-form)", None),
            ("Payada / Cifra (gaucho improvised song)", None),
            ("El Entrerriano (early tango, 1897)", "Rosendo Mendizabal"),
            ("Don Juan (tango, 1898)", "Ernesto Ponzio"),
            ("El Choclo (tango, 1903)", "Angel Villoldo"),
            ("La Morocha (tango-cancion, 1905)", "Enrique Saborido"),
        ],
    ),
    (
        "BRAZIL: MODINHA, LUNDU & THE BIRTH OF CHORO (c. 1800-1900)",
        "Brazil's parlor sentimental song (MODINHA) and its Afro-Brazilian syncopated dance (LUNDU) "
        "fused with European polka and schottische in Rio to produce CHORO -- the country's first "
        "urban instrumental popular music, and the seedbed of everything from samba to bossa nova. "
        "Chiquinha Gonzaga, a boundary-breaking woman composer, and Ernesto Nazareth are its "
        "founding voices.",
        [
            ("Modinha (Luso-Brazilian parlor song)", None),
            ("Lundu (Afro-Brazilian song-dance)", None),
            ("Atraente (choro-polka, 1877)", "Chiquinha Gonzaga"),
            ("O Abre Alas (carnival marcha, 1899)", "Chiquinha Gonzaga"),
            ("Flor Amorosa", "Joaquim Callado"),
            ("Brejeiro (tango brasileiro / maxixe, 1893)", "Ernesto Nazareth"),
            ("Odeon (choro)", "Ernesto Nazareth"),
        ],
    ),
    (
        "MEXICO: THE VALS, THE CANCION & THE SEEDS OF MARIACHI (c. 1860-1900)",
        "Porfirian Mexico loved the European waltz -- and promptly made it its own, producing the "
        "most globally famous Latin waltz of the century. Alongside it the romantic CANCION "
        "MEXICANA matured and the string-band SON of Jalisco (guitars, vihuela, violins) hardened "
        "into what would become mariachi. Name the work where a composer is known; the sones stay "
        "traditional.",
        [
            ("Sobre las Olas (Over the Waves, vals, 1888)", "Juventino Rosas"),
            ("Cielito Lindo (1882)", "Quirino Mendoza y Cortes"),
            ("Dios Nunca Muere (vals)", "Macedonio Alcala"),
            ("La Golondrina", "Narciso Serradell"),
            ("Marcha Zacatecas (1891)", "Genaro Codina"),
            ("La Bamba (son jarocho, traditional roots)", None),
            ("Son de Jalisco (early mariachi string-band)", None),
        ],
    ),
    (
        "THE CRIOLLO FOLK REPUBLICS MATURE (19th century, traditional)",
        "Away from the capitals, the mestizo string-band forms of Installment 1 ripened into the "
        "national folk dances still danced today -- the Andean and Southern Cone waltz-and-dance "
        "families, the Colombian/Andean-highland songs, and the Venezuelan plains music. Pre-"
        "recording living tradition; search a version you like.",
        [
            ("Vals Criollo (Peruvian creole waltz)", None),
            ("Yaravi (Andean mestizo lament)", None),
            ("Huayno (Andean highland song-dance)", None),
            ("Zamba (Argentine folk song-dance)", None),
            ("Chacarera (Argentine folk dance)", None),
            ("Pasillo (Colombian / Ecuadorian)", None),
            ("Bambuco: Cuatro Preguntas (Colombian)", None),
            ("Joropo: Seis por Derecho (Venezuelan/Colombian plains)", None),
        ],
    ),
    (
        "THE AFRO-DESCENDANT CURRENT DEEPENS (19th century, traditional)",
        "Under and inside every genre above, Afro-descendant communities kept elaborating the "
        "rhythmic engine -- and in the 1800s it surfaced as named urban forms: the Afro-Brazilian "
        "MAXIXE, the Afro-Cuban RUMBA taking shape in Havana and Matanzas solares, and the Afro-"
        "Peruvian and Afro-Venezuelan traditions that a 20th-century revival would later carry "
        "worldwide. This current is the direct rhythmic ancestor of samba, salsa, and beyond.",
        [
            ("Maxixe (Afro-Brazilian urban dance)", None),
            ("Rumba: Yambu (Afro-Cuban, Havana/Matanzas)", None),
            ("Rumba: Guaguanco (Afro-Cuban)", None),
            ("Festejo (Afro-Peruvian)", None),
            ("Lando (Afro-Peruvian)", None),
            ("Tambor / Sangueo (Afro-Venezuelan)", None),
            ("Garifuna Punta (Afro-Caribbean, Central America)", None),
        ],
    ),
]

STEM = "latam_music_2_INDEPENDENCE_CRIOLLO"


def build():
    md = [f"# {TITLE}", "", FRAMING, ""]
    imp = []
    for sec_title, intro, tracks in SECTIONS:
        md.append(f"## {sec_title}")
        md.append("")
        md.append(intro)
        md.append("")
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
