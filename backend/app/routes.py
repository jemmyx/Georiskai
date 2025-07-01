from fastapi import APIRouter
from app.utils import sentinel_downloader

router = APIRouter()
router.include_router(sentinel_downloader.router)
