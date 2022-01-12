Module Module1

    Sub Main()
        Dim x As Long

        For x = 1 To 100
            If (x Mod 7 = 0 Or x Mod 9 = 0 And x Mod 5 = 0) Then
                Console.WriteLine(x)
            End If
        Next

    End Sub

End Module
