$(document).ready(function () {

    $('#quantity').on('change', function () {
        var total_price = $(this).val() * parseFloat($("#goods_price").text())
        $("#goods_total").text(total_price);
        $("#pre_price").text(total_price);
        $("#total_price").text(total_price);
    });

});