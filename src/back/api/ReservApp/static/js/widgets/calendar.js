"use strict";
const { useState, useEffect, useMemo, useCallback } = React;

//https://cdn.jsdelivr.net/npm/dayjs@1/locale/es.js

//https://blog.logrocket.com/react-calendar-tutorial-build-customize-calendar/#what-react-calendar   
const App = ({ }) => {
  const [date, setDate] = useState(new Date());
  return (
    <div className='app'>
      <h1 className='text-center'>Calendario</h1>
      <div className='calendar-container'>
        <Calendar
          onChange={setDate}
          value={date}
          selectRange={true}
        />
      </div>
      {date.length > 0 ? (
        <p className='text-center'>
          <span className='bold'>Start:</span>{' '}
          {date[0].toDateString()}
          &nbsp;|&nbsp;
          <span className='bold'>End:</span> {date[1].toDateString()}
        </p>
      ) : (
        <p className='text-center'>
          <span className='bold'>Fecha Seleccionada:</span>{' '}
          {date.toDateString()}
        </p>
      )}
    </div>
  );
};

 
const html_root = document.getElementById('application');
const r = ReactDOM.createRoot(html_root).render(<App/> );

 
