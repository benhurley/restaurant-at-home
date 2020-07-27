import React, { useState, useEffect } from 'react';
import './App.css';
import { List } from './components/list';

function App() {
  const [restaurants, setRestaurants] = useState([]);
  const [selectedRestaurant, setSelectedRestaurant] = useState(() => {})
  const [details, setDetails] = useState([]);

  useEffect(() => {
    fetch('/restaurants').then(res => res.json()).then(data => {
      setRestaurants(data.restaurants);
    });
  }, []);

  useEffect(() => {
    const request = '/restaurants?id=' + selectedRestaurant
    fetch(request).then(res => res.json()).then(data => {
      console.log(data)
      setDetails(data.restaurants);
    });
  }, [selectedRestaurant]);

  return (
    <div className="App">
      <header className="App-header">
        <div className="row">
          <div>
            <List list={ restaurants } onClick={setSelectedRestaurant} title="Restaurants"/>
          </div>
          <div>
            <List list={ details } title="Details"/>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
