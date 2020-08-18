import React from 'react';
import './App.css';
import PoemContainer from './components/PoemContainer';
import Title from './components/title';
// import WhatIsThis from './components/Wtf';

function App() {
  return (
    <div>
      <div className="App">
        <Title />
        <PoemContainer />
      </div>
      {/* <WhatIsThis /> */}
    </div>
  );
}

export default App;
