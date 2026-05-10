import json
from fastapi import FastAPI

app = FastAPI()

# Load hospital data from JSON
with open("hospital_data.json", "r") as file:
    hospital_data = json.load(file)

@app.get("/")
def home():
    return {"message": "Hospital Voice Helpdesk API Running"}

@app.get("/ask")
def ask(query: str):
    query = query.lower()
    for key in hospital_data:
        if key in query:
            return {"answer": hospital_data[key]}
    return {"answer": "Sorry, information not available"}
