#!/usr/bin/env python3
"""Build Sub-Saharan Africa: West, installment 2: Palm-Wine Guitar & the Early Recording Era.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file (living tradition / no single definitive recording).
Covers c. 1900-1950.
"""

TITLE = ("The Story of West African Music — Installment 2: "
         "Palm-Wine Guitar & the Early Recording Era (c. 1900-1950)")

FRAMING = (
    "If Installment 1 was the deep oral root, this is the first new growth of the colonial century -- "
    "and the birth of West African POPULAR music. Its engine is a foreign instrument, the acoustic "
    "GUITAR, carried ashore by the KRU mariners of Liberia and Sierra Leone, who worked the coastal "
    "steamers and spread a distinctive two-finger picking style ('mainline', 'fireman') from port to "
    "port. Married to local rhythm and the palm-wine bar, it produced MARINGA in Sierra Leone, "
    "OSIBISAABA and the brass ADAHA in the Gold Coast (Ghana), and the first JUJU in Lagos -- the "
    "seedbed of highlife, which explodes in Installment 3. Running underneath is the GUMBE drum, "
    "brought by Jamaican Maroons repatriated to Freetown, and the returnee (Krio, Saro, Afro-Brazilian "
    "Aguda) networks that made the coast one node of a Black Atlantic music economy. In the late 1920s "
    "the record companies arrived -- Zonophone's West African series put African pop on shellac for "
    "the first time. Cross-links run hot: palm-wine guitar is a cousin of Trinidadian calypso and "
    "Cuban son, and soon of Congolese rumba; the whole thing rides colonial shipping and the legacy of "
    "slavery's returnees. Because this is early-recording and pre-recording material, most entries are "
    "'(Traditional)' or genre bare titles that will need manual searching; a handful of canonical 78s "
    "are named. Region: all named artists are West African; scope calls flagged."
)

