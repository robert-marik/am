# %%
"""Metoda konečných prvků v 1D: tažená tyč upnutá na jednom konci.

Spuštění:  python mkp_tyc.py   (vytvoří obrázek tyc.png)
"""
import numpy as np
import matplotlib.pyplot as plt

# [zadani]
E = 10e9     # Youngův modul [Pa]
A = 0.01     # plocha průřezu [m^2]
L = 3.0      # délka tyče [m]
f = 20e3     # osové zatížení na jednotku délky [N/m]
n = 3        # počet prvků
# [konec zadani]


def tyc(n):
    """Vrátí uzly, posunutí v uzlech, napětí v prvcích a reakci v upnutí."""
    # [sestaveni]
    x = np.linspace(0, L, n + 1)             # souřadnice uzlů
    K = np.zeros((n + 1, n + 1))             # globální matice tuhosti
    b = np.zeros(n + 1)                      # globální vektor zatížení
    for e in range(n):                       # smyčka přes prvky
        h = x[e + 1] - x[e]                  # délka prvku
        Ke = E * A / h * np.array([[1, -1], [-1, 1]])   # matice tuhosti prvku
        be = f * h / 2 * np.array([1, 1])               # zatížení prvku
        uzly = [e, e + 1]                    # globální čísla uzlů prvku
        K[np.ix_(uzly, uzly)] += Ke          # přičtení do globální matice
        b[uzly] += be
    # [konec sestaveni]

    # [reseni]
    volne = np.arange(1, n + 1)              # uzel 0 je upnutý, u_0 = 0
    u = np.zeros(n + 1)
    u[volne] = np.linalg.solve(K[np.ix_(volne, volne)], b[volne])

    sigma = E * np.diff(u) / np.diff(x)      # napětí v prvcích [Pa]
    reakce = K[0] @ u - b[0]                 # síla v upnutí [N]
    # [konec reseni]
    return x, u, sigma, reakce, K, b


MODRA, ORANZOVA, ZELENA, SEDA, TMAVA = "#2a78d6", "#d9660b", "#1f9d7a", "#5f6b7a", "#1f2933"
BARVY_PRVKU = [MODRA, ORANZOVA, ZELENA]
DREVO = "#e9d8b8"


def stena(ax, x0, y0, vyska):
    """Šrafovaná stěna, do které je tyč upnutá."""
    ax.plot([x0, x0], [y0 - vyska / 2, y0 + vyska / 2], color=TMAVA, lw=2)
    for y in np.linspace(y0 - vyska / 2, y0 + vyska / 2, 8):
        ax.plot([x0 - 0.12, x0], [y - 0.1, y], color=TMAVA, lw=1)


def sipka(ax, odkud, kam, barva, lw=2):
    ax.annotate("", xy=kam, xytext=odkud,
                arrowprops=dict(arrowstyle="-|>", color=barva, lw=lw, shrinkA=0, shrinkB=0))


