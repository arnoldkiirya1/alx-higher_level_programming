// Wait for the document to be ready
$(document).ready(function () {
  // Define a click event handler for DIV#red_header
  $('#red_header').click(function () {
    // Add the .red class to the <header> element
    $('header').addClass('red');
  });
});
