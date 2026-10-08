"""Voice-over with word timings (edge-tts, pt-PT-DuarteNeural).

say(text, out_mp3) writes the audio and returns (duration_s, words), where
words = [(display_text, start_s, end_s)]. The voice reads the brand as
"Haive Code"; the words come back with the real spelling for the captions.
"""
import asyncio
import json
import re
import subprocess

import edge_tts

VOICE = "pt-PT-DuarteNeural"

# Spoken form -> how the brand is written on screen.
SPOKEN = [
    ("hivecode.pt/business", "Haive Code ponto pê tê barra bízness"),
    ("hivecode.pt", "Haive Code ponto pê tê"),
    ("HiveCode", "Haive Code"),
]
MERGE = [
    (["Haive", "Code", "ponto", "pê", "tê", "barra", "bízness"], "hivecode.pt/business"),
    (["Haive", "Code", "ponto", "pê", "tê"], "hivecode.pt"),
    (["Haive", "Code"], "HiveCode"),
]


def norm(word):
    return re.sub(r"[^\wÀ-ÿ]", "", word).lower()


def align(written, words):
    """Gives each written token (with punctuation) the time of the spoken piece(s) that say it.

    The voice can split a token ("perdem-se" -> "perdem", "se"), so pieces are
    joined until they spell the written token.
    """
    out, j = [], 0
    for token in written:
        target, got, start, end = norm(token), "", None, None
        while j < len(words) and (not got or len(got) < len(target)):
            piece = words[j]
            got += norm(piece[0])
            start = piece[1] if start is None else start
            end = piece[2]
            j += 1
        if got != target:
            raise ValueError(f"voice and text out of step at {token!r} (heard {got!r})")
        out.append((token, start, end))
    return out


def spoken(text):
    for written, said in SPOKEN:
        text = re.sub(re.escape(written), said, text, flags=re.I)
    return text


def merge(words):
    """Joins the spoken brand words back into the written brand, keeping trailing punctuation."""
    out, i = [], 0
    while i < len(words):
        for seq, written in MERGE:
            got = [re.sub(r"[^\wÀ-ÿ]", "", w[0]) for w in words[i:i + len(seq)]]
            if got == seq:
                tail = re.sub(r"^[\wÀ-ÿ]+", "", words[i + len(seq) - 1][0])
                out.append((written + tail, words[i][1], words[i + len(seq) - 1][2]))
                i += len(seq)
                break
        else:
            out.append(words[i])
            i += 1
    return out


async def _say(text, out_mp3, rate):
    comm = edge_tts.Communicate(spoken(text), VOICE, rate=rate, boundary="WordBoundary")
    words = []
    with open(out_mp3, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                start = chunk["offset"] / 1e7
                words.append((chunk["text"], start, start + chunk["duration"] / 1e7))
    return words


def duration(path):
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(json.loads(probe.stdout)["format"]["duration"])


def say(text, out_mp3, rate="+0%"):
    words = merge(asyncio.run(_say(text, out_mp3, rate)))
    # Word boundaries carry no punctuation; the written tokens put it back.
    return duration(out_mp3), align(text.split(), words)
