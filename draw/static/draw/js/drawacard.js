console.log("hello");

var apple = "apple";


$("#card").flip({
  axis: 'y',
  trigger: 'manual'
});



// finish this
$(document).ready(function() {

  // show share link
  $(".card-share").click(function() {
    console.log("blueberries are wonderful.");
    $(".share-input").toggleClass('active');
  });

  // change english / other language button
  $(".show-english").click(function() {
    $("#card").flip('toggle');

    if ($(".show--otherlang").hasClass('show')){
      $(".show--otherlang").removeClass('show');
      $(".show--english").removeClass('hide');
      $(".show--otherlang").addClass('hide');
      $(".show--english").addClass('show');
    } else {
      $(".show--otherlang").removeClass('hide');
      $(".show--english").removeClass('show');
      $(".show--otherlang").addClass('show');
      $(".show--english").addClass('hide');
    }
  });


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