def obrazek_zadani():
    """Zadání úlohy a rovnováha kousku tyče."""
    from matplotlib.patches import Rectangle
    fig, axs = plt.subplots(1, 2, figsize=(11, 2.9), gridspec_kw=dict(width_ratios=[1.5, 1]))

    ax = axs[0]
    stena(ax, 0, 0, 1.1)
    ax.add_patch(Rectangle((0, -0.22), L, 0.44, fc=DREVO, ec=TMAVA, lw=1.2))
    for xs in np.linspace(0.15, L - 0.45, 8):
        sipka(ax, (xs, 0), (xs + 0.3, 0), ORANZOVA, lw=1.6)
    ax.text(L / 2, 0.36, "osové zatížení $f$ [N/m]", ha="center", color=TMAVA)
    ax.text(L + 0.08, 0, "volný konec", va="center", color=SEDA)
    ax.text(0, 0.68, "upnutí, $u(0)=0$", color=SEDA)
    sipka(ax, (0, -0.75), (L + 0.35, -0.75), SEDA, lw=1.2)
    for xs, popis in [(0, "0"), (L, "$L$")]:
        ax.plot([xs, xs], [-0.8, -0.7], color=SEDA, lw=1.2)
        ax.text(xs, -0.98, popis, ha="center", color=SEDA)
    ax.text(L + 0.42, -0.75, "$x$", va="center", color=SEDA)
    ax.set_title("Zadání: tyč s průřezem $A$ a modulem $E$", loc="left")
    ax.set_xlim(-0.3, L + 0.9)
    ax.set_ylim(-1.1, 0.9)

    ax = axs[1]
    ax.add_patch(Rectangle((0, -0.22), 1.2, 0.44, fc=DREVO, ec=TMAVA, lw=1.2))
    sipka(ax, (0, 0), (-0.55, 0), MODRA)
    sipka(ax, (1.2, 0), (2.0, 0), MODRA)
    sipka(ax, (0.4, 0), (0.8, 0), ORANZOVA)
    ax.text(-0.3, 0.14, "$N(x)$", ha="center", color=TMAVA)
    ax.text(1.65, 0.14, r"$N(x+\Delta x)$", ha="center", color=TMAVA)
    ax.text(0.6, 0.32, r"$f\,\Delta x$", ha="center", color=TMAVA)
    for xs, popis in [(0, "$x$"), (1.2, r"$x+\Delta x$")]:
        ax.plot([xs, xs], [-0.5, -0.3], color=SEDA, lw=1)
        ax.text(xs, -0.72, popis, ha="center", color=SEDA)
    ax.set_title("Síly na kousek tyče", loc="left")
    ax.set_xlim(-0.8, 2.3)
    ax.set_ylim(-1.1, 0.9)
    for ax in axs:
        ax.set_aspect("equal")
        ax.axis("off")
    fig.savefig("tyc_zadani.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


def obrazek_prvky(x):
    """Dělení tyče na prvky a bázové funkce."""
    from matplotlib.patches import Rectangle
    fig, axs = plt.subplots(2, 1, figsize=(9, 4.6), sharex=True,
                            gridspec_kw=dict(height_ratios=[1, 2.6]))
    ax = axs[0]
    for e in range(n):
        ax.add_patch(Rectangle((x[e], -0.2), x[e + 1] - x[e], 0.4, fc=BARVY_PRVKU[e],
                               alpha=0.25, ec="none"))
        ax.text((x[e] + x[e + 1]) / 2, 0, f"prvek {e}", ha="center", va="center", color=TMAVA)
    ax.add_patch(Rectangle((0, -0.2), L, 0.4, fc="none", ec=TMAVA, lw=1.2))
    stena(ax, 0, 0, 0.9)
    for i, xi in enumerate(x):
        ax.plot(xi, 0, "o", ms=16, color=TMAVA, zorder=3)
        ax.text(xi, 0, str(i), color="white", ha="center", va="center", fontweight="bold",
                zorder=4)
    ax.set_ylim(-0.55, 0.55)
    ax.axis("off")
    ax.set_title("Uzly 0 až 3 a tři prvky", loc="left")

    ax = axs[1]
    e = 1                                        # zvýrazněný prvek
    ax.axvspan(x[e], x[e + 1], color=BARVY_PRVKU[e], alpha=0.12, lw=0)
    for i in range(n + 1):
        y = np.zeros(n + 1)
        y[i] = 1
        ax.plot(x, y, color=SEDA, lw=1.5)
        ax.text(x[i], 1.06, rf"$\varphi_{i}$", ha="center", color=TMAVA)
    ax.plot(x[e:e + 2], [1, 0], color=BARVY_PRVKU[e], lw=3)
    ax.plot(x[e:e + 2], [0, 1], color=BARVY_PRVKU[e], lw=3)
    ax.text((x[e] + x[e + 1]) / 2, 0.96, r"$\varphi_1$ klesá, derivace $-\frac{1}{h}$",
            ha="center", va="center", color=TMAVA, fontsize=9)
    ax.text((x[e] + x[e + 1]) / 2, 0.85, r"$\varphi_2$ roste, derivace $+\frac{1}{h}$",
            ha="center", va="center", color=TMAVA, fontsize=9)
    ax.annotate("", xy=(x[e], -0.12), xytext=(x[e + 1], -0.12),
                arrowprops=dict(arrowstyle="<->", color=SEDA, lw=1))
    ax.text((x[e] + x[e + 1]) / 2, -0.2, "$h$", ha="center", va="top", color=SEDA)
    ax.set_xticks(x, [f"$x_{i}$" for i in range(n + 1)])
    ax.set_yticks([0, 1])
    ax.set_ylim(-0.32, 1.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Bázové funkce; na prvku 1 jsou nenulové jen $\\varphi_1$ a $\\varphi_2$",
                 loc="left")
    fig.tight_layout()
    fig.savefig("tyc_prvky.png", dpi=150)
    plt.close(fig)


def obrazek_sestaveni(x):
    """Tyč jako pružiny za sebou a skládání matice tuhosti."""
    from matplotlib.patches import Rectangle
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.4), gridspec_kw=dict(width_ratios=[1.7, 1]))

    ax = axs[0]
    stena(ax, 0, 0, 0.9)
    for e in range(n):
        a, b_ = x[e] + 0.14, x[e + 1] - 0.14
        zx = np.linspace(a + 0.12, b_ - 0.12, 13)
        zy = 0.14 * np.r_[0, (-1) ** np.arange(11), 0]
        ax.plot(np.r_[a, zx, b_], np.r_[0, zy, 0], color=BARVY_PRVKU[e], lw=2)
        ax.text((a + b_) / 2, 0.32, r"$\frac{EA}{h}$", ha="center", color=TMAVA, fontsize=12)
        ax.text((a + b_) / 2, -0.42, f"prvek {e}", ha="center", color=SEDA, fontsize=9)
    sily = [r"$\frac{fh}{2}$", "$fh$", "$fh$", r"$\frac{fh}{2}$"]
    for i, xi in enumerate(x):
        ax.plot(xi, 0, "o", ms=16, color=TMAVA, zorder=3)
        ax.text(xi, 0, str(i), color="white", ha="center", va="center", fontweight="bold",
                zorder=4)
        if i > 0:
            sipka(ax, (xi, -0.85), (xi + 0.45, -0.85), ORANZOVA)
            ax.text(xi + 0.22, -1.2, sily[i], ha="center", color=TMAVA, fontsize=12)
    sipka(ax, (0, -0.85), (-0.45, -0.85), SEDA)
    ax.text(-0.22, -1.2, "reakce", color=SEDA, fontsize=9, ha="center")
    ax.set_title("Tyč jako tři pružiny za sebou, zatížení přenesené do uzlů", loc="left")
    ax.set_xlim(-0.6, L + 0.7)
    ax.set_ylim(-1.45, 0.75)
    ax.set_aspect("equal")
    ax.axis("off")

    ax = axs[1]
    for e in range(n):
        ax.add_patch(Rectangle((e, e), 2, 2, fc=BARVY_PRVKU[e], alpha=0.3, ec=BARVY_PRVKU[e],
                               lw=2))
    hodnoty = [["1", "−1", "0", "0"], ["−1", "1+1", "−1", "0"],
               ["0", "−1", "1+1", "−1"], ["0", "0", "−1", "1"]]
    for i in range(4):
        for j in range(4):
            ax.text(j + 0.5, i + 0.5, hodnoty[i][j], ha="center", va="center",
                    color=TMAVA if hodnoty[i][j] != "0" else "#a9b1bb", fontsize=11)
        ax.text(i + 0.5, -0.25, f"$u_{i}$", ha="center", color=SEDA)
        ax.text(-0.3, i + 0.5, f"{i}", ha="center", va="center", color=SEDA)
    ax.add_patch(Rectangle((0, 0), 4, 4, fill=False, ec=SEDA, lw=1))
    ax.set_xlim(-0.6, 4.2)
    ax.set_ylim(4.2, -0.7)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(r"Matice $K$ (bez násobku $\frac{EA}{h}$): bloky prvků se překrývají",
                 loc="left", fontsize=10)
    fig.savefig("tyc_sestaveni.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    x, u, sigma, reakce, K, b = tyc(n)
    obrazek_zadani()
    obrazek_prvky(x)
    obrazek_sestaveni(x)
    np.set_printoptions(precision=4, suppress=True)
    print("K [MN/m] =\n", K / 1e6)
    print("b [kN] =", b / 1e3)
    print("u [mm] =", u * 1e3)
    print("presne u v uzlech [mm] =", f / (E * A) * (L * x - x**2 / 2) * 1e3)
    print("sigma [MPa] =", sigma / 1e6)
    print("reakce [kN] =", reakce / 1e3)

    # %% obrázek: srovnání s přesným řešením
    xx = np.linspace(0, L, 200)
    u_presne = f / (E * A) * (L * xx - xx**2 / 2)
    s_presne = f * (L - xx) / A

    MODRA, ORANZOVA, SEDA = "#2a78d6", "#d9660b", "#5f6b7a"
    fig, axs = plt.subplots(1, 2, figsize=(10, 3.8))
    ax = axs[0]
    ax.plot(xx, u_presne * 1e3, color=SEDA, lw=2, label="přesné řešení")
    ax.plot(x, u * 1e3, "o-", color=MODRA, lw=2, ms=7, label=f"MKP, {n} prvky")
    ax.set(xlabel="poloha $x$ [m]", ylabel="posunutí $u$ [mm]", title="Posunutí")
    ax.legend(frameon=False)

    ax = axs[1]
    ax.plot(xx, s_presne / 1e6, color=SEDA, lw=2, label="přesné řešení")
    for e in range(n):
        ax.plot(x[e:e + 2], [sigma[e] / 1e6] * 2, color=ORANZOVA, lw=2,
                label=f"MKP, {n} prvky" if e == 0 else None)
    ax.set(xlabel="poloha $x$ [m]", ylabel=r"napětí $\sigma$ [MPa]", title="Napětí")
    ax.legend(frameon=False)

    for ax in axs:
        ax.grid(color="#e3e6ea", lw=0.8)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_xticks(x)
    fig.tight_layout()
    fig.savefig("tyc.png", dpi=150)