SECTIONS = [
    (
        "THE KRU MARINERS & THE GUITAR COMES ASHORE (c. 1900-1930)",
        "The guitar entered West African popular music not through the concert hall but through the "
        "docks. The Kru (Kroo) sailors of Liberia and Sierra Leone, working the coastal steamships, "
        "picked up guitars in the Atlantic ports and developed the two-finger 'mainline' and 'fireman' "
        "styles, seeding a coastal guitar language from Freetown to Lagos. This is oral, undocumented "
        "on record -- search living-tradition or reconstruction recordings.",
        [
            ("Kru mariners' guitar (\"mainline\" two-finger picking)", None),
            ("Dagomba (Kru coastal guitar rhythm)", None),
            ("Fireman (Kru guitar style)", None),
            ("Osode (early coastal guitar song)", None),
        ],
    ),
    (
        "SIERRA LEONE: MARINGA & THE PALM-WINE BAR (c. 1920-1950)",
        "In the Krio bars of Freetown, guitar, a box-drum, and concertina made MARINGA -- the classic "
        "palm-wine music, named for the drink it was played over. Ebenezer Calender became its king, "
        "cutting sides that circulated across the coast and onto colonial radio. Palm-wine is loose, "
        "witty, topical song -- the Sierra Leonean cousin of calypso.",
        [
            ("Fire Fire Fire", "Ebenezer Calender"),
            ("Double Decker Bus", "Ebenezer Calender"),
            ("Maringa (Sierra Leone palm-wine)", None),
            ("Gumbe (box-drum palm-wine song)", None),
        ],
    ),
    (
        "GHANA (GOLD COAST): OSIBISAABA, ADAHA BRASS & THE ROOT OF 'HIGHLIFE' (c. 1900-1940)",
        "The word HIGHLIFE was coined in 1920s Accra for the imported ballroom dance music of the "
        "coastal elite -- but its roots were popular: Fante OSIBISAABA palm-wine, the brass-band ADAHA, "
        "and its cheaper marching cousin KONKOMA. The single most important early recording is the "
        "Kumasi Trio's 1928 'Yaa Amponsah', whose guitar figure became a template for generations. "
        "This is the direct on-ramp to Installment 3.",
        [
            ("Yaa Amponsah (1928)", "Kwame Asare (Kumasi Trio)"),
            ("Osibisaaba (Fante palm-wine highlife)", None),
            ("Adaha (Gold Coast brass-band highlife)", None),
            ("Konkoma (marching-band highlife)", None),
            ("Fante guitar-band highlife (early)", None),
        ],
    ),
    (
        "NIGERIA: THE BIRTH OF JUJU & LAGOS PALM-WINE (c. 1920-1950)",
        "In cosmopolitan Lagos, Yoruba palm-wine music picked up guitar, samba-tinged rhythm, and the "
        "tambourine to become JUJU -- a term Tunde King is credited with coining around 1932. Alongside "
        "it ran the older Yoruba-Muslim percussion forms SAKARA and APALA and the agidigbo thumb-piano "
        "song. Most survives only in obscure 78s and living tradition -- search a version.",
        [
            ("Early juju (Tunde King era, 1930s Lagos)", None),
            ("Sakara (Yoruba Muslim percussion song)", None),
            ("Apala (Yoruba roots percussion)", None),
            ("Agidigbo / Asiko (Yoruba palm-wine percussion)", None),
            ("Sea Never Dry (Lagos palm-wine standard)", None),
        ],
    ),
    (
        "GUMBE, THE RETURNEES & THE BLACK ATLANTIC (c. 1800s-1950)",
        "One of West Africa's most widespread drums arrived from the diaspora: the square-frame GUMBE "
        "(gome/goombay), brought by Jamaican Maroons repatriated to Freetown in 1800 and carried by "
        "Krio and Afro-Brazilian (Aguda) returnee networks to Ghana, Guinea-Bissau, Mali, and Lagos. "
        "It is living proof that the Atlantic music traffic ran both ways. Cross-link: to the Caribbean "
        "and Brazilian threads of the Latin America survey.",
        [
            ("Gome / Gumbe (square-frame drum, Maroon-returnee origin)", None),
            ("Goombay (the Atlantic returnee drum)", None),
            ("Aguda / Afro-Brazilian returnee songs (Lagos)", None),
            ("Krio maskarade / Christmas masquerade music (Freetown)", None),
        ],
    ),
    (
        "THE FIRST RECORDS: ZONOPHONE, HMV & THE WEST AFRICAN 78 (c. 1927-1950)",
        "In the late 1920s the British labels came recording: Zonophone's 'EZ' West African series and "
        "HMV's 'JZ' series put Gold Coast and Nigerian musicians onto shellac and sold the discs back "
        "into the colonies. It is the moment West African popular music becomes a commodity you could "
        "own. These entries point to the reissue compilations that preserve those first sides.",
        [
            ("Zonophone EZ West African series (first Gold Coast 78s, 1927)", None),
            ("Living Is Hard: West African music in Britain 1927-1929", None),
            ("HMV JZ West African series (early Nigerian 78s)", None),
        ],
    ),
    (
        "THE DANCE-BAND & BRASS SEEDBED (toward highlife, c. 1920-1950)",
        "Parallel to the guitar bands, the coastal elite danced to ballroom 'orchestras' and to "
        "colonial military brass, and the streets marched to konkoma -- the immediate precursors of the "
        "dance-band highlife that E.T. Mensah's Tempos would perfect in Installment 3. This is the "
        "ballroom half of highlife's double parentage (guitar band + dance band).",
        [
            ("Ballroom orchestra highlife (Cape Coast/Accra elite, 1930s)", None),
            ("Colonial brass-band adaha (Gold Coast)", None),
            ("Konkoma marching highlife (street version)", None),
            ("Sugar Babies / Cape Coast dance-band highlife (pre-Tempos)", None),
            ("Ashanti / coastal ballroom dance highlife (1940s)", None),
        ],
    ),
    (
        "CROSS-LINKS: THE BLACK ATLANTIC GUITAR (thematic)",
        "Palm-wine guitar was one node in an Atlantic network: Trinidadian calypso, Cuban son on "
        "imported 78s, and soon Congolese rumba all cross-pollinated through the same sailors and "
        "record shops, and the Kru two-finger style would feed highlife and the wider African "
        "guitar-pop to come. (Scope note: S.E. Rogie's 'My Lovely Elizabeth' is the classic surviving "
        "palm-wine recording but dates to c. 1962 -- placed here as the definitive document of this "
        "older style, and flagged as slightly later.) Content note: this whole circulation rode "
        "colonial shipping and the returnee legacy of slavery.",
        [
            ("My Lovely Elizabeth", "S.E. Rogie"),
            ("Palm-wine guitar (the Atlantic two-finger style)", None),
            ("Maringa <-> Calypso (the coastal song exchange)", None),
        ],
    ),
]

STEM = "ssa_west_music_2_PALMWINE_EARLY_RECORDING"


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
