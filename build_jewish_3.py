#!/usr/bin/env python3
"""Build the Jewish Diaspora, installment 3: Sephardi & Mizrahi.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Jewish Music — Installment 3: "
         "Sephardi & Mizrahi (Ladino, the Judeo-Arab World & the Eastern Jewish Traditions)")

FRAMING = (
    "Beyond Ashkenaz lie the other great Jewish musical worlds. The SEPHARDI Jews, expelled from Spain in "
    "1492, carried their Judeo-Spanish language and song -- LADINO -- around the Mediterranean, and its "
    "haunting romances ('Adio Kerida', 'Los Bilbilikos') survived five centuries in Salonika, Istanbul, "
    "and beyond. The MIZRAHI (Eastern) Jews of the Arab and Muslim lands made music indistinguishable in "
    "sound from their neighbors': the Judeo-Arab ANDALUSI and piyyut tradition of the Maghreb, the "
    "BUKHARAN Jews at the heart of Central Asian shashmaqam, the PERSIAN Jewish musicians of Iran, the "
    "YEMENITE Jewish DIWAN of Shabazi's sacred poetry, and the IRAQI Jews who were the very masters of the "
    "Baghdadi maqam. This installment maps these Sephardi and Mizrahi worlds between the Ashkenazi (#2) "
    "and the modern era (#4). Content notes: the 1492 expulsion and the 20th-century departure of nearly "
    "all Jews from Arab and Muslim lands are treated strictly factually, evenhandedly, and with care -- as "
    "is the shared Judeo-Arab heritage. Cross-links: MENA; Central Asia (shashmaqam); Spain/flamenco. "
    "Names transliterated. Region: the Sephardi & Mizrahi Jewish world."
)

SECTIONS = [
    (
        "1492 & THE SEPHARDI DISPERSION",
        "In 1492 the Jews were expelled from Spain, ending a golden age of Iberian Jewish life and "
        "scattering the SEPHARDIM across the Ottoman Mediterranean and North Africa. They carried with them "
        "their Judeo-Spanish tongue and a treasury of song that would survive, astonishingly, for five "
        "hundred years. Content note: the expulsion is remembered factually, as history and loss.",
        [
            ("The 1492 expulsion & the Sephardi dispersion", None),
            ("The Sephardi Mediterranean (Salonika, Istanbul, the Balkans)", None),
            ("The golden age of Spain remembered (the Sephardi memory)", None),
            ("Five centuries of Ladino song (the survival)", None),
        ],
    ),
    (
        "LADINO: THE JUDEO-SPANISH SONG",
        "LADINO (Judeo-Spanish) song preserved medieval Spanish romances, love songs, and life-cycle "
        "songs, sung by women in the home and evolving with each Ottoman city. 'Adio Kerida', 'Los "
        "Bilbilikos', and 'Durme Durme' are its immortal melodies -- a living museum of a lost Spain, "
        "colored by the Balkans and the Levant.",
        [
            ("Adio Kerida (the Ladino farewell song)", None),
            ("Los Bilbilikos (the nightingales, a Ladino classic)", None),
            ("Durme Durme (the Ladino lullaby)", None),
            ("La Rosa Enflorese (a Ladino romance)", None),
            ("Ladino / Judeo-Spanish song (the Sephardi tradition)", None),
        ],
    ),
    (
        "THE LADINO SONG KEEPERS",
        "A line of singers kept Ladino alive and carried it to the world: Flory Jagoda, the "
        "'keeper of the flame' from Bosnia, wrote the beloved Hanukkah song 'Ocho Kandelikas'; and Yasmin "
        "Levy fused Ladino with flamenco, honoring the shared Andalusian root. Cross-link: flamenco (the "
        "Europe survey).",
        [
            ("Ocho Kandelikas (the Ladino Hanukkah song)", "Flory Jagoda"),
            ("Cuando el Rey Nimrod (the Sephardi ballad)", None),
            ("Yasmin Levy (Ladino meets flamenco)", None),
            ("Flory Jagoda (the keeper of the Ladino flame)", None),
            ("Ladino & flamenco (the shared Andalusian root, cross-link)", None),
        ],
    ),
    (
        "THE OTTOMAN-SEPHARDI SACRED TRADITION",
        "In the Ottoman world the Sephardim built a rich sacred music: the MAFTIRIM, a choral tradition "
        "that set Hebrew sacred poetry to Ottoman classical makam, and coplas and piyyutim sung to the "
        "melodies of the surrounding culture. It is a profound meeting of Jewish word and Turkish art "
        "music. Cross-link: Ottoman makam (MENA).",
        [
            ("The maftirim (the Ottoman-Sephardi sacred choir)", None),
            ("Hebrew poetry in Ottoman makam (the maftirim art)", None),
            ("The Sephardi piyyut (the eastern sacred song)", None),
            ("Coplas (the Sephardi para-liturgical songs)", None),
        ],
    ),
    (
        "THE MAGHREB: THE JUDEO-ANDALUSI TRADITION",
        "The Jews of Morocco, Algeria, and Tunisia were central to the Andalusi classical music of the "
        "Maghreb, and kept a rich tradition of the baqashot (dawn devotional songs) and piyyut sung in the "
        "Arab-Andalusi modes. The Moroccan-Jewish diva Zohra Al Fassia was a star of the wider Moroccan "
        "song. Cross-link: the Maghreb & Andalusi music (MENA #5).",
        [
            ("The Judeo-Andalusi tradition (the Maghrebi Jewish music)", None),
            ("The baqashot (the dawn devotional songs)", None),
            ("Zohra Al Fassia (the Moroccan-Jewish diva)", None),
            ("Moroccan Jewish piyyut (the Andalusi sacred song)", None),
            ("Jews & the Andalusi orchestra (the shared Maghreb music)", None),
        ],
    ),
    (
        "THE BUKHARAN & PERSIAN JEWS",
        "In Central Asia, the BUKHARAN Jews were central custodians of the Uzbek-Tajik SHASHMAQAM, the "
        "region's classical crown (cross-link: Central Asia #2). In Iran, PERSIAN Jewish musicians were "
        "prominent masters of Persian classical music. Across the Persianate world, Jews were often the "
        "professional keepers of the high art music.",
        [
            ("The Bukharan Jews & the shashmaqam (cross-link)", None),
            ("Bukharan Jewish song (the Central Asian tradition)", None),
            ("Persian Jewish musicians (the Iranian classical masters)", None),
            ("Levi Babakhanov (the Bukharan shashmaqam master)", None),
            ("Jews as keepers of the Persianate art music", None),
        ],
    ),
    (
        "YEMENITE JEWISH SONG: THE DIWAN",
        "The Jews of Yemen kept one of the most ancient and distinctive traditions: the DIWAN, a body of "
        "sacred and para-liturgical poetry (above all by the 17th-century poet Shalom SHABAZI) sung to "
        "hand-drum and hand-clap, with a unique modal sound. Content note: it is the deep root of later "
        "Yemenite-Israeli stars (Ofra Haza, A-WA -- cross-link MENA #6).",
        [
            ("The Yemenite Jewish Diwan (the sacred poetry)", None),
            ("Shalom Shabazi (the great Yemenite Jewish poet)", None),
            ("Se'i Yona (the classic Yemenite Jewish song)", None),
            ("Yemenite Jewish song (the ancient modal tradition)", None),
            ("The Yemenite root of Israeli music (cross-link)", None),
        ],
    ),
    (
        "THE IRAQI JEWS & THE BAGHDADI MAQAM",
        "The Jews of Iraq were not just part of but often the masters of the Baghdadi MAQAM and the city's "
        "musical life -- the brothers Saleh and Daoud AL-KUWAITI were the leading composers of Iraqi music "
        "in the 20th century. Content note: nearly the entire community left Iraq around 1950-51, carrying "
        "the maqam into exile. Cross-link: the Arab maqam (MENA).",
        [
            ("The Al-Kuwaiti brothers (the masters of Iraqi music)", None),
            ("The Iraqi Jews & the Baghdadi maqam", None),
            ("The Jewish musicians of Baghdad (the city's sound)", None),
            ("The maqam carried into exile (content note)", None),
            ("Iraqi Jewish song (the Mesopotamian tradition)", None),
        ],
    ),
    (
        "THE SEPHARDI-MIZRAHI WORLD & THE ROAD AHEAD",
        "From Ladino romances to the Judeo-Andalusi baqashot, the Bukharan shashmaqam, the Yemenite Diwan, "
        "and the Baghdadi maqam, the Sephardi and Mizrahi Jews made music wholly at home in the "
        "Mediterranean and Islamic worlds -- a shared heritage now largely carried in exile and Israel. "
        "From here the survey turns to the modern era (#4). Cross-links: MENA; Central Asia; Spain; "
        "modern Israel (#4).",
        [
            ("The Sephardi-Mizrahi musical world (the eastern branches)", None),
            ("A shared Mediterranean & Islamic-world heritage", None),
            ("From the Arab lands to Israel (the exodus & the music)", None),
            ("Toward modern Israel & the global diaspora (roads ahead)", None),
        ],
    ),
]

STEM = "jewish_music_3_SEPHARDI_MIZRAHI"


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
