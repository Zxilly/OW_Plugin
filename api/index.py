from fastapi import FastAPI,Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import render
from cla import *
import hashlib
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def entry(cred:str):
    with open('cache/'+cred+'.json','r+') as f:
        info = json.loads(f.read())
    account = info[0]
    password = info[1]
    a = Player(account,password)
    return_value = render.render(a.getprofile())
    return Response(content=return_value,media_type='image/svg+xml')

@app.get("/reg")
async def register(account:str,password:str):
    md5_string = hashlib.md5((account+password).encode(encoding='UTF-8')).hexdigest()
    cred = json.dumps((account,password))
    with open('cache/'+md5_string+'.json','w+') as f:
        f.write(cred)
    return 'https://ow.plugin.learningman.top/api?cred='+md5_string

    



if __name__ == '__main__':
    uvicorn.run(app='index:app', host="0.0.0.0", port=3000, reload=False, debug=False)