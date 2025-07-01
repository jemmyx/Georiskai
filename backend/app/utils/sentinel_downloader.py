from fastapi import APIRouter
from pydantic import BaseModel
from sentinelsat import SentinelAPI
from app.utils.sentinel_processor import process_image_with_ai
from app.utils.uploader import upload_to_s3

router = APIRouter()

class AreaRequest(BaseModel):
    min_lon: float
    min_lat: float
    max_lon: float
    max_lat: float

@router.post("/download-sentinel")
def download_sentinel_image(area: AreaRequest):
    api = SentinelAPI("your_username", "your_password", "https://scihub.copernicus.eu/dhus")
    footprint = f"POLYGON(({area.min_lon} {area.min_lat}, {area.min_lon} {area.max_lat}, {area.max_lon} {area.max_lat}, {area.max_lon} {area.min_lat}, {area.min_lon} {area.min_lat}))"

    products = api.query(
        footprint,
        date=('20240101', '20240630'),
        platformname='Sentinel-2',
        processinglevel='Level-2A',
        cloudcoverpercentage=(0, 10)
    )

    if not products:
        return {"message": "Aucun produit disponible pour cette zone."}

    product_id = list(products.keys())[0]
    product_info = api.download(product_id, directory_path="downloads")

    output_path = f"processed/{product_id}_mask.tif"
    os.makedirs("processed", exist_ok=True)
    processed_path = process_image_with_ai(product_info['path'], output_path)

    url = upload_to_s3(processed_path, "georiskai-bucket", os.path.basename(processed_path))
    return {"message": "Téléchargement et traitement terminés", "product_id": product_id, "s3_url": url}
