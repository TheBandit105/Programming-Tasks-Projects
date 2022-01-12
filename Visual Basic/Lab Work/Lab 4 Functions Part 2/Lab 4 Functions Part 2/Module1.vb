Module Module1

    Sub Main()
        Dim v1 As Double, v2 As Double, p1 As Double, loc1 As Double

        v1 = 6.3
        v2 = 0
        Console.WriteLine("Before v1 =" + Str$(v1))
        Console.WriteLine("Before v2 =" + Str$(v2))
        v2 = TestLocal(v1)
        Console.WriteLine("After v1 =" + Str$(v1))
        Console.WriteLine("After v2 =" + Str$(v2))

    End Sub
    Function TestLocal(ByVal p1 As Double) As Double
        Dim loc1 As Double

        loc1 = p1 + 100
        p1 = 5678
        Console.WriteLine("Within p1 =" + Str$(p1))
        Console.WriteLine("Within loc1 =" + Str$(loc1))
        TestLocal = loc1
    End Function



End Module
