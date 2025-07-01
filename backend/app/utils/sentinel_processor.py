import rasterio
import numpy as np

import os
from samgeo import SamGeo

def process_image_with_ai(image_path: str, output_path: str):
    with rasterio.open(image_path) as src:
        rgb = np.stack([src.read(4), src.read(3), src.read(2)], axis=-1)
    model = SamGeo(model_type="vit_b")
    segmented = model.predict(rgb)
    model.save(output_path)
    return output_path
