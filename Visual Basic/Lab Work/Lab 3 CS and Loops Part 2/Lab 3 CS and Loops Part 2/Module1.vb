Module Module1

    Sub Main()
        Dim a, b, c As Long

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
