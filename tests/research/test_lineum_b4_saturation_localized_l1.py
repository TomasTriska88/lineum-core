#!/usr/bin/env python3
"""Verified pytest loader for the canonical permanent tests embedded in the standalone B4 report."""
from __future__ import annotations
import hashlib, io, lzma, tarfile
from pathlib import Path
_REPORT = Path(__file__).resolve().parents[2] / "research" / "lineum-public-tolog-galactic-shape-b4.md"
_text = _REPORT.read_text(encoding="utf-8")
_heading = "#### Normalized complete-history archive — XZ plus Unicode15"
_s = _text.rindex(_heading); _b = _text.index("```text", _s) + len("```text"); _e = _text.index("```", _b)
_acc = _bits = 0; _compressed = bytearray()
for _char in "".join(_text[_b:_e].split()):
    _value = ord(_char) - 0x3400
    if not 0 <= _value < (1 << 15): raise RuntimeError("Invalid Unicode15 archive character")
    _acc = (_acc << 15) | _value; _bits += 15
    while _bits >= 8 and len(_compressed) < 34756:
        _bits -= 8; _compressed.append((_acc >> _bits) & 0xFF); _acc &= (1 << _bits) - 1 if _bits else 0
if len(_compressed) != 34756 or hashlib.sha256(_compressed).hexdigest() != "171f2862469b19cc0aa003f173fb87d093c1c960c6651bfb493f72a09140f36f": raise RuntimeError("Embedded archive fingerprint mismatch")
_tar = lzma.decompress(bytes(_compressed))
with tarfile.open(fileobj=io.BytesIO(_tar), mode="r:") as _tf: _CANONICAL_SOURCE = _tf.extractfile("tests/research/test_lineum_b4_saturation_localized_l1.py").read()
if hashlib.sha256(_CANONICAL_SOURCE).hexdigest() != "95a5892f140543361eaffbee311016869e780f9bd21c559757b02b427f3b19ec": raise RuntimeError("Embedded canonical source fingerprint mismatch")
exec(compile(_CANONICAL_SOURCE, __file__, "exec"), globals(), globals())
