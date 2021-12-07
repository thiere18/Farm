data={"type":"FeatureCollection","features":[{"type":"Feature","properties":{"jj":""},"geometry":{"type":"Point","coordinates":[48.515625,67.87554134672945]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[129.375,68.26938680456564]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[77.6953125,56.559482483762245]}}]}

from typing import Any, List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user
from .. import oauth2
from app.repository import user_repository
from app.schemas import token, user as schemas
from ..database import get_db

router = APIRouter(
    prefix="/areas",
    tags=['Areas']
)

@router.get('/custom-areas')
def get_custom_areas():
    {"msg": "List of custom areas"}
    
@router.get('/custom-areas/{mrgid1}/{mrgid2}')
def get_custom_areas_params(mrgid1:int, mrgid2:int):
    return {"Area shapefile":mrgid1, "Areas geohashes":mrgid2}
    

@router.get('/geo-areas/{mrgid1},{mrgid2}', response_model=schemas.User)
def get_user(mrgid1: int, mrgid2: int)->Any:
    return {"Area shapefile":mrgid1, "Areas geohashes":mrgid2}

@router.put('/custom-areas/put', response_model=List[schemas.User])
def get_all_area_params()->Any:
    pass
 
