console.log("hello");

var apple = "apple";


$("#card").flip({
  axis: 'y',
  trigger: 'manual'
});

$(".show-english").click(function() {
  $("#card").flip('toggle');
});

// background image change when refreshed
// function randomImage(){
//   var images = [
//    '{% static "draw/img/bg_01.jpg" %}',
//    '{% static "draw/img/bg_02.jpg" %}',
//   ];
//   var size = images.length;
//   var x = Math.floor(size * Math.random());
//   console.log(x);
//   var element = document.getElementsByClassName('background');
//   console.log(element);
//   element[0].style["background-image"] = "url("+ images[x] + ")";
// }
//
// document.addEventListener("DOMContentLoaded", randomImage);
