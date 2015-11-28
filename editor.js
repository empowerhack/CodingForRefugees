$(document).ready(function() {
  var editor = ace.edit("editor");
  editor.setTheme("ace/theme/monokai");
  editor.getSession().setMode("ace/mode/python");

  $('.getCode').click(function() {
    // event.preventDefault();
    console.log(editor.getValue());
  });
});
