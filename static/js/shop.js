(function ($) {

    "use strict";
    var total_price = $('#quantity').val() * parseFloat($("#goods_price").text())
    $("#goods_total").text(total_price);
    $("#pre_price").text(total_price);
    $("#total_price").text(total_price);

    console.log(total_price)
    $('#quantity').on('change', function () {
        var total_price = $(this).val() * parseFloat($("#goods_price").text())
        $("#goods_total").text(total_price);
        $("#pre_price").text(total_price);
        $("#total_price").text(total_price);
    });

    function add_cart(gid, count) {
        //登录判断
        if (gid && count) {
            console.log('addcat', gid, count)
            $.post('/shop/cart', {'gid': gid, 'count': count}, function (data) {
                console.log(data)
            })
        } else {
            console.log('addcat is null')
        }
    }

    /* ==========================================================================
       When document is ready, do
       ========================================================================== */

    $(document).on('ready', function () {
        add_cart()
    });
})(window.jQuery);