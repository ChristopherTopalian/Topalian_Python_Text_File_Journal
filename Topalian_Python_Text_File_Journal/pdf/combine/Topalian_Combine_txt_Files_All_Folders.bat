:: Topalian_Combine_txt_Files.bat

:: This .bat File Combines All .txt files in all folders of our project folder, into one main.txt file.

:: To activate this .bat file, we double click the .bat file, while it is located in our folder.

@echo off
:: set the output file name
set "output=main.txt"

:: clear existing output file
type nul > "%output%"

:: loop through all txt files in subdirectories
for /r %%i in (*.txt) do (
    :: append content of each file to output file
    type "%%i" >> "%output%"
)

echo "Text files combined into %output% successfully."