    var yf1 = 0;
    var pyf1 = 0;
    var fixj = 0;
    var pfixj = 0;
    var ci = 0;
    var tetr = 0;
    var a = 0;
    var b = 0;
    var c = 0;
    var promoter1 = 1;
    var promoter2 = 0;
    var promoterA = 1;
    var promoterB = 0;
    var promoterC = 0;
    var rbs1 = 1;
    var rbs2 = 0.75;
    var dePhosCoeff1 = 0.5;
    var dePhosCoeff2 = 0.5;
    var phosp = 1;
    var blue_intensity = 0;
    var red_intensity = 0;  // for the intensity switch
    var degCoeffYF1 = 1;
    var degCoeffFixJ = 1;
    var degCoeffCI = 1;
    var degCoeffTetR = 1;
    var degCoeffA = 0.5;
    var degCoeffB = 0.5;
    var degCoeffC = 0.5;
    var timeStep = 0.1;
    var iterations = 600;
    var data = {"YF1":[yf1],
                "PYF1":[pyf1],
                "FixJ":[fixj],
                "PFixJ":[pfixj],
                "CI":[ci],
                "TetR":[tetr],
                "A":[a],
                "B":[b],
                "C":[c]
            }
    var timesteps = [0]; // ??
    //var visualization = Visualization(self) // ??
    //var visualization.start() // ??

function getAmount(proteinName){
    return data[proteinName][data[proteinName].length -1];
}

function derivativeYF1(currentConcentration){
    return promoter1 * rbs1 + dePhosCoeff1 * getAmount('PYF1') - (degCoeffYF1 + blue_intensity) * currentConcentration;
}

function derivativePYF1(currentConcentration){
    return blue_intensity * getAmount('YF1') - (dePhosCoeff1 + degCoeffYF1) * currentConcentration;
}

function derivativeFixJ(currentConcentration){
    return promoter1 * rbs1 + dePhosCoeff2 * getAmount('PFixJ') - (phosp * getAmount('PYF1') + degCoeffFixJ) * currentConcentration;
}

function derivativePFixJ(currentConcentration){
    return phosp * getAmount('FixJ') * getAmount('PYF1') - (dePhosCoeff2 + degCoeffFixJ) * currentConcentration;
}

function derivativeCI(currentConcentration){
    return promoter2 * rbs1 - degCoeffCI * currentConcentration;
}

function derivativeTetR(currentConcentration){
    return (promoterA + promoterB) * rbs2 - degCoeffTetR * currentConcentration;
}

function derivativeA(currentConcentration){
    return promoterA * rbs1 - degCoeffA * currentConcentration;
}

function derivativeB(currentConcentration){
    return promoterB * rbs1 - degCoeffB * currentConcentration;
}

function derivativeC(currentConcentration){
    return promoterC * rbs1 - degCoeffC * currentConcentration;
}

function derivativeSelect(proteinName, currentConcentration){
    //Select appropriate derivative
    if (proteinName == 'YF1'){
        return derivativeYF1(currentConcentration);
    }
    else if (proteinName == 'PYF1'){
        return derivativePYF1(currentConcentration);
    }
    else if (proteinName == 'FixJ'){
        return derivativeFixJ(currentConcentration);
    }
    else if (proteinName == 'PFixJ'){
        return derivativePFixJ(currentConcentration);
    }
    else if (proteinName == 'CI'){
        return derivativeCI(currentConcentration);
    }
    else if (proteinName == 'TetR'){
        return derivativeTetR(currentConcentration);
    }
    else if (proteinName == 'A'){
        return derivativeA(currentConcentration);
    }
    else if (proteinName == 'B'){
        return derivativeB(currentConcentration);
    }
    else if (proteinName == 'C'){
        return derivativeC(currentConcentration);
    }
}

function promoterUpdate(){
    promoter2 = 7 * getAmount('PFixJ');
    promoterA = (1 - red_intensity) * (1 - getAmount('CI'));
    if (getAmount('CI') < 1){
        promoterB = (1 - red_intensity) * (getAmount('CI'));
    }
    else{
        promoterB = (1 - red_intensity) * (1 - 2.5 * (getAmount('CI') - 1));
    }
    promoterC = (1 - red_intensity) * (1 - (1.75 / 0.75) * getAmount('TetR'));
}

function oneStep(i){
    var keyList = Object.keys(data);

    for(var j = 0; j < keyList.length;j++){
        x = getAmount(keyList[j]);
        coeff1 = derivativeSelect(keyList[j], x);
        coeff2 = derivativeSelect(
            keyList[j], (x + (coeff1) * timeStep / 2));
        coeff3 = derivativeSelect(
            keyList[j], (x + (coeff2) * timeStep / 2));
        coeff4 = derivativeSelect(
            keyList[j], (x + (coeff3) * timeStep));
        x = x + (timeStep / 6) * (coeff1 + 2 * coeff2 + 2 * coeff3 + coeff4);
        if(x > 0){
            data[(keyList[j])].push(x);
        }
        else{
            data[(keyList[j])].push(0);
        }
    }
    timesteps.push(i + 1);
    promoterUpdate();
    var R = 200 + (getAmount('A') * 27.5) - (getAmount('B') * 45) - (getAmount('C') * 45);
    var G = 185 + (getAmount('B') * 35) - (getAmount('A') * 40) - (getAmount('C') * 40);
    var B = 125 + (getAmount('C') * 65) - (getAmount('B') * 25) - (getAmount('C') * 25);
    // A = red, B = green, C = blue. They reduce the others to make the colors more vivid.
    // The base values for each color are for a nice E.Coli light brown.
    setColonyColor("RGB(" + R  + ","  + G + "," + B + ")");
}

function run(){
    //Runge-Kutta computation for protein concentrations
    var i = 0;
    setInterval(function() {
        var light = getLightIntensities();
        blue_intensity = light.blue/100;
        red_intensity = 1 - light.red/100;
        //console.log(blue_intensity);
        //console.log(red_intensity);
        i++;
        oneStep(i);
    }, 100)
}

run();
