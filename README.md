# latex-flashcards
This python script takes takes in a set of flashcards and creates a ``.tex`` file which you can compile, print double-sided (flip on long edge) and cut out. You need to have Python and a TeX compiler installed to use it. Instructions below.

Example of code generated from ``sample_set.txt``:
![image](https://github.com/user-attachments/assets/4fa5d00a-d820-4342-8b19-578e9a1d3252)

Screenshots of the corresponding output:
 - First 4 cards on question page:
![image](https://github.com/user-attachments/assets/09d6e99e-0425-46ee-8660-9e3cd861a77e)
 - First 4 cards on answer page:
![image](https://github.com/user-attachments/assets/59fc7889-4a1d-44fb-b4f0-a693d2d78e38)



### Instructions

See ``sample_set.txt`` for what an input file should look like. Download or clone this repository.

###### Windows
Run ``latex-flashcards.bat`` and follow the instructions. (``python`` must be a valid command in the command line. If it is not, add your Python installation to PATH.)

###### Other/manually
Open the command line or terminal in the same directory as the file ``latex-flashcards.py`` and run the following command (``python`` must be a valid command):
```
python latex-flashcards.py sample_set.txt
```
replacing ``sample_set.txt`` with the path/filename of your set of flashcards. (If you use only the filename, make sure the file is in the same directory as ``latex-flashcards.py``.)

The script will create a folder called "output" containing the ``.tex`` file.

There will be 8 flashcards per A4 page, so make sure the contents of the flashcards are small enough to fit. The script supports newlines (using \n in the source file, see ``sample_set.txt``) and line wrapping.

### Tips
 - To use $\LaTeX$ packages, edit the variable ``head_text`` in ``latex-flashcards.py``
