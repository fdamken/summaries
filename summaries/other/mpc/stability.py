import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.constants


def stable(x):
    return np.exp(-x)

def unstable(x):
    return np.exp(x)

def marginally_stable(x):
    return np.ones_like(x)


def not_ringing(x):
    return np.ones_like(x)

def ringing(x):
    return np.sin(10 * x)


def main():
    x = np.arange(0, 5, 0.01)
    figwidth = 7.088
    fig, axss = plt.subplots(nrows=2, ncols=3, figsize=(figwidth, figwidth * 1 / sp.constants.golden))
    for title_suffix, ring, axs in zip(["", ", Ringing"], [not_ringing, ringing], axss):
        for col, (title, stability, ax) in enumerate(zip(["Stable", "Unstable", "Marginally Stable"], [stable, unstable, marginally_stable], axs)):
            ax.plot(x, stability(x) * ring(x))
            ax.axhline(0, color="black", alpha=0.5)
            ax.set_xticks([])
            if col == 0:
                ax.set_yticks([0])
            else:
                ax.set_yticks([])
            ax.set_title(title + title_suffix)
            ylim = np.max(np.abs(ax.get_ylim()))
            ax.set_ylim((-ylim, ylim))
    plt.tight_layout()
    fig.savefig("tmp-stability.pgf")


if __name__ == "__main__":
    main()
