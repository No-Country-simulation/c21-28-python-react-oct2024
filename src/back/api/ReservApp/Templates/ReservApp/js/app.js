"use strict";
import { Clock } from "./widgets/clock/clock";

class MainReact extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <div>
            <strong>app.js</strong> is loaded<br/>
            <Clock />
        </div>
    )
  }
}

ReactDOM.render(<MainReact />, document.getElementById("root-react"));