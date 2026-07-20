#!/usr/bin/env python3
"""Build East Asia: Japan, installment 2: The Modern Turn -- Meiji Westernization, Ryukoka & Enka's Roots.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/romaji only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Japanese Music — Installment 2: "
         "The Modern Turn — Meiji, Ryukoka & the Roots of Enka (c. 1868-1945)")

FRAMING = (
    "When the Meiji Restoration (1868) flung Japan open to the West, its music changed faster than "
    "almost anywhere on Earth. The state adopted Western scales and harmony wholesale for education, "
    "teaching SHOKA (school songs) to a new generation, and the first Japanese composers of Western "
    "art music emerged -- Rentaro Taki, whose 'Moon over the Ruined Castle' fused Western form with "
    "Japanese melancholy, and Kosaku Yamada, father of Japanese orchestral music. The Taisho era added "
    "the tender DOYO children's songs ('Furusato', 'Akatombo') and, with records and radio, the first "
    "true pop: RYUKOKA, whose stars (Noriko Awaya, the 'Queen of Blues') filled a jazz-mad, cosmopolitan "
    "Tokyo. Meanwhile the sentimental minor-key ballad that would become ENKA took shape from Meiji "
    "street-singing. Then militarism darkened everything: jazz was banned as enemy music, and gunka "
    "war-songs took over -- until defeat in 1945 opened the door to the American-drenched postwar boom "
    "(Installment 3). Cross-links: Western classical and American jazz entering Japan; the shoka model "
    "echoing China's and Korea's school songs. Content note: militarism and the Pacific War are kept "
    "with care. Names transliterated (romaji). Region: Japan."
)

SECTIONS = [
    (
        "THE MEIJI OPENING & THE SHOKA SCHOOL SONGS (c. 1868-1900)",
        "Meiji Japan embraced Western music as a tool of modernization. Under reformers like Izawa "
        "Shuji, schools taught SHOKA -- newly composed songs in Western scales and harmony -- brass and "
        "military bands formed, and the pentatonic ear began absorbing the diatonic. It was a wholesale, "
        "state-driven musical reinvention.",
        [
            ("Shoka (the Meiji Western-style school songs)", None),
            ("Izawa Shuji & Meiji music education", None),
            ("Western scales & harmony adopted (the great turn)", None),
            ("Military & brass bands (Meiji Westernization)", None),
            ("The pentatonic ear meets the diatonic West", None),
        ],
    ),
    (
        "THE FIRST WESTERN-STYLE COMPOSERS",
        "Japan produced its first composers of Western art music with startling speed. Rentaro Taki's "
        "'Moon over the Ruined Castle' (1901) is a small masterpiece of Japanese melancholy in Western "
        "dress; and Kosaku Yamada built the foundations of Japanese orchestral and art-song writing, "
        "conducting the nation's first symphonic concerts.",
        [
            ("Kojo no Tsuki (Moon over the Ruined Castle)", "Rentaro Taki"),
            ("Rentaro Taki (the pioneer composer, d. 1903)", None),
            ("Kosaku Yamada (father of Japanese orchestral music)", None),
            ("The birth of Japanese art music (Western form, Japanese soul)", None),
            ("Hana (Taki's beloved springtime song)", None),
        ],
    ),
    (
        "DOYO: THE CHILDREN'S ART SONG (Taisho era)",
        "The Taisho era's doyo movement created artistic songs for children -- gentle, nostalgic, and "
        "beautifully crafted by poets like Kitahara Hakushu and composers like Kosaku Yamada and Teiichi "
        "Okano. 'Furusato' (Hometown) and 'Akatombo' (Red Dragonfly) became so beloved they function as "
        "unofficial national songs of longing.",
        [
            ("Furusato (Hometown)", "Teiichi Okano"),
            ("Akatombo (Red Dragonfly)", "Kosaku Yamada"),
            ("Doyo (the Taisho children's art songs)", None),
            ("Kitahara Hakushu (the doyo poet)", None),
            ("The Japanese song of nostalgia & longing", None),
        ],
    ),
    (
        "RYUKOKA & THE FIRST POP STARS (c. 1914-1935)",
        "Records and radio (NHK began in 1925) created Japan's first mass popular music: RYUKOKA. "
        "'Katyusha's Song' (1914), from a stage play and composed by Shinpei Nakayama, is often called "
        "Japan's first pop hit; the Nippon Columbia and Victor labels churned out stars, and the popular "
        "song became a national industry.",
        [
            ("Katyusha no Uta (Katusha's Song)", "Sumako Matsui"),
            ("Ryukoka (early Japanese popular song)", None),
            ("Shinpei Nakayama (the pioneer pop composer)", None),
            ("The record industry (Nippon Columbia & Victor)", None),
            ("NHK radio (1925) & the pop song", None),
        ],
    ),
    (
        "THE JAZZ AGE & MODERN TOKYO (c. 1925-1940)",
        "Cosmopolitan Taisho-and-early-Showa Tokyo went jazz-mad -- dance halls, jazz kissa cafes, and "
        "the stylish moga and mobo ('modern girls and boys'). Noriko Awaya, the 'Queen of Blues', sang "
        "smoky ballads like 'Farewell Blues', and a glamorous, Western-facing urban culture bloomed "
        "before the militarists shut it down.",
        [
            ("Wakare no Blues (Farewell Blues)", "Noriko Awaya"),
            ("Noriko Awaya (the Queen of Blues)", None),
            ("Ichiro Fujiyama (the ryukoka crooner)", None),
            ("Tokyo's jazz age (dance halls & jazz kissa)", None),
            ("Moga & mobo (the modern girls and boys)", None),
        ],
    ),
    (
        "THE ROOTS OF ENKA",
        "The genre later called ENKA -- the sentimental, minor-key ballad of heartbreak and stoic "
        "endurance -- grew from Meiji-era 'enzetsu-ka', political street-songs used to dodge censorship, "
        "and the enka-shi street performers who sold their song-sheets. Its full sentimental flowering "
        "would come after the war (Installment 3), but its melancholy roots are here.",
        [
            ("Enka's roots (the Meiji enzetsu-ka protest songs)", None),
            ("The enka-shi (the street singers & song-sheets)", None),
            ("The minor-key ballad of endurance (the enka feeling)", None),
            ("Political street song into sentimental ballad", None),
        ],
    ),
    (
        "WAR & THE SUPPRESSION OF SONG (1937-1945)",
        "As Japan went to war, music was militarized. GUNKA (war songs) and propaganda anthems like 'Umi "
        "Yukaba' filled the airwaves, jazz and Western 'enemy' music were banned, and the cosmopolitan "
        "Tokyo scene went dark. Content note: this is music under militarism, in the years of the "
        "Pacific War and its catastrophe -- kept with care.",
        [
            ("Gunka (the wartime military songs)", None),
            ("Umi Yukaba (the solemn wartime anthem)", None),
            ("Jazz banned as enemy music (wartime suppression)", None),
            ("Music under militarism (content note)", None),
            ("The silencing of cosmopolitan Tokyo", None),
        ],
    ),
    (
        "DEFEAT & THE ROAD AHEAD (1945)",
        "Defeat and occupation in 1945 shattered the old order -- and flung the doors open to American "
        "music: jazz, boogie-woogie, and country poured in with the GIs. From the ruins a new postwar "
        "popular song (kayokyoku) would rise, and a teenage Hibari Misora would soon become its queen "
        "(Installment 3). Cross-link: American pop reshapes Japan.",
        [
            ("Defeat & occupation (1945, the shattered order)", None),
            ("American music floods in (jazz, boogie & the GIs)", None),
            ("The ruins & the coming postwar song (kayokyoku ahead)", None),
            ("Toward Hibari Misora & the postwar boom (roads ahead)", None),
        ],
    ),
]

STEM = "japan_music_2_MEIJI_RYUKOKA_ENKA_ROOTS"


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
