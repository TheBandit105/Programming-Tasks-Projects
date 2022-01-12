Module Module1

    Sub Main()
        Dim i As Long, j As Long

        For i = 1 To 7 Step 2
            For j = 1 To i Step 2
                Console.Write(i)
            Next j
        Next i

    End Sub

End Module
