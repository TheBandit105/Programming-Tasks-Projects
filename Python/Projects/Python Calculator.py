import math
import cmath
import statistics

print('\nHello, welcome to the Python Calculator V1! \n')

while True:
    print('Please select an operation below: \n')

    print('Addition \t-> \ta  \t\tGamma Function \t -> \tgamma \t\tComplementary Error Function \t -> \terfc \t\tComplex Hyperbolic Cosine \t ->\tccosh')
    print('Subtraction \t-> \ts \t\tFind Hypotenuse  ->\thypot \t\tIs Square Root \t\t\t ->\tisqrt \t\tE^(complex) \t\t ->\tcexp')
    print('Multiplication \t-> \tm  \t\tIs Close \t -> \tisclose \tPerm \t\t\t\t ->\tperm \t\tComplex Is Close \t ->\tcisclose')
    print('Division \t-> \td    \t\tIs Finite \t -> \tisf \t\tHarmonic Mean \t\t\t ->\thmean \t\tComplex Is Finite \t ->\tcisf')
    print('Floor Division \t-> \tf  \t\tIs Infinite \t -> \tisinf \t\tMean \t\t\t\t ->\tmean \t\tComplex Is Infinite \t ->\tcisinf')
    print('Ceiling Division -> \tc  \t\tIs Not a Number  -> \tisNaN \t\tMedian \t\t\t\t ->\tmedian \t\tComplex Is Not a Number  ->\tcisNaN')
    print('Modulus (Remainder) -> \tmod \t\tInverse Mantissa & Exponent -> \tldexp\tHigh Median \t\t\t ->\thmedian \tComplex Log \t\t ->\tclog')
    print('Greatest Common Divisor -> gcd \t\tLog Gamma \t -> \tlgamma\t\tLow Median \t\t\t ->\tlmedian \tComplex Base-10 Log \t ->\tclog10')
    print('Arc Cosine \t-> \tacos \t\tLog \t\t -> \tlog\t\tMode \t\t\t\t ->\tmode \t\tComplex Log \t\t ->\tclog')
    print('Inverse Hyperbolic Cosine -> acosh \tBase-10 Log \t -> \tlog10\t\tStandard Deviation (Population)\t ->\tpstdev \t\tPhase \t\t\t ->\tphase')
    print('Arc Sine \t-> \tasin \t\tLog(1 + x) \t -> \tlog1p\t\tStandard Deviation (Data Sample) ->\tstdev \t\tPolar \t\t\t ->\tpolar')
    print('Inverse Hyperbolic Sine -> asinh \tBase-2 Log \t -> \tlog2\t\tVariance (Population) \t\t ->\tpvar \t\tPolarRect \t\t ->\trect')
    print('Arc Tangent \t-> \tatan \t\tPower \t\t -> \tpow\t\tVariance (Data Sample) \t\t ->\tvar \t\tComplex Sine \t\t ->\tcsin')
    print('Arc Tangent of a/b -> \tatan2 \t\tDegrees to Radians -> \trad\t\tComplex Addition \t\t ->\tca \t\tComplex Hyperbolic Sine  ->\tcsinh')
    print('Inverse Hyperbolic Tangent -> atanh \tSine \t\t -> \tsin\t\tComplex Subtraction \t\t ->\tcs \t\tComplex Square root \t ->\tcsqrt') 
    print('Possibility Finder -> \tcomb \t\tHyperbolic Sine  -> \tsinh\t\tComplex Multiplication \t\t ->\tcm \t\tComplex Tangent \t ->\tctan')
    print('Cosine \t\t-> \tcos \t\tSquare Root \t -> \tsqrt\t\tComplex Division \t\t ->\tcd \t\tComplex Hyperbolic Tangent ->\tctanh')
    print('Hyperbolic Cosine -> \tcosh \t\tTangent \t -> \ttan\t\tComplex Arc Cosine \t\t ->\tcacos \t\tSummation \t\t ->\tfsum')
    print('Radians to Degrees -> \tdeg \t\tHyperbolic Tangent -> \ttanh\t\tComplex Hyperbolic Arc Cosine \t ->\tcacosh \t\tProduct \t\t ->\tprod')
    print('E^x \t\t-> \texp \t\tTruncate \t -> \ttrunc\t\tComplex Arc Sine \t\t ->\tcasin')
    print('(E^x) - 1 \t-> \texpm1 \t\tRemainder \t -> \tremder\t\tComplex Hyperbolic Arc Sine \t ->\tcasinh')
    print('Absolute Value of Number -> fabs \tDistance \t -> \tdist\t\tComplex Arc Tangent \t\t ->\tcatan')
    print('Factorial \t-> \tfctrl \t\tCopysign \t -> \tcpysgn\t\tComplex Hyperbolic Arc Tangent \t ->\tcatanh')
    print('Mantissa & Exponent -> \tfrexp \t\tError Function \t -> \terf \t\tComplex Cosine \t\t\t ->\tccos  \t\tQuit \t\t -> \tquit or q')

    selection = input('\nInput: ')

    if selection == 'a':
        print('\nPlease input two values to add: \n')
        a = float(input())
        b = float(input())
        print('\n',a + b)
        print('\n')

    elif selection == 's':
        print('\nPlease input two values to subtract: \n')
        a = float(input())
        b = float(input())
        print('\n',a - b)
        print('\n')
              
    elif selection == 'm':
        print('\nPlease input two values to multiply: \n')
        a = float(input())
        b = float(input())
        print('\n',a * b)
        print('\n')
              
    elif selection == 'd':
        print('\nPlease input two values to divide: \n')
        a = float(input())
        b = float(input())
        print('\n',a / b)
        print('\n')

    elif selection == 'f':
        print('\nPlease input two values to find the floor division: \n')
        a = float(input())
        b = float(input())
        print('\n',math.floor(a / b))
        print('\n')

    elif selection == 'c':
        print('\nPlease input two values to find the ceiling division: \n')
        a = float(input())
        b = float(input())
        print('\n',math.ceil(a / b))
        print('\n')

    elif selection == 'mod':
        print('\nPlease input two values to find the modulus: \n')
        a = float(input())
        b = float(input())
        print('\n',math.fmod(a, b))
        print('\n')

    elif selection == 'gcd':
        print('\nPlease input values to find the gcd: \n')
        a = int(input())
        b = int(input())
        print('\n',math.gcd(a, b))
        print('\n')

    elif selection == 'acos':
        print('\nPlease input a value to find the arc cosine: \n')
        a = float(input())
        print('\n',math.acos(a))
        print('\n')

    elif selection == 'acosh':
        print('\nPlease input a value to find the inverse hyperbolic cosine: \n')
        a = float(input())
        print('\n',math.acosh(a))
        print('\n')

    elif selection == 'asin':
        print('\nPlease input a value to find the arc sine: \n')
        a = float(input())
        print('\n',math.asin(a))
        print('\n')
        
    elif selection == 'asinh':
        print('\nPlease input a value to find the inverse hyperbolic sine: \n')
        a = float(input())
        print('\n',math.asinh(a))
        print('\n')

    elif selection == 'atan':
        print('\nPlease input a value to find the arc tangent: \n')
        a = float(input())
        print('\n',math.atan(a))
        print('\n',math.atan(a) * (180/math.pi))
        print('\n')

    elif selection == 'atan2':
        print('\nPlease input values to find the arc tangent of a/b: \n')
        a = float(input())
        b = float(input())
        print('\n',math.atan2(a, b))
        print('\n',math.atan2(a, b) * (180/math.pi))

    elif selection == 'atanh':
        print('\nPlease input a value to find the inverse hyperbolic tangent: \n')
        a = float(input())
        print('\n',math.atanh(a))
        print('\n')

    elif selection == 'comb':
        print('\nPlease input the values of n and k to find number of possibilities (without repetition and order): \n')
        n = int(input())
        k = int(input())
        print('\n',math.comb(n, k))
        print('\n')

    elif selection == 'cos':
        print('\nPlease input a value to find the cosine: \n')
        a = float(input())
        print('\n',math.cos(a))
        print('\n')

    elif selection == 'cosh':
        print('\nPlease input a value to find the hyperbolic cosine: \n')
        a = float(input())
        print('\n',math.cosh(a))
        print('\n')

    elif selection == 'cpysgn':
        print('\nPlease input a value to find the value of the first parameter and the sign of the second parameter: \n')
        a = float(input())
        b = float(input())
        print('\n',math.copysign(a, b))
        print('\n')

    elif selection == 'deg':
        print('\nPlease input a value to convert from radians to degrees: \n')
        a = float(input())
        print('\n',math.degrees(a))
        print('\n')

    elif selection == 'dist':
        print('\nPlease input 4 values to find the Euclidean distance between 2 points: \n')
        a_1 = float(input())
        a_2 = float(input())
        b_1 = float(input())
        b_2 = float(input())

        x = [a_1, a_2]
        y = [b_1, b_2]

        print('\nx =', x)
        print('\ny =', y)
        
        print('\n',math.dist(x, y))
        print('\n')

    elif selection == 'erf':
        print('\nPlease input a value to find the error function of given value: \n')
        a = float(input())
        print('\n',math.erf(a))
        print('\n')

    elif selection == 'erfc':
        print('\nPlease input a value to find the complementary error function of given value: \n')
        a = float(input())
        print('\n',math.erfc(a))
        print('\n')

    elif selection == 'exp':
        print('\nPlease input a value to find E raised to the power of inputted value: \n')
        a = float(input())
        print('\n',math.exp(a))
        print('\n')

    elif selection == 'expm1':
        print('\nPlease input a value to same value as exp function, but subtracting 1 from it: \n')
        a = float(input())
        print('\n',math.expm1(a))
        print('\n')

    elif selection == 'fabs':
        print('\nPlease input a value to find its absolute: \n')
        a = float(input())
        print('\n',math.fabs(a))
        print('\n')

    elif selection == 'fctrl':
        print('\nPlease input a value to find its factorial: \n')
        a = int(input())
        print('\n',math.factorial(a))
        print('\n')

    elif selection == 'frexp':
        print('\nPlease input a value to find the mantissa and the exponent (m, e): \n')
        a = float(input())
        print('\n',math.frexp(a))
        print('\n')

    elif selection == 'gamma':
        print('\nPlease input a value to find the gamma function: \n')
        a = float(input())
        print('\n',math.gamma(a))
        print('\n')

    elif selection == 'hypot':
        print('\nPlease input 2 values to find the hypotenuse: \n')
        p = float(input('Parendicular: '))
        b = float(input('Base: '))
        print('\n',math.hypot(p, b))
        print('\n')

    elif selection == 'isclose':
        print('\nPlease input 2 values to check if they are close to each other: \n')
        a = float(input())
        b = float(input())
        print('\n',math.isclose(a, b))
        print('\n')

    elif selection == 'isf':
        print('\nPlease input a value to check if it is finite: \n')
        a = float(input())
        print('\n',math.isfinite(a))
        print('\n')

    elif selection == 'isinf':
        print('\nPlease input a value to check if it is infinite: \n')
        a = float(input())
        print('\n',math.isinf(a))
        print('\n')

    elif selection == 'isNaN':
        print('\nPlease input a value to check if it is Not a Number: \n')
        a = float(input())
        print('\n',math.isnan(a))
        print('\n')

    elif selection == 'isqrt':
        print('\nPlease input a square root value to the nearest integer, to check if the value is a true square root: \n')
        a = int(input())
        print('\n',math.isqrt(a))
        print('\n')

    elif selection == 'ldexp':
        print('\nPlease input 2 values (mantissa and exponent) to find the inverse of frexp: \n')
        m = float(input())
        e = float(input())
        print('\n',math.ldexp(m, e))
        print('\n')

    elif selection == 'lgamma':
        print('\nPlease input a value to find its natural log gamma: \n')
        a = float(input())
        print('\n',math.lgamma(a))
        print('\n')

    elif selection == 'log':
        print('\nPlease input a value to find the natural log: \n')
        a = float(input())
        print('\n',math.log(a))
        print('\n')

    elif selection == 'log10':
        print('\nPlease input a value to find the base-10 log: \n')
        a = float(input())
        print('\n',math.log10(a))
        print('\n')

    elif selection == 'log1p':
        print('\nPlease input a value to find log(1 + value): \n')
        a = float(input())
        print('\n',math.log1p(a))
        print('\n')

    elif selection == 'log2':
        print('\nPlease input a value to find the base-2 log: \n')
        a = float(input())
        print('\n',math.log2(a))
        print('\n')

    elif selection == 'perm':
        print('\nPlease input the values of n and k to find number of possibilities (with order and without repetition): \n')
        n = int(input())
        k = int(input())
        print('\n',math.perm(n, k))
        print('\n')

    elif selection == 'pow':
        print('\nPlease input 2 values to find the x ^ y: \n')
        x = float(input())
        y = float(input())
        print('\n',math.pow(x, y))
        print('\n')

    elif selection == 'rad':
        print('\nPlease input a value to convert from degrees to radians: \n')
        a = float(input())
        print('\n',math.radians(a))
        print('\n')

    elif selection == 'remder':
        print('\nPlease input two values to find the remainder: \n')
        a = float(input())
        b = float(input())
        print('\n',math.remainder(a, b))
        print('\n')

    elif selection == 'sin':
        print('\nPlease input a value to find the sine: \n')
        a = float(input())
        print('\n',math.sin(a))
        print('\n')

    elif selection == 'sinh':
        print('\nPlease input a value to find the hyperbolic sine: \n')
        a = float(input())
        print('\n',math.sinh(a))
        print('\n')

    elif selection == 'sqrt':
        print('\nPlease input a value to find the square root: \n')
        a = float(input())
        print('\n',math.sqrt(a))
        print('\n')

    elif selection == 'tan':
        print('\nPlease input a value to find the tan: \n')
        a = float(input())
        print('\n',math.tan(a))
        print('\n')

    elif selection == 'tanh':
        print('\nPlease input a value to find the hyperbolic tan: \n')
        a = float(input())
        print('\n',math.tanh(a))
        print('\n')

    elif selection == 'trunc':
        print('\nPlease input a value to be truncated: \n')
        a = float(input())
        print('\n',math.trunc(a))
        print('\n')

    elif selection == 'hmean':
        print('\nPlease input a number of values to calculate the harmonic mean: \n')
        a = [float(a) for a in input("Enter multiple values: ").split()]
        print('\n',statistics.harmonic_mean(a))
        print('\n')

    elif selection == 'mean':
        print('\nPlease input a number of values to calculate the mean: \n')
        a = [float(a) for a in input("Enter multiple values: ").split()]
        print('\n',statistics.mean(a))
        print('\n')

    elif selection == 'median':
        print('\nPlease input a number of values to calculate the median: \n')
        a = [float(a) for a in input("Enter multiple values: ").split()]
        print('\n',statistics.median(a))
        print('\n')

    elif selection == 'hmed':
        print('\nPlease input a number of values to calculate the high median: \n')
        a = [float(a) for a in input("Enter multiple values: ").split()]
        print('\n',statistics.median_high(a))
        print('\n')

    elif selection == 'lmed':
        print('\nPlease input a number of values to calculate the low median: \n')
        a = [float(a) for a in input("Enter multiple values: ").split()]
        print('\n',statistics.median_low(a))
        print('\n')

    elif selection == 'mode':
        print('\nPlease input a number of values to calculate the mode: \n')
        a = [float(a) for a in input("Enter multiple values: ").split()]
        print('\n',statistics.mode(a))
        print('\n')

    elif selection == 'pstdev':
        print('\nPlease input a number of values to calculate the standard deviation of the generated population: \n')
        a = [float(a) for a in input("Enter multiple values: ").split()]
        print('\n',statistics.pstdev(a))
        print('\n')

    elif selection == 'stdev':
        print('\nPlease input a number of values to calculate the standard deviation of the data sample generated: \n')
        a = [float(a) for a in input("Enter multiple values: ").split()]
        print('\n',statistics.pstdev(a))
        print('\n')

    elif selection == 'pvar':
        print('\nPlease input a number of values to calculate the variance of the generated population: \n')
        a = [float(a) for a in input("Enter multiple values: ").split()]
        print('\n',statistics.pvariance(a))
        print('\n')

    elif selection == 'var':
        print('\nPlease input a number of values to calculate the variance of the data sample generated: \n')
        a = [float(a) for a in input("Enter multiple values: ").split()]
        print('\n',statistics.variance(a))
        print('\n')

    elif selection == 'ca':
        print('\nPlease input two complex numbers to add: \n')
        a1, a2, b1, b2 = [float(x) for x in input("Enter four values: ").split()]
        a = complex(a1, a2)
        b = complex(b1, b2)
        print('\n', a + b)
        print('\n')
            
    elif selection == 'cs':
        print('\nPlease input two complex numbers to subtract: \n')
        a1, a2, b1, b2 = [float(x) for x in input("Enter four values: ").split()]
        a = complex(a1, a2)
        b = complex(b1, b2)
        print('\n', a - b)
        print('\n')

    elif selection == 'cm':
        print('\nPlease input two complex numbers to multiply: \n')
        a1, a2, b1, b2 = [float(x) for x in input("Enter four values: ").split()]
        a = complex(a1, a2)
        b = complex(b1, b2)
        print('\n', a * b)
        print('\n')

    elif selection == 'cd':
        print('\nPlease input two complex numbers to divide: \n')
        a1, a2, b1, b2 = [float(x) for x in input("Enter four values: ").split()]
        a = complex(a1, a2)
        b = complex(b1, b2)
        print('\n', a / b)
        print('\n')

    elif selection == 'cacos':
        print('\nPlease input a complex value to find the arc cosine: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.acos(a))
        print('\n')

    elif selection == 'cacosh':
        print('\nPlease input a complex value to find the hyperbolic arc cosine: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.acosh(a))
        print('\n')

    elif selection == 'casin':
        print('\nPlease input a complex value to find the arc sine: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.asin(a))
        print('\n')

    elif selection == 'casinh':
        print('\nPlease input a complex value to find the hyperbolic arc sine: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.asinh(a))
        print('\n')

    elif selection == 'catan':
        print('\nPlease input a complex value to find the arc tangent: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.atan(a))
        print('\n')

    elif selection == 'catanh':
        print('\nPlease input a complex value to find the hyperbolic arc tangent: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.atanh(a))
        print('\n')

    elif selection == 'ccos':
        print('\nPlease input a complex value to find the cosine: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.cos(a))
        print('\n')

    elif selection == 'ccosh':
        print('\nPlease input a complex value to find the hyperbolic cosine: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.cosh(a))
        print('\n')

    elif selection == 'cexp':
        print('\nPlease input a complex value to find E raised to the power of inputted complex value: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.exp(a))
        print('\n')

    elif selection == 'cisclose':
        print('\nPlease input 2 complex values to check if they are close to each other: \n')
        a1, a2, b1, b2 = [float(x) for x in input("Enter four values: ").split()]
        a = complex(a1, a2)
        b = complex(b1, b2)
        print('\n', cmath.isclose(a, b))
        print('\n')

    elif selection == 'cisf':
        print('\nPlease input a complex value to check if it is finite: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.isfinite(a))
        print('\n')

    elif selection == 'cisinf':
        print('\nPlease input a complex value to check if it is infinite: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.isinf(a))
        print('\n')

    elif selection == 'cisNaN':
        print('\nPlease input a complex value to check if it is Not a Number: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.isnan(a))
        print('\n')

    elif selection == 'clog':
        print('\nPlease input a complex value to find the natural log: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.log(a))
        print('\n')

    elif selection == 'clog10':
        print('\nPlease input a complex value to find the base-10 log: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.log10(a))
        print('\n')

    elif selection == 'phase':
        print('\nPlease input a complex value to find its phase: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.phase(a))
        print('\n')

    elif selection == 'polar':
        print('\nPlease input a complex value to convert into its polar coordinates form: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.polar(a))
        print('\n')

    elif selection == 'rect':
        print('\nPlease input a polar coordinate to convert into its rectangular form: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.rect(a))
        print('\n')

    elif selection == 'csin':
        print('\nPlease input a complex value to find the sine: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.sin(a))
        print('\n')

    elif selection == 'csinh':
        print('\nPlease input a complex value to find the hyperbolic sine: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.sinh(a))
        print('\n')

    elif selection == 'csqrt':
        print('\nPlease input a complex value to find the square root: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.sqrt(a))
        print('\n')

    elif selection == 'ctan':
        print('\nPlease input a complex value to find the tangent: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.tan(a))
        print('\n')

    elif selection == 'ctanh':
        print('\nPlease input a complex value to find the hyperbolic tangent: \n')
        a1, a2 = [float(x) for x in input("Enter two values: ").split()]
        a = complex(a1, a2)
        print('\n',cmath.tanh(a))
        print('\n')

    elif selection == 'fsum':
        print('\nPlease input a number of values to calculate the sum of all the values: \n')
        a = [float(a) for a in input("Enter multiple values: ").split()]
        print('\n',math.fsum(a))
        print('\n')

    elif selection == 'prod':
        print('\nPlease input a number of values to calculate the product of all the values: \n')
        a = [float(a) for a in input("Enter multiple values: ").split()]
        print('\n',math.prod(a))
        print('\n')

    elif selection == '' or selection == ' ' or selection == '  ' \
         or selection == '   ' or selection == '    ' or selection == '     ':
        print('\nNo input given, please try again: \n')
        continue

    elif selection == 'quit' or 'q':
        break

    

