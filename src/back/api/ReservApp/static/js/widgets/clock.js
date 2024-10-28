"use strict";

const { useState, useEffect, useMemo, useCallback } = React;

const Clock = () => {

  const culture = 'es-AR';//'en-GB';
  const [date, setDate] = useState(new Date());

  useEffect(() => {
    const timerID = setInterval(() => tick(), 1000);
    return () => clearInterval(timerID);
  }, []);

  const tick = useCallback(() => {
    setDate(new Date());
  }, []);

  const options = { hour: "2-digit", minute: "2-digit", hour12: false };
  const timeString = useMemo(() => date.toLocaleTimeString(culture, options), [date]);

  return ( 
    <div className="clock">
       <span className="clock-time">{timeString}</span>
    </div>
  );
  
  return (
    <div className="clock">
      <div className="clock-body">
        <div className="clock-app">
          <div className="clock-elementcontainer">
            <div className="clock-timeparent">
              <div className="clock-timecontainer title">
                <span className="clock-time">{timeString}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}