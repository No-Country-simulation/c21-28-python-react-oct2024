import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import Main from "./pages/main/main";
import './default.css'
import './styles.css'
//import ReactDOM from 'react-dom'
//ReactDOM.render( <App />, document.getElementById('root'))
const rootElement = document.getElementById("root");
const root = createRoot(rootElement);
root.render(
  <StrictMode>
    <Main />
  </StrictMode>
);