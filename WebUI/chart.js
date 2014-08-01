var width = $(document).width()*0.8;
var height = $(document).height()*0.9;
$("#chart").css("margin-top", (0.05*$(document).height()).toString() + "px");
$("#chart").css("margin-left", (0.1*$(document).width()).toString() + "px");
$("#chart").attr("width", width).attr("height", height);
var context = $("#chart").get(0).getContext("2d");

function updateChart() {
    continue
}

var data = {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
        {
            label: "My First dataset",
            fillColor: "rgba(220,220,220,0.2)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: [65, 59, 80, 81, 56, 55, 40]
        },
        {
            label: "My Second dataset",
            fillColor: "rgba(151,187,205,0.2)",
            strokeColor: "rgba(151,187,205,1)",
            pointColor: "rgba(151,187,205,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(151,187,205,1)",
            data: [28, 48, 40, 19, 86, 27, 90]
        }
    ]
};
var options = {
    bezierCurve: true
};
var graphChart = new Chart(context).Line(data, options);
$("#data-visualization").click(function(){
    $("#data-visualization").fadeOut()
})
$("#paper1").click(function(){
    $("#data-visualization").fadeIn()
})

setTimeout(updateChart, 500);