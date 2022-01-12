Imports System.Math
Module Module1

    Sub Main()
        taskReverseString()
        taskLeapYear()
        taskDaysinaMonth()
        taskDaysAlive()
        taskTheFibonacciSequence()
    End Sub

    Sub taskReverseString()
        Console.WriteLine("Reversing 'Thomas': " & StrReverse("Thomas"))
        Console.WriteLine(" ")
        Console.WriteLine("Reversing 'Reading': " & StrReverse("Reading"))
        Console.WriteLine(" ")
    End Sub

    Sub taskLeapYear()
        Dim y As Long, ly As Boolean, r As String
        For y = 1990 To 2030
            ly = Leapyear(y)
            If ly = True Then
                r = "leap year"
            Else
                r = "not a leap year"
            End If
            Console.WriteLine(Str(y) + " is " + r)

        Next y

        Console.WriteLine(" ")
    End Sub
    Function Leapyear(ByVal year As Integer) As Boolean
        If Not (year Mod 4 = 0) Then
            Leapyear = False
            Exit Function
        ElseIf (year Mod 100 = 0) And (Not year Mod 400 = 0) Then
            Leapyear = False
            Exit Function

        End If
        Leapyear = True

    End Function
    Sub taskDaysinaMonth()
        Dim m As Integer, y As Integer, number_of_days_in_month As Integer

        m = 3
        y = 2008
        number_of_days_in_month = Month(m, y)

        If m = m And y = y Then
            Console.WriteLine("In month" + Str(m) + " of" + Str(y) + ", there are" + Str(Month(m, y)) + " days")
            Console.WriteLine(" ")
        End If
    End Sub
    Function Month(ByVal m As Integer, ByVal year As Integer) As Integer

        Select Case m
            Case 1
                Return 31
            Case 2
                If (Leapyear(year)) Then
                    Return 29
                Else
                    Return 28
                End If
            Case 3
                Return 31
            Case 4
                Return 30
            Case 5
                Return 31
            Case 6
                Return 30
            Case 7
                Return 31
            Case 8
                Return 31
            Case 9
                Return 30
            Case 10
                Return 31
            Case 11
                Return 30
            Case 12
                Return 31

        End Select

        Return 0
    End Function
    Sub taskDaysAlive()



        Dim myDouble As Double = Nothing
        Dim d As Date, dob As DateTime = DateTime.FromOADate(myDouble), number_of_days_alive_since_date_of_birth As Integer, d0 As Date = Now

        number_of_days_alive_since_date_of_birth = DaysAlive(d)




    End Sub

    Function DaysAlive(ByVal d As Date) As Long
        Dim d0 As Date = Now
        Return DateDiff(DateInterval.Day, d, d0)
    End Function

    Sub taskTheFibonacciSequence()
        Dim a As Integer, s As Integer

        a = -5
        s = Fibonacci(a)

        If a < 0 Then
            Console.WriteLine(" ")
            Console.WriteLine("Invalid input - the number chosen must be a positive integer.")
        End If

    End Sub
    Function Fibonacci(ByVal n As Integer) As Integer
        If (n < 0) Then
            Console.WriteLine("Negative number")
            Return -1
        End If

        Dim i As Integer, fn_2 As Integer, fn_1 As Integer, fn As Integer
        For i = 0 To n
            Select Case i
                Case 0
                    Console.WriteLine(0)
                Case 1
                    Console.WriteLine(1)
                Case 2
                    Console.WriteLine(1)
                    fn_1 = 1
                    fn_2 = 1
                Case Else
                    fn = fn_1 + fn_2
                    fn_2 = fn_1
                    fn_1 = fn
                    Console.WriteLine(fn)

            End Select
        Next i
        Return fn
    End Function


End Module
