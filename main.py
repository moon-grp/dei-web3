from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.basic_eth import basicEth


app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(basicEth, prefix="/api/v1/basiceth")