"""Metoda konečných prvků pro rovinnou napjatost, lineární trojúhelníkové prvky.

Jednotky: mm, N, MPa. Stupně volnosti jsou číslovány tak, že uzel i má
posunutí ve směru x na pozici 2i a ve směru y na pozici 2i+1.
"""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve


# [sit]
def sit_obdelnik(delka, vyska, nx, ny):
    """Pravidelná síť trojúhelníků na obdélníku, nx krát ny čtverců po dvou."""
    X, Y = np.meshgrid(np.linspace(0, delka, nx + 1), np.linspace(0, vyska, ny + 1))
    uzly = np.column_stack([X.ravel(), Y.ravel()])
    prvky = []
    for j in range(ny):
        for i in range(nx):
            a = j * (nx + 1) + i                 # levý dolní roh čtverce
            b, c, d = a + 1, a + nx + 1, a + nx + 2
            if (i + j) % 2 == 0:                 # střídáme směr úhlopříčky
                prvky += [[a, b, d], [a, d, c]]
            else:
                prvky += [[a, b, c], [b, d, c]]
    return uzly, np.array(prvky)
# [konec sit]


# [material]
def material(Ex, Ey, nu_xy, Gxy):
    """Matice tuhosti C ortotropního materiálu při rovinné napjatosti."""
    nu_yx = nu_xy * Ey / Ex
    d = 1 - nu_xy * nu_yx
    return np.array([[Ex / d,         nu_yx * Ex / d, 0],
                     [nu_xy * Ey / d, Ey / d,         0],
                     [0,              0,              Gxy]])
# [konec material]


# [prvek]
def matice_B(xy):
    """Matice B (3x6) a plocha trojúhelníka s vrcholy xy (3x2)."""
    (x1, y1), (x2, y2), (x3, y3) = xy
    plocha = ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
    dx = np.array([y2 - y3, y3 - y1, y1 - y2]) / (2 * plocha)   # dN_i/dx
    dy = np.array([x3 - x2, x1 - x3, x2 - x1]) / (2 * plocha)   # dN_i/dy
    B = np.zeros((3, 6))
    B[0, 0::2] = dx          # epsilon_x  = du_x/dx
    B[1, 1::2] = dy          # epsilon_y  = du_y/dy
    B[2, 0::2] = dy          # gamma_xy   = du_x/dy + du_y/dx
    B[2, 1::2] = dx
    return B, plocha


def stupne_volnosti(prvek):
    """Čísla šesti neznámých, které patří ke třem uzlům prvku."""
    return np.column_stack([2 * prvek, 2 * prvek + 1]).ravel()
# [konec prvek]


# [sestaveni]
def sestav(uzly, prvky, C, tloustka):
    """Globální matice tuhosti K (řídká)."""
    m = len(prvky)
    radky = np.zeros((m, 36), dtype=int)
    sloupce = np.zeros((m, 36), dtype=int)
    hodnoty = np.zeros((m, 36))
    for k, prvek in enumerate(prvky):
        B, plocha = matice_B(uzly[prvek])
        Ke = tloustka * plocha * B.T @ C @ B         # matice tuhosti prvku 6x6
        sv = stupne_volnosti(prvek)
        radky[k] = np.repeat(sv, 6)
        sloupce[k] = np.tile(sv, 6)
        hodnoty[k] = Ke.ravel()
    n = 2 * len(uzly)
    # coo_matrix sečte příspěvky, které míří na stejné místo
    return coo_matrix((hodnoty.ravel(), (radky.ravel(), sloupce.ravel())),
                      shape=(n, n)).tocsr()
# [konec sestaveni]


# [reseni]
def vyres(K, f, pevne):
    """Vyřeší K u = f, kde stupně volnosti `pevne` mají nulové posunutí."""
    n = K.shape[0]
    volne = np.setdiff1d(np.arange(n), pevne)
    u = np.zeros(n)
    u[volne] = spsolve(K[volne][:, volne], f[volne])
    reakce = K @ u - f           # nenulové jen v uchycených stupních volnosti
    return u, reakce
# [konec reseni]


