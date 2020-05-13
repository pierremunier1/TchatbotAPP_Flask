
// Index.js contain all functions of the GrandPy website

function initMap(query) {
// function initialize the google map on the front

      let googlemap = new google.maps.Map(document.getElementById("map"),{
      zoom: 17,
      center: query
      });

      let marker = new google.maps.Marker({
      map:googlemap,
      draggable: true,
      position :query,
      animation: google.maps.Animation.DROP,
      });
      
      let infoWindow = new google.maps.InfoWindow({
            content: "<h4>C'est ici !</h4>"
            });
            marker.addListener('mouseover', function(){
              infoWindow.open(map, marker);    
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
              lat:json["lat"],
              extract:json["extract"],
              response:json["response"],
              globalAddress:json["globalAddress"],
              url:json["url"],
              user:json["user"]
          };

          if (query["user"] !='') {
            let newDiv_0 = document.createElement("imessages");
            newDiv_0.innerHTML = query["user"];
            newDiv_0.className = "from-me";
            document.getElementById("imessages").appendChild(newDiv_0);
          }
                         
          let newDiv_1 = document.createElement("imessages");
          newDiv_1.innerHTML = query["response"]+query["globalAddress"];
          newDiv_1.className = "from-them";
          document.getElementById("imessages").appendChild(newDiv_1);
          let div = document.getElementById("imessages");
          div.scrollTop = div.scrollHeight;
          
          if (query["globalAddress"] !='') {
            let newDiv_2 = document.createElement("imessages");
            newDiv_2.innerHTML = query["extract"]+(
              '<a href="'+query["url"]+'">-En savoir plus sur Wikipedia.</a>'
            );
            newDiv_2.className = "from-them";
            document.getElementById("imessages").appendChild(newDiv_2);
            let div = document.getElementById("imessages");
            div.scrollTop = div.scrollHeight;
      
            let newDiv_3 = document.createElement("map");
            newDiv_3.innerHTML = initMap(query);
            document.getElementById("map").appendChild(newDiv_3);
            document.getElementById("map").style.visibility="visible";
          }
          });
})
}