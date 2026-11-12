# %%
"""Obrázky k případové studii o metodě konečných prvků.

Spuštění:  python obrazky.py   (potřebuje numpy, scipy, matplotlib)
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
from matplotlib.tri import Triangulation

import mkp_2d as m

MODRA, ORANZOVA, SEDA, TMAVA = "#2a78d6", "#d9660b", "#5f6b7a", "#1f2933"
MRIZKA = "#e3e6ea"
plt.rcParams.update({"font.size": 10, "axes.titlesize": 11, "savefig.dpi": 150,
                     "axes.edgecolor": SEDA, "xtick.color": SEDA, "ytick.color": SEDA})


def uprav(ax):
    ax.grid(color=MRIZKA, lw=0.8)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)


def podpory_a_sila(ax, posun=0.0, meritko=1.0):
    """Nakreslí podpory jako trojúhelníky a sílu jako šipku."""
    for x in m.X_PODPORA:
        ax.plot(x, -2.2 * meritko + posun, marker="^", ms=11, color=TMAVA, clip_on=False)
    ax.annotate("", xy=(m.X_SILA, m.VYSKA + posun), xytext=(m.X_SILA, m.VYSKA + 16 * meritko + posun),
                arrowprops=dict(arrowstyle="-|>", color=ORANZOVA, lw=2))
    ax.text(m.X_SILA + 4, m.VYSKA + 9 * meritko + posun, "$F$", color=TMAVA, va="center")


def nosnik_osy(ax, ymin=-8, ymax=38):
    ax.set_aspect("equal")
    ax.set_xlim(-3, m.DELKA + 3)
    ax.set_ylim(ymin, ymax)
    ax.axis("off")


def deformovane(v, zvetseni):
    uzly, u = v["uzly"], v["u"]
    return uzly[:, 0] + zvetseni * u[0::2], uzly[:, 1] + zvetseni * u[1::2]


# %% 1. Přehled postupu
def postup():
    v = m.nosnik(56, 4)
    uzly, prvky = v["uzly"], v["prvky"]
    fig, axs = plt.subplots(3, 1, figsize=(10, 5.4))

    ax = axs[0]
    ax.add_patch(Rectangle((0, 0), m.DELKA, m.VYSKA, fc="#e9d8b8", ec=TMAVA, lw=1.2))
    for y in np.linspace(2.5, 17.5, 7):
        ax.plot([2, m.DELKA - 2], [y, y], color="#c9b086", lw=0.7)
    podpory_a_sila(ax)
    ax.set_title("1. Zadání: tvar, materiál, uchycení, zatížení", loc="left")

    ax = axs[1]
    ax.triplot(uzly[:, 0], uzly[:, 1], prvky, color=MODRA, lw=0.6)
    podpory_a_sila(ax)
    ax.set_title(f"2. Síť: {len(prvky)} trojúhelníkových prvků, {len(uzly)} uzlů, "
                 f"{2 * len(uzly)} neznámých posunutí", loc="left")

    ax = axs[2]
    zv = 8
    X, Y = deformovane(v, zv)
    obr = ax.tripcolor(X, Y, prvky, facecolors=v["s"][:, 0], cmap="RdBu_r", vmin=-45, vmax=45)
    ax.set_title(f"3. Výsledek: posunutí uzlů (zvětšeno {zv}×) a z nich spočítané napětí "
                 r"$\sigma_x$", loc="left")
    cb = fig.colorbar(obr, ax=axs, shrink=0.3, anchor=(0, 0.05), extend="both", pad=0.02)
    cb.set_label(r"$\sigma_x$ [MPa]")
    for ax in axs:
        nosnik_osy(ax, ymin=-22)
    fig.savefig("postup.png", bbox_inches="tight")
    plt.close(fig)


# %% 2. Tvarové funkce
def tvarove_funkce():
    fig = plt.figure(figsize=(10, 4.2))
    ax = fig.add_subplot(1, 2, 1, projection="3d")
    uzly, prvky = m.sit_obdelnik(4, 4, 4, 4)
    stred = m.uzel(uzly, 2, 2)
    z = np.zeros(len(uzly))
    z[stred] = 1
    ax.plot_trisurf(uzly[:, 0], uzly[:, 1], z, triangles=prvky, color=MODRA, alpha=0.55,
                    edgecolor=TMAVA, lw=0.5)
    ax.set_title("Bázová funkce $\\varphi_i$ příslušná uzlu $i$:\n"
                 "1 v uzlu $i$, 0 ve všech ostatních uzlech")
    ax.set(xlabel="$x$", ylabel="$y$", zticks=[0, 1], xticks=[], yticks=[])
    ax.view_init(28, -60)

    ax = fig.add_subplot(1, 2, 2, projection="3d")
    xy = np.array([[0, 0], [3, 0.5], [1, 2.5]])
    hodnoty = np.array([0.5, 1.2, 0.8])
    ax.plot_trisurf(xy[:, 0], xy[:, 1], np.zeros(3), triangles=[[0, 1, 2]], color=MRIZKA,
                    edgecolor=TMAVA, lw=1)
    ax.plot_trisurf(xy[:, 0], xy[:, 1], hodnoty, triangles=[[0, 1, 2]], color=ORANZOVA,
                    alpha=0.6, edgecolor=TMAVA, lw=1)
    for k in range(3):
        ax.plot([xy[k, 0]] * 2, [xy[k, 1]] * 2, [0, hodnoty[k]], color=TMAVA, lw=1.2, ls="--")
        ax.text(xy[k, 0], xy[k, 1], hodnoty[k] + 0.1, f"$u_{k + 1}$", color=TMAVA)
        ax.text(xy[k, 0], xy[k, 1], -0.22, f"{k + 1}", color=SEDA)
    ax.set_title("Posunutí uvnitř prvku: rovina určená\ntřemi hodnotami ve vrcholech")
    ax.set(xlabel="$x$", ylabel="$y$", zticks=[], xticks=[], yticks=[], zlim=(0, 1.4))
    ax.view_init(24, -70)
    fig.savefig("tvarove_funkce.png", bbox_inches="tight")
    plt.close(fig)


# %% 3. Sestavení globální matice
def sestaveni():
    uzly, prvky = m.sit_obdelnik(2, 1, 2, 1)
    vybrany = 2
    fig, axs = plt.subplots(1, 3, figsize=(13, 4.3), gridspec_kw=dict(width_ratios=[1.15, 1, 1]))

    ax = axs[0]
    for k, prvek in enumerate(prvky):
        ax.add_patch(Polygon(uzly[prvek], fc="#f6c9a3" if k == vybrany else "white",
                             ec=TMAVA, lw=1.2))
        t = uzly[prvek].mean(axis=0)
        ax.text(*t, f"prvek {k}", ha="center", va="center", color=TMAVA, fontsize=9)
    for i, (x, y) in enumerate(uzly):
        ax.plot(x, y, "o", ms=17, color=MODRA)
        ax.text(x, y, str(i), color="white", ha="center", va="center", fontweight="bold")
    ax.set_aspect("equal")
    ax.set_xlim(-0.2, 2.2)
    ax.set_ylim(-0.25, 1.25)
    ax.axis("off")
    ax.set_title(f"Síť: 6 uzlů, 4 prvky.\nPrvek {vybrany} má uzly "
                 f"{', '.join(map(str, prvky[vybrany]))}")

    ax = axs[1]
    pocet = np.zeros((12, 12))
    for prvek in prvky:
        sv = m.stupne_volnosti(prvek)
        pocet[np.ix_(sv, sv)] += 1
    ax.imshow(pocet, cmap="Blues", vmin=0, vmax=5)
    for i in range(12):
        for j in range(12):
            if pocet[i, j]:
                ax.text(j, i, int(pocet[i, j]), ha="center", va="center", fontsize=8,
                        color=TMAVA)
    sv = m.stupne_volnosti(prvky[vybrany])
    for i in sv:
        for j in sv:
            ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, ec=ORANZOVA, lw=2))
    popisky = [f"{i}{s}" for i in range(6) for s in "xy"]
    ax.set_xticks(range(12), popisky, fontsize=8)
    ax.set_yticks(range(12), popisky, fontsize=8)
    ax.xaxis.tick_top()
    ax.set_xticks(np.arange(-0.5, 12), minor=True)
    ax.set_yticks(np.arange(-0.5, 12), minor=True)
    ax.grid(which="minor", color=MRIZKA, lw=0.6)
    ax.tick_params(which="both", length=0)
    ax.set_xlabel(f"Matice $K$ (12×12): počet prvků přispívajících\ndo každého místa; "
                  f"oranžově místa prvku {vybrany}")

    ax = axs[2]
    v = m.nosnik(56, 4)
    K = v["K"]
    ax.spy(K, markersize=0.35, color=MODRA)
    ax.tick_params(labelsize=8)
    ax.set_xlabel(f"Nenulové prvky matice $K$ pro síť nosníku\n"
                  f"s {K.shape[0]} neznámými: zaplněno {100 * K.nnz / K.shape[0] ** 2:.1f} %")
    fig.savefig("sestaveni.png", bbox_inches="tight")
    plt.close(fig)


# %% 4. Deformovaný tvar
def deformace(v):
    zv = 10
    fig, ax = plt.subplots(figsize=(10, 2.3))
    uzly, prvky = v["uzly"], v["prvky"]
    ax.triplot(uzly[:, 0], uzly[:, 1], prvky, color="#c5cbd3", lw=0.4)
    X, Y = deformovane(v, zv)
    obr = ax.tripcolor(X, Y, prvky, -v["u"][1::2], cmap="Blues", shading="gouraud", vmin=0)
    ax.triplot(X, Y, prvky, color=TMAVA, lw=0.25, alpha=0.6)
    podpory_a_sila(ax)
    nosnik_osy(ax, ymin=-26, ymax=38)
    cb = fig.colorbar(obr, ax=ax, shrink=0.8, pad=0.02)
    cb.set_label("posunutí dolů [mm]")
    fig.savefig("nosnik_deformace.png", bbox_inches="tight")
    plt.close(fig)


# %% 5. Pole napětí
def pole_napeti(v):
    uzly, prvky, s = v["uzly"], v["prvky"], v["s"]
    nazvy = [r"$\sigma_x$ (podél vláken)", r"$\sigma_y$ (napříč vlákny)", r"$\tau_{xy}$ (smyk)"]
    meze = [45, 6, 3]
    fig, axs = plt.subplots(3, 1, figsize=(10, 5.2))
    for k, ax in enumerate(axs):
        obr = ax.tripcolor(uzly[:, 0], uzly[:, 1], prvky, facecolors=s[:, k], cmap="RdBu_r",
                           vmin=-meze[k], vmax=meze[k])
        podpory_a_sila(ax)
        nosnik_osy(ax)
        ax.set_title(nazvy[k], loc="left")
        cb = fig.colorbar(obr, ax=ax, shrink=0.9, pad=0.02, extend="both")
        cb.set_label("MPa")
    fig.savefig("nosnik_napeti.png", bbox_inches="tight")
    plt.close(fig)


# %% 6. Řez nosníkem
def rez(v, x_rez=80.0):
    uzly, su = v["uzly"], v["s_uzly"]
    v_rezu = np.isclose(uzly[:, 0], x_rez)
    y = uzly[v_rezu, 1]
    yy = np.linspace(0, m.VYSKA, 100)
    I = m.TLOUSTKA * m.VYSKA ** 3 / 12
    posouvajici = m.SILA / 2
    moment = posouvajici * (x_rez - m.X_PODPORA[0])
    sx = -moment * (yy - m.VYSKA / 2) / I
    tau = 1.5 * posouvajici / (m.TLOUSTKA * m.VYSKA) * (1 - (2 * yy / m.VYSKA - 1) ** 2)

    fig, axs = plt.subplots(1, 2, figsize=(9, 3.8), sharey=True)
    ax = axs[0]
    ax.plot(sx, yy, color=SEDA, lw=2, label="nosníková teorie")
    ax.plot(su[v_rezu, 0], y, "o", color=MODRA, ms=6, label="MKP (hodnoty v uzlech)")
    ax.set(xlabel=r"$\sigma_x$ [MPa]", ylabel="výška $y$ [mm]", title="Normálové napětí")
    ax.legend(frameon=False, loc="upper right", fontsize=9)
    ax = axs[1]
    ax.plot(tau, yy, color=SEDA, lw=2, label="nosníková teorie")
    ax.plot(np.abs(su[v_rezu, 2]), y, "o", color=ORANZOVA, ms=6, label="MKP (hodnoty v uzlech)")
    ax.set(xlabel=r"$|\tau_{xy}|$ [MPa]", title="Smykové napětí")
    ax.legend(frameon=False, loc="center left", fontsize=9)
    for ax in axs:
        uprav(ax)
    fig.suptitle(f"Řez nosníkem v místě $x={x_rez:.0f}$ mm", y=1.0)
    fig.tight_layout()
    fig.savefig("nosnik_rez.png")
    plt.close(fig)


# %% 7. Konvergence
def konvergence():
    nasobky = [1, 2, 4, 8, 16, 32]
    neznamych, w, sx, sy = [], [], [], []
    print(" neznámých  průhyb  sigma_x(80,0)  max|sigma_y|")
    for k in nasobky:
        v = m.nosnik(28 * k, 2 * k)
        neznamych.append(v["K"].shape[0])
        w.append(m.pruhyb(v))
        sx.append(v["s_uzly"][m.uzel(v["uzly"], 80, 0), 0])
        sy.append(np.abs(v["s"][:, 1]).max())
        print(f"{neznamych[-1]:10d} {w[-1]:7.4f} {sx[-1]:10.2f} {sy[-1]:12.1f}")
    ohyb, se_smykem = m.nosnikova_teorie()

    fig, axs = plt.subplots(1, 3, figsize=(13, 3.8))
    ax = axs[0]
    ax.axhline(se_smykem, color=SEDA, lw=1.2, ls="--")
    ax.axhline(ohyb, color=SEDA, lw=1.2, ls="--")
    ax.text(neznamych[0], se_smykem + 0.03, "nosník, ohyb a smyk", color=SEDA)
    ax.text(neznamych[-1], ohyb - 0.04, "nosník, jen ohyb", color=SEDA, ha="right", va="top")
    ax.plot(neznamych, w, "o-", color=MODRA, lw=2, ms=7)
    ax.set(title="Průhyb uprostřed rozpětí: ustálí se", ylabel="průhyb [mm]")

    ax = axs[1]
    ax.axhline(22.5, color=SEDA, lw=1.2, ls="--")
    ax.text(neznamych[0], 22.5 + 0.4, "nosníková teorie", color=SEDA)
    ax.plot(neznamych, sx, "o-", color=MODRA, lw=2, ms=7)
    ax.set(title=r"$\sigma_x$ ve spodním vlákně, $x=80$ mm: ustálí se", ylabel="napětí [MPa]")

    ax = axs[2]
    ax.plot(neznamych, sy, "o-", color=ORANZOVA, lw=2, ms=7)
    ax.set(title=r"Největší $|\sigma_y|$ pod silou: roste bez omezení", ylabel="napětí [MPa]")
    for ax in axs:
        ax.set_xscale("log")
        ax.set_xlabel("počet neznámých")
        ax.set_ylim(0, 1.12 * ax.get_ylim()[1])
        uprav(ax)
    fig.tight_layout()
    fig.savefig("konvergence.png")
    plt.close(fig)


if __name__ == "__main__":
    postup()
    tvarove_funkce()
    sestaveni()
    stredni = m.nosnik(112, 8)
    deformace(stredni)
    pole_napeti(stredni)
    rez(m.nosnik(224, 16))
    konvergence()
