var homeSection = $('#title').offset().top;
var servicesSection = $('#services').offset().top;
var reviewsSection = $('#reviews').offset().top;
var contactSection = $('#contact').offset().top;

$(document).scroll(function() {
    var scrollPos = $(document).scrollTop();
    if (scrollPos >= homeSection && scrollPos < servicesSection) {
        var color = $('#title').css('background-color');
        $('.navbar').css('background-color', color);
    } else if (scrollPos >= servicesSection && scrollPos < reviewsSection) {
        var color = $('#services').css('background-color');
        $('.navbar').css('background-color', color);
    }
    else if (scrollPos >= reviewsSection && scrollPos < contactSection) {
        var color = $('#reviews').css('background-color');
        $('.navbar').css('background-color', color);
    } else if (scrollPos >= contactSection) {
        var color = $('#contact').css('background-color');
        $('.navbar').css('background-color', color);
    }
});