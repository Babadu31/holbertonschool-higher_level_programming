const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});

/*
const $ = window.$;
$('DIV#update_header').click(function () {
  $('HEADER').text('New Header!!!');
});
*/
