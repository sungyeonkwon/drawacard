console.log('connected');
//
// var bg = [
//   '/static/home/img/bg_00.jpg',
//   '/static/home/img/bg_01.jpg',
//   '/static/home/img/bg_02.jpg',
//   '/static/home/img/bg_03.jpg',
//   '/static/home/img/bg_04.jpg',
//   '/static/home/img/bg_05.jpg',
//   '/static/home/img/bg_06.jpg',
//   '/static/home/img/bg_07.jpg',
//   '/static/home/img/bg_08.jpg',
//   '/static/home/img/bg_09.jpg',
// ]
// // var i = bg.indexOf(currentBg);
// var currentBg = $('.background');
//
// $('.draw-again').click(function() {
//   // e.preventDefault();
//   console.log('draw again clicked');
//   var current = $('.background.active');
//   var next = $('.background.active + img');
//   current.removeClass('active')
//   current.addClass('inactive')
//   next.removeClass('inactive')
//   next.addClass('active')
//   // var i = bg.indexOf($currentBg);
//   // var index = (i + bg.length + 1) % bg.length;
//   // $currentBg.attr("src", bg[3]);
//
// });


// var backgrounds = ['bg_desert.jpg', 'bg_grass.jpg', 'bg_stone.jpg'];
// // '{% static "pspace/img/bg_desert.jpg" %}';
//
// function changeBg(direction){
//     var bg_img = document.querySelector("#bg_desert"); //Select the img element by ID
//     var bgNameRegex = /\/([^\/]+)$/;
//     var matches = bg_img.src.match(bgNameRegex);
//     var currentBg = matches[1];
//     var i = backgrounds.indexOf(currentBg);
//
//     // bg text
//     var bg_text = document.getElementById('game_bg_type'); //select text bg
//     if (direction == "left") {
//         i--;
//     } else {
//         i++;
//     }
//     var index = (i + backgrounds.length) % backgrounds.length;
//     var chosenBg = backgrounds[index];
//     bg_img.src = bg_img.src.replace(currentBg, chosenBg);
// };


$("#card").flip({
  axis: 'y',
  trigger: 'manual'
});


// finish this
$(document).ready(function() {

  $(function() {
    $('.backgroundTransition').backgroundTransition({
        backgrounds:[
          { src: '/static/home/img/bg_00.jpg' },
          { src: '/static/home/img/bg_01.jpg' },
          { src: '/static/home/img/bg_02.jpg' },
          { src: '/static/home/img/bg_03.jpg' },
          { src: '/static/home/img/bg_04.jpg' },
          { src: '/static/home/img/bg_05.jpg' },
          { src: '/static/home/img/bg_06.jpg' },
          { src: '/static/home/img/bg_07.jpg' },
          { src: '/static/home/img/bg_08.jpg' },
          { src: '/static/home/img/bg_09.jpg' },
        ],
        transitionDelay: 5,
        animationSpeed: 3000
    });
  });


  // $('.backgroundTransition').backgroundTransition({
  //
  //   //  CSS Selectors
  //   classNameBottomImage: "image-bottom",
  //   classNameTopImage: "image-top",
  //   idNameDownloadImage: "image-download",
  //
  //   // an array of image objects
  //   backgrounds: [],
  //
  //   // the delay between image transition
  //   transitionDelay: 10,
  //
  //   // animation speed
  //   animationSpeed: 500
  //
  // });

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
