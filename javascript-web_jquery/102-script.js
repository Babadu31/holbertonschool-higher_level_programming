const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=$' + languageCode, function (data, status) {
      $('DIV#hello').text(data.hello);
    });
  });
};

/*
const $ = window.$;
$(document).ready(() => {
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val();
    console.log({ languageCode });
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`,
      type: 'get',
      success: (data, status) => {
        $('#hello').text(data.hello);
      }
    });
  });
})
;
*/

/*
const $ = window.$;
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();

    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      data: {
        lang: languageCode
      },
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  });
});
*/
