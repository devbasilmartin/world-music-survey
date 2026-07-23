#!/usr/bin/env python3
"""Build the Jewish Diaspora, installment 4 (FINALE): Modern Israel & the Diaspora in Global Music.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Jewish Music — Installment 4 (Finale): "
         "Modern Israel & the Diaspora in Global Music")

FRAMING = (
    "The final chapter brings Jewish music into the modern world -- through the new nation of ISRAEL and "
    "the diaspora's vast footprint in global pop. Modern Israel forged a new Hebrew song culture: the "
    "SHIREI ERETZ YISRAEL (the pioneer songbook of the kibbutz and the hora), the anthem HaTikvah, and "
    "Naomi Shemer's 'Yerushalayim Shel Zahav'. From it grew Israeli rock (Arik Einstein, Kaveret), the "
    "rise of long-marginalized MIZRAHI pop into the mainstream, the pan-ethnic Idan Raichel Project, and a "
    "modern pop and Eurovision presence. Meanwhile, the diaspora shaped 20th-century global music itself: "
    "the Great American Songbook (Irving Berlin, Gershwin), Leonard Cohen, Bob Dylan, Barbra Streisand, "
    "Amy Winehouse, Serge Gainsbourg, and Drake all carry a thread of this story -- noted here as "
    "cross-links, since they live in other surveys. This closes the Jewish-music survey and ties its "
    "whole arc -- liturgy, Ashkenazi, Sephardi/Mizrahi, and the modern world -- together. Content notes: "
    "HaTikvah, the founding of Israel, and the Israeli-Palestinian context are treated strictly factually, "
    "evenhandedly, and with care, as music. Cross-links: the US, Europe, MENA. Names transliterated. "
    "Region: modern Israel & the global Jewish diaspora."
)

SECTIONS = [
    (
        "HATIKVAH & THE PIONEER SONGBOOK",
        "Modern Hebrew song was built by the Zionist movement: HaTikvah (the anthem, its melody kin to a "
        "European folk tune) and the SHIREI ERETZ YISRAEL -- the pioneer 'songs of the Land of Israel', "
        "sung on the kibbutz and danced as the HORA. They forged a new secular Hebrew musical identity. "
        "Content note: the national anthem and its context noted factually.",
        [
            ("HaTikvah (the Israeli anthem)", None),
            ("Shirei Eretz Yisrael (the pioneer songbook)", None),
            ("The hora (the Israeli pioneer dance)", None),
            ("The kibbutz song (the new Hebrew culture)", None),
            ("Hava Nagila (the global Hebrew celebration song)", None),
        ],
    ),
    (
        "NAOMI SHEMER & THE SONG OF THE LAND",
        "Naomi Shemer, the 'first lady of Israeli song', wrote its most beloved music, above all "
        "'Yerushalayim Shel Zahav' (Jerusalem of Gold, 1967), which became a near-second anthem. Her "
        "songs, and the era's, defined the lyrical, poetic heart of the Israeli songbook.",
        [
            ("Yerushalayim Shel Zahav (Jerusalem of Gold)", "Naomi Shemer"),
            ("Naomi Shemer (the first lady of Israeli song)", None),
            ("Lu Yehi (the beloved Shemer song)", "Naomi Shemer"),
            ("The lyrical Israeli songbook (the poetic heart)", None),
        ],
    ),
    (
        "THE BIRTH OF ISRAELI ROCK & POP",
        "From the 1960s-70s, Israel built a modern pop and rock scene. Arik Einstein is considered the "
        "father of Israeli rock; the wildly inventive band Kaveret (Poogy) became a national institution; "
        "and the comic trio HaGashash HaHiver and singers like Chava Alberstein and Shalom Hanoch shaped "
        "the sound of a young nation.",
        [
            ("Ani Ve'Ata (You and I, the Einstein classic)", "Arik Einstein"),
            ("Arik Einstein (the father of Israeli rock)", None),
            ("Kaveret / Poogy (the beloved Israeli band)", None),
            ("Chava Alberstein (the great Israeli singer)", None),
            ("Shalom Hanoch (the Israeli rock pioneer)", None),
        ],
    ),
    (
        "MIZRAHI POP RISES TO THE MAINSTREAM",
        "The Mizrahi (Eastern) music of Israel's Jews from Arab and Muslim lands -- long dismissed as "
        "'cassette music' from the margins -- rose over decades to dominate Israeli pop. Cross-link: its "
        "stars Zohar Argov, Ofra Haza, and A-WA are covered in the MENA survey (#6); here we note the "
        "arc from margin to mainstream. Content note: a story of ethnic inclusion in Israeli culture.",
        [
            ("Mizrahi-Israeli pop (from the margins to the mainstream)", None),
            ("The 'cassette music' era (the Mizrahi rise, content note)", None),
            ("Mizrahi pop conquers Israel (the cross-link to MENA #6)", None),
            ("The Yemenite-Israeli voice in pop (cross-link)", None),
        ],
    ),
    (
        "IDAN RAICHEL & THE PAN-ETHNIC ISRAEL",
        "The Idan Raichel Project became a landmark of 21st-century Israeli music -- a collective blending "
        "Hebrew song with Ethiopian, Arab, and global sounds, its breakthrough 'Bo'i' featuring Ethiopian-"
        "Israeli voices. It embodied a multicultural, pan-ethnic Israeli music and a global 'world' reach.",
        [
            ("Bo'i (the Idan Raichel Project breakthrough)", "The Idan Raichel Project"),
            ("The Idan Raichel Project (the pan-ethnic Israeli fusion)", None),
            ("Ethiopian-Israeli music (the new Israeli sound)", None),
            ("Multicultural Israeli music (the global fusion)", None),
        ],
    ),
    (
        "MODERN ISRAELI POP & EUROVISION",
        "Israel built a thriving modern pop scene and a long Eurovision history, winning multiple times -- "
        "from Izhar Cohen (1978) and Dana International (1998) to Netta's 'Toy' (2018). Contemporary Israeli "
        "pop, hip-hop, and electronica connect the country to the global mainstream. Cross-link: Eurovision "
        "(the Europe survey).",
        [
            ("Toy (Netta's Eurovision win)", "Netta"),
            ("Diva (Dana International's Eurovision win)", "Dana International"),
            ("Modern Israeli pop (the contemporary scene)", None),
            ("Israel at Eurovision (the pop stage)", None),
            ("Israeli hip-hop & electronica (the modern sound)", None),
        ],
    ),
    (
        "THE DIASPORA & THE GREAT AMERICAN SONGBOOK",
        "Jewish songwriters built the soundtrack of modern America. Cross-links (their full stories live in "
        "the US survey): Irving Berlin wrote 'White Christmas' and 'God Bless America'; George Gershwin "
        "fused jazz and classical; and a vast share of Broadway and Tin Pan Alley was Jewish-authored. A "
        "brief nod to an outsized legacy.",
        [
            ("White Christmas (Irving Berlin, cross-link)", None),
            ("Irving Berlin & the American songbook (cross-link)", None),
            ("George Gershwin (jazz meets classical, cross-link)", None),
            ("Jewish songwriters & Broadway (the Tin Pan Alley legacy)", None),
        ],
    ),
    (
        "THE DIASPORA IN GLOBAL POP & THE NEW JEWISH MUSIC",
        "Across global pop, the diaspora thread runs deep -- cross-links, not full profiles: Leonard "
        "Cohen's 'Hallelujah', Bob Dylan, Barbra Streisand, Amy Winehouse, Serge Gainsbourg, and Drake. "
        "And a new Jewish music emerged: John Zorn's Radical Jewish Culture and klezmer-jazz, and "
        "Matisyahu's Hasidic reggae -- Jewish tradition remade for the 21st century.",
        [
            ("Hallelujah (Leonard Cohen, cross-link)", None),
            ("The diaspora in global pop (Dylan, Winehouse, Drake, cross-link)", None),
            ("John Zorn & Radical Jewish Culture (klezmer-jazz)", None),
            ("Matisyahu (the Hasidic reggae voice)", None),
            ("The new Jewish music (tradition remade)", None),
        ],
    ),
    (
        "THE JEWISH MUSIC ARC: A FINALE",
        "Four installments span a people and its song: the ancient liturgy and cantillation, the Ashkenazi "
        "Yiddish and klezmer world, the Sephardi and Mizrahi Mediterranean, and now modern Israel and a "
        "global diaspora. One sacred thread, refracted through every land the Jewish people lived in, from "
        "the shofar to global pop. This closes the Jewish-music survey. Cross-links: the US, Europe, MENA, "
        "and Central Asia -- and the whole world survey.",
        [
            ("The Jewish music arc (from the shofar to global pop)", None),
            ("One sacred thread, many lands (the diaspora genius)", None),
            ("Tradition, exile & renewal (the Jewish through-line)", None),
            ("Toward the world survey's close (roads onward)", None),
        ],
    ),
]

STEM = "jewish_music_4_MODERN_ISRAEL_DIASPORA"


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
