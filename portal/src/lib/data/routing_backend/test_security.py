from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_dos_oversized_grid():
    payload = {
        "resolution": 4000,
        "pump_cycles": 1500
    }
    resp = client.post("/api/v1/ai/true-rng", json=payload)
    # Pydantic should return 422 Unprocessable Entity because le=256
    assert resp.status_code == 422
    assert "resolution" in resp.text

    # RouteRequest test
    payload_route = {
        "size": 1024,
        "agents": [],
        "target": {"x": 10, "y": 10},
        "kappa_flat": [1.0] * (1024*1024),
        "max_steps": 5000
    }
    resp_route = client.post("/api/route/task", json=payload_route)
    assert resp_route.status_code == 422
    assert "size" in resp_route.text
    
def test_dos_oversized_payload():
    payload = {
        "payload": "A" * 20000, # 20kb string
        "grid_size": 64,
        "iterations": 1500
    }
    resp = client.post("/api/v1/ai/hash", json=payload)
    assert resp.status_code == 422
    # The max length string violation will throw a 422 error
