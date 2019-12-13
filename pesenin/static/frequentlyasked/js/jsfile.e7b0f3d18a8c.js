$(document).ready(function(){
    $(".accordion-head1").click(function(){
        $(".accordion-body2").addClass("display");
        $(".accordion-body3").addClass("display");
        $(".accordion-body4").addClass("display");
        $(".accordion-body1").toggleClass("display");
    });


    $(".accordion-head2").click(function(){
        $(".accordion-body1").addClass("display");
        $(".accordion-body3").addClass("display");
        $(".accordion-body4").addClass("display");
        $(".accordion-body2").toggleClass("display");

    });

    $(".accordion-head3").click(function(){
        $(".accordion-body1").addClass("display");
        $(".accordion-body2").addClass("display");
        $(".accordion-body4").addClass("display");
        $(".accordion-body3").toggleClass("display");
    });

    $(".accordion-head4").click(function(){
        $(".accordion-body1").addClass("display");
        $(".accordion-body2").addClass("display");
        $(".accordion-body3").addClass("display");
        $(".accordion-body4").toggleClass("display");
    });
});


