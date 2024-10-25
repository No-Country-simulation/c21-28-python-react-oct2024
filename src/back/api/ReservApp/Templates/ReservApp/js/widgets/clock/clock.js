"use strict";
import { useState } from "react";
import "./clock.css";

class Clock extends React.Component {
    constructor(props) {
      super(props);
    }
    render() {
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
  
      return <span>{timeString}</span>;
/*
      let time  = new Date().toLocaleTimeString()
      const [ctime,setTime] = useState(time)
      const UpdateTime=()=>{
        time =  new Date().toLocaleTimeString()
        setTime(time)
      }
      setInterval(UpdateTime)
      return (
        <h1 class='clock'>{ctime}</h1>
        )              
        */
    }
}

customElements.define('clock', Clock);