#!/usr/bin/env python3
"""Build the Jewish Diaspora, installment 1: The Liturgical & Ancient Roots.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Jewish Music — Installment 1: "
         "The Liturgical & Ancient Roots (Cantillation, the Cantor, Nusach & the Sacred Song)")

FRAMING = (
    "Jewish music is a vast, cross-regional family united not by one sound but by a shared sacred core -- "
    "the sung word of prayer and Torah, carried for millennia and refracted through every land the Jewish "
    "people lived in. Its oldest layer is TORAH CANTILLATION: the chanted reading of scripture, guided by "
    "the TE'AMIM (trope) signs, a musical grammar older than notation. Around it grew the art of the HAZZAN "
    "(cantor) and CHAZZANUT -- the soaring, ornamented prayer-leading that reached a golden age with voices "
    "like Yossele Rosenblatt -- sung in the modal NUSACH of the liturgy and its distinctive synagogue "
    "modes (the Ahavah Rabbah steiger, the 'Jewish scale'). The SHOFAR sounds the High Holy Days; PIYYUT "
    "(sacred poetry) is sung differently in every community; ZEMIROT grace the Sabbath table; and the "
    "wordless NIGUN carries prayer beyond words. This installment lays the sacred foundation shared across "
    "the three great branches -- Ashkenazi, Sephardi, and Mizrahi -- before their distinct musical worlds "
    "(#2-3) and the modern era (#4). Content note: this is a living, sacred religious tradition, treated "
    "with deep respect. Names transliterated. Cross-links: the branches (#2-4); MENA & Central Asia."
)

SECTIONS = [
    (
        "TORAH CANTILLATION & THE TE'AMIM",
        "The oldest layer of Jewish music is the chanted reading of scripture -- TORAH CANTILLATION -- "
        "guided by the TE'AMIM (also called trope or ta'amei ha-mikra), a system of signs marking the "
        "melody, phrasing, and accent of every verse. A musical grammar passed down for well over a "
        "thousand years, it differs by community but shares one ancient root.",
        [
            ("Torah cantillation (the chanted scripture)", None),
            ("The te'amim / trope (the cantillation signs)", None),
            ("The chant of the Torah reading (the oldest layer)", None),
            ("Cantillation of the Prophets & the Megillot", None),
        ],
    ),
    (
        "THE HAZZAN & THE ART OF CHAZZANUT",
        "The HAZZAN (cantor) leads the congregation in prayer, and CHAZZANUT is the high art of that "
        "leading -- ornamented, emotional, virtuosic vocal prayer that pours the heart out to God. Its "
        "golden age (early 20th century) produced legendary voices, above all Yossele Rosenblatt, whose "
        "recordings still astonish.",
        [
            ("Chazzanut (the art of the cantor)", None),
            ("Yossele Rosenblatt (the legendary cantor)", None),
            ("The hazzan (the prayer-leader)", None),
            ("The golden age of the cantors", None),
            ("Ornamented vocal prayer (the cantorial art)", None),
        ],
    ),
    (
        "NUSACH & THE SYNAGOGUE MODES",
        "Jewish prayer is chanted in NUSACH -- the traditional modal melody that changes with the service, "
        "the day, and the season, so that a trained ear can hear the calendar in the music. It moves "
        "through distinctive synagogue modes (steiger), above all the AHAVAH RABBAH, the augmented-second "
        "mode often called 'the Jewish scale'.",
        [
            ("Nusach (the modal prayer chant)", None),
            ("Ahavah Rabbah (the Jewish-scale synagogue mode)", None),
            ("The synagogue modes / steiger", None),
            ("The nusach of the seasons (the sung calendar)", None),
            ("Magen Avot & Adonai Malach (the prayer modes)", None),
        ],
    ),
    (
        "THE SHOFAR & THE HIGH HOLY DAYS",
        "The SHOFAR -- a ram's horn -- is the most ancient Jewish instrument, sounded on Rosh Hashanah and "
        "at the close of Yom Kippur in its piercing calls (tekiah, shevarim, teruah). It is the raw, "
        "wordless voice of the High Holy Days, and the sound of awe and repentance. Content note: a sacred "
        "ritual instrument.",
        [
            ("The shofar (the ram's-horn)", None),
            ("Tekiah, shevarim & teruah (the shofar calls)", None),
            ("The High Holy Days sound (Rosh Hashanah & Yom Kippur)", None),
            ("Kol Nidre (the Yom Kippur prayer)", None),
        ],
    ),
    (
        "PIYYUT: THE SACRED POETRY IN SONG",
        "PIYYUT -- liturgical poetry sung within or alongside the prayers -- is one of the great shared "
        "yet diverse Jewish arts: the same beloved poems (like 'Adon Olam', 'Yigdal', or 'Lecha Dodi') are "
        "sung to utterly different melodies in every community, from Ashkenaz to Baghdad to Morocco. It is "
        "a living meeting of word and local song.",
        [
            ("Piyyut (the sung liturgical poetry)", None),
            ("Adon Olam (the beloved piyyut, sung many ways)", None),
            ("Lecha Dodi (the Sabbath-welcoming poem)", None),
            ("Yigdal & Ein Keloheinu (the sung prayers)", None),
            ("One poem, many melodies (the piyyut tradition)", None),
        ],
    ),
    (
        "THE PSALMS & THE ANCIENT TEMPLE",
        "The Book of PSALMS (Tehillim) is the ancient songbook of Jewish worship, once sung by the Levite "
        "choirs and orchestras of the Temple in Jerusalem. Though the Temple's music was lost with its "
        "destruction, the Psalms sing on through all Jewish liturgy, from Hallel to Kabbalat Shabbat. "
        "Content note: the Temple tradition is remembered through scripture.",
        [
            ("The Psalms / Tehillim (the ancient songbook)", None),
            ("Hallel (the psalms of praise)", None),
            ("The Levite Temple music (the remembered tradition)", None),
            ("Psalm 137 (By the Rivers of Babylon, the exile song)", None),
            ("The chanted psalm (the liturgical core)", None),
        ],
    ),
    (
        "ZEMIROT & THE SABBATH TABLE",
        "Beyond the synagogue, song fills the Jewish home -- above all the ZEMIROT, the melodies sung "
        "around the Sabbath and festival table (like 'Shalom Aleichem' welcoming the Sabbath angels, and "
        "'Yah Ribon'). These table songs, warm and communal, carry the sacred into daily family life "
        "across every Jewish community.",
        [
            ("Zemirot (the Sabbath table songs)", None),
            ("Shalom Aleichem (welcoming the Sabbath)", None),
            ("Yah Ribon (the Sabbath-table hymn)", None),
            ("The Sabbath home song (the family table)", None),
            ("Birkat Hamazon & the sung grace", None),
        ],
    ),
    (
        "THE NIGUN: PRAYER BEYOND WORDS",
        "The NIGUN is a wordless melody -- sung on syllables like 'bim-bim-bam' or 'ya-ba-bam' -- through "
        "which, especially in Hasidic practice, the soul reaches toward God beyond the limits of language. "
        "A deveykut (cleaving) in pure melody, repeated and built to ecstasy, it is one of Judaism's most "
        "profound musical ideas. Cross-link: the Hasidic world (#2).",
        [
            ("The nigun (the wordless Hasidic melody)", None),
            ("Deveykut in melody (prayer beyond words)", None),
            ("The Hasidic nigun (the ecstatic wordless song)", None),
            ("The repeated melody & the rise to ecstasy", None),
        ],
    ),
    (
        "THE SACRED THREAD & THE ROAD AHEAD",
        "From Torah cantillation and the shofar to chazzanut, nusach, piyyut, and the nigun, a shared "
        "sacred core binds Jewish music across the world -- yet each community clothed it in the sound of "
        "its own land. From this liturgical foundation the survey turns to the distinct musical worlds of "
        "the Ashkenazi (#2), the Sephardi and Mizrahi (#3), and the modern era (#4). Cross-links: MENA; "
        "Central Asia; Europe; the US.",
        [
            ("The shared sacred core (the Jewish musical thread)", None),
            ("One faith, many local sounds (the diaspora principle)", None),
            ("The word, the mode & the melody (the liturgical roots)", None),
            ("Toward the branches & the modern era (roads ahead)", None),
        ],
    ),
]

STEM = "jewish_music_1_LITURGICAL_ROOTS"


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
