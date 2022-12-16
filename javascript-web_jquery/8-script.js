const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let x = 0; x <= data.results.length; x++) {
    $('UL#list_movies').append('<li>' + data.results[x].title + '</li>');
  }
});

/*
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
*/