# [napeti]
def napeti(uzly, prvky, C, u):
    """Napětí (sigma_x, sigma_y, tau_xy) v jednotlivých prvcích."""
    s = np.zeros((len(prvky), 3))
    for k, prvek in enumerate(prvky):
        B, _ = matice_B(uzly[prvek])
        s[k] = C @ B @ u[stupne_volnosti(prvek)]
    return s


def do_uzlu(uzly, prvky, s):
    """Vyhlazení: hodnota v uzlu je průměrem hodnot z přilehlých prvků."""
    soucet = np.zeros((len(uzly), s.shape[1]))
    pocet = np.zeros(len(uzly))
    for k, prvek in enumerate(prvky):
        soucet[prvek] += s[k]
        pocet[prvek] += 1
    return soucet / pocet[:, None]
# [konec napeti]


def uzel(uzly, x, y):
    """Číslo uzlu, který leží nejblíže bodu (x, y)."""
    return int(np.argmin((uzly[:, 0] - x) ** 2 + (uzly[:, 1] - y) ** 2))


# ---------------------------------------------------------------------------
# Úloha: dřevěný nosník v tříbodovém ohybu
# ---------------------------------------------------------------------------
# [zadani]
DELKA, VYSKA, TLOUSTKA = 280.0, 20.0, 20.0     # rozměry nosníku [mm]
X_PODPORA = (20.0, 260.0)                      # polohy podpor [mm]
X_SILA = 140.0                                 # působiště síly [mm]
SILA = 1000.0                                  # velikost síly [N]
# smrk, vlákna ve směru x (L), výška ve směru y (R); hodnoty v MPa
E_L, E_R, NU_LR, G_LR = 12000.0, 800.0, 0.4, 700.0
# [konec zadani]


# [nosnik]
def nosnik(nx, ny):
    """Tříbodový ohyb na síti nx krát ny čtverců. Vrací slovník s výsledky."""
    uzly, prvky = sit_obdelnik(DELKA, VYSKA, nx, ny)
    C = material(E_L, E_R, NU_LR, G_LR)
    K = sestav(uzly, prvky, C, TLOUSTKA)

    leva = uzel(uzly, X_PODPORA[0], 0)
    prava = uzel(uzly, X_PODPORA[1], 0)
    nahore = uzel(uzly, X_SILA, VYSKA)

    f = np.zeros(2 * len(uzly))
    f[2 * nahore + 1] = -SILA                        # síla míří dolů
    pevne = [2 * leva, 2 * leva + 1, 2 * prava + 1]  # pevná a posuvná podpora

    u, reakce = vyres(K, f, pevne)
    s = napeti(uzly, prvky, C, u)
    return dict(uzly=uzly, prvky=prvky, K=K, u=u, reakce=reakce, s=s,
                s_uzly=do_uzlu(uzly, prvky, s),
                leva=leva, prava=prava, nahore=nahore)
# [konec nosnik]


def pruhyb(v):
    """Průhyb střednice uprostřed rozpětí vůči střednici nad podporami [mm]."""
    uzly, uy = v["uzly"], v["u"][1::2]
    stred = uy[uzel(uzly, X_SILA, VYSKA / 2)]
    kraje = [uy[uzel(uzly, x, VYSKA / 2)] for x in X_PODPORA]
    return np.mean(kraje) - stred


def nosnikova_teorie():
    """Průhyb podle nosníkové teorie: ohyb a ohyb se smykem [mm]."""
    rozpeti = X_PODPORA[1] - X_PODPORA[0]
    I = TLOUSTKA * VYSKA ** 3 / 12
    ohyb = SILA * rozpeti ** 3 / (48 * E_L * I)
    smyk = SILA * rozpeti / (4 * (5 / 6) * G_LR * TLOUSTKA * VYSKA)
    return ohyb, ohyb + smyk


if __name__ == "__main__":
    v = nosnik(112, 8)
    print("neznámých:", v["K"].shape[0])
    print("reakce v podporách [N]:", v["reakce"][2 * v["leva"] + 1],
          v["reakce"][2 * v["prava"] + 1], " vodorovná:", v["reakce"][2 * v["leva"]])
    print("průhyb [mm]:", pruhyb(v), " nosníková teorie:", nosnikova_teorie())
