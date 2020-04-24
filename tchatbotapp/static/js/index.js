var pos;
      

function inputForm() {  

  form = document.querySelector("#usertext-form");

  form.addEventListener("submit", function(event) {
      event.preventDefault();
      console.log("ok");

      
      fetch("/ajax", {
        method:"POST",
        body: new FormData(form)
      })
      .then(response => response.json())
      .then(data => pos = data)
      .then(() => console.log(pos))
      .then((json) => console.log('this is the json data', json))
      .catch(error => console.log(error))
});
}


function initMap() {
    var myLatLng = {lat: -25.363, lng: 131.044};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'Hello World!'
    });
    }