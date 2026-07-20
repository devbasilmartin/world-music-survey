#!/usr/bin/env python3
"""Build Sub-Saharan Africa: East, installment 3: The Cassette Era & Modern Swahili Pop.

Data as (section_title, intro, [(title, artist_or_None), ...]); emits the .md + _IMPORT.txt.
artist=None => bare title in the import file. Covers c. 1980-1995.
Dedup is by TITLE only -- every title unique region-wide.
"""

TITLE = ("The Story of East African Music — Installment 3: "
         "The Cassette Era & Modern Swahili Pop (c. 1980-1995)")

FRAMING = (
    "The cassette changed everything. Cheap to copy and carry, it broke the old 45-rpm order, "
    "democratized who could record and sell music, and pushed sound out of the capitals into every "
    "matatu, kiosk, and wedding. On the Swahili coast, TAARAB modernized and sped up: Zanzibar's "
    "Culture Musical Club and the immortal BI KIDUDE drove a faster, danceable, insult-trading style "
    "-- RUSHA ROHO and the small-ensemble kidumbak -- turning stately poetry into a competitive "
    "wedding sport. In Kenya the benga machine rolled into the 1980s (Kamba stars like Kakai Kilonzo), "
    "and the coastal band THEM MUSHROOMS minted the tourist-Swahili anthem 'Jambo Bwana' (Hakuna "
    "Matata). In Tanzania the dance bands hit a late golden peak -- DDC Mlimani Park's 'Sikinde' vs "
    "Orchestra Safari Sound -- and REMMY ONGALA became the conscience of dansi, singing about poverty "
    "and AIDS and breaking out to world stages. But economic liberalization and the cassette's own "
    "chaos began to fragment the big bands, seeding the studio pop -- bongo flava, genge -- to come. "
    "Cross-links: taarab's Arab/Indian roots (Installment 1); Congo rumba still echoing; the coming "
    "hip-hop era. Content note: the AIDS epidemic's toll is kept. Region-integrity note: Remmy Ongala "
    "and Samba Mapangala were Congolese-born pillars of the East African scene -- kept and flagged. "
    "Region: Kenya, Tanzania & Zanzibar."
)

