from fastapi import APIRouter

from apis.v1 import router_product


api_router = APIRouter()
api_router.include_router(router_product.router, prefix="/wines", tags=["wines"])
