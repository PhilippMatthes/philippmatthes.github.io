$(window).on("scroll", function() {
    var y = window.pageYOffset;
    var screenHeight = $(window).height();
    var maxScrollHeight = $("body").height() - screenHeight - 5;
    var offset = 0.5;

    var color = $("[data-target=color-trigger]").sort(function(a, b) {
        var elementA = $(a);
        var elementB = $(b);
        var positionA = elementA.offset().top;
        var positionB = elementB.offset().top;
        var pointA = positionA - (screenHeight * offset);
        var pointB = positionB - (screenHeight * offset);
        var dA = Math.abs(y - pointA);
        var dB = Math.abs(y - pointB);
        return dA - dB;
    }).first().css("background-color");

    $("[data-target=color-target]").each(function() {
        $(this).css("background-color", color);
    })

});