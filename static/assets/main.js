;(function () {


    'use strict';

    // Placeholder
    var placeholderFunction = function () {
        $('input, textarea').placeholder({customClass: 'my-placeholder'});
    }

    // Placeholder
    var contentWayPoint = function () {
        var i = 0;
        $('.animate-box').waypoint(function (direction) {

            if (direction === 'down' && !$(this.element).hasClass('animated-fast')) {

                i++;

                $(this.element).addClass('item-animate');
                setTimeout(function () {

                    $('body .animate-box.item-animate').each(function (k) {
                        var el = $(this);
                        setTimeout(function () {
                            var effect = el.data('animate-effect');
                            if (effect === 'fadeIn') {
                                el.addClass('fadeIn animated-fast');
                            } else if (effect === 'fadeInLeft') {
                                el.addClass('fadeInLeft animated-fast');
                            } else if (effect === 'fadeInRight') {
                                el.addClass('fadeInRight animated-fast');
                            } else {
                                el.addClass('fadeInUp animated-fast');
                            }

                            el.removeClass('item-animate');
                        }, k * 200, 'easeInOutExpo');
                    });

                }, 100);

            }

        }, {offset: '85%'});
    };
    // On load
    $(function () {
        placeholderFunction();
        contentWayPoint();

    });

}());


//注册刷新验证码点击事件

$('img.captcha').click({'form_id': 'register_form'}, refresh_captcha);
$('img.captcha').click({'form_id': 'login_form'}, refresh_captcha);

// 刷新验证码
function refresh_captcha(event) {
    $.get("/captcha/refresh/?" + Math.random(), function (result) {
        $('#' + event.data.form_id + ' .captcha').attr("src", result.image_url);
        $('#id_captcha_0').attr("value", result.key);
    });
    return false;
}