#!/usr/bin/env python3
"""Build the Jewish Diaspora, installment 2: Ashkenazi & Klezmer.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Jewish Music — Installment 2: "
         "Ashkenazi & Klezmer (Yiddish Song, the Wedding Band & the Revival)")

FRAMING = (
    "The ASHKENAZI Jews of Eastern and Central Europe -- the Yiddish-speaking world -- built one of the "
    "richest secular musical cultures in the diaspora. Its heart is the YIDDISH SONG: tender lullabies "
    "('Oyfn Pripetshik'), love songs, and the fierce labor and Bund workers' anthems of the shtetl and "
    "the city. On the stage it became the roaring YIDDISH THEATER of New York's Second Avenue, giving the "
    "world 'Bei Mir Bistu Sheyn'. And at every wedding played KLEZMER -- the ecstatic instrumental "
    "celebration music of the klezmorim, its wailing, laughing CLARINET and crying fiddle dancing through "
    "the freylekhs and bulgars in the distinctive klezmer modes. Masters like Naftule Brandwein and Dave "
    "Tarras were its stars. Beneath it all ran the wordless HASIDIC NIGUN. Content note: the Holocaust "
    "annihilated the Yiddish heartland of Europe -- this is kept factual, with care, and as memory -- and "
    "the KLEZMER REVIVAL from the 1970s is a story of rescue and continuity. Cross-links: the nigun & "
    "liturgy (#1); Europe; the US; the Yiddish stage & American song. Names transliterated. Region: the "
    "Ashkenazi Yiddish world."
)

SECTIONS = [
    (
        "THE YIDDISH FOLK SONG",
        "The Yiddish folk song is the tender voice of Ashkenazi life -- lullabies, love songs, songs of "
        "poverty, faith, and the everyday. 'Oyfn Pripetshik' (a rebbe teaching children the alphabet by "
        "the hearth) and 'Tumbalalaika' are beloved the world over, carrying the warmth and melancholy of "
        "a whole civilization.",
        [
            ("Oyfn Pripetshik (the hearth-side lullaby)", None),
            ("Tumbalalaika (the Yiddish riddle-song)", None),
            ("The Yiddish folk song (the voice of the shtetl)", None),
            ("Rozhinkes mit Mandlen (Raisins and Almonds)", None),
            ("Yiddish lullabies & love songs", None),
        ],
    ),
    (
        "THE SONGS OF LABOR & STRUGGLE",
        "In the factories and movements of the late-19th and early-20th centuries, Yiddish became a "
        "language of struggle -- the labor anthems of the Jewish Bund and the sweatshop poets. Content "
        "note: some of these became songs of resistance, including the partisans' hymn 'Zog Nit Keyn "
        "Mol' -- kept factual and as memory.",
        [
            ("Zog Nit Keyn Mol (the Partisans' Song)", None),
            ("Daloy Politsey (the Yiddish protest song)", None),
            ("In Ale Gasn (the Bund labor song)", None),
            ("Yiddish labor & workers' songs", None),
            ("The sweatshop poets in song", None),
        ],
    ),
    (
        "THE YIDDISH THEATER & SECOND AVENUE",
        "From the 1880s, Yiddish THEATER exploded -- in Warsaw, in London, and above all on New York's "
        "Second Avenue, the 'Yiddish Broadway'. Its melodramas and musical comedies made stars of Molly "
        "Picon and Aaron Lebedeff and produced enduring songs, blending Old-World melody with the American "
        "stage. Cross-link: the American musical (US survey).",
        [
            ("The Yiddish theater (Second Avenue, the Yiddish Broadway)", None),
            ("Rumania Rumania", "Aaron Lebedeff"),
            ("Molly Picon (the Yiddish stage star)", None),
            ("Belz (the beloved Yiddish theater song)", None),
            ("Yiddish musical comedy (the Old World on stage)", None),
        ],
    ),
    (
        "BEI MIR BISTU SHEYN & THE CROSSOVER",
        "The Yiddish stage gave the world a global hit: 'Bei Mir Bistu Sheyn', written for a 1932 Yiddish "
        "musical, became a smash for the Andrews Sisters in 1937 and a swing standard. The Barry Sisters "
        "carried Yiddish song into American pop. It marks the moment Yiddish music entered the mainstream. "
        "Cross-link: American swing (US survey).",
        [
            ("Bei Mir Bistu Sheyn", "The Barry Sisters"),
            ("The Yiddish song crosses over (Bei Mir Bistu Sheyn)", None),
            ("The Barry Sisters (Yiddish meets American pop)", None),
            ("Yiddish swing (the crossover era)", None),
        ],
    ),
    (
        "KLEZMER: THE MUSIC OF CELEBRATION",
        "KLEZMER is the instrumental music of Ashkenazi celebration -- above all the wedding -- played by "
        "the klezmorim. Built on dance forms like the FREYLEKHS, the BULGAR, and the SHER, and the "
        "sighing, unmetered DOINA, it is music of ecstatic joy shot through with tears, the sound of a "
        "community's every simcha.",
        [
            ("Klezmer (the Ashkenazi celebration music)", None),
            ("Freylekhs & bulgar (the klezmer dances)", None),
            ("The doina (the klezmer lament)", None),
            ("The sher & the khosidl (the klezmer dance forms)", None),
            ("The klezmer wedding (the simcha music)", None),
        ],
    ),
    (
        "THE KLEZMER SOUND: CLARINET, FIDDLE & MODE",
        "Klezmer's voice is the CLARINET -- wailing, laughing, sobbing, bending notes in imitation of the "
        "human voice and the cantor -- with the fiddle, the tsimbl (hammered dulcimer), and brass. It "
        "moves in distinctive klezmer modes (the freygish/Ahavah Rabbah), full of augmented seconds. "
        "Cross-link: the synagogue modes (#1).",
        [
            ("The klezmer clarinet (the wailing, laughing voice)", None),
            ("The klezmer fiddle & tsimbl", None),
            ("The freygish mode (the klezmer scale)", None),
            ("Krekhts & the vocal ornaments (the klezmer cry)", None),
            ("The klezmer ensemble (clarinet, fiddle, brass)", None),
        ],
    ),
    (
        "THE GREAT KLEZMORIM",
        "The golden age of American klezmer (1910s-40s) crowned virtuoso stars. The wild, brilliant "
        "clarinetist Naftule Brandwein billed himself 'the King of Jewish Music'; his rival Dave Tarras "
        "brought elegant mastery and a long career. Their 78s are the classic canon that the later revival "
        "would rediscover.",
        [
            ("Der Heyser Bulgar", "Naftule Brandwein"),
            ("Naftule Brandwein (the King of Jewish Music)", None),
            ("Dave Tarras (the master klezmer clarinetist)", None),
            ("The klezmer 78s (the classic recordings)", None),
            ("Abe Schwartz & the klezmer orchestras", None),
        ],
    ),
    (
        "THE HASIDIC NIGUN & THE HASIDIC SONG WORLD",
        "The HASIDIC movements gave Ashkenazi music a deep well of song: the wordless NIGUN raised to an "
        "art (the Modzitz dynasty famed for its melodies, Chabad for its nigunim), and a whole world of "
        "Hasidic melody carrying joy and devotion. Cross-link: the nigun (#1); modern Hasidic pop (#4).",
        [
            ("The Ashkenazi nigun tradition (the wordless melody, cross-link)", None),
            ("The Modzitzer niggunim (the Hasidic melody dynasty)", None),
            ("The Chabad niggunim (the Lubavitch melodies)", None),
            ("Hasidic song (joy & devotion in melody)", None),
            ("The tish & the Hasidic gathering (the sung table)", None),
        ],
    ),
    (
        "THE KLEZMER REVIVAL & THE ROAD AHEAD",
        "The Holocaust and assimilation nearly silenced klezmer -- but from the 1970s a REVIVAL brought it "
        "roaring back. The Klezmorim, the Klezmer Conservatory Band, Giora Feidman, and then the "
        "genre-bending Klezmatics rediscovered the old 78s and made klezmer a living, global music again. "
        "From the Ashkenazi world the survey turns to the Sephardi and Mizrahi (#3). Content note: revival "
        "as rescue and continuity.",
        [
            ("The klezmer revival (the 1970s rebirth)", None),
            ("The Klezmatics (the genre-bending revival band)", None),
            ("Giora Feidman (the King of Klezmer, the revival voice)", None),
            ("The Klezmer Conservatory Band (the revival pioneers)", None),
            ("Klezmer lives again (rescue & continuity)", None),
        ],
    ),
]

STEM = "jewish_music_2_ASHKENAZI_KLEZMER"


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
