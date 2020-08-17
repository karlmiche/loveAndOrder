import React from 'react';
import './App.css';
import PoemContainer from './components/PoemContainer';
import ChoosePoem from './components/ChoosePoem';
import ChooseArticle from './components/ChooseArticle';
import HowToUse from './components/HowToUse';

function App() {
  return (
    <div className="App">
      <PoemContainer />
      <ChooseArticle />
      <HowToUse />
    </div>
  );
}

export default App;
