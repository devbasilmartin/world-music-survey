#!/usr/bin/env python3
"""Build India / South Asia, installment 5: The Film-Song Juggernaut -- Bollywood's Golden Age.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/Latin only. Dedup is by TITLE only.
Named-heavy: this is India's true pop songbook -- name the SONG - singer.
"""

TITLE = ("The Story of Indian & South Asian Music — Installment 5: "
         "The Film-Song Juggernaut — Bollywood's Golden Age (c. 1931-1970)")

FRAMING = (
    "For most of the world, India's pop music IS film music. Since the first talkie in 1931, the "
    "Hindi-cinema song has been the subcontinent's true popular music -- there was never a separate pop "
    "industry, because the movies were it. This installment covers the GOLDEN AGE, when a unique system "
    "produced an inexhaustible songbook: on screen, glamorous stars; behind the microphone, a tiny "
    "circle of PLAYBACK SINGERS whose voices dubbed everyone; and orchestrating it all, MUSIC DIRECTORS "
    "who fused Hindustani raga, folk, ghazal, and Western orchestration into three-minute miracles. "
    "Naushad's classical grandeur, S.D. Burman's poetry, Shankar-Jaikishan's romance; the reign of LATA "
    "MANGESHKAR and Mohammed RAFI, the mischief of Kishore Kumar, the ache of Mukesh and Talat -- these "
    "are the songs a billion people still know by heart. Cross-links: Hindustani classical (#2) and folk "
    "(#3) feeding the film song; the golden age flowing into the modern filmi/Indipop era (#6); Indian "
    "film music's global reach (from the USSR to sampling). Content notes: the female-playback monopoly "
    "and Guru Dutt's tragic life are kept in view. Names are SONG - singer; bare titles are directors, "
    "forms, or concepts. Region: India (Hindi cinema)."
)

