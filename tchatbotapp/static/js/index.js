
// Index.js contain all functions of the GrandPy website

function initMap() {
// function initialize the google map on the front

      googlemap = new google.maps.Map(document.getElementById("map"),{
      zoom: 17,
      center: {lat:48.866,lng:2.333}
      
      });

      marker = new google.maps.Marker({
      position :{lat: 48.866,lng:2.333},
      animation: google.maps.Animation.DROP,
      icon: {path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
             scale: 6
             }
      });
}

function inputForm() {  
// analyze the text into the form to the server

  form = document.querySelector("#usertext-form");

  form.addEventListener("submit", function(event) {
      event.preventDefault();

      
      fetch("/ajax", {
        method:"POST",
        body: new FormData(form)
        })
      .then(response => response.json())

      .then(function (json) {
          let query ={ 
              lng:json["lng"],
              extract:json["extract"],
              response:json["response"],
              globalAddress:json["globalAddress"],
              url:json["url"]
          };
                           
          let newDiv = document.createElement("grandpy");
          newDiv.innerHTML = query["response"]+query["globalAddress"];
          newDiv.className = "grandpy-class";
          document.getElementById("grandpy_1").appendChild(newDiv);
          form.addEventListener("submit", function(event) {
          event.preventDefault();
          newDiv.remove();
          })

          let newDiv_1 = document.createElement("wiki");
          newDiv_1.innerHTML = query["extract"]+query["url"];
          newDiv_1.className = "wiki-class";
          document.getElementById("wiki_1").appendChild(newDiv_1);
          form.addEventListener("submit", function(event) {
          event.preventDefault();
          newDiv_1.remove();
          });
          })
})
}