// $("#card").flip({
//   axis: 'y',
//   trigger: 'click'
// });

$("#card").flip('toggle');

var apple = "apple";

console.log("hello");

$(window).load(function() {

  $("#card").flip({
    axis: 'y',
    trigger: 'manual'
  });


	// var theWindow        = $(window),
	//     $bg              = $("#bg_01"),
	//     aspectRatio      = $bg.width() / $bg.height();
  //
	// function resizeBg() {
	// 	if ( (theWindow.width() / theWindow.height()) < aspectRatio ) {
	// 	    $bg
	// 	    	.removeClass()
	// 	    	.addClass('bgheight');
	// 	} else {
	// 	    $bg
	// 	    	.removeClass()
	// 	    	.addClass('bgwidth');
	// 	}
	// }
	// theWindow.resize(resizeBg).trigger("resize");
});
