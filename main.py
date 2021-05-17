from fastapi import Request, FastAPI
from pydantic import BaseModel
from functions import computeTextSimilarity
app = FastAPI()


class item(BaseModel):
    text1:str
    text2:str

@app.get("/")
def index():
    return "Welcome to Fetch Word Similarity Check!"


@app.post("/")
def get_body(request: item):

    ins = computeTextSimilarity(request.text1, request.text2)
    result = ins.similarity(2)
    return {'similarity score between these two sentences are': str(result)}
