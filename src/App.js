import React, { useState, useEffect } from 'react';
import './App.css';
import { List } from './components/list';
import { updateUrl } from './helpers/app_helper';

function App() {
  const [restaurants, setRestaurants] = useState([]);
  const [selectedRestaurant, setSelectedRestaurant] = useState(() => {})
  const [details, setDetails] = useState([]);

  useEffect(() => {
    const request = '/restaurants' + window.location.search
    fetch(request).then(res => res.json()).then(data => {
      setRestaurants(data.restaurants);
    });
  }, []);

  useEffect(() => {
    const request = '/restaurants?id=' + selectedRestaurant
    updateUrl(selectedRestaurant)
    fetch(request).then(res => res.json()).then(data => {
      setDetails(data.restaurants);
    });
  }, [selectedRestaurant]);

  return (
    <div className="App">
      <header className="App-header">
        <div className="row">
          <div className="names">
            <List list={ restaurants } onClick={setSelectedRestaurant} title="Restaurants"/>
          </div>
          <div className="details">
            <List list={ details } title="Details"/>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
