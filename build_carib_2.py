#!/usr/bin/env python3
"""Build the Caribbean, installment 2: Jamaica -- Ska, Rocksteady, Reggae & Dub.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Caribbean Music — Installment 2: "
         "Jamaica -- Ska, Rocksteady, Reggae & Dub")

FRAMING = (
    "No island of its size has shaped world music like JAMAICA. From the folk MENTO and the sacred "
    "NYABINGHI drumming of RASTAFARI grew, in a single astonishing decade, a chain of new genres: the "
    "up-tempo SKA of the early 1960s (the Skatalites, Prince Buster), the slower, soulful ROCKSTEADY, and "
    "then REGGAE -- the offbeat 'skank', the one-drop drum, and the deep bass that carried Rastafari faith "
    "and social protest around the globe through BOB MARLEY, Peter Tosh, Burning Spear, and Toots & the "
    "Maytals. In the studio, engineers turned the mixing board into an instrument, inventing DUB (King "
    "Tubby, Lee 'Scratch' Perry, Augustus Pablo) -- remix and bass science decades ahead of their time -- "
    "while DJs 'toasting' over riddims (U-Roy, Big Youth) seeded rap itself. All of it rode Jamaica's "
    "SOUND-SYSTEM culture. Content note: Rastafari is a living faith and Marley's music carried real "
    "political weight -- kept factual and with care. Cross-links: toasting -> hip-hop (US survey); "
    "reggae's global children (UK, Africa, the world); dancehall ahead (#4). Names as commonly romanized. "
    "Region: Jamaica."
)

SECTIONS = [
    (
        "THE FOLK ROOTS: MENTO",
        "Before ska there was MENTO -- Jamaica's rural acoustic folk song of banjo, guitar, hand-drum, and "
        "the rhumba box (a big thumb-piano bass), witty and risque, often confused with calypso. It is the "
        "deep country root from which the island's modern music grew.",
        [
            ("Mento (the Jamaican rural folk song)", None),
            ("The rhumba box & the mento band", None),
            ("Sly Mongoose (the mento standard)", None),
            ("The country root of Jamaican music", None),
        ],
    ),
    (
        "RASTAFARI & NYABINGHI DRUMMING",
        "The RASTAFARI faith -- which rose in 1930s Jamaica, revering Haile Selassie and calling for a "
        "return to Africa -- gave the music its spiritual heart. Its NYABINGHI hand-drumming (bass, funde, "
        "and repeater drums) and chants, carried by elders like Count Ossie, beat beneath all of reggae. "
        "Content note: a living religion, treated with respect.",
        [
            ("Nyabinghi drumming (the Rastafari sacred drums)", None),
            ("Rastafari & the roots of reggae (the faith)", None),
            ("Count Ossie & the Mystic Revelation of Rastafari", None),
            ("Grounation chants (the Rasta repertoire)", None),
        ],
    ),
    (
        "THE SKA BOOM & THE SOUND SYSTEM",
        "As Jamaica gained independence in 1962, SKA burst out -- a jumping, horn-driven fusion of mento, "
        "American R&B, and jazz, its guitar chopping on the offbeat. The Skatalites were its virtuoso band "
        "and Prince Buster a founding star, all of it powered by the SOUND SYSTEM -- mobile DJ rigs and "
        "the producers (Coxsone Dodd, Duke Reid) who ruled the dancehalls.",
        [
            ("Guns of Navarone", "The Skatalites"),
            ("Al Capone", "Prince Buster"),
            ("Ska (the first Jamaican pop explosion)", None),
            ("The sound system (Coxsone, Duke Reid & the dancehall)", None),
            ("Studio One (the Jamaican Motown)", None),
        ],
    ),
    (
        "ROCKSTEADY",
        "By 1966 the tempo slowed and the mood deepened into ROCKSTEADY -- soulful, bass-forward, and "
        "romantic, with lush vocal harmonies and a brief, golden two-year reign. Alton Ellis (its 'godfather') "
        "and vocal groups like the Techniques and the Paragons defined its sweet, aching sound.",
        [
            ("Get Ready to Rock Steady", "Alton Ellis"),
            ("Queen Majesty", "The Techniques"),
            ("The Tide Is High", "The Paragons"),
            ("Rocksteady (the soulful slow-down)", None),
            ("The rocksteady harmony groups", None),
        ],
    ),
    (
        "ROOTS REGGAE & BOB MARLEY",
        "Reggae arrived c.1968 -- the offbeat 'skank', the one-drop drum, deep bass, and lyrics of faith "
        "and resistance. BOB MARLEY & the Wailers carried it to the whole world ('No Woman No Cry', "
        "'Redemption Song'), with Peter Tosh and Bunny Wailer beside him. Content note: Marley's music "
        "carried real political weight (the 1978 One Love Peace Concert), kept factual.",
        [
            ("No Woman No Cry", "Bob Marley & The Wailers"),
            ("Redemption Song", "Bob Marley"),
            ("Legalize It", "Peter Tosh"),
            ("Roots reggae (the offbeat skank & the one-drop)", None),
            ("Bob Marley (reggae's global voice)", None),
        ],
    ),
    (
        "THE REGGAE GREATS & THE HARDER THEY COME",
        "Reggae's golden age was deep. Burning Spear sang Marcus Garvey; Toots & the Maytals coined the "
        "word 'reggae' ('Do the Reggay') and roared gospel-soul; and Jimmy Cliff's film 'The Harder They "
        "Come' (1972) brought Jamaican music to the world. The harmony trio the Abyssinians sang the "
        "hymn-like 'Satta Massagana'.",
        [
            ("Marcus Garvey", "Burning Spear"),
            ("Pressure Drop", "Toots & the Maytals"),
            ("The Harder They Come", "Jimmy Cliff"),
            ("Satta Massagana", "The Abyssinians"),
            ("The roots reggae greats (the golden age)", None),
        ],
    ),
    (
        "DUB & THE STUDIO AS INSTRUMENT",
        "Jamaican engineers reinvented recording itself. DUB -- stripping a song to bass and drums, then "
        "drenching it in echo, reverb, and drop-outs -- turned the mixing board into an instrument. King "
        "Tubby pioneered it, Lee 'Scratch' Perry made his Black Ark a studio-as-laboratory, and Augustus "
        "Pablo's melodica haunted 'King Tubby Meets Rockers Uptown'. This is the ancestor of remixing.",
        [
            ("King Tubby Meets Rockers Uptown", "Augustus Pablo"),
            ("Dub (the studio remix science)", None),
            ("King Tubby (the inventor of dub)", None),
            ("Lee 'Scratch' Perry & the Black Ark", None),
            ("The version & the riddim (the B-side dub culture)", None),
        ],
    ),
    (
        "TOASTING: THE DJ & THE ROOT OF RAP",
        "Over the instrumental 'versions', Jamaican DJs began TOASTING -- chatting, rhyming, and hyping "
        "the crowd on the mic -- a practice U-Roy pioneered and Big Youth and I-Roy carried, and which, "
        "brought to the Bronx by Jamaican-born DJ Kool Herc, helped seed HIP-HOP itself. Cross-link: rap "
        "in the US survey.",
        [
            ("Wear You to the Ball", "U-Roy"),
            ("Screaming Target", "Big Youth"),
            ("Toasting (the Jamaican DJ mic-chatting)", None),
            ("U-Roy (the originating toaster)", None),
            ("Toasting seeds hip-hop (the cross-link)", None),
        ],
    ),
    (
        "JAMAICA'S GLOBAL ECHO & THE ROAD AHEAD",
        "From a tiny island, ska, reggae, dub, and toasting reshaped global music -- British 2-Tone and "
        "lovers rock, reggae in Africa and everywhere, and the DNA of hip-hop, dub, and remix culture "
        "worldwide. From roots reggae the island's music would harden into dancehall (#4). Cross-links: "
        "the Cuban root (#1); calypso & the wider isles (#3); hip-hop (US).",
        [
            ("Jamaica's global echo (ska & reggae worldwide)", None),
            ("2-Tone & lovers rock (reggae's British children)", None),
            ("Reggae goes global (the worldwide faith)", None),
            ("Toward dancehall & the modern Caribbean (roads ahead)", None),
        ],
    ),
]

STEM = "carib_music_2_JAMAICA_SKA_REGGAE_DUB"


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
