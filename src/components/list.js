import React from 'react'
import "../styles/list.css"

export const Item = ({ restaurant, index, onClick }) => {
  return(
    <div 
      class="listItem"
      key={ index } 
      onClick={ () => onClick(restaurant.id)}
    >
      { restaurant.name }
    </div>
  )
}

export const List = ({ restaurants, onClick }) => {
  return (
    <div class="list">
      <div class="title">restaurant names</div>
      <div class="scoll">
        { restaurants.map((restaurant, index) => <Item restaurant={restaurant} index={index} onClick={onClick} />) }
      </div>
    </div>
  )
}