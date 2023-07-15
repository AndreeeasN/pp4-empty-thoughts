// Enables select2 for id="form-tag-widget" using bootstrap5 styling
// Separate from enableSearchTagWidget to avoid overlap from base template
$(document).ready(function() {
  $('#form-tag-widget').select2({
    theme: "bootstrap-5"
  });
});