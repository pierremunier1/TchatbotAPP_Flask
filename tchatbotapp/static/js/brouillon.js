function initMap() {


    googlemap = new google.maps.Map(document.getElementById('map'),{
    zoom: 17,
    center: {lat:48.866,lng:2.333}
    
    });

    marker = new google.maps.Marker({
      position :{lat: 48.866,lng:2.333},
      animation: google.maps.Animation.DROP,
      icon: { 
        path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
        scale: 6
      }
     });
    }
