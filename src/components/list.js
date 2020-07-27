import React from 'react'
import "../styles/list.css"

export const List = ({ list, onClick, title }) => {
  return (
    <div className="list">
      <div className="title">{ title }</div>
      <div className="scroll">
        { title === "Restaurants" &&
            list.map((item, index) => <Names item={item} key={item.id} onClick={onClick} />) 
        }
        { title === "Details" &&
            list.map((item, index) => <Details item={item} key={item.id}/>) 
        }
      </div>
    </div>
  )
}

export const Details = ({ item }) => {    
    return(
      <div className="details">
        <div className="detailItem">{ item.playlist && `Playlist: ${item.playlist}` }</div>
        <div className="detailItem">{ item.lighting && `Lighting: ${item.lighting}` } </div>
        <div className="detailItem">{ item.scent && `Scent: ${item.scent}` } </div>
        <div className="detailItem">{ item.tableItems.length > 0 && `Tabletop Items: ${item.tableItems}` } </div>
      </div>
    )
}

export const Names = ({ item, onClick }) => {  
  return(
    <div 
      className="restaurantNames"
      onClick={ () => onClick(item.id)}
    >
      { item.name } 
    </div>
  )
}