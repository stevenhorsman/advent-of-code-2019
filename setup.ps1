[string]$template_day="03"
[string]$template_name="crossed_wires"
[string]$day=$args[0]
$day=$day.PadLeft(2,'0')
[string]$name=$args[1]
Write-Host "Creating day $day with name $name"
Copy-Item -Path .\day-$template_day\ -Destination day-$day -recurse -Force
Remove-Item -Path .\day-$day\__pycache__ -recurse
Clear-Content .\day-$day\input.txt
Rename-Item -Path .\day-$day\$template_name.py -NewName "$name.py"
Rename-Item -Path .\day-$day\test_$template_name.py -NewName test_$name.py
(Get-Content .\day-$day\$name.py).replace($template_day, $day) | Set-Content .\day-$day\$name.py
(Get-Content .\day-$day\test_$name.py).replace($template_name, $name) | Set-Content .\day-$day\test_$name.py