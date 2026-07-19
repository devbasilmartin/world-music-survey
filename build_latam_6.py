#!/usr/bin/env python3
"""Build Latin America installment 6: Late-20th-Century Pop (c. 1975-1995).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file.
"""

TITLE = ("The Story of Latin American Music — Installment 6: "
         "Late-20th-Century Pop (c. 1975-1995)")

FRAMING = (
    "The boom becomes the mainstream. In these two decades the movements of Installment 5 harden into "
    "the region's mass-popular sound and split into the streams still dominant today. Fania SALSA turns "
    "conscious and literary in Ruben Blades and Willie Colon, then smooths into salsa romantica; MPB "
    "matures into a golden adult songbook while Brazil grows its own arena ROCK (BRock); Argentine ROCK "
    "NACIONAL survives the junta as coded resistance and, with Soda Stereo, ignites a continental ROCK "
    "EN ESPANOL; humble CUMBIA and chicha spread from Colombia and Peru into a pan-continental "
    "underground; the romantic BALADA and a RANCHERA revival rule radio and television; and Astor "
    "Piazzolla drags the tango into the concert hall as NUEVO TANGO. Cross-links to the US survey stay "
    "loud -- salsa and Latin pop are a New York industry too. Content notes are kept: this is the era "
    "of the Southern Cone dictatorships, and much of its rock is protest in disguise. Scope calls "
    "(Panama, the Dominican Republic, Puerto Rico) are flagged, not buried."
)

