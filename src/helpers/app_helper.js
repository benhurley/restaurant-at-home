export const updateUrl = (selectedRestaurant) => {
    let newURL = ""

    if (selectedRestaurant) {
        if (window.location.search) {
          if (window.location.search.includes('id')){
           newURL = window.location.href.replace(/(id=)[^]+/, '$1' + selectedRestaurant)
          } else {
           newURL = window.location.href + `&id=${selectedRestaurant}`
          }
        } else {
         newURL = window.location.href + `?id=${selectedRestaurant}`
        }
        window.history.replaceState({}, null, newURL);    
    }
}