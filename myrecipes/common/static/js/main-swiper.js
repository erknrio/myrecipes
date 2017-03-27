$(document).ready(function () {
    // $("#erk-form").on("submit", function(ev) {
    //     // ev.preventDefault();
    //     window.alert($(this).serialize());
    // });
    //initialize swiper when document ready
    var mySwiper = new Swiper ('.swiper-container', {
        // Optional parameters
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        pagination: '.swiper-pagination',
        paginationType: 'progress',
        keyboardControl: true
        // onReachEnd: function(swiper) {
        //     $("#erk-form").trigger("submit");
        // }
    });
});