SECTIONS = [
    (
        "THE CASSETTE REVOLUTION (c. 1980-1995)",
        "The compact cassette democratized East African music: anyone could dub, sell, and spread a "
        "recording, and the trade moved from a few city labels to a sprawl of kiosks and home tapers. "
        "It broadened access and killed the 45's dominance -- but its piracy also began to undercut the "
        "bands. Cross-link: the same shift that would soon enable bedroom bongo flava.",
        [
            ("The cassette boom (music democratized)", None),
            ("Home taping & the kiosk trade", None),
            ("Cassette piracy & the squeeze on bands", None),
            ("Music leaves the capitals (the matatu soundtrack)", None),
            ("The decline of the 45-rpm single", None),
        ],
    ),
    (
        "ZANZIBAR TAARAB MODERNIZES: RUSHA ROHO & BI KIDUDE (c. 1980-1995)",
        "Zanzibar's taarab sped up and let loose. The Culture Musical Club and star singers drove RUSHA "
        "ROHO ('release the soul') -- fast, danceable taarab whose lyrics traded veiled insults ("
        "mipasho) across the wedding floor -- and the small percussive KIDUMBAK. Presiding over it all "
        "was Bi Kidude, the fearless grande dame of Swahili music.",
        [
            ("Muhogo wa Jang'ombe", "Bi Kidude"),
            ("Rusha roho (fast danceable modern taarab)", None),
            ("Bi Kidude (the fearless grande dame of taarab)", None),
            ("Culture Musical Club (Zanzibar taarab institution)", None),
            ("Kidumbak (the small-ensemble taarab offshoot)", None),
            ("Mipasho (the taarab art of veiled insult)", None),
            ("East African Melody (modern taarab orchestra)", None),
        ],
    ),
    (
        "MOMBASA & THE COASTAL TAARAB (c. 1980-1995)",
        "Across the water on the Kenyan coast, Mombasa kept its own taarab tradition -- the oud master "
        "Zein l'Abidin among its greats -- woven through Swahili weddings and Maulidi celebrations. The "
        "coastal chakacha dance rhythm added a hip-swaying pulse. Cross-link: the Arab/Indian coastal "
        "roots of Installment 1, still living.",
        [
            ("Zein l'Abidin (Mombasa taarab oud master)", None),
            ("Mombasa taarab (the Kenyan coastal school)", None),
            ("Chakacha (the coastal wedding dance rhythm)", None),
            ("Swahili wedding & Maulidi music", None),
            ("The oud & violin on the Kenyan coast", None),
        ],
    ),
    (
        "KENYAN BENGA & VERNACULAR POP IN THE 1980s",
        "Benga rolled on as Kenya's pop backbone. Kakai Kilonzo and Les Kilimambogo made Kamba benga a "
        "national force; the Kalambya bands kept the up-country dancefloors full; and Luo, Kikuyu, and "
        "Luhya bands kept pressing cassettes. The sound was maturing even as the industry's economics "
        "wobbled.",
        [
            ("Kakai Kilonzo & Les Kilimambogo (Kamba benga star)", None),
            ("Kalambya Boys & Sisters (Kamba benga)", None),
            ("Luo benga into the 1980s (the machine rolls on)", None),
            ("Vernacular cassette pop (Kenya's many-tongued benga)", None),
            ("Benga guitar maturity (the 80s studio sound)", None),
        ],
    ),
    (
        "THEM MUSHROOMS & THE TOURIST-SWAHILI SOUND (c. 1982)",
        "On the Kenyan coast's hotel circuit, Them Mushrooms turned a welcome chant into 'Jambo Bwana' "
        "-- the 'Hakuna Matata' singalong that became the most globally recognized Swahili song and a "
        "tourist-era anthem. The coastal chakacha-pop scene turned hospitality into a whole style. "
        "Content note: the 'safari' packaging of African music, kept in view.",
        [
            ("Jambo Bwana", "Them Mushrooms"),
            ("Them Mushrooms & the coast hotel-band scene", None),
            ("Hakuna Matata (the tourist-Swahili anthem)", None),
            ("Chakacha-pop & the beach-resort sound", None),
            ("Swahili as a global pop phrase-book", None),
        ],
    ),
    (
        "TANZANIA'S LATE DANCE-BAND GOLDEN AGE (c. 1980-1992)",
        "Tanzania's muziki wa dansi peaked. DDC Mlimani Park -- its 'Sikinde' style a byword -- battled "
        "Orchestra Safari Sound in a legendary rivalry, while Msondo Ngoma and others kept the horn-and-"
        "guitar orchestras huge. This was the last, grandest flowering of the big Swahili dance band "
        "before liberalization thinned the ranks.",
        [
            ("Sikinde", "DDC Mlimani Park Orchestra"),
            ("The Sikinde versus Safari Sound rivalry", None),
            ("Msondo Ngoma (the enduring Dar orchestra)", None),
            ("Late muziki wa dansi (the orchestras at their peak)", None),
            ("Malako Disco", "Samba Mapangala"),
            ("Swahili dance-band arrangements (horns & rumba guitar)", None),
        ],
    ),
    (
        "REMMY ONGALA & THE CONSCIENCE OF DANSI (c. 1980-1994)",
        "Remmy Ongala -- 'Doctor Remmy', Congolese-born and Dar-based -- made his Orchestra Super "
        "Matimila the voice of the poor, singing plainly about hunger, injustice, and, daringly, AIDS "
        "('Mambo Kwa Soksi', a frank plea for condoms). His WOMAD and Real World releases carried "
        "Tanzanian dansi to the world. Content note: the AIDS epidemic; region-integrity: Congolese-"
        "born, flagged.",
        [
            ("Mambo Kwa Soksi", "Remmy Ongala"),
            ("Remmy Ongala & Orchestra Super Matimila (flagged Congolese-born)", None),
            ("Dansi as social conscience (songs of the poor)", None),
            ("Singing AIDS out loud (the condom song controversy)", None),
            ("Remmy Ongala goes global (WOMAD & Real World)", None),
        ],
    ),
    (
        "LIBERALIZATION, DECLINE & THE SEEDS OF THE NEW (c. 1990-1995)",
        "Economic liberalization, cassette piracy, and shifting tastes fragmented the big bands; state "
        "and parastatal patronage dried up. But the same open market and cheap studios that undercut "
        "the orchestras were about to hand microphones to a hip-hop generation. Cross-link: the seeds "
        "of bongo flava and genge, the modern era to come.",
        [
            ("Economic liberalization & the band decline", None),
            ("Parastatal patronage dries up (the orchestras fragment)", None),
            ("Cheap studios & the coming hip-hop generation", None),
            ("Seeds of bongo flava & genge (roads ahead)", None),
            ("From dance halls to cassette pop (the transition)", None),
        ],
    ),
]

STEM = "ssa_east_music_3_CASSETTE_ERA_SWAHILI_POP"


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
