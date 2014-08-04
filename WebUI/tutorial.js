function startTutorial(){
    $("#tutorial div.info").each(function(){
        $(this).css("margin-top", (height/2*0.7).toString() + "px")
        $(this).css("font-size", (height*0.04).toString() + "px");
        $("#"+$(this).attr("id")+" table").css("margin-top", (height*0.015).toString() + "px");
        $("#"+$(this).attr("id")+" span").each(function(){
            console.log()
            $(this).css("font-size", (height*0.045).toString() + "px");
        })
    })
    $("#tutorial-color").css("margin-top", (height/2*0.55).toString() + "px")


    $("#tutorial").fadeIn();
    $("#tutorial-dish").fadeIn();
    $("#tutorial-color").fadeOut();
    $("#tutorial-sliders").fadeOut();
    $("#tutorial-graph").fadeOut();

    $(".left-slider-shade").fadeIn();
    $(".right-slider-shade").fadeIn();

}


$("#tutorial-dish .skip").click(function(){
    console.log("click!");
    $("#tutorial-dish").fadeOut();

    $(".shade").fadeOut();
    $("#tutorial").fadeOut();
})

$("#tutorial-dish .next").click(function(){
    $("#tutorial-dish").fadeOut();
    $("#tutorial-color").fadeIn();
})

$("#tutorial-color").click(function(){
    $("#tutorial-color").fadeOut();
    $("#tutorial-sliders").fadeIn();

    $(".shade").fadeOut();
    $(".middle-shade").fadeIn();
})

$("#tutorial-sliders").click(function(){
    $("#tutorial-sliders").fadeOut();
    $("#tutorial-graph").fadeIn();

    $(".shade").fadeOut();
    $(".left-slider-shade").fadeIn();
    $(".right-slider-shade").fadeIn();
})

$("#tutorial-graph").click(function(){
    $("#tutorial-graph").fadeOut();
    $("#tutorial").fadeOut();

    $(".shade").fadeOut();
})

$(".colony").css("height", (width*0.08).toString() + "px")
$(".colony").css("width", (width*0.08).toString() + "px")
$(".colony").css("border-radius", (width*0.1).toString() + "px")
$(".colony").css("margin-left", (width*0.06).toString() + "px")

$("#help").css("font-size", (height*0.15).toString() + "px");
$("#help").css("top", (height*0.010).toString() + "px");
$("#help").css("right", (width*0.14).toString() + "px");
$("#help").click(startTutorial);