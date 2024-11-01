function App() {
   // const THREE_DAYS_IN_MS = 3 * 24 * 60 * 60 * 1000;
   // const THREE_DAYS_IN_MS = 3 * 24 * 60 * 60 * 1000;
   const ELAPSED_MIN = 5 * 60 * 1000;
   const NOW_IN_MS = new Date().getTime();
    const dateTimeAfterThreeDays = NOW_IN_MS + ELAPSED_MIN;
    return (
      <div>
        <CountDownTimer targetDate={dateTimeAfterThreeDays} />
        <Clock/>
      </div>
    );
  }


const html_root = document.getElementById('application');
const r = ReactDOM.createRoot(html_root).render(<App/> );

 
//ReactDOM.render(<App />, document.getElementById("application"));