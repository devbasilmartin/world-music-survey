#!/usr/bin/env python3
"""Build Sub-Saharan Africa: Central, installment 2: The Golden Age of Congolese Rumba.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1953-1965.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of Central African Music — Installment 2: "
         "The Golden Age of Congolese Rumba (c. 1953-1965)")

FRAMING = (
    "This is the decade Congolese rumba became the sound of a continent -- and of a nation being born. "
    "Two great bands and two philosophies defined it. Joseph Kabasele's AFRICAN JAZZ (founded 1953) "
    "played an elegant, Cuban-refined rumba of sweet harmonies and dazzling guitar (its ranks held Dr "
    "Nico and a young Tabu Ley Rochereau); Franco Luambo's OK JAZZ (1956) answered with an earthier, "
    "folk-rooted, Lingala-deep sound. Their rivalry drove the music to greatness. The era's supreme "
    "moment came in January 1960, when Kabasele's band, in Brussels for the Round Table talks that "
    "would grant Congo independence, recorded 'INDEPENDENCE CHA CHA' -- which became the anthem of "
    "African liberation from Kinshasa to the whole continent. Independence in June 1960 was followed "
    "almost at once by the Congo Crisis and the January 1961 assassination of Prime Minister Patrice "
    "Lumumba -- the music carries that hope and that wound together. Cross-links: 'Independence Cha "
    "Cha' as a pan-African anthem; Cuban son <-> Congo rumba (Latin survey); and Congo rumba pouring "
    "out over the radio to seed the guitar pop of East, West, and Southern Africa. Content note: "
    "independence, the Crisis, and Lumumba -- kept with context. Region: DR Congo & Congo-Brazzaville."
)

SECTIONS = [
    (
        "LE GRAND KALLE & AFRICAN JAZZ: THE ELEGANT SCHOOL (c. 1953-1963)",
        "Joseph Kabasele -- 'Le Grand Kalle', the father of modern Congolese music -- founded African "
        "Jazz in 1953 and refined rumba into a suave, harmonically rich art, sung in silky Lingala over "
        "Cuban-derived rhythm. His band was a finishing school for the era's greatest talents. Cross-"
        "link: the Cuban son template of Installment 1, now fully Congolese.",
        [
            ("Africa Mokili Mobimba", "Le Grand Kalle"),
            ("Table Ronde", "Le Grand Kalle"),
            ("African Jazz (Kabasele's elegant rumba)", None),
            ("Le Grand Kalle (father of modern Congolese music)", None),
            ("Kabasele's Cuban-refined rumba sound", None),
        ],
    ),
    (
        "INDEPENDENCE CHA CHA & THE POLITICS OF 1960",
        "In January 1960, at the Brussels Round Table where Congo's independence was negotiated, "
        "Kabasele's band cut 'Independence Cha Cha' -- a jubilant roll-call of the delegates that "
        "instantly became the anthem of the whole decolonizing continent. Content note: independence "
        "came in June 1960, but the Congo Crisis and the assassination of Patrice Lumumba (January "
        "1961) followed within months; the era's joy is shadowed by that betrayal.",
        [
            ("Independence Cha Cha", "Le Grand Kalle"),
            ("Congo independence anthem (June 1960, pan-African)", None),
            ("Lumumba and the Congo Crisis (music of 1960-61)", None),
            ("Vive Patrice Lumumba (independence-era song)", None),
            ("Pan-African independence rumba (spreads continent-wide)", None),
        ],
    ),
    (
        "FRANCO & OK JAZZ: THE EARTHY SCHOOL (c. 1956-1965)",
        "Franco Luambo Makiadi -- 'the Sorcerer of the Guitar' -- founded OK Jazz in 1956 and built the "
        "opposite pole: a rootsier, heavier, streetwise rumba, sung in deep Lingala with biting social "
        "commentary. His rhythmic 'mi-solo' guitar and the band's motto ('On Entre O.K., On Sort K.O.') "
        "made OK Jazz the people's band and Franco a colossus for three decades.",
        [
            ("On Entre OK On Sort KO", "OK Jazz"),
            ("Marie Naboyi", "Franco"),
            ("Franco Luambo (the Sorcerer of the Guitar)", None),
            ("OK Jazz (the folk-rooted rumba school)", None),
            ("Vicky Longomba (OK Jazz founding voice)", None),
            ("Sebene guitar (the dance section emerges)", None),
        ],
    ),
    (
        "THE TWO SCHOOLS & THE GUITAR MASTERS",
        "The African-Jazz-versus-OK-Jazz rivalry organized the whole scene and pushed the guitar to new "
        "heights. Dr Nico Kasanda's crystalline lead lines with African Jazz set a standard every "
        "Congolese guitarist still measures against; Tino Baroza and Brazzos were pioneers too; and the "
        "young Tabu Ley Rochereau was learning his craft as an African Jazz vocalist before his own "
        "reign (Installment 3).",
        [
            ("Dr Nico Kasanda (African Jazz guitar virtuoso)", None),
            ("Tino Baroza (pioneer Congo lead guitar)", None),
            ("African Jazz versus OK Jazz (the defining rivalry)", None),
            ("Rochereau emerges (young Tabu Ley with African Jazz)", None),
            ("Brazzos and the OK Jazz guitar", None),
            ("Mi-solo, rhythm and bass guitar layering (Congo style)", None),
        ],
    ),
    (
        "THE RUMBA ODEMBA & THE ARRANGEMENT",
        "The classic form crystallized: the RUMBA ODEMBA, a sung, slow-to-mid rumba that breaks into an "
        "accelerating guitar-driven dance section (the sebene). Horn sections of saxes and trumpets, "
        "sweet vocal harmony, and Lingala poetry became the template that ruled African dance floors "
        "for a generation.",
        [
            ("Rumba odemba (the classic slow-to-fast form)", None),
            ("Cha-cha-cha and bolero in Congo rumba", None),
            ("Horn-section rumba (saxophones and trumpets)", None),
            ("Lingala lyric rumba (the language of Congo pop)", None),
            ("Maringa-to-modern rumba refinement", None),
        ],
    ),
    (
        "THE BRAZZAVILLE SCENE & THE CONTINENTAL SPREAD",
        "Across the river, Brazzaville built its own scene -- Les Bantous de la Capitale (1959) chief "
        "among them -- and, carried on shortwave radio and 78s, Congo rumba became the pan-African "
        "popular music, reshaping guitar pop from Nairobi to Abidjan to Johannesburg. Cross-link: this "
        "is the tide the East, West, and Southern Africa surveys all feel.",
        [
            ("Brazzaville rumba scene (across the river)", None),
            ("Les Bantous de la Capitale (Brazzaville, 1959)", None),
            ("Congo rumba on the radio (spreads across Africa)", None),
            ("Rumba reaches East Africa (Nairobi)", None),
            ("Rumba reaches West and Southern Africa (the guitar tide)", None),
        ],
    ),
]

STEM = "ssa_central_music_2_RUMBA_GOLDEN_AGE"


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
