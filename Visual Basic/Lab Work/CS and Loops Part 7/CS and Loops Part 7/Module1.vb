Module Module1

    Sub Main()
        Dim a, b, c As Integer

        a = 68
        b = 172
        Console.WriteLine("The Highest Common Factor between" + Str(a) + " and" + Str(b) + " is:")

        c = a Mod b
        Do While c > 0
            a = b
            b = c
            c = a Mod b
        Loop

        Console.WriteLine(b)
        Console.WriteLine("")

    End Sub

End Module
