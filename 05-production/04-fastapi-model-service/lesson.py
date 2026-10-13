"""FastAPI model service: Define a typed FastAPI request and prediction endpoint with explicit input validation.

Lesson walkthrough:
    1. Declare input schema: Require a number between 0 and 100.
    2. Connect schema and route: FastAPI validates request JSON before calling the handler.
    3. Start locally: Run `uvicorn lesson:app --reload` in this lesson folder and inspect `/docs`.

See README.md for concept explanations and a practice task.
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Course Prediction API")

class PredictionRequest(BaseModel):
    feature: float = Field(ge=0, le=100)

@app.post("/predict")
def predict(request: PredictionRequest) -> dict[str, float]:
    # Replace this transparent baseline with a loaded, versioned model.
    return {"prediction": request.feature * 0.5}

if __name__ == "__main__":
    print("Start locally with: uvicorn lesson:app --reload")
