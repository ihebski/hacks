function get(i,div_page)
{
  $.ajax({
url:i+".php",
success:function(msg)
{
  $("#"+div_page).html(msg);
}


});
}



$(document).ready(function(){
get("home","home");
get("feeds","comments");


});
