from fastapi import FastAPI,Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
import render
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

app.mount("/api", StaticFiles(directory="cache"), name="static")

class Item(BaseModel):
    data:str

@app.post("/update")
async def update(data:Item):
    profile = json.loads(data.data)['data']
    file_name = hashlib.md5(profile['player']['displayName'].encode(encoding='UTF-8')).hexdigest()
    with open('cache/'+file_name+'.svg','w+',encoding='UTF-8') as f:
        f.write(render.render(profile))
    return 'Successful update.Link is https://ow.plugin.learningman.top/api/'+file_name+'.svg'

""" 
async def entry(cred:str):
    with open('cache/'+cred+'.json','r+') as f:
        info = json.loads(f.read())
    account = info[0]
    password = info[1]
    a = Player(account,password)
    return_value = render.render(a.getprofile())
    return Response(content=return_value,media_type='image/svg+xml')
"""



if __name__ == '__main__':
    uvicorn.run(app='index:app', host="0.0.0.0", port=3000, reload=False, debug=True)