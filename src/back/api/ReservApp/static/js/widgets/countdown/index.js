"use strict";
import React, { useState, useEffect } from "react";
import "./index.css";

class CountDownTimer extends React.Component {
    constructor(props) {
        super(props);
    }

    render() { 
        return (
            <div className="countdown-body">
                <div className="countdown-app">
                    <div className="countdown-elementcontainer">
                        <div className="countdown-timeparent">
                            <div className="countdown-timecontainer title">
                                <span className="countdown-time">
                                    <div>
                                        <p>Tiempo Restante :</p>
                                        <p>{`${hours}h ${minutes}m ${seconds}s`}</p>
                                    </div>
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

customElements.define('countdown', CountDownTimer);


const CountdownTimer = () => {
    // Initial time in seconds (1 hour)
    const initialTime = 60 * 60;
    const [timeRemaining, setTimeRemaining] = useState(initialTime);

    useEffect(() => {
        const timerInterval = setInterval(() => {
            setTimeRemaining((prevTime) => {
                if (prevTime === 0) {
                    clearInterval(timerInterval);
                    // Perform actions when the timer reaches zero
                    console.log('Countdown complete!');
                    return 0;
                } else {
                    return prevTime - 1;
                }
            });
        }, 1000);

        // Cleanup the interval when the component unmounts
        return () => clearInterval(timerInterval);
    }, []); // The empty dependency array ensures the effect runs only once on mount

    // Convert seconds to hours, minutes, and seconds
    const hours = Math.floor(timeRemaining / 3600);
    const minutes = Math.floor((timeRemaining % 3600) / 60);
    const seconds = timeRemaining % 60;

    return (
        <div>
            <p>Tiempo Restante :</p>
            <p>{`${hours}h ${minutes}m ${seconds}s`}</p>
        </div>
    );
};

export default CountdownTimer;