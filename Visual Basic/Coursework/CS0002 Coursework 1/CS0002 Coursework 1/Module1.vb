Imports System.Math
Module Module1

    Sub Main() ' "Sub Main()" opens up the main subroutine where the main programming is executed on command when tested.

        Dim selection As Integer ' "Dim selection As Integer" means you have declared 'selection' as an integer, meaning that the input value can only be whole numbers.

        Do Until selection < 7 And selection > 0  ' "Do Until selection < 7 and selection > 0" means that this loop will repeat until the user inputs an numbered option which falls in the range that is < 7 and > 0. The error "Invalid input! Please select one of the options below and try again." is there to remind the user to select the correct options and try again and is only implemented upon the user inputting a value that falls outside the specified range of selection < 7 and selection > 0.

            Console.Clear()
            Console.Title = "CS0002 Programming Coursework - Thomas Croos" ' "Console.Title" is where the an inputted string is displayed on the title bar of the output console (Windows Command Processor) upon execution of the program.
            Console.WriteLine("CS0002 Programming Coursework")
            Console.WriteLine("by Thomas Croos")
            Console.WriteLine("-----------------------------------------------------------------------")

            Console.WriteLine("1) Accuracy Option")    ' "Console.WriteLine()" means whatever you type as a string will be displayed on the output console when the program is executed.
            Console.WriteLine("2) Quadratic Equation")
            Console.WriteLine("3) Monte-Carlo Integration")
            Console.WriteLine("4) Prime Decision")
            Console.WriteLine("5) Help")
            Console.WriteLine("6) Exit")
            Console.WriteLine(" ")
            Console.WriteLine("Select from options 1-6 and then press enter:")

            selection = Console.ReadLine() ' "Console.Readline()" allows for the user to input a value 
            Console.WriteLine(" ")
            Console.Clear()
            Console.WriteLine("Invalid input! Please select one of the options below and try again.")
            Console.WriteLine(" ")

        Loop

        Select Case selection ' "Select Case selection" means when you type a number from 1 to 6 in the "selection = Console.ReadLine()", the number inputed by the user is compared to the cases that have been inputed into the program.
            Case 1
                Console.Clear()
                Console.WriteLine("Accuracy Option") 'This "Console.WriteLine("Accuracy Option")"  and the others are shown in their respective private subroutines as the title for them.
                Console.WriteLine(" ")
                Task1() ' Once a case has been selected, the program will take you to a private subroutine based on what option you made in the menu (e.g. option 1 means you go to the private subroutine "Task1()").
            Case 2
                Console.Clear()
                Console.WriteLine("Quadratic Equation")
                Console.WriteLine(" ")
                Task2()
            Case 3
                Console.Clear()
                Console.WriteLine("Monte-Carlo Integration")
                Console.WriteLine(" ")
                Task3()
            Case 4
                Console.Clear()
                Console.WriteLine("Prime Decision")
                Console.WriteLine(" ")
                Task4()
            Case 5
                Console.Clear()
                Console.WriteLine("Help")
                Console.WriteLine(" ")
                Task5()
            Case 6
                Console.Clear()
                Environment.Exit(-1)


        End Select

    End Sub

    Private Sub Task1()

        Dim selectionacc As Integer ' "Dim selectionacc As Integer" means that only an integer value can inputted into selectionacc, since this has been declared as an integer.

        Do Until selectionacc < 6 And selectionacc > 0

            Console.WriteLine("Please select the number of decimal places (1 to 5) and then press enter:")
            selectionacc = Console.ReadLine()
            Console.WriteLine(" ")
            Console.Clear()

            Console.WriteLine("Invalid input! Please select the number of decimal places (1 to 5) and try again.")

            Console.WriteLine(" ")

        Loop

        Select Case selectionacc
            Case 1
                Console.WriteLine(" ")
                Console.WriteLine("Number of decimal places set to 1.")
                Console.WriteLine(" ")
                Console.WriteLine(Format(selectionacc, "#,#0.0"))
                Console.WriteLine(" ")
            Case 2
                Console.WriteLine(" ")
                Console.WriteLine("Number of decimal places set to 2.")
                Console.WriteLine(" ")
                Console.WriteLine(Format(selectionacc, "#,#0.00"))
                Console.WriteLine(" ")
            Case 3
                Console.WriteLine(" ")
                Console.WriteLine("Number of decimal places set to 3.")
                Console.WriteLine(" ")
                Console.WriteLine(Format(selectionacc, "#,#0.000"))
                Console.WriteLine(" ")
            Case 4
                Console.WriteLine(" ")
                Console.WriteLine("Number of decimal places set to 4.")
                Console.WriteLine(" ")
                Console.WriteLine(Format(selectionacc, "#,#0.0000"))
                Console.WriteLine(" ")
            Case 5
                Console.WriteLine(" ")
                Console.WriteLine("Number of decimal places set to 5.")
                Console.WriteLine(" ")
                Console.WriteLine(Format(selectionacc, "#,#0.00000"))
                Console.WriteLine(" ")
        End Select

        Console.WriteLine("Press any key to return to the main menu")
        Console.ReadLine()
        Call Main()


    End Sub
    Private Sub Task2()
        Dim a, b, c, x1, x2 As Double
        Dim det As Double

        Console.WriteLine("Please input a, b, c with any numbers as long as a is not 0")

        Do Until a <> 0
            a = Console.ReadLine()
            Console.Clear()
            Console.WriteLine("a =" + Str(a))


            If a = 0 Then
                Console.WriteLine("Re-enter a value for a which is not 0.")
            End If
        Loop
        b = Console.ReadLine()
        Console.Clear()
        Console.WriteLine("b =" + Str(b))
        c = Console.ReadLine()
        Console.Clear()
        Console.WriteLine("c =" + Str(c))
        Console.Clear()

        Console.WriteLine("a =" + Str(a))
        Console.WriteLine("b =" + Str(b))
        Console.WriteLine("c =" + Str(c))


        det = b * b - 4 * a * c


        If det >= 0 Then
            If det = 0 Then
                x1 = (-b + Math.Sqrt((b ^ 2) - (4 * a * c))) / (2 * a)
                x2 = (-b - Math.Sqrt((b ^ 2) - (4 * a * c))) / (2 * a)

                x1 = x2

                Console.WriteLine(" ")

                Console.WriteLine("root 1 =" + Str(x1))
                Console.WriteLine("root 2 =" + Str(x2))
                Console.WriteLine(" ")
                Console.WriteLine(Str(x1) + " = " + Str(x2))
                Console.WriteLine(" ")
                Console.WriteLine("Since the values" + Str(a) + ", " + Str(b) + " and" + Str(c) + " produce root 1 and root 2 with the same answers, the quadratic equation has only one solution.")
                Console.WriteLine("Therefore, the roots are real and equal.")
                Console.WriteLine(" ")
            Else
                x1 = (-b + Math.Sqrt((b ^ 2) - (4 * a * c))) / (2 * a)
                Console.WriteLine("root 1 =" + Str(x1))
                x2 = (-b - Math.Sqrt((b ^ 2) - (4 * a * c))) / (2 * a)
                Console.WriteLine("root 2 =" + Str(x2))
                Console.WriteLine(" ")
                Console.WriteLine("Since the values" + Str(a) + ", " + Str(b) + " and" + Str(c) + " produce root 1 and root 2 with different answers, the quadratic equation has two solutions.")
                Console.WriteLine("Therefore, the roots are real and different.")

            End If

        Else
            Console.WriteLine("Roots are complex.")
            Console.WriteLine(" ")
            Console.WriteLine("Roots x1 and x2 are: ")
            'Console.WriteLine((-b / (2 * a)) + "+" + (Math.Sqrt(det * -1)) / ((2 * a)) + "i")
            Console.WriteLine((Str(-b) / Str(2 * a)) + "+" + (Str(Math.Sqrt(det * -1)) / Str(2 * a)) + "i")
            Console.WriteLine(" ")
            'Console.WriteLine((-b / (2 * a)) + "-" + (Math.Sqrt(det * -1)) / ((2 * a)) + "i")
            Console.WriteLine((Str(-b) / Str(2 * a)) + "-" + (Str(Math.Sqrt(det * -1)) / Str(2 * a)) + "i")


        End If

        Console.WriteLine("Press any key to return to the main menu")
        Console.ReadLine()
        Call Main()

    End Sub

    Private Sub Task3()
        Dim MCI As Double

        MCI = MonteCarlo()

        Console.WriteLine(" ")
        Console.WriteLine("Press any key to return to the main menu")
        Console.ReadLine()
        Call Main()

    End Sub

    Function MonteCarlo()

        Dim a As Double
        Dim b As Double
        Dim x As Double
        Dim func As Double
        Dim total As Double
        Dim result As Double
        Dim j As Integer
        Dim N As Integer

        Console.WriteLine("Input a :")
        a = Console.ReadLine()
        Console.WriteLine(" ")
        Console.WriteLine("Input b :")
        b = Console.ReadLine()
        Console.WriteLine(" ")
        Console.WriteLine("Input n :")
        N = Console.ReadLine()
        Console.WriteLine(" ")

        For j = 1 To N
            'Generate a new number between a and b
            x = (b - a) * Rnd()

            'Evaluate function at new number 
            func = (x ^ 2) + (2 * x) + 1

            'Add to previous value 
            total = total + func

        Next j

        result = (total / N) * (b - a)
        Console.WriteLine("The integral is" + Str(result))
        Return result

    End Function


    Private Sub Task4()

        Dim check As Integer, num As Integer, StartTime As Double, EndTime As Double
        check = 1
        Console.WriteLine("Please input a positive integer and press enter: ")
        num = Console.ReadLine()

        StartTime = Timer

        For i = 2 To (num - 1)
            If num Mod i = 0 Then
                check = 0
                Exit For
            End If
        Next
        If check = 0 Then
            Console.WriteLine(" ")
            Console.WriteLine(Str(num) + “ is not a prime number.”)
        Else
            Console.WriteLine(" ")
            Console.WriteLine(Str(num) + “ is a prime number.”)
        End If

        EndTime = Timer
        Console.WriteLine(" ")
        Console.WriteLine("Calculated in" + Str(EndTime - StartTime) + " seconds.")

        Console.WriteLine("Press any key to return to the main menu")
        Console.ReadLine()
        Call Main()

    End Sub

    Private Sub Task5()

        Dim selectionhelp As Integer

        Do Until selectionhelp < 5 And selectionhelp > 0
            Console.WriteLine("Please select one of the options from 1 - 4 below to get help on the topic:")
            selectionhelp = Console.ReadLine()
            Console.WriteLine(" ")
            Console.Clear()
            Console.WriteLine("Invalid input! Please select one of the options below and try again.")
            Console.WriteLine(" ")
        Loop

        Select Case selectionhelp
            Case 1
                Console.Clear()
                Console.WriteLine("Accuracy Option Help")
                Console.WriteLine(" ")
                Console.WriteLine("In this option, you input the number of decimal places from 1 to 5 and then press enter.
The number you have inputted will be set as the number of decimal places for the rest of the program in the other subroutines.")
                Console.WriteLine(" ")
            Case 2
                Console.Clear()
                Console.WriteLine("Quadratic Equation Help")
                Console.WriteLine(" ")
                Console.WriteLine("In this option, you input the values of a, b, c (the value a must not be 0). Based of these values you have given, the program will then use these values to calculate the discriminant first (under the name 'det').
This value calculates how many solutions (also called roots) to the quadratic equation there will be. If it is negative, then there will be no solutions to the quadratic equation (at this point, the solutions, which are 'x1' and 'x2', aren't calculated).
If this value is equal to 0 exactly, then there is only one solution to the quadratic equation.
If this value is positive, then there are 2 solutions to the quadratic equation. After this, the solutions are calculated in 'x1' and 'x2', depending on the value of the discriminant. When the discriminant = 0, the solutions 'x1' and 'x2' are the same, hence why the quadratic
equation has only one solution. However, when the discriminant equals a positive number, you get the two individual solutions of 'x1' and 'x2', suggesting that the quadratic equation has 2 solutions.")
                Console.WriteLine(" ")
            Case 3
                Console.Clear()
                Console.WriteLine("Monte-Carlo Integration Help")
                Console.WriteLine(" ")
                Console.WriteLine("In this option, all you do is input the values of a, b and N, then the integral result will be given.")
                Console.WriteLine(" ")
            Case 4
                Console.Clear()
                Console.WriteLine("Prime Decision Help")
                Console.WriteLine(" ")
                Console.WriteLine("In this option, you input an integer into 'num' and then this value will be divided by the value of i in the range of i = 2 To (num - 1) in the equation num Mod i.
If the equation gives a remainder of 0, then the integer you have inputted into 'num' is not a prime number. However, if a remainder is produced, then the integer inputted into 'num' is a prime number.")
                Console.WriteLine(" ")
        End Select

        Console.WriteLine("Press any key to return to the main menu")
        Console.ReadLine()
        Call Main()

    End Sub

End Module
