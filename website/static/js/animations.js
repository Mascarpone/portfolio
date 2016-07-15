$(document).ready(function(){
  
  $('.imgAnimate').each(function(){
    var src = $(this).attr('src');
    $(this).hover(function(){
      $(this).attr('src', src.replace('.gif', '_anim.gif'));
      console.log($(this).attr('src'));
    }, function(){
      $(this).attr('src', src);
    });
  });
  
});
