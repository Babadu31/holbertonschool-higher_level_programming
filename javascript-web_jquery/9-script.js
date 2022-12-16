const $ = window.$;
$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
});

/* alter
const $ = window.$;
$(document).ready(function () {
  $.getJSON('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});
*/

/* base
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let x = 0; x <= data.results.length; x++) {
    $('UL#list_movies').append('<li>' + data.results[x].title + '</li>');
  }
});
*/
