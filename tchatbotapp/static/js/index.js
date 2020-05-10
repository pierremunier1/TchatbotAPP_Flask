
// Index.js contain all functions of the GrandPy website

function initMap() {
// function initialize the google map on the front

      var googlemap = new google.maps.Map(document.getElementById("map"),{
      zoom: 17,
      center: {lat:48.866,lng:2.333}
      
      });

      var marker = new google.maps.Marker({
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
              url:json["url"],
              user:json["user"]
          };

          let newDiv_0 = document.createElement("imessages");
          newDiv_0.innerHTML = query["user"];
          newDiv_0.className = "from-me";
          document.getElementById("imessages").appendChild(newDiv_0);
          form.addEventListener("submit", function(event) {
          event.preventDefault();

          })                 
          
          let newDiv_1 = document.createElement("imessages");
          newDiv_1.innerHTML = query["response"]+query["globalAddress"];
          newDiv_1.className = "from-them";
          document.getElementById("imessages").appendChild(newDiv_1);
          let div = document.getElementById("imessages");
          div.scrollTop = div.scrollHeight;
          form.addEventListener("submit", function(event) {
          event.preventDefault();

          })

          if (query["globalAddress"] !='') {
            let newDiv_2 = document.createElement("imessages");
            newDiv_2.innerHTML = query["extract"]+query["url"];
            newDiv_2.className = "from-them";
            document.getElementById("imessages").appendChild(newDiv_2);
          }
          });
})
}