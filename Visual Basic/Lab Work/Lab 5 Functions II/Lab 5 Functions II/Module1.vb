Module Module1

    Sub Main()
        task521()
        task522()
        task523()
        task524()
        task525()

    End Sub

    Sub task521()
        Dim x As Integer, ftl As Integer

        x = 13

        ftl = Factorial(x)

        Console.WriteLine("The factorial of" + Str(x) + " is" + Str(Factorial(x)))

    End Sub

    Function Factorial(ByVal y As Byte) As Long
        Dim I As Long
        If y <= 0 Then
            Exit Function
        Else
            Factorial = 1
            For I = 1 To y
                Factorial = Factorial * I
            Next I
        End If

        Return I

    End Function


    Sub task522()

    End Sub

    Sub task523()

    End Sub

    Sub task524()

    End Sub

    Sub task525()

    End Sub
End Module
