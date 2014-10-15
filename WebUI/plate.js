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
    var minFlashWidth = 0.3*flashWidth;
    var maxFlashColor = 255;
    var colorString = ((value)/100*(maxFlashColor)).toString();
    leftFlash.attr({
        fill: 'r(0.5, 0.5)rgb(' + colorString + "," + colorString +
            ",255)-rgba(255,255,255):"+ (minFlashWidth + (flashWidth - minFlashWidth)*(100-value)/100).toString()
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
    var minFlashWidth = 0.3*flashWidth;
    var maxFlashColor = 255;
    var colorString = ((value)/100*(maxFlashColor)).toString();
    rightFlash.attr({
        fill: 'r(0.5, 0.5)rgb(255,' + colorString + "," + colorString +
            ")-rgba(255,255,255):"+ (minFlashWidth + (flashWidth - minFlashWidth)*(100-value)/100).toString()
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
    setTimeout(checkOrientation, 1000);
}

/* Init drawing area */
var width = $(document).width()*0.8;
var height = $(document).height()*0.9;
// Colony parameters
var minSize = 15;
var maxSize = 45;
var scalingConstant = height/2/500;

var radius = Math.min(height,width)/2;

$("#paper1").css("margin-top", (0.02*$(document).height()).toString() + "px");
$("#paper1").css("margin-left", (0.1*$(document).width()).toString() + "px");
var stroke = 10;
var fade = 0;
var paper = Raphael("paper1", width, height);

// Create plate background
paper.circle(width/2, height/2, radius-stroke).attr({
    fill: "rgb(230,230,230)",
    "stroke-opacity": 0
});
// Create light bars
var arcRight = paper.circularArc(width/2,height/2,radius-stroke,270,90).attr({
    "stroke-width":10,
    stroke: "rgb(250,0,0)"
});
var arcLeft = paper.circularArc(width/2,height/2,radius-stroke,90,270).attr({
    "stroke-width":10,
    stroke: "rgb(50,50,255)"
});

function createColonies() {
    var colonyAmount = Math.floor(Math.random() * 3) + 2;

    for (var i = 0; i < colonyAmount; i ++) {
        createColony();
    }
}


function createColony() {
    var notFound = true;
    j = 0;

    var centerX = width/2;
    var centerY = height/2;
    var radius = (Math.min(height, width)-stroke)/2;
    var distance = 0;
    var angle = 0;
    var size = 0;

    while (j < 5 && notFound) {
        if (colonyList.length >= 25){
            notFound = false;
        }
        if (growing) {
            size = 5*scalingConstant;
        } else {
            size = (minSize+Math.random()*(maxSize-minSize))*scalingConstant;
        }
        distance = Math.random()*radius-size-stroke;
        angle = Math.random()*2*Math.PI;
        var colony = paper.circle(centerX+Math.cos(angle)*distance, centerY+Math.sin(angle)*distance, size).attr({'stroke-opacity': 0})
        if (overlap(colony, colonyList)){
            colony.remove()
        } else {
            colonyList.push(colony);
            notFound = false;
        }
        if (! notFound) {
            break;
        }
    }

    if (notFound) {
        return false;
    } else {
        return true;
    }


}

function isInside(circ) {
    var params = circ.attr(["cx","cy","r"]);
    var pointX = 0;
    var pointY = 0;
    var xDistance = 0;
    var yDistance = 0;
    var testPoints = 6;
    for (var i = 0; i < 6; i++) {
        pointX = params.cx + Math.cos(Math.PI*i/(testPoints/2))*params.r;
        xDistance = Math.abs(width/2 - pointX);
        pointY = params.cy + Math.sin(Math.PI*i/(testPoints/2))*params.r;
        yDistance = Math.abs(height/2 - pointY);
        if (Math.sqrt(xDistance*xDistance + yDistance*yDistance) >= radius - stroke*1.55){
            console.log("is outside");
            return false;
        }
    }
    return true;
}

function overlap(circ, list) {
    for (var i = 0; i < list.length; i++){
        if (circ !== list[i]){
            if (_overlap(circ, list[i])){
                return true;
            }
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

function growColonies() {
    var circle = 0;
    for (var i=0; i<colonyList.length; i++) {
        circle = colonyList[i];
        if (!overlap(circle, colonyList) && isInside(circle)){
            circle.attr("r", growFunction(circle.attr("r")))
        }
    }
    if (Math.random() < 0.025) {
        createColony()
    }
}

function growFunction(value) {
    var h = 1;
    return value + (maxSize*0.8 - value)/maxSize*h*scalingConstant;
}

function setColonyColor(rgbString) {
    for (var i = 0; i < colonyList.length; i++) {
        colonyList[i].attr({
            fill: 'r(0.5, 0.5)' + rgbString + "-" + rgbString +':'+ 2.3*colonyList[i].attr("r") +'-rgb(230,230,230)'
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
        slide: setBlueLight,
        value: 100,
        animate: "slow"
    }).draggable();

    $("#slider-right").slider({
        max: 100,
        min: 0,
        orientation: "vertical",
        slide: setRedLight,
        value: 100,
        animate: "slow"
    }).draggable();
} else {
    $("#alert").addClass("visible")
}

var colonyList = [];
createColonies();


// Bulb gradients
var flashWidth = 0.22*height
var leftFlashPaper = Raphael("flash-left", flashWidth, flashWidth);
var leftFlash = leftFlashPaper.circle(flashWidth/2,flashWidth/2,flashWidth/2).attr("stroke-opacity",0)
var rightFlashPaper = Raphael("flash-right", flashWidth, flashWidth);
var rightFlash = rightFlashPaper.circle(flashWidth/2,flashWidth/2,flashWidth/2).attr("stroke-opacity",0)

setBlueLight(123, {value:100})
setRedLight(123, {value:100})

var growing = true;
setInterval(growColonies, 300);
