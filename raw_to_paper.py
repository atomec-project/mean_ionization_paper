import os

nb_name = "supp_info.ipynb"

os.system("jupyter-nbconvert supp_info.ipynb --to latex")

with open("supp_info.tex", "r") as f:

    lines = f.readlines()

with open("supp_info_for_paper.tex", "w") as f:

    for i, line in enumerate(lines):
        if i == 0:
            linenew = "\\documentclass[preprint,aps]{revtex4-2}" + "\n"
            f.write(linenew)
            print(line)
        elif i == 157:
            linenew = "\\title{Supplementary Information} \n"
            print(line)
            f.write(linenew)
        elif i == 317:
            linenew = "\\renewcommand{\\Verbatim}[1][1]{\\small %}" + "\n"
            print(line)
            f.write(line)
        elif "Add a bibliography block to the postdoc" in line:
            linenew = "\\bibliographystyle{unsrt} \n \\bibliography{main}"
            f.write(linenew)
        elif "supp_info_9_0.png" in line:
            linenew = " \n".join(
                [
                    "\\begin{figure}",
                    "\\includegraphics{figures/density_example.pdf}",
                    "\\label{Al:dens_example}",
                    "\\caption{Radial density distribution for Aluminium}",
                    "\\end{figure}",
                ]
            )
            f.write(linenew)
            print(linenew)

        elif "supp_info_25_0.png" in line:
            linenew = " \n".join(
                [
                    "\\begin{figure}",
                    "\\includegraphics{figures/Carbon_DOS_comp.pdf}",
                    "\\label{C:dos_example}",
                    "\\caption{Radial density distribution for Aluminium}",
                    "\\end{figure}",
                ]
            )
            f.write(linenew)
            print(linenew)

        elif "supp_info_31_0.png" in line:
            linenew = " \n".join(
                [
                    "\\begin{figure}",
                    "\\includegraphics{figures/ELF_example.pdf}",
                    "\\label{Al:ELF_example}",
                    "\\caption{Radial density distribution for Aluminium}",
                    "\\end{figure}",
                ]
            )
            f.write(linenew)
            print(linenew)
        else:
            f.write(line)
