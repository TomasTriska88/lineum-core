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
    from tools.build_vfx_pack import run_vfx
    run_vfx("water_drop", view_sizes=[64], variant=1)
    
    webp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'output_assets', 'vfx_pack', 'water_drop_v1_64.webp'))
    assert os.path.exists(webp_path), "Generated WebP asset does not exist."
    
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
