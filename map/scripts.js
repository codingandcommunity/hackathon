var map;

// simple script that initializes the embedded Google Map
function initMap() {
  // create new map centered in Troy, NY
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 42.7284, lng: -73.6918},
    zoom: 8
  });
  // place a marker centered in Troy, NY
  var marker = new google.maps.Marker({
    position: {lat: 42.7284, lng: -73.6918},
    map: map
  });
}
