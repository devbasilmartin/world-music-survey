#!/usr/bin/env python3
"""Build Central Asia & the Caucasus, installment 3: The Caucasus.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Central Asian & Caucasian Music — Installment 3: "
         "The Caucasus (Georgian Polyphony, the Armenian Duduk & the Mountain Traditions)")

FRAMING = (
    "The Caucasus mountains hold some of the most singular music on Earth. GEORGIA sings in ancient "
    "three-part VOCAL POLYPHONY -- independent voices interweaving in bold, sometimes startling harmony, "
    "one of the oldest polyphonic traditions in the world, heard in Orthodox chant, the yodel-like "
    "krimanchuli of Guria, and the table songs of the feast (supra). 'Chakrulo' rode the Voyager Golden "
    "Record into space. ARMENIA's music is voiced by the DUDUK -- an apricot-wood double-reed of almost "
    "unbearable plaintive beauty (Djivan Gasparyan) -- and was saved by KOMITAS, the priest-musicologist "
    "who collected thousands of folk songs and rebuilt a national music. AZERBAIJAN adds the balaban reed "
    "and its dance music, and the shared mountains ring with the panduri and chonguri lutes and the songs "
    "of the Ossetians, Chechens, and Circassians. Content notes: Komitas witnessed the 1915 Armenian "
    "Genocide and was broken by it, and the Caucasus has known deep conflict -- all treated strictly "
    "factually, evenhandedly, and with care, as music. Cross-links: the Silk Road mugham (#2); Orthodox "
    "chant (Europe/Russia). Names transliterated. Region: the Caucasus (Georgia, Armenia, Azerbaijan & "
    "the North Caucasus)."
)

SECTIONS = [
    (
        "GEORGIAN VOCAL POLYPHONY",
        "Georgia's national treasure is its three-part vocal POLYPHONY -- three independent lines woven "
        "together, often in strikingly dissonant, powerful harmony unlike anything in Western music, and "
        "among the oldest polyphony on Earth. Sung by men's choirs a cappella, it is a UNESCO Masterpiece "
        "and the beating heart of Georgian identity.",
        [
            ("Georgian vocal polyphony (the three-part singing)", None),
            ("Chakrulo (on the Voyager Golden Record)", None),
            ("The men's choir a cappella (the Georgian sound)", None),
            ("The bold dissonant harmony (the Georgian idiom)", None),
        ],
    ),
    (
        "THE REGIONAL STYLES & THE TABLE SONG",
        "Georgian polyphony varies by region: the complex, three-voice GURIAN songs with their yodel-like "
        "KRIMANCHULI top voice; the archaic, austere SVAN songs of the high mountains; and the Kakhetian "
        "table songs with a long drone. All come alive at the SUPRA, the ritual feast where singing and "
        "toasting bind the community.",
        [
            ("Gurian song & the krimanchuli (the yodel voice)", None),
            ("Svan songs (the archaic mountain polyphony)", None),
            ("Kakhetian table songs (the long-drone style)", None),
            ("The supra (the Georgian feast & its songs)", None),
            ("Chakrulo & the Rustavi Choir (the polyphony ensemble)", "Rustavi Choir"),
        ],
    ),
    (
        "GEORGIAN SACRED CHANT & INSTRUMENTS",
        "Georgian Orthodox CHANT is itself polyphonic -- a distinct three-voice liturgical tradition, "
        "long suppressed in the Soviet era and painstakingly revived. Alongside the voice sound the "
        "panduri and chonguri lutes, the chuniri fiddle, and the duduki and salamuri pipes of village "
        "music. Cross-link: Orthodox chant of the wider region.",
        [
            ("Georgian Orthodox chant (the polyphonic liturgy)", None),
            ("Shen Khar Venakhi (the beloved Georgian hymn)", None),
            ("Panduri & chonguri (the Georgian lutes)", None),
            ("The salamuri & chuniri (the Georgian pipe & fiddle)", None),
            ("The revival of Georgian chant (post-Soviet)", None),
        ],
    ),
    (
        "THE ARMENIAN DUDUK",
        "Armenia's soul sings through the DUDUK -- a double-reed pipe of apricot wood whose warm, mournful, "
        "almost-human tone, floating over a second player's held drone (dam), is one of the most moving "
        "sounds in music. Djivan Gasparyan carried it to the world and into film scores. It is a UNESCO "
        "Masterpiece.",
        [
            ("The duduk (the Armenian apricot-wood reed)", None),
            ("Dle Yaman", "Djivan Gasparyan"),
            ("Djivan Gasparyan (the master of the duduk)", None),
            ("The duduk & its drone (the dam accompaniment)", None),
            ("The plaintive duduk tone (the Armenian voice)", None),
        ],
    ),
    (
        "KOMITAS & THE SAVING OF ARMENIAN SONG",
        "The priest, composer, and musicologist KOMITAS (Soghomon Soghomonian) collected and transcribed "
        "thousands of Armenian folk songs, rescuing a national music and founding Armenian ethnomusicology. "
        "Content note: he witnessed the 1915 Armenian Genocide, was deported, and was so traumatized that "
        "he fell silent for his last decades -- his story treated factually and with deep care.",
        [
            ("Komitas (the savior of Armenian folk song)", None),
            ("Krunk (The Crane, an Armenian song of exile)", None),
            ("Armenian folk song (the Komitas collection)", None),
            ("The sharakan (Armenian sacred chant)", None),
            ("Komitas & 1915 (the genocide & his silence, content note)", None),
        ],
    ),
    (
        "ARMENIAN INSTRUMENTS & THE DIASPORA",
        "Beyond the duduk, Armenian music rings with the kanun zither, the tar and oud lutes, the kamancha "
        "fiddle, the shvi and zurna pipes, and the dhol drum. A vast diaspora (after 1915) carried the "
        "music worldwide, from folk-dance bands to Gomidas choirs. Cross-link: the diaspora and its music.",
        [
            ("The kanun & tar (the Armenian strings)", None),
            ("The zurna & dhol (the Armenian pipe & drum)", None),
            ("The kamancha (the Armenian spike fiddle)", None),
            ("Armenian folk dance music (the diaspora bands)", None),
            ("Sayat-Nova (the great Armenian-Caucasian ashugh)", None),
        ],
    ),
    (
        "AZERBAIJANI FOLK & THE BALABAN",
        "Beside its classical mugham (#2), Azerbaijan has a rich folk world: the BALABAN (a double-reed kin "
        "to the duduk), the zurna-and-nagara pipe-and-drum of weddings and dance, the lively yalli line "
        "dances, and the mahni folk song. The tar and kamancha bind its classical and folk musics together.",
        [
            ("The balaban (the Azerbaijani double-reed)", None),
            ("Zurna & nagara (the Azerbaijani pipe & drum)", None),
            ("Yalli (the Azerbaijani line dance)", None),
            ("Azerbaijani mahni (the folk song)", None),
            ("The Azerbaijani wedding music (the dance repertoire)", None),
        ],
    ),
    (
        "THE MOUNTAIN TRADITIONS OF THE NORTH CAUCASUS",
        "The North Caucasus -- Ossetia, Chechnya, Ingushetia, Dagestan, Circassia -- rings with its own "
        "fierce, proud music: the accordion (pshine) and the lezginka, the Caucasus's electrifying fast "
        "dance, played across the whole range. Content note: this is a region of many peoples and a hard "
        "history, its music a source of identity and endurance.",
        [
            ("The lezginka (the fast Caucasus dance)", None),
            ("The Caucasian accordion (pshine & garmon)", None),
            ("Ossetian, Chechen & Circassian song", None),
            ("The Dagestani mountain music (many peoples)", None),
            ("The doli & the dance-drum of the Caucasus", None),
        ],
    ),
    (
        "THE CAUCASUS SOUND & THE ROAD AHEAD",
        "From Georgian polyphony to the Armenian duduk to the Azerbaijani balaban and the North Caucasus "
        "lezginka, the mountains hold a music of extraordinary depth -- ancient, vocal, plaintive, and "
        "fierce. From here the survey turns to the Soviet century and the modern pop present (#4, the "
        "finale). Cross-links: the Silk Road (#2); the steppe (#1); Orthodox Europe; the diaspora.",
        [
            ("The Caucasus musical world (polyphony, reed & dance)", None),
            ("The ancient voice of the mountains (the Caucasus depth)", None),
            ("Faith, feast & endurance (the Caucasus through-line)", None),
            ("Toward the Soviet century & modern pop (roads ahead)", None),
        ],
    ),
]

STEM = "casia_music_3_CAUCASUS_POLYPHONY_DUDUK"


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
