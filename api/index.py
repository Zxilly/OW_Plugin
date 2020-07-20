from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from cla import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def entry(account:str,password:str):
    a = Player(account,password)
    return a.getprofile()
    



if __name__ == '__main__':
    uvicorn.run(app='index:app', host="0.0.0.0", port=8000, reload=True, debug=True)