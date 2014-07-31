/* Some helping functions to make arcs easier*/
Raphael.fn.arc = function(startX, startY, endX, endY, radius1, radius2, angle) {
  var arcSVG = [radius1, radius2, angle, 0, 1, endX, endY].join(' ');
  return this.path('M'+startX+' '+startY + " a " + arcSVG);
};

Raphael.fn.circularArc = function(centerX, centerY, radius, startAngle, endAngle) {
  var startX = centerX+radius*Math.cos(startAngle*Math.PI/180);
  var startY = centerY+radius*Math.sin(startAngle*Math.PI/180);
  var endX = centerX+radius*Math.cos(endAngle*Math.PI/180);
  var endY = centerY+radius*Math.sin(endAngle*Math.PI/180);
  return this.arc(startX, startY, endX-startX, endY-startY, radius, radius, 0);
};

function setBlueLight(event, ui){
    var value = ui.value

    if (value < 0) {
        value = 0;
    }

    if (value > 100) {
        value = 100;
    }

    value = 100-value
    arcLeft.attr({
        stroke: "rgb("+(50+value).toString()+","+(50+value).toString()+","+(255-value).toString()+")"
    });
}

function setRedLight(event, ui){
    var value = ui.value

    if (value < 0) {
        value = 0;
    }

    if (value > 100) {
        value = 100;
    }

    value = 100-value
    arcRight.attr({
        stroke: "rgb("+(255-value).toString()+","+(50+value).toString()+","+(50+value).toString()+")"
    });
}

function checkOrientation(){
    if (window.innerHeight < window.innerWidth){
        location.reload();
    } else {
        setTimeout(checkOrientation, 1000);
    }
}

window.onresize = function() {
    location.reload();
}

var landscape = true;
if(window.innerHeight > window.innerWidth){
    landscape = false;
    setTimeout(checkOrientation, 1000)
}
console.log(landscape)

/* Init drawing area */
var width = $(document).width()*0.8;
var height = $(document).height()*0.9;
var radius = Math.min(height,width)/2;
$("#paper1").css("margin-top", (0.05*$(document).height()).toString() + "px");
$("#paper1").css("margin-left", (0.1*$(document).width()).toString() + "px");
console.log(height)
console.log(width)
var stroke = 10;
var fade = 0;
var paper = Raphael("paper1", width, height);

var arcRight = paper.circularArc(width/2,height/2,radius-stroke,270,90).attr({
    "stroke-width":10,
    stroke: "rgb(250,0,0)"
});
var arcLeft = paper.circularArc(width/2,height/2,radius-stroke,90,270).attr({
    "stroke-width":10,
    stroke: "rgb(50,50,255)"
});

function drawCircles() {
    var circleAmount = Math.floor(Math.random() * 6) + 4;

    var circleList = [];
    var centerX = width/2;
    var centerY = height/2;
    var radius = (Math.min(height, width)-stroke)/2;
    var distance = 0;
    var angle = 0;
    var size = 0;
    var tmp = 0;

    for (var i = 0; i < circleAmount; i ++) {
        size = (15+Math.random()*30)*centerY/500;
        distance = Math.random()*radius-size-stroke;
        angle = Math.random()*2*Math.PI;
        tmp = paper.circle(centerX+Math.cos(angle)*distance, centerY+Math.sin(angle)*distance, size)
        if (overlap(tmp, circleList)){
            i --;
            tmp.remove()
        } else {
            circleList.push(tmp);
        }
    }
    return circleList;
}

function overlap(circ, list) {
    for (var i = 0; i < list.length; i++){
        if (_overlap(circ, list[i])){
            return true;
        }
    }
    return false;
}
function _overlap(circ1, circ2) {
    var attrs = ["cx", "cy", "r"];
    var c1 = circ1.attr(attrs);
    var c2 = circ2.attr(attrs);
    var dist = Math.sqrt(Math.pow(c1.cx - c2.cx ,2) + Math.pow(c1.cy - c2.cy, 2));
    return (dist < (c1.r + c2.r));
}

function setColonyColor(rgbString, circleList) {
    for (var i = 0; i < circleList.length; i++) {
        circleList[i].attr({
            fill: rgbString
        })
    }
}

function getLightIntensities() {
    return {
        blue: $("#slider-left").slider("value"),
        red: $("#slider-right").slider("value")
    };
}

/* Init UI */
if (landscape) {
    $("#slider-left").slider({
        max: 100,
        min: 0,
        orientation: "vertical",
        change: setBlueLight,
        value: 100,
        animate: "slow"
    }).draggable();

    $("#slider-right").slider({
        max: 100,
        min: 0,
        orientation: "vertical",
        change: setRedLight,
        value: 100,
        animate: "slow"
    }).draggable();
} else {
    $("#alert").addClass("visible")
}

var circleList = drawCircles();