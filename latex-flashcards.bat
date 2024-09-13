@echo off
set /p userInput=Enter the filename of the flashcard set (including file extension): 

python latex-flashcards.py %userInput%

echo If there were no errors, you will find the .tex file in the 'output' folder
pause
