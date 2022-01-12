Module Module1

    Sub Main()
        Dim x As Long

        x = 5

        Select Case x
            Case 1 To 9
                Console.WriteLine("Less than 10")
            Case 90 To 100
                Console.WriteLine("Greater than or equal than 90")
            Case 30 To 40
                Console.WriteLine("Between 30 and 40 inclusive")
            Case 11
                Console.WriteLine("Equal to 11")
            Case 21
                Console.WriteLine("Equal to 21")
            Case 51
                Console.WriteLine("Equal to 51")
            Case 61
                Console.WriteLine("Equal to 61")
            Case x < 70 And x > 80
                Console.WriteLine("Between 70 and 80 exclusive")

        End Select

    End Sub

End Module
