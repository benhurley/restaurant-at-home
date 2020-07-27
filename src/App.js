import React, { useState, useEffect } from 'react';
import './App.css';
import { List } from './components/list';

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
    let newURL
    const request = '/restaurants?id=' + selectedRestaurant

    // update the url showing the selected restaurant id
    if (selectedRestaurant) {
      if (window.location.search) {
        if (window.location.search.includes('id')){
         newURL = window.location.href.replace(/(id=)[^\&]+/, '$1' + selectedRestaurant)
        } else {
         newURL = window.location.href + `&id=${selectedRestaurant}`
        }
      } else {
       newURL = window.location.href + `?id=${selectedRestaurant}`
      }
      window.history.replaceState({}, null, newURL);    
    }

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
