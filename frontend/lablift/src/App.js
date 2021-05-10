import React, {useState, useEffect} from 'react'
import './App.css';

function App() {
  const [peso, setPeso] = useState([{}])
  const [altura, setaltura] = useState([{}])

  useEffect(() => {
    fetch('/').then(
      response => response.json()
    ).then(data => peso(data))
  });

  return (
    <div className="App">
      <h2>{peso.peso}</h2>
      <h2>{altura.altura}</h2>
    </div>
  );
}

export default App;
