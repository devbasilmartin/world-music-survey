#!/usr/bin/env python3
"""Build Oceania / the Pacific, installment 2: Polynesia (Maori, Hawaiian & the Island Nations).

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. ASCII/transliterated only. Dedup is by TITLE only.
"""

TITLE = ("The Story of Pacific & Oceanian Music — Installment 2: "
         "Polynesia (Maori, Hawaiian & the Island Nations)")

FRAMING = (
    "Polynesia -- the great triangle from Aotearoa to Hawaii to Rapa Nui -- shares a single Austronesian "
    "voyaging heritage and a music built on the chanted word, the drum, and the dance. The MAORI of "
    "Aotearoa/New Zealand sing waiata and thunder the HAKA posture-dance, spin the poi, and are reviving "
    "the haunting TAONGA PUORO (their traditional flutes and instruments). HAWAII holds the ancient MELE "
    "and HULA -- chant (oli) and dance over the pahu drum and ipu gourd -- and then built one of the "
    "world's most beloved modern sounds: KI HO'ALU (slack-key guitar), the soaring falsetto (leo "
    "ki'eki'e), the Hawaiian steel guitar, and the ukulele, from Gabby Pahinui to Israel Kamakawiwo'ole. "
    "Across WEST POLYNESIA -- Samoa, Tonga, Tahiti, the Cook Islands -- ring the fast to'ere drum-dances, "
    "the slap-dances, and the glorious massed church HYMNODY that missionaries seeded and Polynesians made "
    "utterly their own. Content notes: colonization nearly extinguished the Maori and Hawaiian languages "
    "and musics; their revival is a story of resilience, told with respect. Names romanized to plain "
    "ASCII (okina and macrons dropped). Region: Polynesia."
)

