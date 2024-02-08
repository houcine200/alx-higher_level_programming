/* global $ */
$(function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    $.ajax({
      type: 'GET',
      url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  });
});
