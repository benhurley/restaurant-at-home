import React, { useState, useEffect } from 'react';
import './App.css';
import { List } from './components/list';

function App() {
  const [restaurants, setRestaurants] = useState([]);
  const [selectedRestaurant, setSelectedRestaurant] = useState(() => {})

  useEffect(() => {
    fetch('/restaurants').then(res => res.json()).then(data => {
      setRestaurants(data.restaurants);
    });
  }, []);

  useEffect(() => {
    console.log(`${selectedRestaurant} has been selected`)
  }, [selectedRestaurant]);

  return (
    <div className="App">
      <header className="App-header">
        <List restaurants={ restaurants } onClick={setSelectedRestaurant} />
      </header>
    </div>
  );
}

export default App;
