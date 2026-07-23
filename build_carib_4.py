#!/usr/bin/env python3
"""Build the Caribbean, installment 4 (FINALE): Dancehall, Reggaeton & the Modern Caribbean.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Caribbean Music — Installment 4 (Finale): "
         "Dancehall, Reggaeton & the Modern Caribbean")

FRAMING = (
    "The final Caribbean chapter carries the islands into a digital, global present. In Jamaica, reggae "
    "hardened into DANCEHALL -- rawer, faster, and, after the 1985 'Sleng Teng' riddim, fully DIGITAL -- "
    "the sound of the deejay (Yellowman, Shabba Ranks, Beenie Man, Bounty Killer) and, in Sean Paul and "
    "the riddim system, a global pop force. Meanwhile, from the meeting of Jamaican dancehall, Panama's "
    "Spanish reggae, and Puerto Rico's underground came REGGAETON -- built on the DEMBOW riddim -- which "
    "exploded worldwide with Daddy Yankee's 'Gasolina' and now, through J Balvin and BAD BUNNY, is the "
    "biggest sound on Earth. Soca went global too, and Barbados gave the planet RIHANNA, the Caribbean's "
    "reigning superstar. This closes the Caribbean survey. Content notes: dancehall's controversies "
    "(slackness and anti-gay lyrics), reggaeton's censorship battles, and Vybz Kartel's legal case are "
    "noted factually and with care. Cross-links: reggaeton and salsa in the Latin America survey "
    "(cross-linked; Caribbean/Puerto Rican-origin tracks live here); toasting/dancehall -> hip-hop (US); "
    "Africa. Names as commonly romanized. Region: the modern Caribbean & its global reach."
)

SECTIONS = [
    (
        "THE DIGITAL TURN: DANCEHALL & SLENG TENG",
        "In the early 1980s, reggae sped up and stripped down into DANCEHALL -- the raw, deejay-driven "
        "sound of the dance. The 1985 'Under Mi Sleng Teng' riddim, built on a Casio keyboard preset, "
        "launched the fully DIGITAL era ('ragga'), where hundreds of deejays voice the same computerized "
        "RIDDIM. It remade Jamaican music for good.",
        [
            ("Under Mi Sleng Teng", "Wayne Smith"),
            ("Dancehall (the raw deejay sound of the dance)", None),
            ("The digital riddim era (ragga & Sleng Teng)", None),
            ("The riddim system (many deejays, one riddim)", None),
            ("Sound clash (the dancehall competition)", None),
        ],
    ),
    (
        "THE DANCEHALL DEEJAYS",
        "Dancehall crowned a line of star deejays. Yellowman broke through in the early 1980s; Shabba "
        "Ranks brought a Grammy-winning international profile; and the fierce rivalry of Beenie Man and "
        "Bounty Killer defined the 1990s. Content note: dancehall's 'slackness' and some anti-gay lyrics "
        "drew real controversy, noted factually.",
        [
            ("Zungguzungguguzungguzeng", "Yellowman"),
            ("Ting-a-Ling", "Shabba Ranks"),
            ("Who Am I (Sim Simma)", "Beenie Man"),
            ("The dancehall deejay (the star toaster)", None),
            ("Beenie Man & Bounty Killer (the 1990s rivalry)", None),
        ],
    ),
    (
        "DANCEHALL GOES GLOBAL: SEAN PAUL & KARTEL",
        "Dancehall conquered the world charts. Sean Paul's 'Temperature' and a run of crossover smashes "
        "made him a global pop star, and dancehall rhythms seeped into US and UK pop for good. Vybz "
        "Kartel became the genre's most influential modern voice. Content note: Kartel recorded on amid a "
        "long-running murder case (later overturned), noted factually.",
        [
            ("Temperature", "Sean Paul"),
            ("Summer Time", "Vybz Kartel"),
            ("Sean Paul (dancehall's global crossover)", None),
            ("Vybz Kartel (the modern dancehall king)", None),
            ("Dancehall in global pop (the riddim spreads)", None),
        ],
    ),
    (
        "THE ROOTS OF REGGAETON",
        "Reggaeton was born of migration: Jamaican dancehall carried to Panama, where artists like El "
        "General toasted in Spanish ('reggae en espanol'), then fused in 1990s Puerto Rico's underground "
        "with rap and the all-important DEMBOW riddim (from Shabba Ranks' 'Dem Bow'). 'Underground' "
        "mixtapes built the sound. Cross-link: the Latin America survey.",
        [
            ("Tu Pum Pum", "El General"),
            ("Reggaeton (the dembow-driven Caribbean sound)", None),
            ("The dembow riddim (the reggaeton heartbeat)", None),
            ("Reggae en espanol (the Panama root)", None),
            ("The Puerto Rico underground (the reggaeton birth)", None),
        ],
    ),
    (
        "REGGAETON EXPLODES: DADDY YANKEE & THE 2000s",
        "In 2004, Daddy Yankee's 'Gasolina' detonated reggaeton worldwide, and a wave of Puerto Rican "
        "stars -- Tego Calderon, Don Omar, Wisin & Yandel, Ivy Queen (the genre's leading woman) -- turned "
        "it into a global Latin-urban juggernaut. Content note: reggaeton faced censorship campaigns in "
        "its early years, noted factually.",
        [
            ("Gasolina", "Daddy Yankee"),
            ("Danza Kuduro", "Don Omar"),
            ("Pa'l Norte", "Calle 13"),
            ("Daddy Yankee (the King of Reggaeton)", None),
            ("Ivy Queen & Tego Calderon (the reggaeton pioneers)", None),
        ],
    ),
    (
        "THE GLOBAL LATIN-URBAN ERA: BALVIN & BAD BUNNY",
        "Reggaeton became the biggest sound on Earth. Colombia's J Balvin globalized its melodic side, and "
        "Puerto Rico's BAD BUNNY became the most-streamed artist in the world, fusing reggaeton, trap, and "
        "Latin roots. The 'Despacito' phenomenon and a new 'Latin-urban' era put the Caribbean at the "
        "center of global pop. Cross-link: the Latin America survey.",
        [
            ("Mi Gente", "J Balvin"),
            ("Titi Me Pregunto", "Bad Bunny"),
            ("Bad Bunny (the global reggaeton superstar)", None),
            ("Latin trap & the modern reggaeton (the global era)", None),
            ("Reggaeton conquers global pop (the Caribbean center)", None),
        ],
    ),
    (
        "RIHANNA & THE CARIBBEAN-GLOBAL SUPERSTAR",
        "The modern Caribbean produced planet-conquering pop stars. Barbados gave the world RIHANNA, one "
        "of the best-selling artists of all time, whose music kept a dancehall-and-island pulse ('Work'); "
        "and the wider Anglophone Caribbean's bashment and its diaspora shaped UK and US pop for a "
        "generation.",
        [
            ("Work", "Rihanna"),
            ("Rude Boy", "Rihanna"),
            ("Rihanna (the Barbadian global superstar)", None),
            ("The Caribbean in global pop (the island pulse)", None),
            ("Bashment & the Caribbean diaspora sound", None),
        ],
    ),
    (
        "SOCA'S GLOBAL REACH & THE MODERN FETE",
        "Soca went global too, driving the huge Caribbean Carnivals of the diaspora -- Notting Hill in "
        "London, Labor Day in Brooklyn, Caribana in Toronto -- and scoring worldwide crossover moments. "
        "Machel Montano and a new generation carried the fete music of Trinidad to the world's dancefloors.",
        [
            ("Hot Wuk (the modern soca fete)", None),
            ("Global soca & the diaspora Carnival (Notting Hill, Brooklyn)", None),
            ("Soca crossover (the fete goes worldwide)", None),
            ("The modern Carnival fete (the global road)", None),
        ],
    ),
    (
        "THE CARIBBEAN ARC: A FINALE",
        "Four installments span a small sea that reshaped world music: the Afro-Cuban clave and son; "
        "Jamaica's reggae, dub, and toasting; Trinidad's calypso, soca, and steelpan and the wider isles; "
        "and now dancehall, reggaeton, and a Caribbean-global present. From the clave to the dembow, this "
        "sea gave the world its rhythm. This closes the Caribbean survey. Cross-links: the Americas, "
        "Africa, and the global present.",
        [
            ("The Caribbean arc (from the clave to the dembow)", None),
            ("A small sea that reshaped world music", None),
            ("The Caribbean rhythm goes global (the shared gift)", None),
            ("Toward the surveys ahead (roads onward)", None),
        ],
    ),
]

STEM = "carib_music_4_DANCEHALL_REGGAETON_MODERN"


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
