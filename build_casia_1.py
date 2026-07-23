#!/usr/bin/env python3
"""Build Central Asia & the Caucasus, installment 1: The Turkic & Steppe Roots.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Central Asian & Caucasian Music — Installment 1: "
         "The Turkic & Steppe Roots (Throat-Singing, the Horse-Head Fiddle & the Epic Bards)")

FRAMING = (
    "Across the vast grasslands from Mongolia to the Caspian sounds one of humanity's oldest and most "
    "astonishing musical worlds: the nomadic music of the STEPPE. Its miracle is THROAT-SINGING (khoomei) "
    "-- a single singer sounding two or more notes at once, whistling a flute-like overtone melody above a "
    "deep drone, an art of the Tuvans and Mongols that imitates wind, water, and animals. Beside it rides "
    "the MORIN KHUUR, the Mongolian horse-head fiddle, and the soaring URTIIN DUU 'long song'; the Kazakh "
    "DOMBRA and its virtuoso kui instrumental poems (Kurmangazy); and the Kyrgyz KOMUZ lute and the "
    "breathtaking MANASCHI -- reciters who chant the million-line Epic of Manas from memory. These are the "
    "sounds of horse cultures, shamanism, and the open sky, carried by bard-musicians (bakhshi, jyrau, "
    "akyn) across a thousand years. This installment lays the steppe foundation before the Silk Road "
    "art-musics and the Caucasus. Content note: Soviet-era suppression of shamanic and nomadic traditions "
    "and their post-1991 revival are treated factually and with respect. Names transliterated. Region: "
    "the Turkic & Mongol steppe (Mongolia, Tuva, Kazakhstan, Kyrgyzstan)."
)

SECTIONS = [
    (
        "THROAT-SINGING: TWO VOICES AT ONCE",
        "The steppe's signature marvel is KHOOMEI (overtone or 'throat' singing) -- one person producing a "
        "sustained low drone while shaping a piercing, whistle-like melody from its own overtones, so that "
        "a single voice sounds like two. Rooted in Tuva and Mongolia, it echoes the sounds of the natural "
        "world: wind, streams, and birds.",
        [
            ("Khoomei (the overtone throat-singing)", None),
            ("Two voices from one throat (the overtone marvel)", None),
            ("The drone & the whistling overtone melody", None),
            ("Sound-mimicry of nature (wind, water & birds)", None),
        ],
    ),
    (
        "THE STYLES OF KHOOMEI & THE TUVAN MASTERS",
        "Throat-singing has many styles -- the whistling SYGYT, the deep, growling KARGYRAA, and the "
        "buzzing khoomei proper -- each a different overtone technique. Tuva's Huun-Huur-Tu brought the "
        "art to the world; Yat-Kha fused it with rock; and Kongar-ool Ondar was among its great masters.",
        [
            ("Sygyt & kargyraa (the throat-singing styles)", None),
            ("Orphan's Lament", "Huun-Huur-Tu"),
            ("Huun-Huur-Tu (the Tuvan throat-singing masters)", None),
            ("Yat-Kha (Tuvan throat-singing meets rock)", None),
            ("Kongar-ool Ondar (the Tuvan master)", None),
        ],
    ),
    (
        "THE MORIN KHUUR: THE HORSE-HEAD FIDDLE",
        "The soul of Mongolian music is the MORIN KHUUR -- a two-string fiddle crowned with a carved "
        "horse's head, its bow drawn across strings of horsehair, voicing a warm, keening tone bound up "
        "with the horse and the herder's life. It carries legends and is a UNESCO-honored national "
        "treasure.",
        [
            ("Morin khuur (the Mongolian horse-head fiddle)", None),
            ("Jonon Khar (the classic morin khuur melody)", None),
            ("The horsehair bow & strings (the fiddle's voice)", None),
            ("The legend of the morin khuur (the horse & the herder)", None),
        ],
    ),
    (
        "THE MONGOLIAN LONG SONG & THE MODERN STEPPE",
        "The URTIIN DUU 'long song' stretches a handful of words across vast, ornamented, breath-defying "
        "melodic lines evoking the endless steppe, sung over the morin khuur. Today the band The HU has "
        "carried Mongolian throat-singing and fiddle into global 'hunnu rock', reaching millions.",
        [
            ("Urtiin duu (the Mongolian long song)", None),
            ("Wolf Totem", "The HU"),
            ("The endless-steppe melody (the long song's art)", None),
            ("Modern Mongolian 'hunnu rock' (the global steppe sound)", None),
            ("Tumen Ekh & the Mongolian ensemble tradition", None),
        ],
    ),
    (
        "KAZAKH MUSIC: THE DOMBRA & THE KUI",
        "Among the Kazakhs, the two-string DOMBRA lute is the national instrument, and the KUI -- a short, "
        "programmatic instrumental piece telling a story or painting a scene -- is its highest art. The "
        "19th-century master Kurmangazy composed kuis (like 'Adai') that remain the pride of Kazakh music.",
        [
            ("Dombra (the Kazakh two-string lute)", None),
            ("Adai (the great Kazakh kui)", "Kurmangazy"),
            ("The kui (the Kazakh programmatic instrumental)", None),
            ("Kurmangazy (the master of the kui)", None),
            ("The Kazakh folk orchestra (the dombra ensemble)", None),
        ],
    ),
    (
        "THE KYRGYZ KOMUZ & THE MANAS EPIC",
        "The Kyrgyz KOMUZ, a three-string fretless lute, is played with dazzling acrobatic flair. Above "
        "all, the MANASCHI are reciters who chant the Epic of Manas -- one of the longest oral epics on "
        "Earth, half a million lines and more -- entirely from memory, in a trance-like flood. It is a "
        "living wonder of world oral literature.",
        [
            ("Komuz (the Kyrgyz three-string lute)", None),
            ("The Epic of Manas (the great Kyrgyz oral epic)", None),
            ("The manaschi (the Manas reciter-bards)", None),
            ("Acrobatic komuz playing (the Kyrgyz virtuoso style)", None),
            ("The temir komuz (the Kyrgyz jew's harp)", None),
        ],
    ),
    (
        "THE BARDS OF THE STEPPE",
        "The steppe's music lived in its poet-singers: the Kazakh AKYN (who duel in improvised sung poetry, "
        "the aitys) and JYRAU (epic reciters), the Central Asian BAKHSHI, and the shaman-singers whose "
        "songs bridged the human and spirit worlds. They were the memory and conscience of nomadic society.",
        [
            ("The akyn & the aitys (the Kazakh sung-poetry duel)", None),
            ("The jyrau (the Kazakh epic bard)", None),
            ("The bakhshi (the Central Asian bard-shaman)", None),
            ("The shaman's song (the spirit-world music)", None),
            ("Improvised sung poetry (the bardic art)", None),
        ],
    ),
    (
        "THE NOMADIC SOUNDWORLD & THE SOVIET CENTURY",
        "Steppe music is inseparable from the horse, the yurt, and the open sky -- and from the jew's harp "
        "(khomus), the end-blown flutes, and animal-sound mimicry that fill it. Content note: the Soviet "
        "era suppressed shamanic and religious music and reshaped folk traditions into state ensembles; "
        "since 1991 a powerful revival has restored them. Cross-link: the Silk Road art-musics (#2).",
        [
            ("The khomus / temir komus (the steppe jew's harp)", None),
            ("The steppe flutes (sybyzgy, tsuur & the end-blown pipes)", None),
            ("Soviet suppression & the folk-ensemble era (content note)", None),
            ("The post-Soviet revival (reclaiming the nomadic sound)", None),
        ],
    ),
    (
        "THE STEPPE FOUNDATION & THE ROAD AHEAD",
        "From throat-singing and the horse-head fiddle to the dombra kui and the Manas epic, the nomadic "
        "Turkic and Mongol steppe holds one of the world's most singular musical inheritances -- a music "
        "of the open sky. From here the survey turns to the settled Silk Road art-musics (#2) and the "
        "Caucasus (#3). Cross-links: the Persianate world; Mongolia & China; the Turkic thread to Turkey.",
        [
            ("The steppe musical inheritance (the music of the open sky)", None),
            ("Nomad & city (the steppe meets the Silk Road)", None),
            ("The Turkic-Mongol thread (from Mongolia to the Caspian)", None),
            ("Toward the Silk Road & the Caucasus (roads ahead)", None),
        ],
    ),
]

STEM = "casia_music_1_TURKIC_STEPPE_THROAT_SINGING"


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
