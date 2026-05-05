# Metody řešení diferenciálních rovnic 2

## Vlnová rovnice 

Vlnová rovnice je rovnice popisující kmity strun (v jednorozměrném
případě), membrán (ve dvourozměrném případě) nebo těles (v trojrozměrném
případě). Odvodíme rovnici kmitání strun. 

<div class='obtekat'>


```{figure} struna.png
K odvození pohybové rovnice struny.
```
</div>

Na kmitající struně uvažujme
v bodě $x$ element o délce $\Delta
x$. Výchylku z rovnovážného stavu označme $u$. Dále označme
$\vec {\mathcal T}$ sílu, která v tomto bodě napíná strunu, vnitřní
napětí ve struně. Tento vektor má podél struny konstantní velikost a
směr se mění podle zakřivení struny. Označíme-li $\phi$ úhel mezi
vektorem $\vec {\mathcal T}$ a vodorovným směrem, je
$\tan \phi=\frac {\partial
  u}{\partial x}$ (derivace je směrnice tečny). Na levý konec působí
síla $\vec {\mathcal T}_1$, kterou pro další počítání rozložíme do
vodorovného a svislého směru. Doleva působí síla o velikosti
$\mathcal T\cos\phi$ a dolů síla $\mathcal T\sin\phi$. Podobně, na pravý
konec, kde je směrnice tečny $\phi+\Delta\phi$ působí doprava síla
$\mathcal{T}\cos(\phi+\Delta\phi)$ a nahoru síla
$\mathcal T\sin(\phi+\Delta\phi)$. Protože se element pohybuje ve
svislém směru, podle Newtonova pohybového zákona platí

$$
 m\frac{\partial ^2u}{\partial t^2}=\mathcal T\sin(\phi+\Delta\phi)-\mathcal T\sin\phi,
$$ 

kde $m$ je hmotnost uvažovaného elementu. 

Je-li
lineární specifická hmotnost struny $\rho$ a délka elementu v rovnovážné
poloze (bez deformace) je přibližně $\Delta x$, je možno vyjádřit
hmotnost jako $m=\rho\Delta x$ a dostáváme po úpravě vztah

$$\begin{equation*}
  \frac {\rho}{\mathcal T}\frac{\partial ^2u}{\partial t^2}=\frac{\sin(\phi+\Delta\phi)-\sin\phi}{\Delta x}
\end{equation*}$$

Pokud pravou stranu přepíšeme do tvaru 

$$\begin{equation*}
  % \frac{\sin(\phi+\Delta\phi)-\sin\phi}{\Delta x}=
  \frac{\sin(\phi+\Delta\phi)-\sin\phi}{\Delta \phi}\frac{\Delta \phi}{\Delta x}
\end{equation*}$$ 

a v limitě stáhneme velikost uvažovaného elementu
k nule, dostáváme napravo výraz známý z definice derivace

$$
  \frac{\partial \sin(\phi)}{\partial \phi}\frac{\partial \phi}{\partial x}\quad\text{ tj.}\quad \cos(\phi)\frac{\partial \phi}{\partial x}.
$$

Potřebujeme nyní vyjádřit výraz
$\frac{\partial \phi}{\partial x}$. Ze vztahu
$\tan \phi=\frac {\partial u}{\partial x}$ derivováním podle $x$
dostáváme $$\begin{equation*}
  \frac{1}{\cos^2 \phi}\frac{\partial \phi}{\partial x}=\frac {\partial^2 u}{\partial x^2}
\end{equation*}$$
a za předpokladu malých výchylek nahradíme
v předchozích dvou vzorcích funkci kosinus její lineární aproximací
v okolí nuly: 
$$\begin{equation*}
\cos(\phi)\approx \cos(0)+(\cos(\phi))'{\Bigl.\Bigr|}_{\phi=0}(\phi -0)= 1+\sin(\phi){\Bigl.\Bigr|}_{\phi=0}\phi=1.
\end{equation*}$$ 
$$
\cos(\phi)\approx \cos(0)+(\cos(\phi))'\Bigr|_{\phi=0}(\phi -0)= 1+\sin(\phi)\Bigr|_{\phi=0}\phi=1.
$$ 
Tím se pravá strana rovnice zjednoduší na
$\frac {\partial^2
  u}{\partial x^2}$ a získáváme rovnici $$\begin{equation*}
  \frac{\partial ^2u}{\partial t^2}=\frac {\cal T}{\rho} \frac {\partial^2 u}{\partial x^2}.
