#!/usr/bin/env python3
"""Build East Asia: Japan, installment 1: Classical & Traditional Roots.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/romaji only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Japanese Music — Installment 1: "
         "Classical & Traditional Roots (the deep tradition)")

FRAMING = (
    "Japanese traditional music is an art of space, restraint, and exquisite timbre -- shaped by an "
    "aesthetic that prizes MA (the charged silence between sounds), wabi-sabi (beauty in imperfection "
    "and transience), and YUGEN (mysterious depth). At its most ancient sits GAGAKU, the imperial court "
    "orchestra, arguably the world's oldest continuously performed orchestral music (over 1,300 years). "
    "Around it grew a world of subtle instruments -- the KOTO zither, the breathy SHAKUHACHI bamboo "
    "flute (a Zen discipline in itself), the SHAMISEN three-string lute, the narrative BIWA, and the "
    "thunderous TAIKO drums; the three great theaters, NOH, KABUKI, and BUNRAKU, each with its own "
    "music; Buddhist SHOMYO chant and Shinto ritual; and a vast MIN'YO folk-song tradition, with "
    "Okinawa's sanshin music a distinct southern branch. This installment lays the pre-modern "
    "foundation before the Meiji Westernization and the pop century to come. Cross-links: the pentatonic "
    "and silk-string world shared with China and Korea (the East Asia surveys); the shamisen's Chinese/"
    "Okinawan origins; and the Japanese aesthetic's later influence on global ambient and minimalist "
    "music. Names are transliterated (romaji); (Traditional) marks forms, instruments, or pieces to seed "
    "listening. Region: Japan."
)

SECTIONS = [
    (
        "GAGAKU: THE ANCIENT COURT MUSIC",
        "Gagaku ('elegant music') is the music of the imperial court, performed almost unchanged for "
        "over a millennium -- a serene, otherworldly sound built on the reedy cluster-chords of the sho "
        "mouth-organ, the piercing hichiriki oboe, and the ryuteki flute. Its most famous piece is "
        "'Etenraku'; the bugaku court dances move to it. It may be the oldest orchestral music on Earth.",
        [
            ("Etenraku (the famous gagaku piece)", None),
            ("Gagaku (the ancient imperial court orchestra)", None),
            ("Sho, hichiriki & ryuteki (the gagaku winds)", None),
            ("Bugaku (the gagaku court dance)", None),
            ("Togaku & Komagaku (the gagaku repertoires)", None),
        ],
    ),
    (
        "SHOMYO & SACRED SOUND",
        "Sacred music runs deep. Buddhist SHOMYO -- the melismatic chant of the sutras, brought from "
        "China and India -- shaped the melodic sense of much later Japanese music; and Shinto ritual "
        "fills the shrines with kagura dance-music and the festive drums and flutes of the matsuri. Both "
        "treat sound as a bridge to the sacred.",
        [
            ("Shomyo (Japanese Buddhist chant)", None),
            ("Kagura (Shinto shrine dance-music)", None),
            ("Matsuri music (the festival drums & flutes)", None),
            ("The sacred in Japanese sound (chant & ritual)", None),
        ],
    ),
    (
        "THE KOTO & THE SO TRADITION",
        "The KOTO -- a long 13-string zither plucked with ivory picks -- is Japan's classical "
        "chamber-music heart. The blind master Yatsuhashi Kengyo shaped its solo art in the 17th century "
        "('Rokudan no Shirabe'), and centuries later Michio Miyagi's 'Haru no Umi' (The Sea in Spring, "
        "1929) became an eternal New Year sound. Its repertoire (sokyoku) often joins voice and "
        "shamisen (jiuta).",
        [
            ("Rokudan no Shirabe", "Yatsuhashi Kengyo"),
            ("Haru no Umi (The Sea in Spring)", "Michio Miyagi"),
            ("Koto (the 13-string zither)", None),
            ("Sokyoku & jiuta (the koto chamber repertoire)", None),
            ("Chidori no Kyoku (a classic koto piece)", None),
        ],
    ),
    (
        "THE SHAKUHACHI: ZEN & BREATH",
        "The SHAKUHACHI, an end-blown bamboo flute, is as much spiritual practice as instrument. The "
        "wandering komuso monks of the Fuke sect played honkyoku -- 'blowing Zen' (suizen) -- as "
        "meditation, and the music lives in the shading of a single note, the breath, and the silence "
        "(ma) around it. 'Shika no Tone' (Distant Cry of Deer) is a beloved classic.",
        [
            ("Shakuhachi (the Zen bamboo flute)", None),
            ("Honkyoku & suizen (the blowing-Zen repertoire)", None),
            ("The komuso monks (the Fuke sect flute)", None),
            ("Shika no Tone (Distant Cry of Deer)", None),
            ("Ma & the single note (the shakuhachi aesthetic)", None),
        ],
    ),
    (
        "THE SHAMISEN & ITS WORLDS",
        "The three-string SHAMISEN -- descended from the Chinese sanxian via Okinawa's sanshin -- became "
        "the sound of Edo-period popular and theater music. It anchors the jiuta chamber song, the "
        "nagauta of kabuki, the gidayu of puppet theater, and, in the snowy north, the fiery virtuoso "
        "Tsugaru-jamisen. Its dry, percussive twang is unmistakably Japanese.",
        [
            ("Shamisen (the three-string lute)", None),
            ("Tsugaru-jamisen (the virtuoso northern folk style)", None),
            ("Nagauta (the kabuki shamisen song)", None),
            ("Jiuta (the shamisen chamber song)", None),
            ("The shamisen's Okinawan & Chinese roots (cross-link)", None),
        ],
    ),
    (
        "THE BIWA & THE TALE OF THE HEIKE",
        "The BIWA, a pear-shaped lute, is the instrument of epic narration. Blind biwa priests "
        "(biwa hoshi) chanted 'The Tale of the Heike' -- the great war epic -- in heikyoku, and later "
        "the Satsuma and Chikuzen biwa styles carried on the storytelling art. Its sparse, dramatic "
        "punctuation of the voice is a world away from Western lute music.",
        [
            ("Biwa (the narrative pear-shaped lute)", None),
            ("Heikyoku (the sung Tale of the Heike)", None),
            ("The blind biwa priests (biwa hoshi)", None),
            ("Satsuma & Chikuzen biwa (the storytelling styles)", None),
            ("Epic narration in Japanese music (the biwa tradition)", None),
        ],
    ),
    (
        "NOH, KABUKI & BUNRAKU: THE THEATER MUSIC",
        "Japan's three great theaters each have their music. NOH -- austere and dreamlike, perfected by "
        "Zeami in the 14th century -- moves to the hayashi (flute and drums) and the utai chant, "
        "embodying yugen; KABUKI dazzles with nagauta and offstage geza music; and BUNRAKU puppet "
        "theater rides the powerful gidayu-bushi narration and shamisen. Total theater, centuries old.",
        [
            ("Noh theater music (hayashi & utai chant)", None),
            ("Zeami & the art of yugen (the noh aesthetic)", None),
            ("Kabuki music (nagauta & the geza)", None),
            ("Bunraku & gidayu-bushi (the puppet-theater narration)", None),
            ("The hayashi ensemble (flute & drums of noh)", None),
        ],
    ),
    (
        "MIN'YO: THE FOLK SONG OF JAPAN",
        "Beneath the court and theater lies the people's MIN'YO -- work songs, festival songs, and "
        "dance-songs from every region. The Hokkaido fishermen's 'Soran Bushi', the ancient 'Kokiriko "
        "Bushi', and the gentle 'Sakura Sakura' are national treasures, and the bon-odori dance fills "
        "summer nights. Okinawa's sanshin songs form a distinct, sunlit southern branch.",
        [
            ("Sakura Sakura (the beloved folk song)", None),
            ("Soran Bushi (the Hokkaido fishermen's song)", None),
            ("Kokiriko Bushi (among the oldest folk songs)", None),
            ("Bon-odori (the summer festival dance-song)", None),
            ("Okinawan sanshin music (the Ryukyu southern branch)", None),
            ("Min'yo (the regional folk song of Japan)", None),
        ],
    ),
    (
        "THE JAPANESE AESTHETIC & THE ROAD AHEAD",
        "Binding it all is an aesthetic of restraint: MA (the eloquent silence), wabi-sabi, and the "
        "in-yo (yo/in) pentatonic scales that give Japanese melody its distinctive color -- plus the "
        "raw power of the TAIKO drums, now heard worldwide in kumi-daiko ensembles. Cross-link: this "
        "pentatonic, timbre-focused world meets Western music in the Meiji era, launching the modern pop "
        "century (Installment 2).",
        [
            ("Ma (the eloquent silence in Japanese music)", None),
            ("Wabi-sabi & yugen (the guiding aesthetics)", None),
            ("The in and yo pentatonic scales (Japanese melody)", None),
            ("Taiko drums & kumi-daiko (the drum ensemble)", None),
            ("Toward Meiji & the West (roads ahead)", None),
        ],
    ),
]

STEM = "japan_music_1_CLASSICAL_TRADITIONAL_ROOTS"


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
