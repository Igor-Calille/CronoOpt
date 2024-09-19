import React from 'react';
import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
  Tooltip,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
} from '@mui/material';

function ScheduleDisplay({ schedule }) {
  const [selectedYear, setSelectedYear] = React.useState('Todos');
  const years = ['Todos', ...new Set(schedule?.map((item) => item.year.toString()))];

  const filteredSchedule = 
    selectedYear === 'Todos' ? schedule : schedule?.filter((item) => item.year.toString() === selectedYear);

  const scheduleData = {};

  if (filteredSchedule) {
    filteredSchedule.forEach((item) => {
      const { year, day, period, class: className, professor } = item;
      if (!scheduleData[year]) {
        scheduleData[year] = {};
      }
      if (!scheduleData[year][day]) {
        scheduleData[year][day] = {};
      }
      if (!scheduleData[year][day][period]) {
        scheduleData[year][day][period] = [];
      }
      scheduleData[year][day][period].push({ className, professor });
    });
  }

  const days = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'];
  const periods = ['7:15-8:55', '9:05-10:45', '10:55-12:35'];

  return (
    <div>
      <Typography variant="h4" gutterBottom>
        Cronograma Gerado
      </Typography>

      <FormControl variant="outlined" style={{ minWidth: 200, marginBottom: '1rem' }}>
        <InputLabel id="year-select-label">Selecionar Ano</InputLabel>
        <Select
          labelId="year-select-label"
          id="year-select"
          value={selectedYear}
          onChange={(e) => setSelectedYear(e.target.value)}
          label="Selecionar Ano"
        >
          {years.map((year) => (
            <MenuItem key={year} value={year}>
              {year === 'Todos' ? 'Todos os Anos' : `Ano ${year}`}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      {Object.keys(scheduleData).map((year) => (
        <div key={year}>
          <Typography variant="h5" gutterBottom>
            Ano {year}
          </Typography>
          <TableContainer component={Paper} style={{ marginBottom: '2rem' }}>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>Períodos \ Dias</TableCell>
                  {days.map((day) => (
                    <TableCell key={day} align="center">
                      {day}
                    </TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {periods.map((period) => (
                  <TableRow key={period}>
                    <TableCell component="th" scope="row">
                      {period}
                    </TableCell>
                    {days.map((day) => (
                      <TableCell key={day} align="center">
                        {scheduleData[year]?.[day]?.[period] 
                          ? scheduleData[year][day][period].map((entry, idx) => (
                              <Tooltip
                                key={idx}
                                title={`Professor: ${entry.professor}`}
                                arrow
                                placement="top"
                              >
                                <Paper
                                  elevation={3}
                                  style={{
                                    marginBottom: '0.5rem',
                                    padding: '0.5rem',
                                    backgroundColor: '#e3f2fd',
                                  }}
                                >
                                  <strong>{entry.className}</strong>
                                  <br />
                                  <span>{entry.professor}</span>
                                </Paper>
                              </Tooltip>
                            ))
                          : '-'}
                      </TableCell>
                    ))}
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </div>
      ))}
    </div>
  );
}

export default ScheduleDisplay;
