

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


function showSpinner() {
  
  spinner = document.getElementById('spinner');
  spinner.className = "show";
  setTimeout(() => {
    spinner.className = spinner.className.replace("show", "");
  }, 5000);
}

// function hideSpinner() {
//   spinner.className = spinner.className.replace("show", "");
// }


function inputForm() {  


  form = document.querySelector("#usertext-form");

  form.addEventListener("submit", function(event) {
      event.preventDefault();

      showSpinner();
      fetch("/ajax", {
        method:"POST",
        body: new FormData(form)
      })
      .then(response => response.json())
      .then(json => console.log(query={lat:json['lat'],
                                        lng:json['lng'],
                                        extract:json['extract'],
                                        response:json['response']}))
      
      .then(function(addElement_gp) {
            // crée un nouvel élément div
            
            var newDiv = document.createElement('grandpy');
            newDiv.innerHTML = query['response'] ;
            newDiv.className = 'grandpy-class';
            document.getElementById("grandpy_1").appendChild(newDiv);
            })                                  
     
            .then(setTimeout(function(addElement) {

            // crée un nouvel élément div
            var newDiv = document.createElement('wiki');
            newDiv.innerHTML = query['extract'] ;
            googlemap.setCenter(query);
            marker.setPosition(query);
            newDiv.className = 'wiki-class';
            document.getElementById("wiki_1").appendChild(newDiv);
            },2000))
  });
  }


