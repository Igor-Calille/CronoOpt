from fastapi import FastAPI
from pydantic import BaseModel
from linearP import LinearP
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração do CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Substitua pelo endereço do seu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScheduleRequest(BaseModel):
    years: list
    days: list
    periods: list
    classes_per_year: dict
    professors: list  # Lista de todos os professores
    labs_per_year: dict
    class_count_per_year: dict
    day_weights: dict
    period_weights: dict
    class_weights: dict
    professor_associations_per_year: dict
    restricoes_indisponibilidade_professors: dict
    restricoes_dependencia: dict

@app.post("/schedule")
def Schedule(request: ScheduleRequest):
    """
    Endpoint para gerar o cronograma com base nos parâmetros fornecidos.

    Args:
        request (ScheduleRequest): Objeto contendo todos os parâmetros necessários.

    Returns:
        dict: Dicionário com o cronograma gerado.
    """
    # Inicializa o modelo com os parâmetros fornecidos
    final_schedule = LinearP(
        request.years,
        request.days, 
        request.periods, 
        request.classes_per_year, 
        request.professors,  # Passa a lista completa de professores
        request.labs_per_year, 
        request.class_count_per_year, 
        request.day_weights, 
        request.period_weights, 
        request.class_weights, 
        request.restricoes_indisponibilidade_professors, 
        request.restricoes_dependencia, 
        request.professor_associations_per_year
    ).initialize_model()

    return {"schedule": final_schedule}

if __name__ == "__main__":
    import uvicorn
    # Executa a aplicação FastAPI no endereço e porta especificados
    uvicorn.run(app, host="127.0.0.1", port=8000)
