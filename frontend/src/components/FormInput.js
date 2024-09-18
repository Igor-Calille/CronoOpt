import React, { useState } from "react";

function FormInput({ onSubmit}) {
    const [formData, setFormData] = useState({
        days: [],
        periods: [],
        classes: [],
        professors: [],
        labs: [],
        class_count: {},
        day_weights: {},
        period_weights: {},
        class_weights: {},
        professor_associations: {},
        restricoes_indisponibilidade_professors: {},
        restricoes_dependencia: {}
    });

    const handleObjectChange = (e, key) => {
        const value = e.target.value;
        const [objKey, objValue] = key.split(":");
        setFormData({
            ...formData,
            [key]: { ...formData[key], [objKey]: parseFloat(objValue) }
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(formData);
    };

    return (
        <form onSubmit={handleSubmit}>
          <div>
            <label>Dias (separados por vírgula):</label>
            <input
              type="text"
              onChange={(e) => handleArrayChange(e, "days")}
              placeholder="Segunda,Terça,Quarta"
            />
          </div>
    
          <div>
            <label>Períodos (separados por vírgula):</label>
            <input
              type="text"
              onChange={(e) => handleArrayChange(e, "periods")}
              placeholder="7:15-8:55,9:05-10:45"
            />
          </div>
    
          <div>
            <label>Classes (separadas por vírgula):</label>
            <input
              type="text"
              onChange={(e) => handleArrayChange(e, "classes")}
              placeholder="Aula1,Aula2,Aula3"
            />
          </div>
    
          <div>
            <label>Professores (separados por vírgula):</label>
            <input
              type="text"
              onChange={(e) => handleArrayChange(e, "professors")}
              placeholder="ProfessorA,ProfessorB"
            />
          </div>
    
          <div>
            <label>Laboratórios (separados por vírgula):</label>
            <input
              type="text"
              onChange={(e) => handleArrayChange(e, "labs")}
              placeholder="Aula3,Aula5"
            />
          </div>
    
          <div>
            <label>Contagem de Aulas (Aula1:2, Aula2:2):</label>
            <input
              type="text"
              onChange={(e) => handleObjectChange(e, "class_count")}
              placeholder="Aula1:2,Aula2:2"
            />
          </div>
    
          <div>
            <label>Peso de Dias (Segunda:1.0, Terça:1.0):</label>
            <input
              type="text"
              onChange={(e) => handleObjectChange(e, "day_weights")}
              placeholder="Segunda:1.0,Terça:1.0"
            />
          </div>
    
          <div>
            <label>Peso de Períodos (7:15-8:55:1.5):</label>
            <input
              type="text"
              onChange={(e) => handleObjectChange(e, "period_weights")}
              placeholder="7:15-8:55:1.5"
            />
          </div>
    
          <div>
            <label>Peso de Classes (Aula1:1.0, Aula2:1.0):</label>
            <input
              type="text"
              onChange={(e) => handleObjectChange(e, "class_weights")}
              placeholder="Aula1:1.0,Aula2:1.0"
            />
          </div>
    
          <div>
            <label>Associação de Professores (Aula1:ProfessorA):</label>
            <input
              type="text"
              onChange={(e) => handleObjectChange(e, "professor_associations")}
              placeholder="Aula1:ProfessorA"
            />
          </div>
    
          <div>
            <label>Indisponibilidade de Professores (ProfessorA:Segunda-9:05-10:45):</label>
            <input
              type="text"
              onChange={(e) => handleObjectChange(e, "restricoes_indisponibilidade_professors")}
              placeholder="ProfessorA:Segunda-9:05-10:45"
            />
          </div>
    
          <div>
            <label>Dependências de Aulas (Aula3:Quarta-10:55-12:35):</label>
            <input
              type="text"
              onChange={(e) => handleObjectChange(e, "restricoes_dependencia")}
              placeholder="Aula3:Quarta-10:55-12:35"
            />
          </div>
    
          <button type="submit">Gerar Cronograma</button>
        </form>
    );

}

export default FormInput;

