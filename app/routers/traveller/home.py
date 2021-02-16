from typing import List

from fastapi import APIRouter, Depends
from neomodel import db
from pydantic import AnyUrl, BaseModel, constr

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import inflate_query_result
from ...models import database, validation
from ...models.database import Package

# from ...helpers.conversion import deflate_request

router = APIRouter()


class TopPackagesResponse(BaseModel):
    id: str
    name: constr(min_length=5, max_length=100)
    coverUri: AnyUrl
    rating: float


class TopDestinationResponse(BaseModel):
    id: str
    name: constr(min_length=10, max_length=100)
    coverUri: AnyUrl
    rating: float


class TopHotelResponse(BaseModel):
    id: str
    name: constr(max_length=120)
    coverUri: AnyUrl
    rating: float
    # TODO:Add these back
    # locality: str
    # city: str
    price: int


GET_TOP_PACKAGES_QUERY = """
MATCH (p:Package)-[r:REVIEWED_PACKAGE]-()
RETURN p.uid AS id, p.photos[0] AS coverUri, p.name AS name, AVG(r.rating) AS rating
ORDER BY rating DESC 
LIMIT $n
"""
GET_TOP_DESTINATIONS_QUERY = """
MATCH (c:City)-[r:REVIEWED_CITY]-()
RETURN c.uid AS id, c.photos[0] AS coverUri, c.name AS name, AVG(r.rating) AS rating
ORDER BY rating DESC 
LIMIT $n
"""
GET_TOP_HOTEL_QUERY = """
MATCH (h:Hotel)-[r:REVIEWED_HOTEL]-()
RETURN h.uid AS id, h.photos[0] AS coverUri, h.name AS name, AVG(r.rating) AS rating, h.price as price
ORDER BY rating DESC 
LIMIT $n
"""


# TODO: add back `user=Depends(get_registered_user)`,
@router.get("/topPackages", response_model=List[TopPackagesResponse])
async def get_top_packages(n: int = 3):
    return inflate_query_result(
        db.cypher_query(GET_TOP_PACKAGES_QUERY, {"n": n}), TopPackagesResponse
    )


@router.get("/topDestinations", response_model=List[TopDestinationResponse])
async def get_top_destinations(n: int = 5):
    return inflate_query_result(
        db.cypher_query(GET_TOP_DESTINATIONS_QUERY, {"n": n}), TopDestinationResponse
    )


@router.get("/topHotel", response_model=List[TopHotelResponse])
async def get_top_hotel(n: int = 5):
    return inflate_query_result(
        db.cypher_query(GET_TOP_HOTEL_QUERY, {"n": n}), TopHotelResponse
    )
