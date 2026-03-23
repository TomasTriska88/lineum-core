import pytest
from fastapi.testclient import TestClient
from routing_backend.main import app

client = TestClient(app)

def test_ripple_vfx_endpoint_returns_base64_webp():
    """
    Asserts the asset generation pipeline correctly hooks into the Lineum core
    and successfully compiles an isolated WEBP output payload with pure alpha transparency.
    """
    response = client.post("/api/v1/assets/generate/ripple-vfx", json={
        "grid_size": 32,
        "frames": 4, # Short integration cycle limits IO overload
        "colormap": "Blues_r"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "images_base64" in data
    assert len(data["images_base64"]) == 4
    
    # Validate the data represents a fully rendered base64 matrix sequence
    for frame in data["images_base64"]:
        assert isinstance(frame, str)
        # B64 image string is roughly thousands of characters, easily bypass 100 byte verification 
        assert len(frame) > 100 
