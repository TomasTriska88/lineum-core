"""Access to immutable public resources shipped with Lineum Core."""

import json
from importlib.resources import files
from typing import Any


def load_claims() -> list[dict[str, Any]]:
    """Load the claim registry that belongs to the installed Core version."""
    resource = files("lineum_core.data").joinpath("claims.json")
    return json.loads(resource.read_text(encoding="utf-8"))
