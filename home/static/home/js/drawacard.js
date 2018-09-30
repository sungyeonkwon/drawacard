
// var backgrounds = [
//
//   'https://img00.deviantart.net/6d10/i/2015/115/b/2/delver_of_squeakrets_by_alradeck-d8r1lz7.jpg',
//   'https://img00.deviantart.net/8e77/i/2015/143/9/e/tasipurr_the_golden_paw_by_alradeck-d8ufbfx.jpg',
//   'https://img00.deviantart.net/bce0/i/2015/205/5/b/deathrite_salmon_by_alradeck-d92mqeo.jpg'
//   ];



// function changeBg(direction){
//     var bg_img = document.querySelector("#bg"); //Select the img element by ID
//     var i = backgrounds.indexOf(currentBg);
//
//     if (direction == "left") {
//         i--;
//         console.log(i);
//     } else {
//         i++;
//     }
//
//     var index = (i + backgrounds.length) % backgrounds.length;
//
//     var chosenBg = backgrounds[index];
//     console.log(index);
//     bg_img.src = bg_img.src.replace(currentBg, chosenBg);
// };



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
