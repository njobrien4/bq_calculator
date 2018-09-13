// document.getElementById("banner").innerHTML = "Hello, World!";
$(document).ready(function () {
  // //your code here
  // console.log($("#url-box").val());
  var text
  $( "#url-submit" ).click(function() {
  console.log($("#url-box").val());
  text = $("#url-box").val();
});
  $.ajax({
  type: "POST",
  url: "server.py",
  data: { param: text}
}).done(function( o ) {
   console.log("good to go")
});
});