SECTIONS = [
    (
        "SALSA MATURES: DURA, CONSCIENTE & THE FANIA PEAK (c. 1975-1985)",
        "Salsa grew a conscience. Ruben Blades turned the dance floor into a newspaper of the barrio -- "
        "'Pedro Navaja' and the landmark album 'Siembra' with Willie Colon made salsa literary and "
        "political -- while Hector Lavoe became its tragic tenor and Oscar D'Leon carried the flame in "
        "Venezuela. (Scope call: Blades is Panamanian and Lavoe Puerto Rican, and Fania salsa is New "
        "York-made -- kept as the direct continuation of the Cuban/Latin dance lineage this survey has "
        "tracked since Installment 2, and shared with the US and open Caribbean surveys; flagged.)",
        [
            ("Pedro Navaja", "Ruben Blades"),
            ("Plastico", "Ruben Blades"),
            ("Pablo Pueblo", "Ruben Blades"),
            ("El Cantante", "Hector Lavoe"),
            ("Periodico de Ayer", "Hector Lavoe"),
            ("Lloraras", "Oscar D'Leon"),
            ("Brujeria", "El Gran Combo de Puerto Rico"),
            ("Juan Pachanga", "Fania All Stars"),
        ],
    ),
    (
        "SALSA ROMANTICA & THE MERENGUE CROSSOVER (c. 1985-1995)",
        "By the late 1980s salsa softened into the bedroom-balladry of SALSA ROMANTICA, and Dominican "
        "MERENGUE became the continent's fastest party music -- above all through Juan Luis Guerra, who "
        "married it to poetry and social comment. (Scope call: merengue and bachata are Dominican and "
        "salsa romantica largely Puerto Rican -- Caribbean forms kept here as pan-Latin popular music, "
        "with the open Caribbean-survey question flagged.)",
        [
            ("Ojala Que Llueva Cafe", "Juan Luis Guerra"),
            ("Burbujas de Amor", "Juan Luis Guerra"),
            ("Ven Devorame Otra Vez", "Lalo Rodriguez"),
            ("Tu Con El", "Frankie Ruiz"),
            ("El Africano", "Wilfrido Vargas"),
        ],
    ),
    (
        "BRAZIL: MPB'S GOLDEN MATURITY & THE CLUBE DA ESQUINA (c. 1974-1988)",
        "Post-Tropicalia, MPB became a sophisticated adult songbook. Elis Regina reigned as its supreme "
        "interpreter, Milton Nascimento's Minas circle (the Clube da Esquina) fused folk, jazz, and the "
        "Andes, and Djavan and Ivan Lins wrote harmonies that jazz musicians worldwide would borrow. "
        "This is Brazilian popular song at its most refined.",
        [
            ("Aguas de Marco", "Elis Regina"),
            ("O Bebado e a Equilibrista", "Elis Regina"),
            ("Cravo e Canela", "Milton Nascimento"),
            ("Nada Sera Como Antes", "Milton Nascimento"),
            ("Oceano", "Djavan"),
            ("Sina", "Djavan"),
            ("Comecar de Novo", "Ivan Lins"),
            ("Aquarela", "Toquinho"),
        ],
    ),
    (
        "BROCK: BRAZILIAN ROCK EXPLODES (c. 1982-1990)",
        "A new generation plugged in. 'BRock' turned 1980s Brazil into a rock nation: Legiao Urbana's "
        "anthemic angst, Os Paralamas' ska-pop, Titas' new wave, and the doomed poet Cazuza with Barao "
        "Vermelho gave post-dictatorship youth its voice. Content note: Cazuza became one of Brazil's "
        "first public faces of the AIDS crisis before his death in 1990.",
        [
            ("Tempo Perdido", "Legiao Urbana"),
            ("Faroeste Caboclo", "Legiao Urbana"),
            ("Alagados", "Os Paralamas do Sucesso"),
            ("Sonifera Ilha", "Titas"),
            ("Ideologia", "Cazuza"),
            ("Bete Balanco", "Barao Vermelho"),
            ("Ha Tempos", "Legiao Urbana"),
        ],
    ),
    (
        "ROCK NACIONAL: ARGENTINA UNDER & AFTER THE JUNTA (c. 1974-1985)",
        "Argentine ROCK NACIONAL matured into art under the shadow of the 1976-83 military dictatorship, "
        "where a song could be a coded act of resistance. Charly Garcia (Sui Generis, Seru Giran) and "
        "Luis Alberto Spinetta were its philosopher-kings, and Fito Paez its next-generation heir. "
        "Content note: 'Los Dinosaurios' and 'Cancion de Alicia en el Pais' are veiled elegies for the "
        "disappeared -- rock as memory under terror.",
        [
            ("Cancion para Mi Muerte", "Sui Generis"),
            ("Los Dinosaurios", "Charly Garcia"),
            ("Cancion de Alicia en el Pais", "Seru Giran"),
            ("Seminare", "Seru Giran"),
            ("Barro Tal Vez", "Luis Alberto Spinetta"),
            ("11 y 6", "Fito Paez"),
        ],
    ),
    (
        "ROCK EN ESPAÑOL GOES CONTINENTAL (c. 1984-1995)",
        "In 1984 Argentina's Soda Stereo detonated a truly pan-Hispanic rock movement, and within a "
        "decade ROCK EN ESPANOL had capitals in Santiago (Los Prisioneros), Buenos Aires (Los Fabulosos "
        "Cadillacs), Mexico City (Caifanes, Mana), and beyond. It was the first rock the whole "
        "Spanish-speaking continent shared as its own. Content note: Los Prisioneros' 'El Baile de los "
        "Que Sobran' was a class-anger anthem under Pinochet's Chile.",
        [
            ("De Musica Ligera", "Soda Stereo"),
            ("Persiana Americana", "Soda Stereo"),
            ("El Baile de los Que Sobran", "Los Prisioneros"),
            ("Matador", "Los Fabulosos Cadillacs"),
            ("La Negra Tomasa", "Caifanes"),
            ("Viento", "Caifanes"),
            ("Rayando el Sol", "Mana"),
            ("Oye Mi Amor", "Mana"),
        ],
    ),
    (
        "CUMBIA'S CONTINENTAL CONQUEST & THE TROPICAL UNDERGROUND (c. 1975-1995)",
        "The humblest form won the widest empire. Colombian CUMBIA and VALLENATO went pop with Carlos "
        "Vives; Peru's Amazon and mountains grew psychedelic CHICHA (Los Mirlos, Chacalon); Mexico's "
        "Rigo Tovar filled stadiums; and Bolivia's Los Kjarkas wrote 'Llorando Se Fue', later pirated "
        "into the global 'Lambada'. This working-class current would become the continent's dominant "
        "popular rhythm. Living folk-derived forms stay named where an author exists.",
        [
            ("La Gota Fria", "Carlos Vives"),
            ("Sin Medir Distancias", "Diomedes Diaz"),
            ("Sonido Amazonico", "Los Mirlos"),
            ("Soy Provinciano", "Chacalon y la Nueva Crema"),
            ("Matamoros Querido", "Rigo Tovar"),
            ("Llorando Se Fue", "Los Kjarkas"),
            ("Mi Cucu", "La Sonora Dinamita"),
        ],
    ),
    (
        "THE BALADA & THE RANCHERA REVIVAL (c. 1975-1995)",
        "Radio and the new Spanish-language television networks crowned the romantic BALADA. Jose Jose "
        "was its 'Principe', Juan Gabriel its most prolific genius, and Roberto Carlos its Brazilian "
        "king; meanwhile Vicente Fernandez led a proud RANCHERA revival that kept the mariachi tradition "
        "of Installment 4 alive and arena-sized. (Scope note: the Spanish-born ranchera star Rocio "
        "Durcal, a huge figure in this repertoire, is cut as European -- her Mexican collaborators "
        "carry the thread here.)",
        [
            ("El Triste", "Jose Jose"),
            ("Volcan", "Jose Jose"),
            ("Amor Eterno", "Juan Gabriel"),
            ("Querida", "Juan Gabriel"),
            ("Detalhes", "Roberto Carlos"),
            ("Volver, Volver", "Vicente Fernandez"),
            ("El Rey", "Vicente Fernandez"),
        ],
    ),
    (
        "ART MUSIC: PIAZZOLLA'S NUEVO TANGO & THE INSTRUMENTAL VANGUARD (c. 1974-1995)",
        "Astor Piazzolla dragged the tango out of the dance hall and into the concert hall, fusing it "
        "with jazz and Bach into NUEVO TANGO -- scandalous in Argentina, revered everywhere else. "
        "Alongside him Brazil's Egberto Gismonti built a singular instrumental language from Amazonian "
        "and classical sources. Name the work, not the performer.",
        [
            ("Adios Nonino", "Astor Piazzolla"),
            ("Libertango", "Astor Piazzolla"),
            ("Balada para un Loco", "Astor Piazzolla"),
            ("Maria de Buenos Aires: Yo Soy Maria", "Astor Piazzolla"),
            ("Agua e Vinho", "Egberto Gismonti"),
            ("Danca das Cabecas", "Egberto Gismonti"),
        ],
    ),
]

STEM = "latam_music_6_LATE20C_POP"


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
