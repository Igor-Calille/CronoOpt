import pulp

class LinearP():
    def __init__(
            self, 
            days, 
            periods, 
            classes, 
            professors,
            labs, 
            class_count, 
            day_weights, 
            period_weights,
            class_weights,
            restricoes_indisponibilidade_professors,
            restricoes_dependencia,
            professor_associations
        ) -> None:
        self.days = days
        self.periods = periods
        self.classes = classes
        self.professors = professors
        self.labs = labs
        self.class_count = class_count
        self.day_weights = day_weights
        self.period_weights = period_weights
        self.class_weights = class_weights
        self.restricoes_indisponibilidade_professors = restricoes_indisponibilidade_professors
        self.restricoes_dependencia = restricoes_dependencia
        self.professor_associations = professor_associations


        

    def initialize_model(self):
        model = pulp.LpProblem("Class_Scheduling", pulp.LpMaximize)
        X = pulp.LpVariable.dicts("X", (self.days, self.periods, self.classes), cat='Binary')
        Prof = pulp.LpVariable.dicts("Prof", (self.days, self.periods, self.classes, self.professors), cat='Binary')

        # Função Objetivo: Maximizar o valor total das alocações com pesos (incluir a alocação de professores)
        model += pulp.lpSum(self.day_weights[d] * self.period_weights[p] * self.class_weights[t] * X[d][p][t]
                            for d in self.days for p in self.periods for t in self.classes)

        # Restrições

        # 1. Garantir que cada aula ocorra o número certo de vezes por semana
        for t in self.classes:
            model += pulp.lpSum(X[d][p][t] for d in self.days for p in self.periods) == self.class_count[t], f"Total_{t}"

        # 2. Garantir que não haja sobreposição de aulas no mesmo período e dia
        for d in self.days:
            for p in self.periods:
                model += pulp.lpSum(X[d][p][t] for t in self.classes) <= 1, f"No_Overlap_{d}_{p}"

        # 3. Garantir que um professor só seja atribuído a uma aula por vez
        for d in self.days:
            for p in self.periods:
                for prof in self.professors:
                    model += pulp.lpSum(Prof[d][p][t][prof] for t in self.classes) <= 1, f"Prof_Unique_{prof}_{d}_{p}"

        # 4. Garantir que cada aula tenha um professor específico atribuído
        for t, assigned_prof in self.professor_associations.items():
            for d in self.days:
                for p in self.periods:
                    # A associação correta deve garantir que, se uma aula é alocada, o professor também o é
                    model += Prof[d][p][t][assigned_prof] == X[d][p][t], f"Prof_Assigned_{t}_{assigned_prof}_{d}_{p}"

        # Restrições de laboratórios
        for d in self.days:
            model += pulp.lpSum(X[d][p][t] for p in self.periods for t in self.labs) <= 2, f"Max_Labs_Per_Day_{d}"

        model += pulp.lpSum(X[d][p][t] for d in self.days for p in self.periods for t in self.labs) <= 10, "Max_Labs_Week"

        # Adicionando as restrições para professores indisponíveis
        for prof, restricoes in self.restricoes_indisponibilidade_professors.items():
            for (dia, periodo) in restricoes:
                for t in self.classes:
                    model += Prof[dia][periodo][t][prof] == 0, f"Restricao_Prof_{prof}_{dia}_{periodo}_{t}"

        # Adicionando as restrições para alunos com dependência
        for t, restricoes in self.restricoes_dependencia.items():
            for (dia, periodo) in restricoes:
                model += X[dia][periodo][t] == 0, f"Restricao_Dependencia_{dia}_{periodo}_{t}"

        model.solve()

        return model, X, Prof