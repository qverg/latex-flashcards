# latex-flashcards
This python script takes takes in a set of flashcards and creates a ``.tex`` file which you can compile, print double-sided (flip on long edge) and cut out. You need to have Python and a TeX compiler installed to use this.

See ``sample_set.txt`` for how an input file should look. Then run the following command in the command line, open in the same folder as the Python file:
```
python latex-flashcards.py sample_set.txt
```
replacing ``sample_set.txt`` with the filename of your set of flashcards.

The script will create a folder called "output" containing the ``.tex`` file.

There will be 8 flashcards per A4 page, so make sure the contents of the flashcards are small enough to fit.