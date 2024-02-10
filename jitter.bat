setlocal enabledelayedexpansion
for /F %%i in (ip.txt) do (
    for /l %%x in (1, 1, 100) do (
    timeout 1
    ping -n 1 %%i | FINDSTR /I reply >> .\output\tmp\%%i-tmp.txt
    )
        for /f "tokens=5" %%a in (.\output\tmp\%%i-tmp.txt) do (
        set str=%%a
        set str=!str:ms=!
        set str=!str:time=!
        set str !str:~1!
        echo !str! >> .\output\out\%%i-out.txt
    )
del .\output\tmp\%%i-tmp.txt
)
