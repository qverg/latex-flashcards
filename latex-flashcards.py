import sys

questions = []
answers = []

#with open(sys.argv[1], "r") as f:
with open("sample_set.txt", "r") as f:
    lines = f.readlines()

print(lines)    # debug

for i, line in enumerate(lines):
    if line[:2] == "Q " and i < len(lines) - 1:
        if lines[i+1][:2] == "A ":
            questions.append(line[2:].strip())
            answers.append(lines[i+1][2:].strip())

print(*zip(questions, answers))  # debug
assert(len(questions) == len(answers))


# Thanks to https://tex.stackexchange.com/questions/73954/how-to-split-a-page-in-six-equally-sized-sectors
#name = sys.argv[1].split(".")[0]
name = "sample_set"

head_text = r"""\documentclass{article}
\usepackage[margin=.2cm,centering,portrait]{geometry}

\newcommand\Block[1]{%
\begin{minipage}[c][\dimexpr.25\textheight-2pt\relax][c]{\dimexpr0.5\textwidth-3pt\relax}
\centering
#1
\end{minipage}%
}

\begin{document}
\thispagestyle{empty}
"""

if len(questions) % 2 != 0:
    questions.append("")
    answers.append("")

with open(name+".tex", "w+") as f:
    f.write(head_text)

    q_counter = 0
    a_counter = 0
    counting = "Q"  # toggle between "Q" and "A"
    while a_counter <= len(answers)-1:
        if counting == "Q":
            if (q_counter % 8 == 0 and a_counter < q_counter) or q_counter == len(questions):
                counting = "A"
                f.write("\\newpage\n")
            else:
                if q_counter % 2 == 0:
                    f.write("\\noindent")
                f.write(rf"\Block{{{questions[q_counter]}}}")
                if q_counter % 2 == 0:
                    f.write(r"\hfill%")
                f.write("\n")
                q_counter += 1
            
        elif counting == "A":
            print(q_counter, a_counter)
            if a_counter == q_counter:
                counting = "Q"
                f.write("\\newpage\n")
            else:

                if a_counter % 2 == 0:
                    f.write("\\noindent")
                    offset = 1
                else:
                    offset = -1
                f.write(rf"\Block{{{answers[a_counter+offset]}}}")
                if a_counter % 2 == 0:
                    f.write(r"\hfill%")
                f.write("\n")
                a_counter += 1

    f.write("\n\\end{document}")