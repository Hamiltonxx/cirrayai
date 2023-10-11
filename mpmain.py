from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    return {"message":"Hello World!"}

@app.get("/mp/callback")
async def mp_callback(echostr=None):
    if echostr:
        # return q.get("echostr")
        return echostr
    return "No q"
    