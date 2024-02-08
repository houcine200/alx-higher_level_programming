/* global $ */
$(function () {
  const f = function () {
    const lang = $('#language_code').val();
    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
      method: 'GET',
      success: function (data) {
        $('#hello').html(data.hello);
      }
    });
  };
  $('#btn_translate').click(function () {
    f();
  });
  $('#language_code').keydown(function (event) {
    if (event.which === 13) {
      f();
    }
  });
});
