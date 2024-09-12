from backend.linearP import LinearP
import pulp

# Parâmetros de entrada
days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
periods = ["7:15-8:55", "9:05-10:45", "10:55-12:35"]
classes = ["Aula1", "Aula2", "Aula3", "Aula4", "Aula5", "Aula6", "Aula7", "Aula8", "Aula9"]
professors = ["ProfessorA", "ProfessorB", "ProfessorC", "ProfessorD", "ProfessorE"]
labs = ["Aula3", "Aula5", "Aula7"]

# Quantas vezes cada aula deve ocorrer por semana
class_count = {
    "Aula1": 2,
    "Aula2": 2,
    "Aula3": 1,
    "Aula4": 1,
    "Aula5": 2,
    "Aula6": 1,
    "Aula7": 1,
    "Aula8": 2,
    "Aula9": 1
}

# Definindo os pesos para dias, horários e tipos de aula
day_weights = {
    "Segunda": 1.0,
    "Terça": 1.0,
    "Quarta": 1.0,
    "Quinta": 1.0,
    "Sexta": 1.0
}

period_weights = {
    "7:15-8:55": 1.5,  # Prioridade para o primeiro período
    "9:05-10:45": 1.0,
    "10:55-12:35": 0.7
}

class_weights = {
    "Aula1": 1.0,
    "Aula2": 1.0,
    "Aula3": 1.0,
    "Aula4": 1.0,
    "Aula5": 1.0,
    "Aula6": 1.0,
    "Aula7": 1.0,
    "Aula8": 1.0,
    "Aula9": 1.0
}

# Mapeamento dos professores para cada aula
professor_associations = {
    "Aula1": "ProfessorA",
    "Aula2": "ProfessorB",
    "Aula3": "ProfessorC",
    "Aula4": "ProfessorD",
    "Aula5": "ProfessorE",
    "Aula6": "ProfessorA",
    "Aula7": "ProfessorB",
    "Aula8": "ProfessorC",
    "Aula9": "ProfessorD"
}

# Restrições dinâmicas de indisponibilidade de professores
restricoes_indisponibilidade_professors = {
    "ProfessorA": [("Terça", "9:05-10:45"), ("Quinta", "9:05-10:45")],
    "ProfessorB": [("Segunda", "7:15-8:55")]
}

restricoes_dependencia = {
    "Aula3": [("Quarta", "10:55-12:35")],  # Restrição de aluno com dependência
    "Aula4": [("Sexta", "7:15-8:55")]  # Restrição de aluno com dependência
}

# Inicializando o modelo
model, X, Prof = LinearP(days, periods, classes, professors, labs, class_count, day_weights, period_weights, class_weights, restricoes_indisponibilidade_professors, restricoes_dependencia, professor_associations).initialize_model()

# Status do resultado
print(f"Status: {pulp.LpStatus[model.status]}")

# Exibindo o cronograma
for d in days:
    print(f"\nCronograma para {d}:")
    for p in periods:
        for t in classes:
            if X[d][p][t].value() == 1:
                print(f"{p}: {t}")
                assigned_professor = None
                for prof in professors:
                    if Prof[d][p][t][prof].value() == 1:
                        assigned_professor = prof
                        break
                if assigned_professor:
                    print(f"   Professor: {assigned_professor}")
                else:
                    print("   Professor: Não atribuído")
