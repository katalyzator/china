//= jquery/jquery.js
//= uikit/uikit.min.js
//= uikit/uikit-icons.min.js
//= slick/slick.min.js
//= lightgallery/lightgallery-all.js

//= ajax_paginator.js
//= contact_form.js
//= jquery.validate.js
//= lang.js
//= language.js
//= validation.js



$(document).ready(function(){

    const slider = $('.slick-fade-carousel');
    const SliderVariableWidth = $('.variable-width');
    // const lightGalleryNews = $('#relative-caption');

    if (slider !== undefined && slider !== null) {
        slider.slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 4000,
            arrows: true,
            speed: 1000,
            fade: true,
            nextArrow: '<img class="next" src="/application/main/assets/img/right-arr.svg" alt="" width="48" height="48">',
            prevArrow: '<img class="prev" src="/application/main/assets/img/left-arr.svg" alt="" width="48" height="48">'
        });
    }

    if (SliderVariableWidth !== undefined && SliderVariableWidth !== null) {
        SliderVariableWidth.slick({
            infinite: true,
            speed: 500,
            autoplay: true,
            slidesToShow: 4,
            centerMode: true,
            variableWidth: true,
            nextArrow: '<img class="next" src="/application/main/assets/img/right.svg" alt="" width="48" height="48">',
            prevArrow: '<img class="prev" src="/application/main/assets/img/left.svg" alt="" width="48" height="48">'

        });
    }






}); //end document ready

