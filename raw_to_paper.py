import os

nb_name = "supp_info.ipynb"

os.system("jupyter-nbconvert supp_info.ipynb --to latex")

author_list = ", ".join(["Timothy J. Callow", "Eli Kraisler", "Attila Cangi"])
title = "Accurate and efficient computation of mean ionization states with an average-atom Kubo--Greenwood approach: Supplementary Material"

with open("supp_info.tex", "r") as f:

    lines = f.readlines()

with open("supp_info_for_paper.tex", "w") as f:

    for i, line in enumerate(lines):
        if i == 0:
            linenew = "\\documentclass[9pt]{article}" + "\n"
            f.write(linenew)
            print(line)
        elif i == 157:
            linenew = "\\title{" + title + "} \n"
            print(line)
            f.write(linenew)
            linenew = "\\author{" + author_list + "}\n"
            f.write(linenew)
        elif i == 317:
            linenew = "\\renewcommand{\\Verbatim}[1][1]{\\small %}" + "\n"
            print(line)
            f.write(line)
        elif "Add a bibliography block to the postdoc" in line:
            linenew = "\\bibliography{main}"
            f.write(linenew)
        elif "supp_info_9_0.png" in line:
            linenew = " \n".join(
                [
                    "\\begin{figure}",
                    "\\centering",
                    "\\includegraphics{figures/density_example.pdf}",
                    "\\label{Al:dens_example}",
                    "\\caption{Radial density distribution $r^2 n(r)$ for Aluminium at \
                    its solid density $\\rho_\\textrm{m}=2.7\\ \\textrm{g cm}^{-3}$ and \
                    temperature $T = 0.01\\ \\textrm{eV}$, for the Dirichlet \
                    boundary condition.}",
                    "\\end{figure}",
                ]
            )
            f.write(linenew)
            print(linenew)

        elif "supp_info_25_0.png" in line:
            linenew = " \n".join(
                [
                    "\\begin{figure}",
                    "\\centering",
                    "\\includegraphics{figures/Carbon_DOS_comp.pdf}",
                    "\\label{C:dos_example}",
                    "\\caption{Density-of-states for Carbon at a range of densities \
                    and temperature $T = 100\ \\textrm{eV}$, calculated with the AA \
                    band-structure model.}",
                    "\\end{figure}",
                ]
            )
            f.write(linenew)
            print(linenew)

        elif "supp_info_32_0.png" in line:
            linenew = " \n".join(
                [
                    "\\begin{figure}",
                    "\\centering",
                    "\\includegraphics{figures/ELF_example.pdf}",
                    "\\label{Al:ELF_example}",
                    "\\caption{Electron localization function $\\textrm{ELF}(r)$ for Aluminium at \
                    its solid density $\\rho_\\textrm{m}=2.7\\ \\textrm{g cm}^{-3}$ and \
                    temperature $T = 0.01\\ \\textrm{eV}$, for the Dirichlet \
                    boundary condition.}",
                    "\\end{figure}",
                ]
            )
            f.write(linenew)
            print(linenew)

        elif "\\usepackage{graphicx}" in line:
            f.write(line)
            linenew = (
                "\\usepackage[square,numbers]{natbib} \n"
                + "\\bibliographystyle{unsrtnat} \n"
            )
            f.write(linenew)

        elif "newcommand{\\WarningTok}" in line:
            f.write(line)
            linenew = "\\newcommand{\\onlinecite}[1]{\\hspace{-1 ex} \\nocite{#1}\\citenum{#1}}"
            f.write(linenew)
        elif "\\DeclareCaptionFormat{nocaption}{}" in line:
            continue
        elif "\\captionsetup{format=nocaption,aboveskip=0pt,belowskip=0pt}" in line:
            continue

        else:
            f.write(line)
