import React from 'react';
import './App.css';
import PoemContainer from './components/PoemContainer';
import ChoosePoem from './components/ChoosePoem';
import ChooseArticle from './components/ChooseArticle';
import HowToUse from './components/HowToUse';
import AllArticles from './components/AllArticles';

function App() {
  return (
    <div className="App">
      <PoemContainer />
      <ChoosePoem />
      <ChooseArticle />
      <HowToUse />
      <AllArticles />
    </div>
  );
}

export default App;
