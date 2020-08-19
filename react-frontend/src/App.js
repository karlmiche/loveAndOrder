import React from 'react';
import './App.css';
import PoemContainer from './components/PoemContainer';
import Title from './components/title';
import WhatIsThis from './components/Wtf';
import {BrowserRouter as Router, Route, Link, Redirect} from "react-router-dom";
import Appbar from './components/Appbar';


function App() {
  return (
      <div className="App">
        <Appbar />
        <Title />
        <Route exact path='/poem' component={PoemContainer} />
      <Route exact path='/explainer' component={WhatIsThis} />
    </div>
  );
}

export default App;
