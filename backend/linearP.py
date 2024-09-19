import pulp

class LinearP():
    def __init__(
            self, 
            years,
            days, 
            periods, 
            classes_per_year, 
            professors,
            labs_per_year, 
            class_count_per_year, 
            day_weights, 
            period_weights,
            class_weights,
            restricoes_indisponibilidade_professors,
            restricoes_dependencia,
            professor_associations_per_year
        ) -> None:
        """
        Inicializa os parâmetros necessários para a criação do modelo de programação linear.

        Args:
            years (list): Lista de anos a serem considerados.
            days (list): Lista de dias da semana.
            periods (list): Lista de períodos disponíveis em cada dia.
            classes_per_year (dict): Dicionário mapeando cada ano para a lista de aulas correspondentes.
            professors (list): Lista de todos os professores.
            labs_per_year (dict): Dicionário mapeando cada ano para a lista de aulas que são laboratórios.
            class_count_per_year (dict): Dicionário mapeando cada ano para um dicionário que mapeia cada aula para o número de vezes que deve ocorrer por semana.
            day_weights (dict): Dicionário de pesos para os dias.
            period_weights (dict): Dicionário de pesos para os períodos.
            class_weights (dict): Dicionário de pesos para as aulas.
            restricoes_indisponibilidade_professors (dict): Dicionário com restrições de indisponibilidade dos professores.
            restricoes_dependencia (dict): Dicionário com restrições de dependência de alunos.
            professor_associations_per_year (dict): Dicionário mapeando cada ano para um dicionário que associa aulas a professores.
        """
        self.years = years
        self.days = days
        self.periods = periods
        self.classes_per_year = classes_per_year
        self.professors = professors
        self.labs_per_year = labs_per_year
        self.class_count_per_year = class_count_per_year
        self.day_weights = day_weights
        self.period_weights = period_weights
        self.class_weights = class_weights
        self.restricoes_indisponibilidade_professors = restricoes_indisponibilidade_professors
        self.restricoes_dependencia = restricoes_dependencia
        self.professor_associations_per_year = professor_associations_per_year

    def initialize_model(self):
        """
        Inicializa e resolve o modelo de programação linear para cada ano, levando em consideração
        as restrições e atualizando as indisponibilidades dos professores.

        Returns:
            list: Lista contendo o cronograma final com as alocações de aulas, professores, dias e períodos.
        """
        final_schedule = []

        # Dicionário para rastrear indisponibilidade dinâmica de professores
        indisponibilidade_professors = self.restricoes_indisponibilidade_professors.copy()

        # Variáveis globais para rastrear alocações de professores em todos os anos
        Prof_all_years = {}

        for y in self.years:
            # Cria um novo modelo para o ano atual
            model = pulp.LpProblem(f"Class_Scheduling_Year_{y}", pulp.LpMaximize)
            classes = self.classes_per_year[str(y)]
            labs = self.labs_per_year.get(str(y), [])
            class_count = self.class_count_per_year[str(y)]
            professor_associations = self.professor_associations_per_year[str(y)]

            # Variáveis de decisão
            X = pulp.LpVariable.dicts(f"X_{y}", (self.days, self.periods, classes), cat='Binary')
            Prof = pulp.LpVariable.dicts(f"Prof_{y}", (self.days, self.periods, classes, self.professors), cat='Binary')

            # Adiciona Prof ao dicionário global
            Prof_all_years[y] = Prof

            # Função Objetivo
            model += pulp.lpSum(
                self.day_weights[d] * self.period_weights[p] * self.class_weights.get(t, 1.0) * X[d][p][t]
                for d in self.days for p in self.periods for t in classes
            )

            # Restrições

            # 1. Cada aula deve ocorrer o número correto de vezes por semana
            for t in classes:
                model += (
                    pulp.lpSum(X[d][p][t] for d in self.days for p in self.periods) == class_count[t],
                    f"Total_{t}_Year_{y}"
                )

            # 2. Não deve haver sobreposição de aulas no mesmo dia e período
            for d in self.days:
                for p in self.periods:
                    model += (
                        pulp.lpSum(X[d][p][t] for t in classes) <= 1,
                        f"No_Overlap_{d}_{p}_Year_{y}"
                    )

            # 3. Professores não podem lecionar mais de uma aula ao mesmo tempo em todos os anos
            for d in self.days:
                for p in self.periods:
                    for prof in self.professors:
                        total_classes = []

                        # Verificar todas as aulas que o professor pode estar lecionando neste período em todos os anos
                        for yy in self.years:
                            if yy <= y:
                                Prof_yy = Prof_all_years.get(yy)
                                if Prof_yy:
                                    classes_yy = self.classes_per_year[str(yy)]
                                    total_classes.extend([Prof_yy[d][p][t][prof] for t in classes_yy if (d in Prof_yy and p in Prof_yy[d] and t in Prof_yy[d][p])])

                        # Soma das aulas que o professor está lecionando neste período
                        if total_classes:
                            model += (
                                pulp.lpSum(total_classes) <= 1,
                                f"Prof_Unique_{prof}_{d}_{p}_UpTo_Year_{y}"
                            )

            # 4. Cada aula deve ter o professor correto atribuído
            for t, assigned_prof in professor_associations.items():
                for d in self.days:
                    for p in self.periods:
                        model += (
                            Prof[d][p][t][assigned_prof] == X[d][p][t],
                            f"Prof_Assigned_{t}_{assigned_prof}_{d}_{p}_Year_{y}"
                        )

            # Restrições de laboratórios
            for d in self.days:
                model += (
                    pulp.lpSum(X[d][p][t] for p in self.periods for t in labs) <= 2,
                    f"Max_Labs_Per_Day_{d}_Year_{y}"
                )

            model += (
                pulp.lpSum(X[d][p][t] for d in self.days for p in self.periods for t in labs) <= 10,
                f"Max_Labs_Week_Year_{y}"
            )

            # Restrições de indisponibilidade de professores
            for prof in self.professors:
                restricoes = indisponibilidade_professors.get(prof, [])
                for (dia, periodo) in restricoes:
                    for t in classes:
                        if professor_associations.get(t) == prof:
                            model += (
                                Prof[dia][periodo][t][prof] == 0,
                                f"Restricao_Prof_{prof}_{dia}_{periodo}_{t}_Year_{y}"
                            )

            # Restrições de dependência de alunos
            for t, restricoes in self.restricoes_dependencia.items():
                if t in classes:
                    for (dia, periodo) in restricoes:
                        model += (
                            X[dia][periodo][t] == 0,
                            f"Restricao_Dependencia_{dia}_{periodo}_{t}_Year_{y}"
                        )

            # Resolver o modelo
            model.solve()

            # Extrair o cronograma
            year_schedule = []
            for d in self.days:
                for p in self.periods:
                    for t in classes:
                        if pulp.value(X[d][p][t]) == 1:
                            assigned_prof = next(
                                (prof for prof in self.professors if pulp.value(Prof[d][p][t][prof]) == 1), 
                                None
                            )
                            year_schedule.append({
                                "year": y,
                                "day": d,
                                "period": p,
                                "class": t,
                                "professor": assigned_prof
                            })

                            # Atualizar indisponibilidade do professor para os próximos anos
                            if assigned_prof:
                                if assigned_prof not in indisponibilidade_professors:
                                    indisponibilidade_professors[assigned_prof] = []
                                indisponibilidade_professors[assigned_prof].append((d, p))

            # Adiciona o cronograma do ano atual ao cronograma final
            final_schedule.extend(year_schedule)

        return final_schedule