\end{equation*}$$ 
Toto je rovnice popisující kmitavý pohyb struny. Ve
vícerozměrném případě je situace obdobná, pouze na pravé straně
dostaneme Laplaceův operátor a výsledná rovnice $$\begin{equation}
   \frac{\partial ^2u}{\partial t^2}=\frac {\cal T}{\rho}\nabla^2 u.
\end{equation}$$ 
se nazývá *vlnová rovnice*.

Po přeznačení je možno vlnovou rovnici zapsat ve tvaru
$$\begin{equation}
   \frac{\partial ^2u}{\partial t^2}=c^2\nabla^2 u,
\end{equation}$$ 
kde $c$ je kladná konstanta. 

<!--
Nechť $f$ je libovolná
dvakrát diferencovatelná funkce jedné proměnné a uvažujme jednorozměrnou
vlnovou rovnici 
$$\begin{equation}
  \frac{\partial ^2u}{\partial t^2}=c^2\frac{\partial ^2u}{\partial x^2}
\end{equation}$$ 
a funkci dvou proměnných $u(x,t)=f(x-ct)$. Potom platí
$$\begin{equation*}
  \begin{aligned}
    \frac {\partial u}{\partial x}&=f'(x-ct) ,
    &\qquad&\frac {\partial^2
      u}{\partial x^2}=f''(x-ct) \\
    \frac {\partial u}{\partial
      t}&=-cf'(x-ct),
    &&\frac {\partial^2 u}{\partial t^2}=c^2f''(x-ct),
  \end{aligned}
\end{equation*}
$$ 
odkud snadno vidíme, že funkce $u$ je řešením rovnice ...
Vrstevnice funkce $u(x,t)$ jsou dány rovnicí $x-ct=\text{konst}$, což
odpovídá tomu, že bod o dané výchylce se za čas $\Delta t$ posune o
$\Delta x=c\Delta t$. Jedná se tedy o postupnou vlnu, která se šíří
rychlostí $c$ doprava. Podobně, funkce $v(x,c)=f(x+ct)$ je řešením
rovnice ..., které odpovídá postupné vlně, která postupuje
rychlostí $c$ doleva.
-->

Rovnice popisující podélné kmity kmity tyče modulu pružnosti $E$ a
hustotě $\rho$ má stejný tvar, přičemž $c=\sqrt{E}\rho$ je rychlost šíření kmitů.
Trojrozměrná analogie této rovnice je vhodná pro popis elastických kmitů
(chvění) v tělese.


## Fourierova metoda (separace proměnných)

Jedna z nejjednodušších metod řešení parciálních diferenciálních
rovnic spočívá v tom, že se řešení rovnic snažíme najít v nějakém
konkrétním tvaru, který nám umožní rovnici redukovat na několik rovnic
jednodušších. Je možné ji použít i pro rovnici vedení tepla, i pro vlnovou rovnici. 

Uvažujme šíření tepla v tyči jednotkové délky bez vnitřních zdrojů
tepelné energie, popsané diferenciální rovnicí $$\begin{equation}
  \frac {\partial u}{\partial t}=  \frac {\partial^2 u}{\partial x^2}.
\end{equation}$$ Pro jednoznačný popis děje je nutno zadat počáteční
teplotu $\phi(x)$ ve všech bodech tyče a podmínky, které udávají,
v jakém prostředí se tyč nachází -- například teplotu konců tyče. Máme
tedy podmínky 
$$\begin{equation}
  u(x,0)=\phi(x),\quad u(0,t)=u_0(t),\quad u(1,t)=u_1(t).
\end{equation}$$ 
Pro jednoduchost uvažujme homogenní okrajové podmínky
$u(0,t)=0=u(1,t)$. Řešení $u$ budeme hledat ve tvaru funkce
$$\begin{equation*}
  u(x,t)=X(x)T(t),
\end{equation*}$$ 
kde $X$ a $T$ jsou funkce jedné proměnné. V tomto
označení platí $\frac{\partial u}{\partial t}=X(x)T'(t)$ a
$\frac{\partial^2
  u}{\partial x^2}=X''(x)T(t)$ a po dosazení do
