# Sistema de Definição de Cronograma de Aulas

## Visão Geral

Este projeto tem como objetivo desenvolver um sistema automatizado para a definição de cronogramas de aulas em uma instituição de ensino. A motivação principal é solucionar problemas recorrentes na organização dos horários das aulas, que atualmente são geridos de forma ineficiente, resultando em conflitos de horários, "buracos" entre as aulas, e indisponibilidade de professores e alunos. O sistema utiliza técnicas de Programação Linear Inteira (ILP) para otimizar o agendamento das aulas, considerando diversas restrições e preferências.

## Principais Requisitos

### 1. **Definição de Horários e Dias:**
   - **Dias da Semana:** Segunda a Sexta.
   - **Horários das Aulas:**
     - 7:15 - 8:55
     - 9:05 - 10:45
     - 10:55 - 12:35

### 2. **Tipos de Aulas:**
   - O sistema gerencia até 10 tipos diferentes de aulas, com diferentes frequências semanais.

### 3. **Restrições Consideradas:**
   - **Frequência das Aulas:** Certas aulas precisam ocorrer mais de uma vez por semana (ex.: Aula 1 deve ocorrer 2 vezes por semana).
   - **Indisponibilidade de Professores:** Certos professores não estão disponíveis em determinados dias e horários (ex.: O professor da Aula 1 não pode dar aula às terças e quintas no período das 9:05 - 10:45).
   - **Alunos com Dependências:** Alunos que possuem matérias de dependência não podem ter aulas em determinados horários para evitar conflitos (ex.: Aula 3 não pode ocorrer na quarta-feira das 10:55 - 12:35).

### 4. **Objetivo de Otimização:**
   - O sistema busca maximizar a eficiência do cronograma considerando os pesos atribuídos aos dias, horários e tipos de aula. Isso inclui priorizar o início das aulas às 7:15 e evitar horários indesejados.

## Motivações para o Projeto

### 1. **Solução de Problemas Práticos:**
   - A organização manual de cronogramas é suscetível a erros e ineficiências, resultando em horários mal distribuídos, sobreposição de aulas e indisponibilidade de professores e alunos. Este sistema automatizado visa minimizar esses problemas, criando cronogramas otimizados e funcionais.

### 2. **Aplicação de Técnicas de Otimização:**
   - O projeto é uma excelente oportunidade para aplicar conceitos de Programação Linear Inteira (ILP), que são amplamente utilizados em problemas de otimização combinatória, como o agendamento de aulas. Essa aplicação prática permite explorar as capacidades de técnicas matemáticas para resolver problemas complexos do mundo real.

### 3. **Melhoria na Experiência Educacional:**
   - Com um cronograma mais bem organizado, a experiência educacional de professores e alunos melhora significativamente. Os professores podem evitar horários indesejados, e os alunos têm um cronograma que minimiza conflitos e "buracos", facilitando o planejamento de suas atividades acadêmicas.

### 4. **Flexibilidade e Escalabilidade:**
   - O sistema foi projetado para ser flexível e facilmente adaptável a diferentes contextos e necessidades. Novas restrições podem ser adicionadas com facilidade, e o modelo pode ser ajustado para diferentes números de aulas, dias e períodos.

## Conclusão

Este sistema de definição de cronograma de aulas é uma ferramenta poderosa para instituições de ensino que buscam otimizar a alocação de aulas, levando em consideração as necessidades e restrições de professores e alunos. Com uma abordagem baseada em otimização matemática, o projeto demonstra como a tecnologia pode ser aplicada para melhorar processos educacionais críticos.

---

