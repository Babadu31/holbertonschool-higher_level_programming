const myUrl = 'https://stefanbohacek.com/hellosalut/?';
const $ = window.$;
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.get(myUrl + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  $(document).keypress(function (e) {
    if (e.which === 13) {
      $.get(myUrl + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
        $('DIV#hello').html(data.hello);
      });
    }
  });
});
