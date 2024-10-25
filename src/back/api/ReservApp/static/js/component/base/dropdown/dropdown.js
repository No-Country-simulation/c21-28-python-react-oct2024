"use strict";
import { useState } from "react";
import "./clock.css";

class DropDown extends React.Component {
  constructor({ open, trigger, menu }) {
    super({ open, trigger, menu });
  }
  render() { 
    return (
      <div className="dropdown">
      {trigger}
      {open ? (
        <ul className="menu">
          {menu.map((menuItem, index) => (
            <li key={index} className="menu-item">{menuItem}</li>
          ))}
        </ul>
      ) : null}
    </div>
    );
  } 
};

 //https://www.robinwieruch.de/react-select/
 //https://www.freecodecamp.org/news/build-a-dynamic-dropdown-component/
customElements.define('dropdown', DropDown);