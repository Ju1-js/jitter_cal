setlocal enabledelayedexpansion
for /F %%i in (ip.txt) do (
    for /l %%x in (1, 1, 100) do (
    timeout 1
    ping -n 1 %%i | FINDSTR /I reply >> C:\Users\James\Desktop\jitter_cal\output\tmp\%%i-tmp.txt
    )
        for /f "tokens=5" %%a in (C:\Users\James\Desktop\jitter_cal\output\tmp\%%i-tmp.txt) do (
        set str=%%a
        set str=!str:ms=!
        set str=!str:time=!
        set str !str:~1!
        echo !str! >> C:\Users\James\Desktop\jitter_cal\output\out\%%i-out.txt
    )
del C:\Users\James\Desktop\jitter_cal\output\tmp\%%i-tmp.txt
)
