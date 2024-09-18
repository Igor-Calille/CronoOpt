import React, { useState } from "react";
import FormInput from "./components/FormInput";
import ScheduleTable from "./components/ScheduleTable";

function App() {
  const [schedule, setSchedule] = useState(null);

  const submitForm = (data) => {
    fetch("http://127.0.0.1:8000/schedule", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => setSchedule(data.schedule));
  };

  return (
    <div className="App">
      <h1>Gerador de Cronograma de Aulas</h1>
      <FormInput onSubmit={submitForm} />
      {schedule && <ScheduleTable schedule={schedule} />}
    </div>
  );
}

export default App;
