$(document).ready(function () {
    var baseurl = window.location.href;
    if (baseurl.includes('ch')) {
        $('#ch').addClass('uk-active');
        $('#ch').siblings().removeClass('uk-active');
    }
    else if ($(baseurl).include('ru')) {
        $('#ru').addClass('uk-active');
        $('#ru').siblings.remove('uk-active');
    }


});