        var yf1 = 0;
        var pyf1 = 0;
        var fixj = 0;
        var pfixj = 0;
        var ci = 0;
        var tetr = 0;
        var a = 0;
        var b = 0;
        var c = 0;
        var promotor1 = 1;
        var promotor2 = 0;
        var promotorA = 1;
        var promotorB = 0;
        var promotorC = 0;
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

    var map = {"YF1":yf1,;
                "PYF1":pyf1,;
                "FixJ":fixj,;
                "PFixJ":pfixj,;
                "CI":ci,;
                "TetR":tetr,;
                "A":aConcentration,;
                "B":bConcentration,;
                "C":cConcentration;
            }
    var timesteps = [0] // ?? 
    var visualization = Visualization(self) // ??
    var visualization.start() // ??

// WHAT THE HELL KIND OF DATA IS PROTEIN, you can use it multiply and use it as a key??????

