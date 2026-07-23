#!/usr/bin/env python3
"""Build MENA, installment 6 (FINAL): Modern Pan-Arab Pop, Mizrahi & the Region Today.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Middle Eastern & North African Music — Installment 6 (Finale): "
         "Modern Pan-Arab Pop, Mizrahi & the Region Today (c. 1990-present)")

FRAMING = (
    "The final chapter carries the region from the golden-age divas into a satellite-and-streaming "
    "present. Satellite TV and the Rotana video-clip industry replaced Cairo's monopoly with a "
    "PAN-ARAB pop market: AMR DIAB fused Arab melody with Mediterranean pop into mega-hits ('Nour El "
    "Ain'), and a glossy Lebanese machine (Nancy Ajram, Elissa) and Iraq's poetic KADIM AL SAHIR ruled "
    "the airwaves. Meanwhile a MIZRAHI wave -- the Middle Eastern Jewish music long marginalized in "
    "Israel -- rose to the mainstream, from Ofra Haza's global 'Im Nin'alu' to A-WA's 'Habib Galbi'. "
    "The 2011 ARAB SPRING turned rap into revolution (El General, Ramy Essam); PALESTINIAN artists (DAM, "
    "Mohammed Assaf) sang identity; and a raw digital underground -- Egyptian MAHRAGANAT street electro, "
    "Omar Souleyman's dabke, Mashrou' Leila's alt-rock -- redefined the sound. This installment closes "
    "the MENA survey. Cross-links: the maqam/golden-age roots (#1-2); the Jewish-diaspora survey "
    "(Mizrahi); the Maghreb-in-France rap (#5). Content notes: the Arab Spring, regional conflicts, and "
    "the Palestinian and Israeli-Mizrahi material are presented factually, evenhandedly, and with care "
    "-- as music. Names transliterated. Region: the Arab world, Israel/Mizrahi & the wider MENA."
)

SECTIONS = [
    (
        "THE SATELLITE ERA & PAN-ARAB POP (c. 1990-2010)",
        "Satellite television and the video clip shattered Cairo's old monopoly and created a single "
        "PAN-ARAB pop market from Morocco to the Gulf. The Saudi-owned Rotana and rival channels turned "
        "singers into glossy, region-wide superstars, and Egyptian 'al-jeel' pop modernized the sound "
        "for a new generation.",
        [
            ("Pan-Arab satellite pop (the video-clip era)", None),
            ("Rotana & the Arab music-video industry", None),
            ("Al-jeel (the modern Egyptian pop generation)", None),
            ("The pan-Arab superstar (region-wide fame)", None),
        ],
    ),
    (
        "AMR DIAB & THE MEDITERRANEAN SOUND (c. 1992-present)",
        "Amr Diab became the best-selling Arab artist of the modern era by fusing Arab melody with "
        "Mediterranean and Western pop. 'Nour El Ain' (1996) was a pan-Arab and international sensation, "
        "and 'Tamally Maak' cemented his reign. He is the defining Arab pop star of the age.",
        [
            ("Nour El Ain (Habibi Ya Nour El Ain)", "Amr Diab"),
            ("Tamally Maak (Always With You)", "Amr Diab"),
            ("Amr Diab (the father of Mediterranean-Arab pop)", None),
            ("Arab melody meets Mediterranean pop (the Diab sound)", None),
        ],
    ),
    (
        "THE LEBANESE POP MACHINE (c. 1998-present)",
        "Beirut became the glamour capital of Arab pop. Nancy Ajram's playful hits ('Ah W Noss'), "
        "Elissa's romantic ballads ('Aaishalak'), and the video-clip stardom of Haifa Wehbe and Nawal "
        "Al Zoghbi filled the satellite channels with a polished, cosmopolitan sound.",
        [
            ("Ah W Noss (Yes and a Half)", "Nancy Ajram"),
            ("Aaishalak (I Live For You)", "Elissa"),
            ("Nancy Ajram (the Lebanese pop star)", None),
            ("Haifa Wehbe & Nawal Al Zoghbi (the video-clip era)", None),
            ("Beirut, the capital of Arab pop", None),
        ],
    ),
    (
        "KADIM AL SAHIR & THE ART-POP OF THE MASHRIQ",
        "Not all modern pop was lightweight. Iraq's Kadim Al Sahir -- the 'Caesar of Arabic song' -- "
        "married sophisticated composition and the poetry of Nizar Qabbani to popular appeal ('Zidini "
        "Ishqan'), keeping the classical soul alive in the pop age, alongside the Gulf's khaleeji "
        "styles.",
        [
            ("Zidini Ishqan (Give Me More Passion)", "Kadim Al Sahir"),
            ("Kadim Al Sahir (the Caesar of Arabic song)", None),
            ("Nizar Qabbani's poetry in song (the art-pop link)", None),
            ("Khaleeji (the Gulf popular styles)", None),
        ],
    ),
    (
        "MIZRAHI & ISRAELI MUSIC (c. 1980-present)",
        "The Mizrahi music of Middle Eastern and North African Jews -- long marginalized in Israel -- "
        "rose to dominate its mainstream. The Yemenite-Israeli Ofra Haza turned Yemenite Jewish "
        "liturgy into the global hit 'Im Nin'alu'; Zohar Argov was the genre's tragic king; and the "
        "sisters A-WA revived Yemenite song as 'Habib Galbi'. Cross-link: the Jewish-diaspora survey.",
        [
            ("Im Nin'alu", "Ofra Haza"),
            ("Ha'Perach Begani (The Flower in My Garden)", "Zohar Argov"),
            ("Habib Galbi", "A-WA"),
            ("Mizrahi music (from the margins to the mainstream)", None),
            ("Yemenite Jewish song (the Mizrahi roots)", None),
        ],
    ),
    (
        "ARABIC HIP-HOP & THE ARAB SPRING (c. 2010-2013)",
        "When the 2011 uprisings swept the Arab world, its youth had a soundtrack. In Tunisia El "
        "General's 'Rais Lebled' became a revolutionary anthem; in Cairo's Tahrir Square, Ramy Essam's "
        "'Irhal' (Leave) rallied the crowds. Content note: this was music amid upheaval, and some "
        "artists were imprisoned or tortured -- kept factual and with care.",
        [
            ("Rais Lebled (Head of State)", "El General"),
            ("Irhal (Leave)", "Ramy Essam"),
            ("Arabic hip-hop (the youth voice)", None),
            ("The Arab Spring soundtrack (music & the 2011 uprisings)", None),
            ("The revolutionary song (protest & its cost)", None),
        ],
    ),
    (
        "PALESTINIAN MUSIC",
        "Palestinian musicians have long sung identity and endurance. The group DAM pioneered Palestinian "
        "hip-hop; Le Trio Joubran turned the oud into chamber art; and Gaza's Mohammed Assaf won Arab "
        "Idol in 2013, his 'Dammi Falastini' an anthem of belonging. Content note: this music carries a "
        "long, painful history, kept factual and with care.",
        [
            ("Dammi Falastini (My Blood Is Palestinian)", "Mohammed Assaf"),
            ("DAM (the Palestinian hip-hop pioneers)", None),
            ("Le Trio Joubran (the oud brothers)", None),
            ("Rim Banna & the Palestinian song of identity", None),
            ("Mohammed Assaf & Arab Idol (2013)", None),
        ],
    ),
    (
        "THE ELECTRONIC & UNDERGROUND SCENE (c. 2010-present)",
        "A raw digital underground reshaped the sound. Egypt's MAHRAGANAT -- Auto-Tuned electro-shaabi "
        "from Cairo's streets -- became the country's real pop (and was periodically banned); Syria's "
        "Omar Souleyman took dabke to global festivals; and Lebanon's Mashrou' Leila brought bold "
        "alt-rock. The region now streams and raves on its own terms. Content note: state and syndicate "
        "restrictions on mahraganat and controversy around Mashrou' Leila are noted.",
        [
            ("Mahraganat (the Egyptian street electro-shaabi)", None),
            ("Omar Souleyman (Syrian dabke goes global)", None),
            ("Mashrou' Leila (the Lebanese alt-rock band)", None),
            ("Acid Arab & the MENA electronic scene", None),
            ("The digital underground (streaming & festivals)", None),
        ],
    ),
    (
        "THE THROUGH-LINE: THE MUSIC OF A REGION",
        "Six installments span a vast, interlocking world: the Arab maqam and the Egyptian golden age, "
        "the Persian dastgah, the Turkish makam, the Maghreb's rai and Gnawa, and now a pan-Arab, "
        "Mizrahi, and digital present. From the maqam to the mahragan, a shared modal soul, a love of "
        "the sung poem, and a genius for the diva unite it all. This closes the MENA survey. Cross-links: "
        "the Jewish diaspora; sub-Saharan Africa; Southeast Asia ahead.",
        [
            ("From the maqam to the mahragan (the MENA arc)", None),
            ("The shared modal soul (Arab, Persian, Turkish, Berber)", None),
            ("The diva & the sung poem (the region's genius)", None),
            ("MENA & the world (diaspora, exile & the digital age)", None),
        ],
    ),
]

STEM = "mena_music_6_MODERN_PANARAB_MIZRAHI_TODAY"


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
