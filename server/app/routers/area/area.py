data={"type":"FeatureCollection","features":[{"type":"Feature","properties":{"jj":""},"geometry":{"type":"Point","coordinates":[48.515625,67.87554134672945]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[129.375,68.26938680456564]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[77.6953125,56.559482483762245]}}]}

from typing import Any, List
from fastapi import  APIRouter
from app.config.config import settings
area_router = APIRouter(
    prefix="/areas",
    tags=['Areas']
)

@area_router.get('/custom-areas')
def get_custom_areas():
    {"msg": "List of custom areas"}
    
@area_router.get('/custom-areas/{mrgid1}/{mrgid2}')
def get_custom_areas_params(mrgid1:int, mrgid2:int):
    return {"Area shapefile":mrgid1, "Areas geohashes":mrgid2}
    

@area_router.get('/geo-areas/{mrgid1},{mrgid2}')
def get_user(mrgid1: int, mrgid2: int)->Any:
    return {"Area shapefile":mrgid1, "Areas geohashes":mrgid2}

@area_router.put('/custom-areas/put')
def get_all_area_params()->Any:
    pass
 
