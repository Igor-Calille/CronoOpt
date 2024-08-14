
import pulp

# Definindo o problema
model = pulp.LpProblem("Class_Scheduling", pulp.LpMaximize)

# Parâmetros
days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
periods = ["7:15-8:55", "9:05-10:45", "10:55-12:35"]
classes = ["Aula1", "Aula2", "Aula3", "Aula4", "Aula5", "Aula6", "Aula7", "Aula8", "Aula9"]

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
    "Aula9": 1.0,
    "Aula10": 1.0
}

# Variáveis de decisão
X = pulp.LpVariable.dicts("X", (days, periods, classes), cat='Binary')

# Função Objetivo: Maximizar o valor total das alocações com pesos
model += pulp.lpSum(day_weights[d] * period_weights[p] * class_weights[t] * X[d][p][t]
                    for d in days for p in periods for t in classes)

# Restrições

# 1. Garantir que cada aula ocorra o número certo de vezes por semana
for t in classes:
    model += pulp.lpSum(X[d][p][t] for d in days for p in periods) == class_count[t], f"Total_{t}"

# 2. Garantir que não haja sobreposição de aulas no mesmo período e dia
for d in days:
    for p in periods:
        model += pulp.lpSum(X[d][p][t] for t in classes) <= 1, f"No_Overlap_{d}_{p}"

# Combinar todas as restrições de indisponibilidade
restricoes_indisponibilidade = {
    "Aula1": [("Terça", "9:05-10:45"), ("Quinta", "9:05-10:45")],  # Restrição do professor
    "Aula5": [("Segunda", "7:15-8:55")],  # Restrição do professor
}

restricoes_dependencia = {
    "Aula3": [("Quarta", "10:55-12:35")],  # Restrição de aluno com dependência
    "Aula4": [("Sexta", "7:15-8:55")]  # Restrição de aluno com dependência
}

# Unindo as restrições dos professores e alunos
for t, restricoes in {**restricoes_indisponibilidade, **restricoes_dependencia}.items():
    for (dia, periodo) in restricoes:
        model += X[dia][periodo][t] == 0, f"Restricao_{dia}_{periodo}_{t}"

# Resolvendo o problema
model.solve()

# Status do resultado
print(f"Status: {pulp.LpStatus[model.status]}")

# Exibindo o cronograma
for d in days:
    print(f"\nCronograma para {d}:")
    for p in periods:
        for t in classes:
            if X[d][p][t].value() == 1:
                print(f"{p}: {t}")
