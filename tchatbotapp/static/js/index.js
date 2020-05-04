

function initMap() {


      googlemap = new google.maps.Map(document.getElementById('map'), {
        zoom: 17,
        center:{lat: 48.853, lng: 2.3488}
        
    });

    }


function inputForm() {  
  
  
  var query;

  form = document.querySelector("#usertext-form");

  form.addEventListener("submit", function(event) {
      event.preventDefault();

      fetch("/ajax", {
        method:"POST",
        body: new FormData(form)
      })
      .then(response => response.json())
      .then(json => query={lat:json['lat'],
                           lng:json['lng'],
                           extract:json['extract']})
                           
                            
                          
      .then(function(addElement) {
            // crée un nouvel élément div
            var newDiv = document.createElement('wiki');

            newDiv.innerHTML = query['extract'];
            googlemap.setCenter(query);
            marker = new google.maps.Marker({
            position: query,
            map: googlemap,
            animation: google.maps.Animation.DROP,
              icon: { 
                path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
                scale: 6
              }
            }),
            document.body.appendChild(newDiv);
            } )

            });
            }

