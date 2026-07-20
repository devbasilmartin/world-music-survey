#!/usr/bin/env python3
"""Build India / South Asia, installment 7 (FINAL): Modern/Global & the Wider South Asia.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/Latin only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Indian & South Asian Music — Installment 7 (Finale): "
         "Modern, Global & the Wider South Asia (c. 2010-present)")

FRAMING = (
    "The final chapter opens South Asian music to the streaming world -- and out beyond India to the "
    "whole region and its diaspora. In India, ARIJIT SINGH's voice rules a single-driven film-pop, "
    "while a PUNJABI-POP juggernaut (Diljit Dosanjh, AP Dhillon, the murdered Sidhu Moose Wala) storms "
    "global charts, and a fierce INDIE and gully-rap scene (Prateek Kuhad; DIVINE and the Gully Boy "
    "wave) finds its own voice. Beyond India, this installment finally gives the WIDER SOUTH ASIA its "
    "due: PAKISTAN, from Nazia Hassan and Junoon to the global juggernaut of Coke Studio ('Pasoori'); "
    "BANGLADESH's band rock and Lalon revival; SRI LANKA (Yohani's worldwide 'Manike Mage Hithe') and "
    "NEPAL; and the vast DIASPORA that put South Asian sound into global pop -- Panjabi MC, the Asian "
    "Underground, M.I.A., Jay Sean. Cross-links: the whole seven-part arc (raga to streaming); bhangra "
    "and qawwali gone global; South Asian music inside the US/UK/Western pop surveys. This installment "
    "also builds the India/South Asia region master. Content notes: Sidhu Moose Wala's 2022 murder is "
    "kept in view. Region: ALL of South Asia (India, Pakistan, Bangladesh, Sri Lanka, Nepal) & diaspora."
)

SECTIONS = [
    (
        "THE STREAMING-ERA FILM SONG & ARIJIT SINGH (c. 2013-present)",
        "The film song still dominates, but streaming reshaped it into a singles game. Arijit Singh "
        "became the defining voice of the age -- his 'Tum Hi Ho' the modern romantic anthem -- while "
        "rap-pop stars (Badshah, Honey Singh) and singers like Neha Kakkar rode YouTube to billions of "
        "views. The soundtrack fragmented into playlists.",
        [
            ("Tum Hi Ho", "Arijit Singh"),
            ("Arijit Singh (the defining voice of streaming-era filmi)", None),
            ("Badshah & Honey Singh (the rap-pop of Bollywood)", None),
            ("The single-driven film soundtrack (the streaming shift)", None),
            ("YouTube & the billion-view Indian song", None),
        ],
    ),
    (
        "THE PUNJABI-POP JUGGERNAUT (c. 2015-present)",
        "Punjabi pop went from regional to planetary. Diljit Dosanjh played Coachella, AP Dhillon's "
        "'Brown Munde' became a diaspora anthem, Guru Randhawa's 'Lahore' racked up billions, and Sidhu "
        "Moose Wala's raw 'So High' made him a generational icon. Content note: Sidhu was murdered in "
        "2022, a shock felt across the Punjabi world.",
        [
            ("Brown Munde", "AP Dhillon"),
            ("So High", "Sidhu Moose Wala"),
            ("Lahore", "Guru Randhawa"),
            ("Diljit Dosanjh (Punjabi pop at Coachella)", None),
            ("The global Punjabi-pop wave (India to the diaspora)", None),
            ("Sidhu Moose Wala's murder (2022, content note)", None),
        ],
    ),
    (
        "INDIAN INDIE & THE HIP-HOP EXPLOSION (c. 2015-present)",
        "For the first time since Indipop, a real non-film scene thrives. Prateek Kuhad's tender "
        "'cold/mess' led an indie-pop wave (The Local Train, When Chai Met Toast), while Mumbai gully "
        "rap erupted -- DIVINE and Naezy's 'Mere Gully Mein' inspired the hit film Gully Boy (2019), and "
        "MC Stan and Seedhe Maut carried desi hip-hop nationwide.",
        [
            ("cold/mess", "Prateek Kuhad"),
            ("Mere Gully Mein", "DIVINE"),
            ("The Indian indie wave (The Local Train, When Chai Met Toast)", None),
            ("Gully rap & Gully Boy (Mumbai street hip-hop, 2019)", None),
            ("MC Stan & Seedhe Maut (desi hip-hop goes national)", None),
        ],
    ),
    (
        "PAKISTAN: FROM VITAL SIGNS TO COKE STUDIO (c. 1980-present)",
        "Pakistan built a mighty pop tradition of its own. Nazia Hassan's 'Aap Jaisa Koi' (1980) was "
        "South Asia's first pop smash; Vital Signs' 'Dil Dil Pakistan' became an anthem; Junoon fused "
        "Sufi poetry with rock ('Sayonee'). Then COKE STUDIO PAKISTAN reinvented the tradition for the "
        "world -- Rahat Fateh Ali Khan's 'Afreen Afreen' and Ali Sethi's 'Pasoori' global sensations.",
        [
            ("Aap Jaisa Koi", "Nazia Hassan"),
            ("Dil Dil Pakistan", "Vital Signs"),
            ("Sayonee", "Junoon"),
            ("Afreen Afreen", "Rahat Fateh Ali Khan"),
            ("Pasoori", "Ali Sethi"),
            ("Coke Studio Pakistan (the tradition remade for the world)", None),
            ("Atif Aslam & the Pakistani pop-rock wave", None),
        ],
    ),
    (
        "BANGLADESH (c. 1972-present)",
        "Bangladesh, born in 1971, built a rich music world in Bengali. A powerful band-rock era rose "
        "(Miles, Ayub Bachchu's LRB, the metal of Warfaze, James's Nagar Baul), alongside a living folk "
        "and Lalon-baul revival and the legendary voice of Runa Laila. Cross-link: Bengal's bauls and "
        "Tagore (#3), on the eastern side of the border.",
        [
            ("Bangladeshi band rock (Miles, LRB, Warfaze)", None),
            ("James / Nagar Baul (the Bangladeshi rock icon)", None),
            ("Ayub Bachchu & LRB (Bangladesh's guitar hero)", None),
            ("Runa Laila (the legendary subcontinental voice)", None),
            ("The Bangladeshi Lalon & folk revival", None),
        ],
    ),
    (
        "SRI LANKA & NEPAL",
        "The smaller nations sing too. Sri Lanka has its Portuguese-rooted baila dance music and the "
        "revered Sinhala maestro W.D. Amaradeva -- and, in 2021, Yohani's 'Manike Mage Hithe' became a "
        "worldwide viral hit. Nepal treasures Narayan Gopal's ghazal-like songs and a lively folk-pop "
        "and hip-hop scene. Both sit at South Asia's cultural crossroads.",
        [
            ("Manike Mage Hithe", "Yohani"),
            ("Baila (the Sri Lankan Portuguese-rooted dance music)", None),
            ("W.D. Amaradeva (the Sinhala music maestro)", None),
            ("Narayan Gopal (the legend of Nepali song)", None),
            ("Nepali folk-pop & hip-hop (the Himalayan scene)", None),
        ],
    ),
    (
        "THE GLOBAL DIASPORA & THE ASIAN UNDERGROUND (c. 1990-present)",
        "The South Asian diaspora put the subcontinent's sound into global pop. Panjabi MC's 'Mundian "
        "To Bach Ke' (with a Jay-Z remix) went worldwide; Bally Sagoo, Nitin Sawhney, and Talvin Singh "
        "built the UK 'Asian Underground'; M.I.A.'s 'Paper Planes' and Jay Sean's 'Down' hit the top of "
        "Western charts. Region note: these are diaspora artists (UK/US), flagged.",
        [
            ("Mundian To Bach Ke", "Panjabi MC"),
            ("Paper Planes", "M.I.A."),
            ("Down", "Jay Sean"),
            ("The Asian Underground (Nitin Sawhney, Talvin Singh, Bally Sagoo)", None),
            ("Bhangra goes global (the UK-diaspora dancefloor)", None),
            ("South Asian sound in Western pop (the diaspora reach)", None),
        ],
    ),
    (
        "THE THROUGH-LINE: SOUTH ASIA'S SOUND",
        "Seven installments trace an astonishing span: from the Samaveda and the raga through the folk "
        "of a thousand villages, the devotion of bhajan and qawwali, the film-song juggernaut, and out "
        "to a global streaming pop. Devotion and cinema are its twin engines; the raga its deep grammar; "
        "and the diaspora its far horizon. Cross-links: the US/UK/Western surveys (where South Asian "
        "sound now lives too), and the East Asia surveys ahead.",
        [
            ("Raga to streaming (the South Asian arc)", None),
            ("Devotion & cinema (the twin engines of South Asian pop)", None),
            ("The film song as the region's popular music", None),
            ("South Asia's global century (the diaspora horizon)", None),
            ("From the Samaveda to the algorithm (the arc closes)", None),
        ],
    ),
]

STEM = "south_asia_music_7_MODERN_GLOBAL_WIDER_SOUTH_ASIA"


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
