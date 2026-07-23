#!/usr/bin/env python3
"""Build Central Asia & the Caucasus, installment 2: Persianate Art Music & the Silk Road.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Central Asian & Caucasian Music — Installment 2: "
         "Persianate Art Music & the Silk Road (Shashmaqam, the Uyghur Muqam & Azerbaijani Mugham)")

FRAMING = (
    "Where the steppe met the settled oasis cities of the Silk Road -- Bukhara, Samarkand, Kashgar, Baku "
    "-- a refined, city-based classical music grew, sharing the great modal idea (maqam / muqam / mugham) "
    "of the wider Persianate world. The Uzbek and Tajik SHASHMAQAM ('six maqams') is the courtly suite of "
    "Bukhara and Samarkand, sung to Persian and Chagatai poetry; the Uyghur ON IKKI MUQAM ('twelve "
    "muqam') is a vast, day-long cycle of song, dance, and instrumental music from Xinjiang; and "
    "Azerbaijani MUGHAM is a soaring improvised modal art crowned by singers like Alim Qasimov, beside the "
    "ASHIQ bard-minstrels who sing to the saz. All of it rides a family of long-necked lutes and spike "
    "fiddles -- the DUTAR, TANBUR, TAR, RUBAB, ghijak, and the doira frame drum. This installment covers "
    "the Silk Road art-musics between the steppe (#1) and the Caucasus (#3). Content notes: the Bukharan "
    "Jewish role in shashmaqam (cross-link: the Jewish-diaspora survey) and the situation of Uyghur "
    "culture in Xinjiang are treated factually and with care. Cross-links: the Persian dastgah & Turkish "
    "makam (MENA survey). Names transliterated. Region: the oasis Silk Road (Uzbekistan, Tajikistan, "
    "Xinjiang/Uyghur, Azerbaijan, Turkmenistan)."
)

SECTIONS = [
    (
        "THE MODAL IDEA: MAQAM ACROSS THE SILK ROAD",
        "The settled musics of Central Asia share the great modal system of the Islamic world -- the "
        "maqam (muqam, mugham) -- a family of melodic modes, each an emotional and structural world, "
        "elaborated in suites of song and instrumental pieces. It links Bukhara to Kashgar to Baku, and "
        "onward to Persia and the Arab world.",
        [
            ("The maqam / muqam / mugham (the Silk Road modal system)", None),
            ("The modal suite (song & instrumental cycle)", None),
            ("The Persianate musical world (the shared inheritance)", None),
            ("Sung classical poetry (the maqam's texts)", None),
        ],
    ),
    (
        "UZBEK & TAJIK SHASHMAQAM",
        "The SHASHMAQAM -- the 'six maqams' of Bukhara and Samarkand -- is the classical crown of Uzbek "
        "and Tajik music: a courtly cycle of vocal and instrumental movements set to Persian and Chagatai "
        "Sufi and love poetry. Content note: the Bukharan Jewish community were historically central to "
        "its transmission (cross-link: the Jewish-diaspora survey).",
        [
            ("Shashmaqam (the six-maqam suite of Bukhara)", None),
            ("The Bukhara-Samarkand court tradition", None),
            ("Bukharan Jewish musicians & the shashmaqam (cross-link)", None),
            ("Sufi & love poetry in the shashmaqam", None),
            ("Munojot (the classic shashmaqam song)", "Munojat Yulchieva"),
        ],
    ),
    (
        "THE UYGHUR ON IKKI MUQAM",
        "The Uyghur ON IKKI MUQAM ('twelve muqam') of Xinjiang is one of the world's grandest musical "
        "structures -- twelve vast suites, each blending sung poetry, dance rhythms, and instrumental "
        "sections into hours of music. Content note: it is a treasured heritage of the Uyghur people, "
        "whose cultural situation in Xinjiang is treated factually and with care.",
        [
            ("On ikki muqam (the Uyghur twelve muqam)", None),
            ("The Uyghur muqam suite (song, dance & instrumental)", None),
            ("The Twelve Muqam ensemble (the Xinjiang tradition)", None),
            ("Uyghur sung poetry & the muqam (the heritage)", None),
            ("The dolan muqam (the Tarim folk muqam)", None),
        ],
    ),
    (
        "AZERBAIJANI MUGHAM",
        "Azerbaijan's MUGHAM is a soaring, deeply expressive improvised modal art -- a vocalist ornamenting "
        "classical poetry over the tar and kamancha, rising through emotional peaks. A UNESCO treasure, it "
        "reached new heights with the master Alim Qasimov, one of the great living voices, and blends with "
        "jazz in the modern 'mugham-jazz'.",
        [
            ("Mugham (the Azerbaijani improvised modal art)", None),
            ("Segah (the classic Azerbaijani mugham mode)", "Alim Qasimov"),
            ("Alim Qasimov (the master of mugham)", None),
            ("The tar & kamancha in mugham (the accompaniment)", None),
            ("Mugham-jazz (the modern Azerbaijani fusion)", None),
        ],
    ),
    (
        "THE ASHIQ & THE BARD-MINSTREL",
        "Across Azerbaijan, Turkey, and Turkmen and Turkic lands sings the ASHIQ (ashug/ashyk) -- a "
        "travelling bard-minstrel who accompanies epic tales, love songs, and improvised verse duels on "
        "the long-necked SAZ lute. It is a UNESCO-recognized art of the sung word, kin to the steppe bards "
        "of #1. Cross-link: the Turkish asik (MENA survey).",
        [
            ("The ashiq (the Azerbaijani bard-minstrel)", None),
            ("The saz (the ashiq's long-necked lute)", None),
            ("The dastan (the epic tale in song)", None),
            ("The ashiq verse-duel (the improvised contest)", None),
            ("Ashiq Alesker (the great ashiq master)", None),
        ],
    ),
    (
        "TURKMEN BAGSHY & THE DUTAR",
        "Turkmen music centers on the BAGSHY -- a bard-singer who performs epic and lyric song in a "
        "distinctive strained, ornamented voice, accompanying himself on the two-string DUTAR, sometimes "
        "with the gyjak spike fiddle. The dutar's art (dutarchylyk) and the bagshy's song are the heart of "
        "Turkmen tradition.",
        [
            ("The bagshy (the Turkmen bard-singer)", None),
            ("Dutarchylyk (the Turkmen dutar art)", None),
            ("The Turkmen dutar & gyjak (the accompaniment)", None),
            ("The Turkmen epic song (the bagshy repertoire)", None),
        ],
    ),
    (
        "THE INSTRUMENTS OF THE SILK ROAD",
        "The settled Central Asian sound rides a great family of instruments: the long-necked lutes DUTAR "
        "(two strings), TANBUR, TAR, and the Afghan-Uzbek RUBAB; the spike fiddles ghijak and kamancha; "
        "the santur hammered dulcimer; the ney flute; and the DOIRA frame drum that drives the rhythm. "
        "Cross-link: the Persian and Turkish instruments (MENA).",
        [
            ("Dutar (the two-string Central Asian lute)", None),
            ("Tanbur & tar (the long-necked Silk Road lutes)", None),
            ("Rubab (the Afghan-Central Asian lute)", None),
            ("Ghijak & kamancha (the spike fiddles)", None),
            ("Doira (the Central Asian frame drum)", None),
        ],
    ),
    (
        "THE SILK ROAD REVIVAL",
        "After Soviet secularization, the Silk Road classical traditions have been revived and carried to "
        "the world -- by the Aga Khan Music Programme, Yo-Yo Ma's Silk Road Ensemble, and master "
        "performers touring globally. The academies of Tashkent, Baku, and beyond keep the maqam and "
        "mugham alive for new generations.",
        [
            ("The Aga Khan Music Programme (the Silk Road revival)", None),
            ("The Silk Road Ensemble (the global collaboration)", None),
            ("The maqam academies (Tashkent & Baku)", None),
            ("Central Asian classical music today (the living tradition)", None),
        ],
    ),
    (
        "THE SILK ROAD SOUND & THE ROAD AHEAD",
        "From shashmaqam to the Uyghur muqam to Azerbaijani mugham, the settled Silk Road built a refined "
        "classical world on the shared modal idea, sung to great poetry over the dutar and tar. From here "
        "the survey turns to the Caucasus (#3) and the Soviet-and-modern era (#4). Cross-links: the steppe "
        "(#1); Persia, Turkey & the Arab maqam (MENA); the Jewish diaspora (shashmaqam).",
        [
            ("The Silk Road classical world (the shared modal art)", None),
            ("Poetry, the lute & the mode (the Persianate sound)", None),
            ("The oasis city & its music (Bukhara to Baku)", None),
            ("Toward the Caucasus & the modern era (roads ahead)", None),
        ],
    ),
]

STEM = "casia_music_2_SILK_ROAD_MAQAM_MUGHAM"


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
