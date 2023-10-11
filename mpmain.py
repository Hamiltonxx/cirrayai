from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
#    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    return {"message":"Hello World!"}

@app.get("/echocallback")
async def echocallback(echostr=None):
    if echostr:
        # return q.get("echostr")
        return echostr
    return "No q"

if __name__ == '__main__':
    uvicorn.run("mpmain:app", host="0.0.0.0", port=8000)
    