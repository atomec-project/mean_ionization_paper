import os

nb_name = "supp_info.ipynb"

os.system("jupyter-nbconvert supp_info.ipynb --to latex")

with open("supp_info.tex", "r") as f:

    lines = f.readlines()

with open("supp_info_for_paper.tex", "w") as f:

    for i, line in enumerate(lines):
        if i == 0:
            linenew = "\\documentclass[9pt]{article}" + "\n"
            f.write(linenew)
            print(line)
        elif i == 157:
            linenew = "\\title{Supplementary Information}" + "\n"
            print(line)
            f.write(linenew)
        elif i == 317:
            linenew = "\\renewcommand{\\Verbatim}[1][1]{\\small %}" + "\n"
            print(line)
            f.write(line)
        elif "Add a bibliography block to the postdoc" in line:
            linenew = "\\bibliography{main}"
            f.write(linenew)
        else:
            f.write(line)