SECTIONS = [
    (
        "THE MAORI: WAIATA & THE HAKA",
        "The Maori of Aotearoa carry a rich tradition of WAIATA (song) and chant, and above all the HAKA "
        "-- a powerful, rhythmic posture-dance of stamping, slapping, and fierce chanted voice, of which "
        "'Ka Mate' (composed by Te Rauparaha) is the most famous, known worldwide through the All Blacks. "
        "It is a living expression of identity, challenge, and mana.",
        [
            ("The haka (the Maori posture-dance)", None),
            ("Ka Mate (the famous haka)", None),
            ("Waiata (the Maori song)", None),
            ("Mana & the chanted voice (the haka's power)", None),
        ],
    ),
    (
        "MAORI CHANT, POI & THE ACTION SONG",
        "Maori musical performance (kapa haka) weaves together the karakia and karanga (chant and call), "
        "the graceful POI (twirled tethered balls) with its sung accompaniment, and the modern waiata-a-"
        "ringa 'action song' that set Maori words to Western-influenced melody. 'Pokarekare Ana' became a "
        "beloved national love song.",
        [
            ("Pokarekare Ana (the beloved Maori love song)", None),
            ("Poi (the twirled-ball dance & song)", None),
            ("Karakia & karanga (Maori chant & call)", None),
            ("Waiata-a-ringa (the Maori action song)", None),
            ("Kapa haka (the Maori performance art)", None),
        ],
    ),
    (
        "TAONGA PUORO: THE MAORI INSTRUMENTS REVIVED",
        "The TAONGA PUORO -- the Maori 'singing treasures', flutes and instruments of wood, bone, and "
        "stone like the putorino, koauau, and nguru, and the whirled purerehua -- fell nearly silent under "
        "colonization. Content note: from the 1980s Hirini Melbourne and Richard Nunns painstakingly "
        "revived them, restoring a lost voice of the land.",
        [
            ("Taonga puoro (the Maori singing treasures)", None),
            ("Putorino & koauau (the Maori flutes)", None),
            ("The purerehua (the Maori bullroarer)", None),
            ("Hirini Melbourne & Richard Nunns (the taonga puoro revival)", None),
            ("The revival of the Maori instruments (content note)", None),
        ],
    ),
    (
        "HAWAII: THE ANCIENT MELE & HULA",
        "Native Hawaiian music begins with the MELE (chant) and HULA (dance) -- the sacred oli chant and "
        "the hula kahiko danced to the pahu shark-skin drum, the ipu gourd, and the ili'ili stones, "
        "carrying genealogy, myth, and prayer. Content note: the hula was suppressed after Western "
        "contact and revived, a cornerstone of the Hawaiian renaissance.",
        [
            ("Mele & oli (the Hawaiian chant)", None),
            ("Hula kahiko (the ancient Hawaiian dance)", None),
            ("The pahu & ipu (the hula drum & gourd)", None),
            ("The Hawaiian chant tradition (genealogy & myth)", None),
            ("The hula's suppression & revival (content note)", None),
        ],
    ),
    (
        "HAWAII: SLACK-KEY, FALSETTO & THE STEEL GUITAR",
        "Modern Hawaiian music gave the world beloved sounds: KI HO'ALU (slack-key guitar), its strings "
        "loosened into ringing open tunings; the leo ki'eki'e (falsetto) with its signature break; the "
        "Hawaiian STEEL GUITAR (invented by Joseph Kekuku), which sailed into country and blues; and the "
        "ukulele. Gabby Pahinui was the slack-key master and heart of the Hawaiian renaissance.",
        [
            ("Ki ho'alu (Hawaiian slack-key guitar)", None),
            ("Hi'ilawe", "Gabby Pahinui"),
            ("Leo ki'eki'e (the Hawaiian falsetto)", None),
            ("The Hawaiian steel guitar (Joseph Kekuku's invention)", None),
            ("Gabby Pahinui (the slack-key master)", None),
        ],
    ),
    (
        "HAWAII: THE UKULELE & IZ",
        "The UKULELE -- adapted from a Portuguese machete -- became the sound of Hawaii and then the world. "
        "The himeni hymn tradition and hapa haole songs shaped the islands' harmony, and Israel "
        "Kamakawiwo'ole ('Iz'), with his ukulele medley of 'Somewhere Over the Rainbow' and 'What a "
        "Wonderful World', became the most beloved Hawaiian voice of all.",
        [
            ("Somewhere Over the Rainbow (the Iz medley)", "Israel Kamakawiwo'ole"),
            ("The ukulele (the Hawaiian four-string)", None),
            ("Israel Kamakawiwo'ole (Iz, the beloved Hawaiian voice)", None),
            ("Himeni (the Hawaiian hymn tradition)", None),
            ("Hapa haole song (the Hawaiian popular style)", None),
        ],
    ),
    (
        "SAMOA & TONGA: SLAP-DANCE, DRUM & VOICE",
        "West Polynesia beats with its own power. Samoa's fa'ataupati (the men's slap-dance), the graceful "
        "siva, and the sasa group dance drive its music, while Tonga is famed for the lakalaka -- a sung "
        "speech-dance of massed voices -- and the nose-flute. Both nations sing soaring church harmony.",
        [
            ("Fa'ataupati (the Samoan slap-dance)", None),
            ("Siva & sasa (the Samoan dances)", None),
            ("Lakalaka (the Tongan sung speech-dance)", None),
            ("The Tongan nose-flute & the fangufangu", None),
            ("Samoan & Tongan song (the West Polynesian voice)", None),
        ],
    ),
    (
        "TAHITI, THE COOK ISLANDS & THE DRUM-DANCE",
        "French Polynesia and the Cook Islands electrify with the fastest drumming in the Pacific: the "
        "'OTE'A and the frenetic to'ere slit-drum ensembles that drive the hip-shaking Tahitian and Cook "
        "Islands dance (the ori Tahiti and the ura), alongside the himene tarava, a stunning close-harmony "
        "choral singing. The Heiva festival is its great showcase.",
        [
            ("'Ote'a (the Tahitian drum-dance)", None),
            ("The to'ere (the Tahitian slit-drum ensemble)", None),
            ("Ori Tahiti & the Cook Islands ura (the fast dance)", None),
            ("Himene tarava (the Tahitian close harmony)", None),
            ("The Heiva festival (the Tahitian showcase)", None),
        ],
    ),
    (
        "POLYNESIAN HYMNODY & THE ROAD AHEAD",
        "Across Polynesia, the missionary hymn met the Polynesian voice and became something glorious: "
        "vast, richly harmonized congregational singing (himene, sacred harmony) that is among the most "
        "moving choral music on Earth. From this deep song-world the survey sails to Micronesia and the "
        "island-pop present (#3). Cross-links: Aboriginal & Melanesian roots (#1); the string bands & "
        "modern Pacific pop (#3-4); the Austronesian tie to Southeast Asia.",
        [
            ("Polynesian church hymnody (the sacred harmony)", None),
            ("The missionary hymn made Polynesian (the choral glory)", None),
            ("Massed congregational singing (the Pacific voice)", None),
            ("Toward Micronesia & the island-pop era (roads ahead)", None),
        ],
    ),
]

STEM = "pacific_music_2_POLYNESIA"


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
