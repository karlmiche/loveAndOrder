import React from 'react';
import './App.css';
import PoemContainer from './components/PoemContainer';
import ChoosePoem from './components/ChoosePoem';
import ChooseArticle from './components/ChooseArticle';

function App() {
  return (
    <div className="App">
      <PoemContainer />
      <ChooseArticle />
    </div>
  );
}

export default App;
