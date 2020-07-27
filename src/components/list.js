import React from 'react'
import "../styles/list.css"

export const Names = ({ item, index, onClick }) => {  
  return(
    <div 
      className="restaurantNames"
      key={ index } 
      onClick={ () => onClick(item.id)}
    >
      { item.name } 
    </div>
  )
}

export const Details = ({ item, index }) => {    
    return(
      <div 
        className="details"
        key={ index } 
      >
        <div className="detailItem">{ item.playlist && `Playlist: ${item.playlist}` }</div>
        <div className="detailItem">{ item.lighting && `Lighting: ${item.lighting}` } </div>
        <div className="detailItem">{ item.scent && `Scent: ${item.scent}` } </div>
        <div className="detailItem">{ item.tableItems.length > 0 && `Tabletop Items: ${item.tableItems}` } </div>
      </div>
    )
}

export const List = ({ list, onClick, title }) => {
  return (
    <div className="list">
      <div className="title">{ title }</div>
      <div className="scroll">
        { title == "Restaurants" &&
            list.map((item, index) => <Names item={item} index={index} onClick={onClick} />) 
        }
        { title == "Details" &&
            list.map((item, index) => <Details item={item} index={index}/>) 
        }
      </div>
    </div>
  )
}