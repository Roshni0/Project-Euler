﻿Module Module1

    Sub Main()
        Dim sum As Integer = 0
        For x = 1 To 999
            If x Mod 3 = 0 Or x Mod 5 = 0 Then
                sum = sum + x
            End If
        Next
        Console.WriteLine("The sum of all multiples of 3 or 5 below 1000 is: " & sum)
        Console.ReadLine()
    End Sub

End Module
