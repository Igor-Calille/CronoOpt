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

## Implementação

A implementação do sistema de definição de cronogramas foi realizada utilizando a biblioteca `pulp` para resolver o problema de Programação Linear Inteira (ILP). A seguir, detalhamos a escolha dessa biblioteca e como ela foi utilizada no projeto.

### Escolha da Biblioteca `pulp`

A escolha da biblioteca `pulp` se deu pelos seguintes motivos:

- **Facilidade de Uso**: `pulp` oferece uma API simples e intuitiva, permitindo a modelagem de problemas de programação linear e inteira de maneira direta e eficiente.
- **Eficiência**: `pulp` utiliza solvers otimizados, como CBC e GLPK, que são altamente eficientes na resolução de problemas de otimização, mesmo quando estes envolvem grande complexidade e número de variáveis.
- **Flexibilidade**: A biblioteca suporta tanto programação linear quanto programação inteira, o que é essencial para modelar as diversas restrições e variáveis binárias envolvidas no cronograma de aulas.
- **Compatibilidade**: `pulp` é uma biblioteca amplamente utilizada e bem documentada, com suporte a diversos solvers, permitindo que o projeto seja escalável e adaptável a diferentes necessidades e contextos.

### Estrutura do Código
- Parâmetros: Os dias da semana, períodos, aulas e suas respectivas frequências são definidos no início do script.
- Função Objetivo: A função objetivo busca maximizar a alocação das aulas considerando os pesos atribuídos aos dias, períodos e tipos de aula.
- Restrições: Restrições de frequência, não sobreposição e disponibilidade são implementadas para garantir a viabilidade da solução.
- Resolução: O problema é resolvido utilizando o solver padrão do pulp, e o resultado é exibido no console.

### Conclusão
Este sistema de definição de cronograma de aulas é uma ferramenta poderosa para instituições de ensino que buscam otimizar a alocação de aulas, levando em consideração as necessidades e restrições de professores e alunos. Com uma abordagem baseada em otimização matemática, o projeto demonstra como a tecnologia pode ser aplicada para melhorar processos educacionais críticos.

curl -X POST "http://127.0.0.1:8000/schedule" -H "Content-Type: application/json" --data "@data.json"
