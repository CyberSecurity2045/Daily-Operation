Get-WmiObject -Class Win32_Processor | Select-Object -Property [a-z]* | select Name, ThreadCount
Get-WmiObject Win32_BaseBoard
Get-WmiObject Win32_PhysicalMemory | Select ConfiguredClockSpeed, Manufacturer,PartNumber
Get-Disk
(Get-WmiObject Win32_VideoController).Name
