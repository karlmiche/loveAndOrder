import React from 'react';
import './App.css';
import PoemContainer from './components/PoemContainer';
import Title from './components/title'
;
function App() {
  return (
    <div className="App">
      <Title />
      <PoemContainer />
    </div>
  );
}

export default App;
