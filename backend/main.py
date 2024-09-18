from fastapi import FastAPI
from pydantic import BaseModel
from linearP import LinearP
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScheduleRequest(BaseModel):
    days: list
    periods: list
    classes: list
    professors: list
    labs: list
    class_count: dict
    day_weights: dict
    period_weights: dict
    class_weights: dict
    professor_associations: dict
    restricoes_indisponibilidade_professors: dict
    restricoes_dependencia: dict

@app.post("/schedule")
def Schedule(request: ScheduleRequest):
    
    """
    model, X, Prof = LinearP(
        request.days, 
        request.periods, 
        request.classes, 
        request.professors, 
        request.labs, 
        request.class_count, 
        request.day_weights, 
        request.period_weights, 
        request.class_weights, 
        request.restricoes_indisponibilidade_professors, 
        request.restricoes_dependencia, 
        request.professor_associations
    ).initialize_model()
    """
    result = [
        {"day": "Segunda", "period": "7:15-8:55", "class": "Aula1", "professor": "ProfessorA"},
        {"day": "Segunda", "period": "9:05-10:45", "class": "Aula2", "professor": "ProfessorB"}
    ]
    return {"schedule": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)