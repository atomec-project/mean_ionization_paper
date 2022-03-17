import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
import matplotlib.font_manager
import matplotlib as mpl


def fig_initialize(
    latex=False,
    setsize=False,
    size="preprint",
    fraction=1,
    subplots=(1, 1),
    plotstyle=1,
):

    mpl.rcParams["lines.marker"] = ""
    mpl.rcParams["lines.markersize"] = 1.2

    if latex:
        # Set up tex rendering
        plt.rc("text", usetex=True)
        plt.rc(
            "text.latex", preamble=r"\usepackage{amsmath, amsthm, amssymb, amsfonts}"
        )
        mpl.rcParams["font.family"] = "serif"
        mpl.rcParams["font.serif"] = "STIX"
        mpl.rcParams["mathtext.fontset"] = "stix"
    if setsize:
        if size == "reprint":
            mpl.rcParams["font.size"] = 10
            mpl.rcParams["axes.linewidth"] = 0.5
            mpl.rcParams["xtick.major.width"] = 0.5
            mpl.rcParams["ytick.major.width"] = 0.5
            mpl.rcParams["lines.linewidth"] = 1
            mpl.rcParams["axes.labelsize"] = 10
            mpl.rcParams["xtick.labelsize"] = 8
            mpl.rcParams["ytick.labelsize"] = 8
            plt.rc("legend", **{"fontsize": 8})
            plt.rc("legend", **{"frameon": False})
            mpl.rcParams["legend.labelspacing"] = 0.25
        elif size == "preprint":
            mpl.rcParams["font.size"] = 10
            mpl.rcParams["axes.linewidth"] = 0.5
            mpl.rcParams["xtick.major.width"] = 0.5
            mpl.rcParams["ytick.major.width"] = 0.5
            mpl.rcParams["lines.linewidth"] = 0.75
            mpl.rcParams["axes.labelsize"] = 10
            mpl.rcParams["xtick.labelsize"] = 8
            mpl.rcParams["ytick.labelsize"] = 8
            plt.rc("legend", **{"fontsize": 8})
            plt.rc("legend", **{"frameon": False})
            mpl.rcParams["legend.labelspacing"] = 0.7
        elif size == "beamer":
            mpl.rcParams["font.size"] = 10
            mpl.rcParams["lines.linewidth"] = 0.75
            mpl.rcParams["axes.labelsize"] = 10
            mpl.rcParams["xtick.labelsize"] = 8
            mpl.rcParams["ytick.labelsize"] = 8
            mpl.rcParams["legend.labelspacing"] = 0.25
            plt.rc("legend", **{"fontsize": 8})
            plt.rc("legend", **{"frameon": False})

    # Define a custom cycler
    if plotstyle == 1:
        custom_cycler = (
            cycler(color=["orange", "steelblue", "violet", "midnightblue", "maroon"])
            + cycler(linestyle=["-", "--", ":", "-.", "-"])
            + cycler(lw=[1.0, 1.1, 1.5, 1.2, 1.0])
            + cycler(alpha=[1.0, 1.0, 1.0, 1.0, 1.0])  # cycler(lw=[1,0.8,1.33,1,1]) + \
            + cycler(
                markerfacecolor=[
                    "orange",
                    "steelblue",
                    "violet",
                    "midnightblue",
                    "maroon",
                ]
            )
        )

    elif plotstyle == 2:
        custom_cycler = (
            cycler(color=["red", "steelblue", "orange", "midnightblue", "maroon"])
            + cycler(linestyle=["-", "-.", ":", "--", "-"])
            + cycler(lw=[1.0, 1.2, 1.3, 1.1, 1.0])
            + cycler(alpha=[1.0, 1.0, 1.0, 1.0, 1.0])  # cycler(lw=[1,0.8,1.33,1,1]) + \
            + cycler(
                markerfacecolor=[
                    "orange",
                    "steelblue",
                    "violet",
                    "midnightblue",
                    "maroon",
                ]
            )
        )

    plt.rc("axes", prop_cycle=custom_cycler)

    # determine fig height and width
    if size == "reprint":
        width_pt = 243
    elif size == "preprint":
        width_pt = 468.0
    elif size == "Hirschegg":
        width_pt = 650
    elif size == "beamer":
        width_pt = 307.0

    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction
    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    golden_ratio = (5 ** 0.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    figdims = (fig_width_in, fig_height_in)

    return figdims


def add_subplot_axes(ax, rect, axisbg="w"):
    fig = plt.gcf()
    box = ax.get_position()
    width = box.width
    height = box.height
    inax_position = ax.transAxes.transform(rect[0:2])
    transFigure = fig.transFigure.inverted()
    infig_position = transFigure.transform(inax_position)
    x = infig_position[0]
    y = infig_position[1]
    width *= rect[2]
    height *= rect[3]  # <= Typo was here
    subax = fig.add_axes([x, y, width, height], facecolor=axisbg)
    # x_labelsize = subax.get_xticklabels()[0].get_size()
    # y_labelsize = subax.get_yticklabels()[0].get_size()
    # x_labelsize *= rect[2]**0.5
    # y_labelsize *= rect[3]**0.5
    # subax.xaxis.set_tick_params(labelsize=x_labelsize)
    # subax.yaxis.set_tick_params(labelsize=y_labelsize)
    return subax


def plot_DOS(densities, chem_pots):

    figdims = fig_initialize(latex=True, setsize=True, fraction=0.8)

    # General figure set-up
    fig, ax = plt.subplots(1, 1, figsize=(figdims))

    zeros1 = np.zeros((len(chem_pots), 2))
    zeros2 = np.zeros_like(zeros1)

    cols = [
        "k",
        "purple",
        "blue",
        "cyan",
        "darkgreen",
        "lightgreen",
        "yellow",
        "orange",
        "r",
    ]

    for i, density in enumerate(densities):
        occ_data = np.loadtxt(
            "/home/callow46/mean_ionization_paper/results/Carbon/bands/dos_"
            + str(density)
            + ".csv",
            unpack=True,
            skiprows=1,
        )

        eigs = 27.2114 * (occ_data[0] - chem_pots[i])
        dos = occ_data[2]

        dos_new = dos[1:][np.where(eigs <= 300)]
        eigs_new = eigs[1:][np.where(eigs <= 300)]

        zero_locs = eigs_new[np.where(dos_new == 0)]
        zeros1[i, 0] = zero_locs[0]
        zeros2[i, 0] = zero_locs[1]

        dos_max = np.amax(dos_new[np.where(eigs_new > chem_pots[i])])

        dos_new = dos_new / dos_max
        dos_new = np.where(dos_new < 1, dos_new, 1)
        dos_new = (dos_new + (1.5 * i)) / 27.2114
        baseline = np.zeros_like((dos_new)) + (1.5 * i) / 27.2114
        zeros1[i, 1] = (1.5 * i) / 27.2114
        zeros2[i, 1] = (1.5 * i) / 27.2114

        ax.plot(eigs_new, dos_new, color="gray", ls="-")
        label = str(density) + r" $\textrm{g cm}^{-3}$"

        ax.fill_between(
            eigs_new, dos_new, baseline, alpha=0.5, color=cols[i], label=label
        )

        # plt.plot(eigs_new, baseline / 27.2114)
    # plt.plot(eigs, dos_new / 27.2114)

    ax.plot(zeros1[:, 0], zeros1[:, 1], ls="--", color="gray")
    ax.plot(zeros2[:, 0], zeros2[:, 1], ls="--", color="gray")

    ax.set_ylim(0, 0.5)
    xticks = [-900, -750, -600, -450, -300, -150, 0, 150, 300]

    xticklabs = [-900, "", -600, "", -300, "", 0, "", 300]
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabs)
    ax.set_xlim(-1100, 300)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], loc="lower left")

    ax.set_ylabel(r"DOS (arbitrary units)")
    ax.set_xlabel(r"$\epsilon - \mu\ (\textrm{eV})$")

    plt.savefig(
        "/home/callow46/mean_ionization_paper/figures/Carbon_DOS_comp.pdf",
        bbox_inches="tight",
    )

    # plt.show()
