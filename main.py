import json
from fastapi import FastAPI
from nlp_engine import get_intent

app = FastAPI()

# Load hospital data
with open("hospital_data.json", "r") as file:
    hospital_data = json.load(file)

@app.get("/")
def home():
    return {"message": "Hospital Voice Helpdesk API Running"}

@app.get("/ask")
def ask(query: str):

    query = query.lower().strip()

    if query == "":
        return {"answer": "Empty input", "intent": "none"}

    # NLP INTENT DETECTION
    intent = get_intent(query)

    # RESPONSE
    answer = hospital_data.get(intent, "Sorry, information not available")

    return {
        "query": query,
        "intent": intent,
        "answer": answer
    }