SECTIONS = [
    (
        "THE BIRTH OF FILM SONG & PLAYBACK (c. 1931-1949)",
        "India's first talkie, Alam Ara (1931), sang from the start, and early films starred "
        "actor-singers -- above all K.L. Saigal, the first great voice of Indian cinema. By the mid-"
        "1930s PLAYBACK singing was born: trained singers recorded, and actors lip-synced. It would "
        "become the defining system of Indian pop.",
        [
            ("Babul Mora", "K.L. Saigal"),
            ("Alam Ara (1931, the first Indian talkie's songs)", None),
            ("The birth of playback singing (mid-1930s)", None),
            ("K.L. Saigal (cinema's first superstar voice)", None),
            ("The actor-singer gives way to the playback singer", None),
        ],
    ),
    (
        "NAUSHAD & THE CLASSICAL-FILMI GRANDEUR (c. 1950-1965)",
        "Naushad wove Hindustani raga and North Indian folk into lavish, orchestrally rich film music -- "
        "Baiju Bawra put pure classical raga on the marquee, and Mughal-e-Azam's 'Pyar Kiya To Darna "
        "Kya' remains the genre's most regal anthem. He proved film song could be high art.",
        [
            ("Pyar Kiya To Darna Kya", "Lata Mangeshkar"),
            ("Naushad (the classical-grandeur music director)", None),
            ("Baiju Bawra (raga on the silver screen)", None),
            ("Raga-based film song (the classical-filmi fusion)", None),
            ("The film-song orchestra (East-West arrangement)", None),
        ],
    ),
    (
        "RAJ KAPOOR, SHANKAR-JAIKISHAN & MUKESH (c. 1949-1965)",
        "The showman Raj Kapoor, the composing duo Shankar-Jaikishan, and the plaintive voice of Mukesh "
        "made the era's most beloved -- and most internationally famous -- songs. 'Awara Hoon' and 'Mera "
        "Joota Hai Japani' swept the USSR, China, and the Middle East, making Raj Kapoor a global star "
        "and Indian film song a worldwide phenomenon.",
        [
            ("Awara Hoon", "Mukesh"),
            ("Mera Joota Hai Japani", "Mukesh"),
            ("Shankar-Jaikishan (the romance-era composing duo)", None),
            ("Mukesh (the plaintive voice of Raj Kapoor)", None),
            ("Indian film song conquers the USSR (Raj Kapoor abroad)", None),
        ],
    ),
    (
        "S.D. BURMAN, GURU DUTT & THE POETIC FILM (c. 1955-1965)",
        "The decade's artistic peak came from the melancholy masterpieces of Guru Dutt, scored by S.D. "
        "Burman: Pyaasa and Kaagaz Ke Phool turned film song into aching poetry, with Geeta Dutt's "
        "'Waqt Ne Kiya Kya Haseen Sitam' its haunting summit. Content note: Guru Dutt's brilliance was "
        "shadowed by depression and an early death.",
        [
            ("Waqt Ne Kiya Kya Haseen Sitam", "Geeta Dutt"),
            ("S.D. Burman (the poet among music directors)", None),
            ("Pyaasa & Kaagaz Ke Phool (Guru Dutt's masterpieces)", None),
            ("Geeta Dutt (the voice of melancholy grace)", None),
            ("Sahir Ludhianvi (the poet-lyricist of the golden age)", None),
        ],
    ),
    (
        "LATA MANGESHKAR: THE NIGHTINGALE OF INDIA (c. 1949-1970)",
        "Lata Mangeshkar's crystalline voice defined the female playback singer for half a century -- "
        "her 'Aye Mere Watan Ke Logon' (1963) reportedly moved Nehru to tears, and 'Lag Ja Gale' (for "
        "Madan Mohan) is an eternal ghazal-song. Content note: the near-monopoly Lata and her sister "
        "Asha held over female playback is part of the story.",
        [
            ("Aye Mere Watan Ke Logon", "Lata Mangeshkar"),
            ("Lag Ja Gale", "Lata Mangeshkar"),
            ("Lata Mangeshkar (the Nightingale of India)", None),
            ("Madan Mohan (the ghazal music director)", None),
            ("The female-playback monopoly (Lata & Asha's reign)", None),
        ],
    ),
    (
        "MOHAMMED RAFI: THE VOICE OF A THOUSAND SONGS (c. 1949-1970)",
        "Mohammed Rafi could sing anything -- classical, qawwali, rock-and-roll, tender romance, comic "
        "songs -- for any actor, and he did, thousands of times. 'Chaudhvin Ka Chand' and 'Baharon Phool "
        "Barsao' show his melting tenderness; he was the male playback king of the age and beloved "
        "across faiths.",
        [
            ("Chaudhvin Ka Chand", "Mohammed Rafi"),
            ("Baharon Phool Barsao", "Mohammed Rafi"),
            ("Mohammed Rafi (the voice of a thousand songs)", None),
            ("O.P. Nayyar (the rhythm-loving music director)", None),
            ("The versatility of the playback voice (Rafi's range)", None),
        ],
    ),
    (
        "KISHORE KUMAR, ASHA & THE VOICES (c. 1955-1970)",
        "A constellation of voices completed the age: the irrepressible Kishore Kumar (whose Aradhana "
        "songs 'Mere Sapno Ki Rani' and 'Roop Tera Mastana' launched a new era in 1969), the endlessly "
        "versatile Asha Bhosle, the rich Manna Dey, and the velvet ghazal of Talat Mahmood. Each was a "
        "world unto itself.",
        [
            ("Mere Sapno Ki Rani", "Kishore Kumar"),
            ("Roop Tera Mastana", "Kishore Kumar"),
            ("Pyar Hua Ikrar Hua", "Manna Dey"),
            ("Aaiye Meharban", "Asha Bhosle"),
            ("Jalte Hain Jiske Liye", "Talat Mahmood"),
            ("Kishore Kumar (the yodeling maverick genius)", None),
            ("Asha Bhosle (the versatile voice of a thousand moods)", None),
        ],
    ),
    (
        "THE FILMI GHAZAL & THE GOLDEN-AGE SONGBOOK",
        "Underpinning it all was poetry: Urdu shayari and the filmi ghazal, penned by lyricists like "
        "Sahir, Shakeel Badayuni, and Majrooh, made the film song literate as well as tuneful. By 1970 "
        "the golden-age songbook WAS Indian popular music -- no separate pop industry ever needed to "
        "exist. Cross-link: the modern filmi era & Indipop (#6).",
        [
            ("Filmi ghazal (the film-song ghazal)", None),
            ("Shakeel Badayuni & Majrooh Sultanpuri (the golden-age lyricists)", None),
            ("Urdu shayari in the film song (poetry as pop)", None),
            ("The film song as India's pop (no separate pop industry)", None),
            ("C. Ramchandra & Roshan (more golden-age composers)", None),
            ("The golden-age songbook (a billion hearts know it)", None),
        ],
    ),
]

STEM = "south_asia_music_5_BOLLYWOOD_GOLDEN_AGE"


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
