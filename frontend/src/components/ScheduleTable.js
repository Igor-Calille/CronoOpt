function ScheduleTable({ schedule }) {
    if (!Array.isArray(schedule)) {
        return <div>Nenhum cronograma disponível</div>;
    }
    return (
      <table>
        <thead>
          <tr>
            <th>Dia</th>
            <th>Período</th>
            <th>Aula</th>
            <th>Professor</th>
          </tr>
        </thead>
        <tbody>
          {schedule.map((item, index) => (
            <tr key={index}>
              <td>{item.day}</td>
              <td>{item.period}</td>
              <td>{item.class}</td>
              <td>{item.professor}</td>
            </tr>
          ))}
        </tbody>
      </table>
    );
  }
  
  export default ScheduleTable;
  