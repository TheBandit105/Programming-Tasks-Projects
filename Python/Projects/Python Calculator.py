import math

print('\nHello, welcome to the Python Calculator! \n')

while True:
    print('Please select an operation below: \n')

    print('Addition \t-> \ta  \t\tGamma Function \t -> \tgamma')
    print('Subtraction \t-> \ts \t\tFind Hypotenuse  ->\thypot')
    print('Multiplication \t-> \tm  \t\tIs Close \t -> \tisclose')
    print('Division \t-> \td    \t\tIs Finite \t -> \tisf')
    print('Floor Division \t-> \tf  \t\tIs Infinite \t -> \tisinf')
    print('Ceiling Division -> \tc  \t\tIs Not a Number  -> \tisNaN')
    print('Modulus (Remainder) -> \tmod \t\tInverse Mantissa & Exponent -> \tldexp')
    print('Greatest Common Divisor -> gcd \t\tLog Gamma \t -> \tlgamma')
    print('Arc Cosine \t-> \tacos \t\tLog \t\t -> \tlog')
    print('Inverse Hyperbolic Cosine -> acosh \tBase-10 Log \t -> \tlog10')
    print('Arc Sine \t-> \tasin \t\tLog(1 + x) \t -> \tlog1p')
    print('Inverse Hyperbolic Sine -> asinh \tBase-2 Log \t -> \tlog2')
    print('Arc Tangent \t-> \tatan \t\tPower \t\t -> \tpow')
    print('Arc Tangent of a/b -> \tatan2 \t\tDegrees to Radians -> \trad')
    print('Inverse Hyperbolic Tangent -> atanh \tSine \t\t -> \tsin') 
    print('Possibility Finder -> \tcomb \t\tHyperbolic Sine  -> \tsinh')
    print('Cosine \t\t-> \tcos \t\tSquare Root \t -> \tsqrt')
    print('Hyperbolic Cosine -> \tcosh \t\tTangent \t -> \ttan')
    print('Radians to Degrees -> \tdeg \t\tHyperbolic Tangent -> \ttanh')
    print('E^x \t\t-> \texp \t\tTruncate \t -> \ttrunc')
    print('(E^x) - 1 \t-> \texpm1 \t\tRemainder \t -> \tremder')
    print('Absolute Value of Number -> fabs \tQuit \t\t -> \tquit or q')
    print('Factorial \t-> \tfctrl')
    print('Mantissa & Exponent -> \tfrexp')

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
        print('\nPlease input the values of n and k to find number of possibilities: \n')
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

    elif selection == 'deg':
        print('\nPlease input a value to convert from radians to degrees: \n')
        a = float(input())
        print('\n',math.degrees(a))
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

    elif selection != '':
        print('\nInvalid choice, please try again: \n')

    elif selection == 'quit' or 'q':
        exit()

