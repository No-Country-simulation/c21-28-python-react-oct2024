"use strict";
import { Clock } from "../../widgets/clock";

class MainReact extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    //https://codesandbox.io/p/sandbox/digital-clock-smyxfv?file=%2Fsrc%2Findex.js%3A14%2C1
    return (
        <div className="main">
            <Clock />
        </div>
    )
  }
}

ReactDOM.render(<MainReact />, document.getElementById("root-react"));