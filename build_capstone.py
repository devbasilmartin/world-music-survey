#!/usr/bin/env python3
"""Build the World Music Survey CAPSTONE: Global Fusion & the Connected World.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of World Music — Capstone (Grand Finale): "
         "Global Fusion & the Connected World")

FRAMING = (
    "This capstone closes the entire World Music Survey. Where every regional survey followed one people, "
    "place, or tradition, this final set follows the CONNECTIONS -- the great cross-cultural fusions, "
    "landmark collaborations, and world-music milestones that stitched the whole planet's music into one "
    "conversation. It is the story of the late-20th and 21st centuries, when 'WORLD MUSIC' became a "
    "category, WOMAD and Real World built stages for it, and musicians from every tradition met and made "
    "something new: Paul Simon in Soweto, Ry Cooder in Bamako and Havana, Yo-Yo Ma on the Silk Road, "
    "Nusrat with the ambient West, Manu Chao everywhere at once. It cross-links every region of this "
    "survey -- Africa, the Americas, Europe, Asia, the Caribbean, the Pacific, and the diaspora -- into a "
    "single connected world. Content notes: the ethics of collaboration, credit, and sampling in world "
    "music (from 'Graceland' to 'Deep Forest') are noted factually and with respect. Cross-links: ALL "
    "regional surveys. Names transliterated. Scope: the global, connected present -- the survey's grand "
    "finale."
)

SECTIONS = [
    (
        "THE WORLD-MUSIC LANDMARK ALBUMS",
        "A handful of records made 'world music' a global phenomenon. Paul Simon's 'Graceland' (1986), "
        "recorded with South African musicians and Ladysmith Black Mambazo, was a watershed (and a debate "
        "about credit and the cultural boycott). Peter Gabriel's WOMAD and Real World label built a lasting "
        "home for it. Content note: the 'Graceland' collaboration and its controversies are noted "
        "factually. Cross-links: Southern Africa; the US.",
        [
            ("Graceland", "Paul Simon"),
            ("Homeless", "Ladysmith Black Mambazo"),
            ("The Graceland phenomenon (world music breaks through)", None),
            ("WOMAD & Real World (Peter Gabriel's world-music home)", None),
            ("The birth of 'world music' (the category & the debate)", None),
        ],
    ),
    (
        "THE GREAT CROSS-CULTURAL COLLABORATIONS",
        "World music's heart is the meeting of masters. Ali Farka Toure and Ry Cooder's 'Talking Timbuktu' "
        "joined Mali and the blues; Ravi Shankar opened Indian classical music to the West (and to Yehudi "
        "Menuhin's violin); and Ry Cooder and V.M. Bhatt's 'A Meeting by the River' bridged slide guitar "
        "and mohan veena. Cross-links: the Sahel; India; the US.",
        [
            ("Talking Timbuktu", "Ali Farka Toure & Ry Cooder"),
            ("A Meeting by the River", "Ry Cooder & V.M. Bhatt"),
            ("West Meets East (Shankar & Menuhin)", "Ravi Shankar"),
            ("The masters' collaboration (the world-music summit)", None),
            ("Mali meets the blues (the desert-blues bridge)", None),
        ],
    ),
    (
        "THE SILK ROAD & THE GLOBAL ENSEMBLE",
        "Some projects gathered the whole world into one band. Yo-Yo Ma's Silk Road Ensemble united "
        "musicians from across Eurasia; the Kronos Quartet commissioned and collaborated across every "
        "tradition; and AfroCubism finally joined the Malian and Cuban musicians that 'Buena Vista' had "
        "once missed. Cross-links: Central Asia; the Caribbean; West Africa.",
        [
            ("The Silk Road Ensemble (Yo-Yo Ma's global band)", None),
            ("AfroCubism (Mali meets Cuba at last)", None),
            ("The Kronos Quartet (the world-collaborating quartet)", None),
            ("The Afro-Cuban All Stars (the Havana supergroup)", None),
            ("The global ensemble (many traditions, one stage)", None),
        ],
    ),
    (
        "THE BUENA VISTA PHENOMENON & THE REVIVAL DECADE",
        "In the late 1990s, Ry Cooder's Buena Vista Social Club project made elderly Cuban soneros global "
        "stars and touched off a worldwide love of 'roots' music from every corner. It was the decade "
        "world music reached its widest audience. Cross-links: the Caribbean; Latin America.",
        [
            ("The Buena Vista Social Club phenomenon (the global revival)", None),
            ("Cuban son goes global (the 1990s world-roots wave)", None),
            ("The roots revival decade (world music's widest reach)", None),
            ("Ry Cooder, the global collaborator (Mali, Cuba & India)", None),
        ],
    ),
    (
        "THE GLOBAL-DIASPORA & MESTIZO SOUND",
        "A restless, border-crossing music arose from migration and the mixed city: Manu Chao's "
        "multilingual 'Clandestino', the gypsy-punk of Gogol Bordello, the Balkan brass of Goran Bregovic "
        "and Fanfare Ciocarlia, and the Mali-blues-pop of Amadou & Mariam. Cross-links: Europe; the Roma "
        "thread; West Africa; Latin America.",
        [
            ("Clandestino", "Manu Chao"),
            ("Je Veux (the modern global-chanson sound)", "Zaz"),
            ("Gogol Bordello (the gypsy-punk fusion)", None),
            ("Balkan brass goes global (Bregovic & Fanfare Ciocarlia)", None),
            ("Amadou & Mariam (the Mali blues-pop of Bamako)", None),
        ],
    ),
    (
        "GLOBAL BASS & THE ELECTRONIC FUSION",
        "The 21st century wired world music to the dancefloor. M.I.A.'s 'Paper Planes' fused global sounds "
        "and hip-hop; Buraka Som Sistema took Angolan kuduro global; and producers like Diplo and the "
        "'global bass' scene spliced cumbia, dancehall, baile funk, and kuduro into a borderless club "
        "music. Cross-links: Central Africa (kuduro); the Caribbean; Latin America.",
        [
            ("Paper Planes", "M.I.A."),
            ("Sound of Kuduro", "Buraka Som Sistema"),
            ("Global bass (the borderless club sound)", None),
            ("Diplo & the global-club producers", None),
            ("Dub's global children (the worldwide bass culture)", None),
        ],
    ),
    (
        "THE SACRED GOES GLOBAL",
        "The world's sacred musics found global audiences and collaborators. The Gyuto Tibetan monks' "
        "overtone chant toured the world; Nusrat Fateh Ali Khan's qawwali met the ambient West (with "
        "Michael Brook and Peter Gabriel); and Deep Forest's use of a Solomon Islands lullaby became a "
        "flashpoint. Content note: the sampling of indigenous and sacred music raised lasting ethical "
        "questions -- cross-link the Pacific & South Asia.",
        [
            ("Mustt Mustt (Nusrat meets the ambient West)", "Nusrat Fateh Ali Khan"),
            ("The Gyuto Monks (Tibetan overtone chant goes global)", None),
            ("Deep Forest & the sampling question (content note)", None),
            ("Qawwali crosses over (Nusrat & Michael Brook)", None),
            ("Sacred music on the world stage (the global sacred)", None),
        ],
    ),
    (
        "THE JAZZ, FLAMENCO & CLASSICAL WORLD NEXUS",
        "Jazz and Western classical music were world music's great meeting-grounds: Paco de Lucia's "
        "flamenco met Chick Corea and John McLaughlin's guitar; jazz drank from Africa, Cuba, India, and "
        "Brazil for a century; and 'Playing for Change' filmed musicians around the planet playing as one. "
        "Cross-links: Europe (flamenco); the US (jazz); Brazil.",
        [
            ("Playing for Change (Stand By Me around the world)", None),
            ("Paco de Lucia & the flamenco-jazz nexus", None),
            ("Jazz meets the world (the century-long fusion)", None),
            ("The guitar summit (de Lucia, McLaughlin & Corea)", None),
            ("The world-classical crossover (the concert-hall meeting)", None),
        ],
    ),
    (
        "ONE CONNECTED WORLD: THE GRAND FINALE",
        "The modern global-pop present -- Afrobeats, reggaeton, K-pop, and the streaming age -- is the "
        "fruit of everything this survey has traced: every tradition now within every other's reach. "
        "Angelique Kidjo bridges Benin and the world; Youssou N'Dour and Neneh Cherry's '7 Seconds' sang "
        "across languages; and the whole planet's music is now one conversation. This closes the World "
        "Music Survey. Cross-links: EVERY region -- Africa, the Americas, Europe, Asia, the Caribbean, the "
        "Pacific, and the diaspora.",
        [
            ("7 Seconds", "Youssou N'Dour & Neneh Cherry"),
            ("Agolo", "Angelique Kidjo"),
            ("One connected musical world (the global present)", None),
            ("The global-pop convergence (Afrobeats, reggaeton, K-pop)", None),
            ("The world survey's close (one planet, one conversation)", None),
        ],
    ),
]

STEM = "capstone_music_GLOBAL_FUSION"


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
