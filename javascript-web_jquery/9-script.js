/* global $ */
$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  }).fail(function () {
    console.log('API request failed.');
    $('#hello').text('Error: Unable to fetch greeting.');
  });
});
