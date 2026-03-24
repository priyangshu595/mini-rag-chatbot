from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.retrieve import retrieve
from app.generate import generate_answer, generate_answer_local

app = FastAPI()

USE_LOCAL = False   # change True/False to switch

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ask")
def ask(query: str):
    context = retrieve(query)

    if USE_LOCAL:
        answer = generate_answer_local(query, context)
    else:
        answer = generate_answer(query, context)

    return {
        "query": query,
        "retrieved_context": context,
        "answer": answer
    }