Module Module1

    Sub Main()
        Dim x As Long
        Dim y As Long
        Dim z As Double
        Dim a As Boolean
        Dim b As Boolean
        Dim c As Long

        x = 100
        y = 204
        z = -23.1
        a = True
        b = False
        c = -204

        '1
        If x < y Then
            Console.WriteLine("True!")
        Else
            Console.WriteLine("False!")
        End If

        '2
        If x > z And a = b Then
            Console.WriteLine("True!")
        Else
            Console.WriteLine("False!")
        End If

        '3
        If 2 * c > y Then
            Console.WriteLine("True!")
        Else
            Console.WriteLine("False!")
        End If

        '4
        If x = b Then
            Console.WriteLine("True!")
        Else
            Console.WriteLine("False!")
        End If

        '5
        If c <> y Or c = y Then
            Console.WriteLine("True!")
        Else
            Console.WriteLine("False!")
        End If

        '6
        If z <> y And c = a Then
            Console.WriteLine("True!")
        Else
            Console.WriteLine("False!")
        End If

        '7
        If y >= y And a + 3 <> 2 Then
            Console.WriteLine("True!")
        Else
            Console.WriteLine("False!")
        End If

    End Sub

End Module
Module Module2

    Sub Main()
        Dim a As Long
        Dim b As Long
        Dim c As Long

        a = 13
        b = 54
        c = 32

        If (a < b) Then
            If (b < c) Then
                Console.WriteLine(a & " " & b & " " & c)
            ElseIf (a < c) Then
                Console.WriteLine(a & " " & c & " " & b)
            Else
                Console.WriteLine(c & " " & a & " " & b)
            End If
        ElseIf (b > c) Then
            Console.WriteLine(c & " " & b & " " & a)
        ElseIf (a > c) Then
            Console.WriteLine(b & " " & c & " " & a)
        Else
            Console.WriteLine(b & " " & a & " " & c)
        End If




    End Sub
End Module