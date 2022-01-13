Imports System.Math
Imports System.Text
Module Module1

    Sub Main()
        Dim x As Double, y As Double, z As Double
        Dim a As String, b As String, c As String
        Dim length As Integer, i As Integer

        x = 123.456
        y = 17 / 3
        z = Sqrt(2)
        a = "Hello"
        b = "World"

        c = ""
        length = Len(a)
        For i = length To 1 Step -1
            c = c + Mid(a, i, 1)
        Next
        c = c + " " + b

        Console.WriteLine(c)

        Console.WriteLine(" ")

        Console.WriteLine(Replace(c, "ll", "ppp"))

        Console.WriteLine(" ")




    End Sub

End Module
