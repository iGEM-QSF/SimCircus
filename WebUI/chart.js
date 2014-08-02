var width = $(document).width()*0.8;
var height = $(document).height()*0.9;
$("#chart").css("margin-top", (0.05*$(document).height()).toString() + "px");
$("#chart").css("margin-left", (0.1*$(document).width()).toString() + "px");
$("#chart").attr("width", width).attr("height", height);
var context = $("#chart").get(0).getContext("2d");

function updateChart(previous) {
    previous ++;
    graphChart.addData([
        getAmount("A"),
        getAmount("B"),
        getAmount("C")],
        previous);
    if (previous > 50) {
        graphChart.removeData();
    }
    if (previous < 10){
    }
    setTimeout(function(){
        updateChart(previous)}, 200)
}

var plotData = {
    labels: [0],
    datasets: [
        {
            label: "Red fluorescent protein",
            fillColor: "rgba(255,0,0,0.05)",
            strokeColor: "rgba(255,100,100,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: [0]
        },
        {
            label: "Green fluorescent protein",
            fillColor: "rgba(0,255,0,0.05)",
            strokeColor: "rgba(100,255,100,1)",
            pointColor: "rgba(151,187,205,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(151,187,205,1)",
            data: [0]
        },
        {
            label: "Blue fluorescent protein",
            fillColor: "rgba(0,0,255,0.05)",
            strokeColor: "rgba(100,100,255,1)",
            pointColor: "rgba(151,187,205,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(151,187,205,1)",
            data: [0]
        }
    ]
};

var options = {
    bezierCurve: false,
    animationEasing: "",
    pointDot: false,
    animation: false,
    scaleOverride: true,
    scaleSteps: 20,
    // Number - The value jump in the hard coded scale
    scaleStepWidth: 0.1,
    // Number - The scale starting value
    scaleStartValue: 0,

};
var graphChart = new Chart(context).Line(plotData, options);
$("#data-visualization").click(function(){
    $("#data-visualization").fadeOut()
})
$("#paper1").click(function(){
    $("#data-visualization").fadeIn()
})

setTimeout(function(){
    updateChart(0)}, 100);
