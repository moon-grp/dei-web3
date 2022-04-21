from fastapi import APIRouter

basicEth = APIRouter()


@basicEth.get("/hello", tags=["basic eth"])
async def hello():
    print("helloooo")