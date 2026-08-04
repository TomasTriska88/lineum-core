#!/usr/bin/env python3
"""Load and execute the losslessly compressed frozen B4 research runner."""
from pathlib import Path
import lzma

_SOURCE = Path(__file__).with_name("lineum_public_tolog_galactic_shape_b4_source.py.xz")
_CODE = lzma.decompress(_SOURCE.read_bytes())
exec(compile(_CODE, str(_SOURCE), "exec"), {"__name__": "__main__", "__file__": str(_SOURCE)})