rovnice a po vydělení faktorem $X(x)T(t)$ dostaneme
$$\begin{equation*}
  \frac {T'(t)}{T(t)}=\frac {X''(x)}{X(x)}.
\end{equation*}$$ 
Protože levá strana závisí pouze na $t$ a pravá strana
pouze na $x$, musí být obě strany rovny stejné konstantě. Tuto konstantu
zapíšeme z důvodů které budou patrné později jako $-\lambda^2$.
Z počátečních a okrajových podmínek naložených na funkce $u$ plyne, že
funkce $X$ musí splňovat $$\begin{equation}
  X(0)=0=X(1).
\end{equation}$$ Funkce $X$ a $T$ tedy musí splňovat rovnice
$$\begin{equation*}
  T'=-\lambda^2 T, \quad X''+\lambda^2 X=0
\end{equation*}
$$ 
a podmínku na okrajích.
. Rovnice $$\begin{equation*}
  T'=-\lambda^2 T
\end{equation*}$$ je lineární a její obecné řešení je libovolný násobek
funkce $T(t)=e^{-\lambda^2 t}$. Úloha najít funkci vyhovující rovnici

$$\begin{equation*}
X''+\lambda^2 X=0
\end{equation*}$$

a podmínce
$$\begin{equation*}
  X(0)=0=X(1)
\end{equation*}$$ 
se nazývá okrajová úloha a věnovali jsme se jí v kapitole o diferenciálních rovnicích druhého řádu.

Netriviální řešení této úlohy existuje jen pro některé hodnoty parametru $\lambda$. Hodnota $\lambda^2$, pro kterou existuje netriviální řešení okrajové úlohy, se nazývá vlastní číslo a příslušné řešení se nazývá vlastní funkcí.

Z rozboru v kapitole věnované diferenciálním rovnicím druhého řádu víme, že obecné řešení rovnice $X''+\lambda^2 X=0$ je tvaru $$\begin{equation*}
  X(x)=A\cos(\lambda x)+B\sin(\lambda x)
\end{equation*}$$ kde $A$ a $B$ jsou reálné konstanty. Z podmínky $X(0)=0$ plyne, že $A=0$. Z podmínky $X(1)=0$ pak plyne, že $B\sin(\lambda)=0$. Nechť $B\neq 0$ (jinak by řešení bylo triviální).
Platí tedy $\sin(\lambda)=0$, neboli $\lambda=k\pi$, kde $k$ je
přirozené číslo. Vlastní hodnoty jsou tedy tvaru $$\begin{equation*}
\lambda^2=k^2\pi^2
\end{equation*}$$ a uvažovaná okrajová úloha pro libovolné přirozené
číslo $k$ má řešení $$\begin{equation*}
  X(x)=C\sin(k\pi x),
\end{equation*}$$ kde $C$ je reálná konstanta.

Protože řešení rovnice
hledáme ve tvaru $u(x,t)=X(x)T(t)$, můžeme
výsledky předchozích odstavců shrnout do poznatku, že pro libovolnou
konstantu $C_k$ a libovolné přirozené číslo $k$ je funkce
$$\begin{equation*}
  C_k\sin(k\pi x)e^{-\lambda^2 t}.
\end{equation*}$$ 
Protože rovnice
 je lineární, je řešením i libovolná lineární
kombinace těchto funkcí. Použijeme-li všechny funkce tohoto tvaru,
dostáváme řešení $$\begin{equation*}
  u(x,t)=\sum_{k=1}^\infty C_k\sin(k\pi x)e^{-\lambda^2 t}.
\end{equation*}$$

Protože máme zadánu počáteční podmínku
ve tvaru $u(x,0)=\phi(x)$, potřebujeme najít
konstanty $C_k$ takové, že platí $$\begin{equation*}
  \sum_{k=1}^\infty C_k\sin(k~\pi x)=\phi(x).
\end{equation*}$$ Tuto úlohu budeme řešit v následující podkapitole.

## Fourierův rozvoj periodické funkce

Nekonečná řada goniometrických funkcí tvaru $$\begin{equation*}
  \frac{a_0}2+\sum_{k=1}^\infty\left(a_k\cos(k~x)+b_k\sin(k~x)\right)
\end{equation*}$$ může pro konkrétní hodnoty koeficientů $a_i$, $b_i$
konvergovat k nějaké funkci $f(x)$ a za jistých podmínek je tato
funkce dostatečně pěkná: je spojitá, je možno ji derivovat člen po členu
apod.

Při řešení rovnic matematické fyziky řešíme opačný problém: pro zadanou
funkci $f(x)$ na intervalu $[-\pi,\pi]$ chceme nalézt koeficienty $a_i$,
$b_i$ tak, aby na tomto intervalu platilo $$\begin{equation*}
  f(x)=\frac{a_0}2+\sum_{k=1}^\infty\left(a_k\cos(kx)+b_k\sin(kx)\right).
\end{equation*}$$ Ukazuje se, že tento zápis funkce $f$ pomocí
goniometrických funkcí je možný, pokud použijeme následující volbu
koeficientů $$\begin{align*}
  a_0&=\frac 1\pi\int_{-\pi}^\pi f(x)\,\mathrm dx\\
  a_k&=\frac 1\pi\int_{-\pi}^\pi f(x)\cos(kx)\,\mathrm dx\\
  b_k&=\frac 1\pi\int_{-\pi}^\pi f(x)\sin(kx)\,\mathrm dx.
\end{align*}$$ Tyto vztahy je možno zobecnit i na jiné intervaly než
$[-\pi,\pi]$ a také pro jiné funkce než goniometrické -- je možné použít
například systém všech vlastních funkcí okrajové úlohy. V našem případě
je možné ukázat, že pokud platí $$\begin{equation*}
  C_k=2\int_{0}^1\phi(x)\sin(k\pi x)\,\mathrm dx,
\end{equation*}$$ potom na intervalu $[0,1]$ platí $$\begin{equation*}
  \sum_{k=1}^\infty C_k\sin(k\pi x)=\phi(x).
\end{equation*}$$ 
Máme tedy koeficienty $C_k$, které je možno použít pro
konečný zápis řešení naší úlohy.


### Fourierova metoda (pokračování)

Řešení rovnice, které splňuje podmínky
je $$\begin{equation*}
  u(x,t)=\sum_{k=1}^\infty C_k\sin(k\pi x)e^{-\lambda^2 t},
\end{equation*}$$ kde $$\begin{equation*}
  C_k=2\int_{0}^1\phi(x)\sin(k\pi x)\,\mathrm dx.
\end{equation*}$$

Podobně, kmity struny jednotkové délky, popsané vlnovou rovnicí
$$\begin{equation*}
  \frac{\partial ^2u}{\partial t^2}=c^2\frac{\partial ^2u}{\partial x^2},
\end{equation*}$$ 
s okrajovými podmínkami 
$$\begin{equation*}
  u(0,t)=0=u(1,t)
\end{equation*}$$ 
(struna upevněná na koncích) a počátečními podmínkami
$$\begin{equation*}
  u(x,0)=\phi(x),\quad \frac{\partial u}{\partial t}(x,0)=\psi(x).
\end{equation*}$$ 
(počáteční poloha a rychlost všech bodů struny) jsou
dány vztahem $$\begin{equation*}
  u(x,t)=\sum_{k=1}^\infty\left(a_n\cos(k\pi t)+b_n\sin(k\pi t)\right)\sin(k\pi x),
\end{equation*}$$
kde 
$$\begin{equation*}
  a_k=2\int_0^1\phi(x)\sin(k\pi x)\,\mathrm dx
\end{equation*}
$$ 
a 
$$\begin{equation*}
  b_k=2\int_0^1\psi(x)\cos(k\pi x)\,\mathrm dx\end{equation*}
$$


## Separace proměnných u parciálních diferenciálních rovnic

https://youtu.be/wfvY6bwlxaw

Budeme se zabývat jednorozměrnou rovnicí vedení tepla ve tvaru

$$\frac{\partial u}{\partial t}=\frac{\partial^2 u}{\partial x^2}.$$ 

V
tomto tvaru rovnice neobsahuje žádné konstanty a je to tvar, se kterým
se pracuje ve většině matematických publikací. Reálnou rovnici vedení
tepla převedeme do tohoto tvaru zavedením bezrozměrných veličin, což
si ukážeme v následující přednášce. Teď si ukážeme, jak řešení rovnice
vede na řešení LDR druhého řádu. Uvažujme pro jednoduchost okrajovou
úlohu, kdy konce tyče jsou udržovány na nulové teplotě, tj. je-li tyč
délky $l$ položena v ose $x$ tak, že levý konec je v počátku, platí pro
teplotu $u(x,t)$ podmínky $u(0,t)=u(l,t)=0$ v libovolném čase $t$.

Budeme řešení hledat ve tvaru $u(x,t)=\varphi(x)\psi(t)$, kde $\varphi$ a $\psi$ jsou funkcemi jedné proměnné.
Platí
$$\frac{\partial u}{\partial t}=\varphi(x)\psi'(t), \quad \frac{\partial^2 u}{\partial x^2}=\varphi''(x) \psi(t)$$
a rovnice má tvar
$$\varphi(x)\psi'(t)=\varphi''(x)\psi (t).$$
Vydělením této rovnice součinem $\varphi(x)\psi(t)$ dostáváme
$$\frac {\psi'(t)}{\psi(t)}=\frac{\varphi''(x)}{\varphi (x)}.$$
Toto je rovnice, kde levá strana je funkcí proměnné $t$ a pravá strana funkcí proměnné $x$. Obě proměnné jsou však nezávislé a uvedená rovnost může být splněna jen tehdy, když se rovnají společné konstantě.
$$\frac {\psi'(t)}{\psi(t)}=\frac{\varphi''(x)}{\varphi (x)}=\omega.$$

Okrajové podmínky vynucují platnost vztahů $\varphi(0)=\varphi(l)=0$. Jesliže je v takovém případě konstanta $\omega$ kladná, má úloha pouze nulové řešení (viz výše výpočet vlastních hodnot pro tuto úlohu). Konstanta $\omega$ tedy musí být záporná. 
Přeznačme ji do tvaru $$\omega = -\lambda^2$$ Platí tedy
$$\frac {\psi'(t)}{\psi(t)}=-\lambda ^2,\quad \frac{\varphi''(x)}{\varphi (x)}=-\lambda ^2.$$
První rovnice představuje lineární diferenciální rovnici prvního řádu
$$\psi'=-\lambda^2\psi$$
s partikulárním řešením $\psi(t)=e^{-\lambda^2 t}.$
Druhá rovnice představuje společně s okrajovou podmínkou okrajovou úlohu pro lineární diferenciální rovnici druhého řádu
$$\varphi''+\lambda^2\varphi=0, \quad \varphi(0)=\varphi(l)=0.$$ Máme tedy Dirichletovu úlohu na vlastní čísla a vlastní funkce, jak jsme ji viděli u kmitů struny nebo u namáhání na vzpěr. Řešením je funkce $\varphi(x)=\sin(\lambda x)$, kde $\lambda$ je vlastní hodnota této úlohy.
Funkce $$u(x,t)=\sin(\lambda x)e^{-\lambda^2 t}$$ je tedy řešením rovnice 
$$\frac{\partial u}{\partial t}=\frac{\partial^2 u}{\partial x^2}.$$ 
Rovnici je možno přepsat do tvaru
$$\frac{\partial u}{\partial t}-\frac{\partial^2 u}{\partial x^2}=0,$$
kdy na levé straně stojí lineární operátor a na pravé straně je nula. Proto je každá lineární kombinace řešení opět řešením a pro libovolnou volbu konstant je funkce
$$u(x,t)=\sum_{\lambda}C_\lambda\sin(\lambda x)e^{-\lambda^2 t}$$
také řešením. Součet na pravé straně je přes všechna vlastní čísla, kterých je nekonečně mnoho.

Nyní začíná být rozbor úlohy nad rámec našeho kurzu, protože se
objevil nekonečný součet. Ukazuje se, že tento zápis je dostatečně
bohatý na to, aby obsáhl libovolnou rozumnou počáteční podmínku a
vzorec je tedy schopen popsat řešení úlohy pro libovolné fyzikálně
relevantní situace. Vidíme i přímo strukturu řešení, které je jakousi
lineární kombinací různých módů. Tato skutečnost lépe vynikne na
analogické diferenciální rovnici kmitání struny, kdy jednotlivé módy
přímo vnímáme sluchem: struna nemůže kmitat na libovolné frekvenci, ale
pouze a frekvenci dané okrajovou podmínkou a na frekvencích násobných.

Poznámka: Podobná situace a možnost separace proměnných je u rovnice
kmitů struny
$$\frac{\partial^2 u}{\partial t^2}=\frac{\partial^2 u}{\partial x^2}$$
nebo jejího zobecnění na kmity desek a chvění těles. Opět separace vede k LDR druhého řádu pro složku závisející na $x$. V tomto případě je druhého řádu i rovnice pro složku závislou na čase.





