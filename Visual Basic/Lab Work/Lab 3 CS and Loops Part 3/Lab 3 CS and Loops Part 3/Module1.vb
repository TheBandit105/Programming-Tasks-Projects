Module Module1

    Sub Main()
        Dim d As String
        Dim e As String
        Dim f As String

        d = "Thomas"
        e = "Suhayb"
        f = "Sumit"

        If (d < e) Then
            If (e < f) Then
                Console.WriteLine(d & " " & e & " " & f)
            ElseIf (d < f) Then
                Console.WriteLine(d & " " & f & " " & e)
            Else
                Console.WriteLine(f & " " & d & " " & e)
            End If
        ElseIf (e > f) Then
            Console.WriteLine(f & " " & e & " " & d)
        ElseIf (d > f) Then
            Console.WriteLine(e & " " & f & " " & d)
        Else
            Console.WriteLine(e & " " & d & " " & f)
        End If

    End Sub

End Module
