function initMap() {
  var locations = [[37.74295, -122.42648], [37.74299, -122.42577], [37.74301, -122.42538]];
  console.log(locations);
  const myLatLng = { lat: 37.74304518280319, lng:  -122.42438793182373};
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 17.5,
    center: myLatLng
  });
  new google.maps.Marker({
    position: myLatLng,
    map,
    title: "Hello World!",
  });
  console.log('zzzzjfhrv');

  for (var i = 0; i<locations.length; i++){
    console.log(locations[i][0], locations[i][1]);
    new google.maps.Marker({
      position: {lat: locations[i][0], lng: locations[i][1]},
      map,
      title: "Hello World!",
    });
  }

  
}