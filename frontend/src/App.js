import React, { useState } from 'react';
import ScheduleForm from './components/ScheduleForm';
import ScheduleDisplay from './components/ScheduleDisplay';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

function App() {
  const [schedule, setSchedule] = useState([]);
  const [error, setError] = useState(null);

  // Criando o tema de maneira correta
  const theme = createTheme({
    palette: {
      mode: 'light',
      primary: {
        main: '#1976d2',
      },
      secondary: {
        main: '#dc004e',
      },
    },
  });

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <div className="App" style={{ padding: '2rem', backgroundColor: '#f5f5f5' }}>
        <h1>CronoOpt</h1>
        {error && <p style={{ color: 'red' }}>Erro: {error}</p>}
        <ScheduleForm setSchedule={setSchedule} setError={setError} />
        <ScheduleDisplay schedule={schedule} />
      </div>
    </ThemeProvider>
  );
}

export default App;
