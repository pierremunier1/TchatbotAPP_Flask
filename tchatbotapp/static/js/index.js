
// Index.js contain all functions of the GrandPy website



function initMap() {
// function initialize the google map on the front

    let googlemap = new google.maps.Map(document.getElementById("map"),{
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

function showSpinner() {
 // function initialize the loader 

  spinner = document.getElementById("spinner");
  spinner.className = "show";
  setTimeout(() => {
    spinner.className = spinner.className.replace("show", "");
  }, 5000);
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

          return query
          })                     
     
      .then(function (query) {
            // add dynamic wiki div in the front page

            newDiv = document.createElement("wiki");
            newDiv.innerHTML = query["extract"]+query["url"];
            newDiv.className = "wiki-class";
            document.getElementById("wiki_1").appendChild(newDiv);
            });
            form.addEventListener("submit", function(event) {
            event.preventDefault();
            newDiv.remove();
  
            })
})
}