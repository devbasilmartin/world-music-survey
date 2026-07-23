#!/usr/bin/env python3
"""Build Central Asia & the Caucasus, installment 4 (FINALE): The Soviet Century & the Modern Present.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Central Asian & Caucasian Music — Installment 4 (Finale): "
         "The Soviet Century & the Modern Present")

FRAMING = (
    "The final chapter carries the whole region -- steppe, Silk Road, and Caucasus -- through the Soviet "
    "century into a globalized present. For seventy years the USSR reshaped this music: it built "
    "conservatories and recorded folklore, but also imposed Russification, suppressed religious and "
    "shamanic music, and turned living traditions into polished STATE FOLK ENSEMBLES and ESTRADA (Soviet "
    "pop). After 1991, the newly independent nations reclaimed and modernized their music. Today the "
    "region has global stars: the astonishing Kazakh vocal phenomenon DIMASH Kudaibergen, the Q-POP wave "
    "(Ninety One), Uzbek and Azerbaijani pop, and a diaspora that gave the world System of a Down and "
    "Katie Melua. And a powerful FOLK-FUSION movement reinvents throat-singing, mugham, the duduk, and "
    "polyphony for the 21st century. This closes the Central Asia & Caucasus survey. Content notes: Soviet "
    "cultural policy and post-Soviet conflicts are treated factually and evenhandedly. Cross-links: the "
    "steppe (#1), the Silk Road (#2), the Caucasus (#3); Russia/Europe; the Jewish diaspora. Names "
    "transliterated. Region: the modern post-Soviet Central Asia & Caucasus."
)

SECTIONS = [
    (
        "THE SOVIET CENTURY: ESTRADA & THE STATE ENSEMBLE",
        "Under the USSR, the region's music was institutionalized. ESTRADA -- the official Soviet pop of "
        "orchestras and crooners -- spread a shared sound from Baku to Tashkent, while STATE FOLK "
        "ENSEMBLES arranged nomadic and classical traditions for the concert stage. Content note: this "
        "brought conservatories and recording, but also Russification and the suppression of religious "
        "music.",
        [
            ("Soviet estrada (the official Soviet pop)", None),
            ("The state folk ensemble (folklore for the stage)", None),
            ("Soviet cultural policy & the music (content note)", None),
            ("The conservatory & the recorded tradition", None),
        ],
    ),
    (
        "THE VIA ERA & SOVIET-EASTERN POP",
        "The Soviet 1970s-80s brought the VIA (vocal-instrumental ensemble) -- state-approved pop-rock "
        "bands -- and a wave of Eastern-flavored Soviet pop. Uzbekistan's Yalla ('Uchquduq') blended "
        "local melody with the era's synths, and stars sang across the whole Union in a shared "
        "Soviet-pop idiom.",
        [
            ("Uchquduq (the Uzbek-Soviet pop classic)", "Yalla"),
            ("The VIA (the Soviet vocal-instrumental ensemble)", None),
            ("Eastern-flavored Soviet pop (the regional sound)", None),
            ("Yalla (the Uzbek Soviet-era band)", None),
        ],
    ),
    (
        "POST-1991: THE AWAKENING & THE ROCK SCENE",
        "Independence in 1991 unleashed a reclaiming of national music and a rock and alternative scene "
        "across the region. Kazakhstan, Azerbaijan, Georgia, and Armenia built new pop industries, and "
        "bands fused Western rock with local roots as the states rediscovered their own traditions.",
        [
            ("The post-Soviet musical awakening (reclaiming the roots)", None),
            ("The Central Asian rock scene (the independence era)", None),
            ("National music revival (the newly independent states)", None),
            ("Rock meets local roots (the post-1991 fusion)", None),
        ],
    ),
    (
        "DIMASH & THE KAZAKH GLOBAL VOICE",
        "Kazakhstan gave the world DIMASH Kudaibergen -- a singer of extraordinary range (across several "
        "octaves) who fuses opera, pop, and Kazakh tradition, and became an international sensation, "
        "especially in China and beyond. He is the region's biggest modern global star and a symbol of "
        "its new confidence.",
        [
            ("SOS d'un terrien en detresse (Dimash's showcase)", "Dimash Kudaibergen"),
            ("Daididau (Dimash sings the Kazakh classic)", "Dimash Kudaibergen"),
            ("Dimash Kudaibergen (the Kazakh global vocal phenomenon)", None),
            ("The multi-octave voice (the Dimash sensation)", None),
        ],
    ),
    (
        "Q-POP & THE MODERN CENTRAL ASIAN POP WAVE",
        "A K-pop-inspired Q-POP wave arose in Kazakhstan, led by the boy band Ninety One, whose modern "
        "look sparked both fandom and controversy in a conservative society. Across the region, Uzbek pop "
        "(Yulduz Usmanova, the 'nightingale of Uzbekistan'), Tajik and Turkmen pop, and a booming "
        "youth-pop scene took hold. Content note: Q-pop faced conservative backlash, noted factually.",
        [
            ("Aiyptama (the Q-pop breakthrough)", "Ninety One"),
            ("Q-pop (the Kazakh modern pop wave)", None),
            ("Ninety One (the Kazakh Q-pop pioneers)", None),
            ("Alqissa", "Yulduz Usmanova"),
            ("Yulduz Usmanova (the star of Uzbek pop)", None),
        ],
    ),
    (
        "AZERBAIJAN, EUROVISION & THE CAUCASUS POP",
        "Azerbaijan won the Eurovision Song Contest in 2011 ('Running Scared', Ell & Nikki) and hosted it, "
        "and the Caucasus built lively modern pop scenes -- Azerbaijani, Georgian, and Armenian pop and "
        "R&B -- often blending Western production with mugham melisma, the duduk, or polyphony. Cross-link: "
        "Eurovision (Europe survey).",
        [
            ("Running Scared (Azerbaijan's Eurovision win)", "Ell & Nikki"),
            ("Azerbaijani modern pop (mugham meets Western pop)", None),
            ("Georgian modern pop & R&B (the Tbilisi scene)", None),
            ("Armenian modern pop (the Yerevan sound)", None),
            ("Caucasus pop & Eurovision (the regional stage)", None),
        ],
    ),
    (
        "THE DIASPORA GOES GLOBAL",
        "The region's diaspora reached the world's biggest stages. The Armenian-American band System of a "
        "Down became global rock stars (and sang of the 1915 genocide), the Georgian-British Katie Melua "
        "sold millions, and Armenian, Georgian, and Central Asian artists abroad carried the music global. "
        "Cross-links: the US and Europe surveys; the Jewish diaspora.",
        [
            ("Chop Suey!", "System of a Down"),
            ("Nine Million Bicycles", "Katie Melua"),
            ("System of a Down (the Armenian-American rock giants)", None),
            ("The Caucasus & Central Asian diaspora (global artists)", None),
            ("Diaspora music & memory (identity abroad)", None),
        ],
    ),
    (
        "THE FOLK-FUSION REINVENTION",
        "A vibrant folk-fusion movement reinvents the region's deep roots for the 21st century: modern "
        "throat-singing crossovers (The HU's global metal, cross-link #1), mugham-jazz and electronic "
        "duduk, ethno-electronica, and world-touring ensembles blending the dutar, morin khuur, and "
        "polyphony with global sounds. The ancient traditions live and travel.",
        [
            ("Modern throat-singing fusion (the global crossover)", None),
            ("Mugham-jazz & electronic duduk (the Caucasus fusion)", None),
            ("Central Asian ethno-electronica (the modern reinvention)", None),
            ("World-touring folk ensembles (the roots go global)", None),
        ],
    ),
    (
        "THE CENTRAL ASIA & CAUCASUS ARC: A FINALE",
        "Four installments span a vast crossroads: the throat-singing and epic bards of the steppe, the "
        "maqam and mugham of the Silk Road cities, the polyphony and duduk of the Caucasus, and now a "
        "post-Soviet, globalized present. From the open sky to the global stage, this is a region where "
        "the most ancient musics and the newest pop live side by side. This closes the survey. "
        "Cross-links: Russia/Europe; the Jewish diaspora; the Pacific ahead.",
        [
            ("The Central Asia & Caucasus arc (steppe to global stage)", None),
            ("Ancient roots & new pop side by side (the region's genius)", None),
            ("A crossroads of empires & peoples (the shared story)", None),
            ("Toward the surveys ahead (roads onward)", None),
        ],
    ),
]

STEM = "casia_music_4_SOVIET_MODERN_POP"


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
