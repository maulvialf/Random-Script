@echo off
set original_dir="%CD%"
cd "C:\utils\hashcat\"
hashcat.exe %*
cd "%original_dir%"