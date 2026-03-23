import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PIL import Image

def test_webp_framerate_is_cinematic():
    """
    Asserts that the exported animated VFX WebP deliverables 
    are properly encoded at a cinematic 30+ FPS (duration <= 34ms).
    Prevents regressions into a 'slideshow' 10 FPS state.
    """
    webp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'output_assets', 'water_drop_32.webp'))
    assert os.path.exists(webp_path), "Asset WebP does not exist. Run generate_droplet.py first."
    
    with Image.open(webp_path) as img:
        assert getattr(img, "is_animated", False), "Output is not an animated format."
        
        duration = img.info.get('duration', None)
        if duration is None:
            try:
                img.seek(1)
                duration = img.info.get('duration', None)
            except EOFError:
                pass
                
        if isinstance(duration, list):
            duration = duration[0]
            
        if duration is not None and duration > 0:
            # 33ms or 16ms is allowed (30-60 fps). 100ms (10 fps) or slideshows are forbidden!
            assert duration <= 34, f"VFX exported as an unacceptable slideshow! Duration must be <= 34ms. Found: {duration}ms"

def test_api_dynamic_frame_scaling():
    """
    Test that the asset API accurately bounds the physics dynamically,
    no matter what frame count is requested via REST payload without crashing velocity limits.
    """
    from routing_backend.asset_api import generate_water_drop, VfxRequest
    req = VfxRequest(grid_size=16, frames=5, colormap="magma")
    
    res = generate_water_drop(req)
    assert len(res["frames"]) == 5, "API failed to generate the explicitly requested dynamic frame count bounds."
