Imports System.Math
Module Module1

    Sub Main()
        Dim i As Long, eo As Boolean, s As String
        For i = 1 To 25
            eo = EvenOdd(i)
            If eo = True Then
                s = "Even"
            Else
                s = "Odd"
            End If
            Console.WriteLine(Str(i) + "is" + s)
        Next i
    End Sub

    Function EvenOdd(ByVal x As Long) As Boolean
        If (x Mod 2 = 0) Then
            EvenOdd = True
            Exit Function
        End If

        EvenOdd = False

    End Function

End Module

