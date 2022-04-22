from fastapi import APIRouter
from web3 import Web3
from pydantic import BaseModel
from dotenv import load_dotenv
basicEth = APIRouter()
import os
load_dotenv()


infuraUrl = os.getenv("IUrl")




class ethInput(BaseModel):
    addr: str
    

@basicEth.get("/get", tags=["basic eth"])
async def hello():
    web3 = Web3(Web3.HTTPProvider(infuraUrl))
    check  = web3.isConnected()
    print (check)
    

@basicEth.get("/latestblock", tags=["basic eth"])
async def get_latest_block():
    web3 = Web3(Web3.HTTPProvider(infuraUrl))
    latestBlock  = web3.eth.blockNumber
    print (latestBlock)


@basicEth.post("/getaddressbalance", tags=["basic eth"])
async def get_address_balance(details:ethInput):
    web3 = Web3(Web3.HTTPProvider(infuraUrl))
    balance  = web3.eth.getBalance(details.addr)
    balanceInWEi = web3.fromWei(balance, "ether")
    print (balance, balanceInWEi)
   