# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import api  # Importing the api module you created

# Initialize FastAPI app
app = FastAPI()

# Request model
class QueryRequest(BaseModel):
    question: str

# Response model
class QueryResponse(BaseModel):
    answer: str

# API endpoint to handle question
@app.post("/ask/", response_model=QueryResponse)
def ask_question(query: QueryRequest):
    try:
        # Use the function from api.py
        result_text = api.ask_question(query.question)
        return QueryResponse(answer=result_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Google Generative AI integration!"}
