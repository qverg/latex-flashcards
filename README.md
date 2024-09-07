# latex-flashcards
This python script takes takes in a set of flashcards and creates a ``.tex`` file which you can compile, print double-sided (flip on long edge) and cut out.

See ``sample_set.txt`` for how an input file should look. Then run
```
python latex-flashcards.py sample_set.txt
```
replacing ``sample_set.txt`` with the filename of your set of flashcards.

The script will create a folder called "output" containing the ``.tex`` file.