""" Health Router """
from fastapi import APIRouter

from ..internal import constants
from ..models.api_health import ApiHealth

router = APIRouter(
    prefix="/api/health",
    tags=["Application"]
)

@router.get("", response_model=ApiHealth)
async def api_health_check():
    """ API Health check endpoint. """
    return ApiHealth(version=constants.api_version)
