## Parciální derivace

### Výpočet pomocí vzorců

Vypočtěte následující parciální derivace

1. $\frac{\partial }{\partial x}(x^2y+2xy^3+x+1)$
1. $\frac{\partial }{\partial y}(x^2y+2xy^3+x+1)$
1. $\frac{\partial }{\partial x}(3x(3-x-2y))$
1. $\frac{\partial }{\partial y}(3x(3-x-2y))$
1. $\frac{\partial }{\partial x}\sqrt{1-x^2-y^2}$
1. $\frac{\partial }{\partial y}\sqrt{1-x^2-y^2}$
1. $\frac{\partial }{\partial x}\frac x{x^2+y^2}$
1. $\frac{\partial }{\partial y}\frac x{x^2+y^2}$

<div class=reseni>

1. $\frac{\partial }{\partial x}(x^2y+2xy^3+x+1)=2x\cdot y+2y^3+1+0=2xy+2y^3+1$
1. $\frac{\partial }{\partial y}(x^2y+2xy^3+x+1)=x^2+2x\cdot 3y^2+0+0=x^2+6xy$
1. $\frac{\partial }{\partial x}(3x(3-x-2y))=\pdv x (9x-3x^2-6xy)=9-3\cdot 2x-6\cdot 1\cdot y=9-6x-6y$
1. $\frac{\partial }{\partial y}(3x(3-x-2y))=\frac{\partial }{\partial y}(9x-3x^2-6xy)=0-0-6x=-6x$
1. $\pdv {x} \sqrt{1-x^2-y^2}=\pdv {x} (1-x^2-y^2)^{\frac 12}=\frac 12 (1-x^2-y^2)^{-\frac 12} (0-2x-0)=
  \frac {x}{\sqrt{1-x^2-y^2}}$
1. $\pdv {y} \sqrt{1-x^2-y^2}= \frac {y} {\sqrt{1-x^2-y^2}}$ (z předchozího výpočtu a symetrie)  
1. $\pdv {x} \frac x{x^2+y^2}=\frac{1(x^2+y^2)-x(2x+0)}{(x^2+y^2)^2}=\cdots$ (derivace podílu)
1. $\pdv{y} \frac x{x^2+y^2}=\pdv {y} x(x^2+y^2)^{-1}=x(-1)(x^2+y^2)^{-2}(0+2y)=\cdots$ (derivace konstantního násobku mocninné funkce s vnitřní složkou)

</div>

![](blizzard.jpg)

### Parciální derivace, pocitová teplota analyticky

Kanadský empirický vzorec pro pocitovou teplotu v zimě (wind chill factor) je
$$
W(T,v) = 13.12+0.6215 T-11.37 v^{0.16}+0.3965 T v^{0.16},
$$
kde $T$ je teplota
(ve stupních Celsia) a $v$ je rychlost větru (v km/hod). Teplota je $-11.0\,{}^\circ\!\text{C}$  a rychlost větru $26
\,\text{km/hod}$. Určete parciální derivace pocitové teploty podle skutečné teploty a podle rychlosti větru (včetně jednotky) a výsledky interpretujte slovně.

<div class=reseni>

Dosazením do vzorce dostáváme $W(-11,26)=-20.212\,{}^\circ\!\text{C}$. Derivováním dostáváme
$$\begin{aligned}\frac{\partial W}{\partial T}(T,v)&=0.6215+0.3965 v^{0.16},\\
\frac{\partial W}{\partial v}(T,v)&=-11.37\times 0.16 v^{-0.84}+0.3965 \times 0.16 Tv^{-0.84}
\end{aligned}
$$
a po dosazení
$$\begin{aligned}\frac{\partial W}{\partial T}(-11,26)&=1.289,\\
\frac{\partial W}{\partial v}(-11,26)&=-0.163 \,{}^\circ\!\text{C}\, /(\mathrm{km}\, \text{hod}^{-1})=-0.163 \,{}^\circ\!\text{C}\, \text{hod} \,\mathrm{km}^{-1}.
\end{aligned}
$$
Za dané teploty a rychlosti větru je pocitová teplota $-20.2$ stupňů
Celsia. Nárůst teploty o jeden stupeň způsobí nárůst pocitové teploty
přibližně o $1.3$ stupně. Tedy změna teploty se projeví na pocitové
teplotě $1.3$-násobkem, tj. každkouzměnu vnímáme o třicet procent
intenzivněji.

Podobně, zesílení větru o jeden kilometr za hodinu způsobí snížení
pocitové teploty přibližně o $0.16$ stupně.

</div>

### Pocitová teplota numericky

![](air-temperature.jpg)

1. Vypočtěte pomocí centrální diference parciální derivaci
$\frac {\partial W}{\partial v}$ pro teplotu $-15^\circ\mathrm C$ a rychlost větru $40\,\mathrm{km}\,\mathrm{hod}^{-1}$ a intepretujte výsledek slovně.
1. Pocitová teplota $W$ je lineární v proměnné $T$. Proto derivace $\frac{\partial W}{\partial T}$ nezávisí na $T$. Jak se tato skutečnost
  odrazí v tabulce?
  1. Odhadněte z tabulky, zda vliv větru klesá nebo roste s rychlostí větru. Potvrďte svou hypotézu analytickým výpočtem parciální derivace $\frac{\partial W}{\partial v}$ a vysvětlete fyzikálně.

<div class=reseni>

1.  $$\frac {\partial W}{\partial v}(T=-15,v=40)\approx\frac{-29-(-26)}{50-30}\frac{{}^\circ \mathrm C}{\mathrm{km}\,\mathrm{hod}^{-1}}=-0.15^\circ \mathrm C/(\mathrm{km}\,\mathrm{hod}^{-1})$$  Za podmínek, kde je $15$ stupňů pod nulou a vítr o rychlosti $40$ kilometrů za hodinu každé další zesílení větru o kilometr za hodinu sníží pocitovou teplotu přibližně o patnáct setin stupně.
1. Neformálně: V rámci každého řádku jsou stejně velké   skoky. Přesněji: V každém řádku je přibližně aritmetická   posloupnost, data se mění odečtením pevné konstantny. Případné  fluktuace od tohoto pravidla jsou způsobeny zaokrouhlením.
1. Pokud se díváme na data po sloupcích, s rostoucí silou větru  jsou skoky menší a proto parciálni derivace podle větru s rostoucí  rychlostí větru klesá. To potvrzuje i analytický výpočet, protože u  rychlosti je mocnina menší než jedna a ta se po zderivání změní na  zápornou mocninu a tím se změní charakter závislosti na rychlosti  větru. Fyzikálně vítr odfoukává izolační mikrovrstvu vzduchu kolem  tváře nebo těla a proto cítíme ve větším větru větší chlad. Pokud je  vítr silný, nestačí se tato mikrovstva vytvořit ani v minimální míře  a proto je jedno, jestli fouká hodně nebo ještě více.

</div>

![Zdroj: Wood handbook](wood_heat_capacity.png)

### Parciální derivace, tepelná kapacita dřeva

Vypočtěte a slovně interpretujte parciální derivaci měrné tepelné kapacity dřeva $c$ podle teploty $T$ a podle obsahu vody MC $w$ v bodě o hodnotě MC 12\% a teplotě $27^\circ\mathrm C$.

Pro obě derivace použijte dopřednou diferenci (v tabulce nejsou ekvidistatní kroky MC).

*Poznámka:* Kromě dopředné diference je možné uvažovat ještě zpětou diferenci definovanou vztahem $$\frac{f(x)-f(x-h)}{h},$$ což je vlastně dopředná diference na předhozím intervalu. Ukažte, že centrální diference je průměrem dopředné a zpětné diference.

<div class=reseni>

$$\pdv{c}{T}=\frac{1.8-1.7}{47-27}=0.005 \,\mathrm{kJ}\,\mathrm{kg}^{-1}\mathrm{K}^{-2}=5 \,\mathrm{J}\,\mathrm{kg}^{-1}\mathrm{K}^{-2}$$
Tato hodnota udává, o kolik vzroste měrná tepelná kapacita dřeva dané teploty a vlhkosti při zvýšení teploty o jeden stupeň Celsia (o jeden Kelvin).

$$\pdv{c}{w}=\frac{1.9-1.7}{20-12}=0.025 \,\mathrm{kJ}\,\mathrm{kg}^{-1}\mathrm{K}^{-1}(\text{procento MC})^{-1}=25 \,\mathrm{J}\,\mathrm{kg}^{-1}\mathrm{K}^{-1}(\text{procento MC})^{-1}$$
Tato hodnota udává, o kolik vzroste měrná tepelná kapacita dřeva dané teploty a vlhkosti při zvýšení obsahu vody o jedno procento.

Průměr centrální a zpětné diference:
$$
  \frac{\frac{f(x)-f(x-h)}{h} + \frac{f(x+h)-f(x)}{h}}{2}=
  \frac{\frac{f(x)-f(x-h)+f(x+h)-f(x)}{h}}{2}=
\frac{f(x+h)-f(x-h)}{2h}
$$

</div>

### Veličiny z rovnice vedení tepla

V případech, kdy je při tepelné výměně nutno uvažovat vedení tepla (vysoké Biotovo číslo), modelujeme změnu teploty podle rovnice vedení tepla, kterou jsme na přednášce odvodili pro jednorozměrný případ ve tvaru
$$\varrho c \frac{\partial T}{\partial t}=\frac{\partial}{\partial x}\Bigl(\lambda\frac{\partial T}{\partial x}\Bigr).$$  Typickým případem vedení tepla v jedné dimenzi je vedení tepla ve stěně. 

Uvažujme jednorozměrnou úlohu s vedením tepla. Osa $x$ směřuje doprava, teplota v bodě $x$ a čase $t$ je $T(x,t)$ ve stupních Celsia. Tok tepla v čase $t$ a v bodě $x$ je $q(x,t)$ v joulech za sekundu. Kladný tok je ve směru osy $x$.
Podle Fourierova zákona je $$q=-\lambda \frac{\partial T}{\partial x}.$$

Tyč má teplotu $0\,^{\circ}\mathrm{C}$, pravý konec udržujeme na této teplotě, levý konec ohříváme na $20\,^{\circ}\mathrm{C}$ a udržujeme na této teplotě. Ve zbytku tyče (stěny) se postupně nastolí rovnováha vlivem vedení tepla.

Vyjádřete následující veličiny a určete jejich znaménko.

1. Rychlost, s jakou v daném místě a čase roste teplota jako funkce času.
1. Rychlost, s jakou v daném místě a čase roste teplota jako funkce polohy, tj. jak rychle  roste teplota směrem doprava.
1. Rychlost, jak rychle se klesá teplota jako funkce polohy, tj. směrem doprava.
1. Rychlost, se kterou roste (směrem doprava) tok tepla jako funkce polohy.
1. Rychlost, se kterou klesá (směrem doprava) tok tepla jako funkce polohy.

<div class=reseni>

1. Rychlost, s jakou v daném místě a čase roste teplota jako funkce času je $\frac {\partial T}{\partial t}$ a tato derivace je v každém bodě kladná, protože tyč se ohřívá. Po čase se asi ustálí rovnováha a derivace bude nulová, teplota se přestaně měnit. Měříme ve stupních celsia za sekundu.
  $\left[\frac {\partial T}{\partial t}\right]={}^\circ\mathrm{C}\,\mathrm{s}^{-1}$
1. Rychlost, s jakou v daném místě a čase roste teplota jako funkce polohy, tj. jak rychle se roste teplota směrem doprava, je $\frac {\partial T}{\partial x}$ a tato derivace je záporná, protože vlevo je horký konec a teplota směrem doprava klesá. Měříme ve stupních celsia na metr.
    $\left[\frac {\partial T}{\partial x}\right]={}^\circ\mathrm{C}\,\mathrm{m}^{-1}$
1. Rychlost, jak rychle se klesá teplota jako funkce polohy, tj. směrem doprava, je $-\frac {\partial T}{\partial x}$ a tato veličina je kladná, protože vlevo je horký konec a teplota směrem doprava opravdu klesá. Měříme ve stupních celsia na metr.
        $\left[-\frac {\partial T}{\partial x}\right]={}^\circ\mathrm{C}\,\mathrm{m}^{-1}$
1. Rychlost, se kterou roste (směrem doprava) tok tepla jako funkce polohy je $\frac {\partial q}{\partial x}$. Teplo teče doprava a přitom se spotřebovává, protože se ohřívá tyč. Proto tok klesá a parciální derivace je záporná.
  Měříme v joulech za sekundu na metr.
          $\left[\frac {\partial q}{\partial x}\right]=\mathrm{J}\,\mathrm{s}^{-1}\,\mathrm{m}^{-1}$
1. Rychlost, se kterou klesá (směrem doprava) tok tepla jako funkce polohy je $-\frac {\partial q}{\partial x}$ a tato veličina je kladná, což plyne z předchozího bodu a z toho, že jsme změnili znaménko.
  Měříme v joulech za sekundu na metr.
            $\left[-\frac {\partial q}{\partial x}\right]=\mathrm{J}\,\mathrm{s}^{-1}\,\mathrm{m}^{-1}$ Tato veličina udává, kolik tepla se za jednotku času ubude v toku na metrovém úseku tyče. Ze zákona zachování energie se toto teplo nemůže ``ztratit'', ale použije se na zvýšení teploty, což je vyjádřeno právě v rovnici vedení tepla.

</div>

### Okrajové podmínky pro rovnici vedení tepla

K modelu stěny pomocí rovnice vedení tepla je ještě nutné přidat podmínky související s počátečním stavem (počáteční podmínky) a s chováním na okrajích (okrajové podmínky).

Nechť stěna je na intervalu $x\in[0,L]$, $x=0$ je vnitřní okraj a $x=L$ je vnější okraj. Výraz $-k\frac{\partial T}{\partial x}$ udává tok tepla ve směru osy $x$. Tok ve směru osy $x$ má kladné znaménko. Naformulujte okrajové podmínky v následujících scénářích.

1. Z venku dokonale izolovaná stěna. Na hranici $x=L$ nedochází k toku tepla.
1. Vnitřní část stěny je udržovaná na konstantní teplotě $T=23^\circ \mathrm C$.
1. Stěna je zvenku osvětlená a zahřívaná Sluncem. Na vnější hranici je konstantní tok tepla směrem do stěny.
1. Stěna je zvenku ochlazována prouděním vzduchu. Tok tepla mezi stěnou a okolím je úměrný rozdílu teplot stěny a okolí.
1. Stěna je zevnitř ohřívána prouděním vzduchu od radiátorů. Tok tepla mezi stěnou a okolím je úměrný rozdílu teplot stěny a okolí.

_Zpracováno podle Cengel: Mass and heat transfer._

<div class=reseni>

1. $\frac{\partial T}{\partial x}(L)=0$
1. $T(0)=23$
1. $-k\frac{\partial T}{\partial x}(L)=-Q$, kde $Q$ je teplo za jednotku času dodané ze Slunce. Jedná se výkon Slunce dopadající na stěnu vynásobený koeficientem absorbce, protože část tepelného výkonu se odráží. Záporné znaménko je proto, že teplo teče do stěny, tj. proti směru osy $x$.
1. $-k\frac{\partial T}{\partial x}(L)=h(T-T_{\text{okolí}})$, kde $h$ je koeficient přestupu tepla.
1. $-k\frac{\partial T}{\partial x}(0)=h(T_{\text{místnost}}-T)$, kde $h$ je koeficient přestupu tepla.

Všimněte si, že poslední dvě podmínky se liší znaménkem u veličiny $T$. To proto, že v jednom případě je kladný směr toku tepla do materiálu a jednou z materiálu. Pokud chceme mít popis jednotný, nebo nezávislý na zvolené souřadné soustavě, formulujeme podmínky pro tok tepla ven z materiálu. Tento tok získáme tak, že tok tepla vynásobíme skalárně s jednotkovým vektorem směřujícím ven z materiálu kolmo na jeho povrch. V tomto případě by pro tok ze stěny do místnosti bylo $k\frac{\partial T}{\partial x}(0)=h(T-T_{\text{místnost}})$. Tento tok by byl záporný, protože ve skutečnosti teplo uniká z místnosti stěnou ven.

</div>

## Gradient

![](blizzard.jpg)

### Linearizace pocitové teploty

Pocitová teplota $W$ z minulého cvičení má v bodě odpovídajícím teplotě $T=-11{}^\circ\mathrm C$ a rcyhlosti větru $v=26\,\mathrm {km}\,\mathrm{hod}^{-1}$ má hodnotu $$W=-20.2 ^\circ\mathrm C$$ a parciální derivace $$\pdv{W}{v}=-0.163 ^\circ\mathrm C\, \mathrm {hod}\,\mathrm{km}^{-1}$$ a
$$\pdv{W}{T}=1.289.$$ Najděte pomocí lineární aproximace vzorec pro pocitovou teplotu v okolí tohoto bodu.

<div class=reseni>

Přímým použitím vzorce pro lineární aproximaci dostáváme
$$
W=-20.2+1.289(T-(-11))-0.163(v-26)=-20.2+1.289(T+11)-0.163(v-26),
$$
přičemž všechny veličiny dostazujeme v jednotkách SI (stupně Celsia a kilometry za hodinu).

</div>

### Parciální derivace, gradient

Určete gradient funkcí $z=ax^2y-2xy^2$ a $h=\frac {ax}{y^2}+5x^3y^2$, kde $a\in\mathbb R$ je reálný parametr.

<div class=reseni>

$$
\begin{aligned}
  \pdv{z}{x} &= 2axy-2y^2\\
  \pdv{z}{y} &= ax^2-4xy\\
  \nabla z &= (2axy-2y^2, ax^2-4xy) = (2axy-2y^2)\vec \imath + (ax^2-4xy)\vec \jmath\\
  \pdv{h}{x} &= \frac a{y^2}+15x^2y^2\\
  \pdv{h}{y} &= ax(-2)y^{-3}+10x^3y=-\frac{2ax}{y^3}+10x^3y\\
  \nabla h &= \left(\frac a{y^2}+15x^2y^2, -\frac{2ax}{y^3}+10x^3y\right) = \left(\frac a{y^2}+15x^2y^2\right)\vec \imath + \left(-\frac{2ax}{y^3}+10x^3y\right)\vec \jmath
  \end{aligned}
$$

</div>

### Gradient funkce s vrstevnicemi ve tvaru kružnic

Určete gradient funkce $z=x^2+y^2$ a zkontrolujte, že je v každém bodě kolmý ke kružnici se středem v počátku. Využijte toho, že spojnice bodu na kružnici se středem kružnice je kolmá k této kružnici. 

<div class=reseni>
$$\begin{aligned}
  \pdv{z}{x} &= 2x\\
  \pdv{z}{y} &= 2y\\
  \nabla z &= (2x, 2y) = 2x\vec \imath + 2y\vec \jmath
\end{aligned}$$
Vektor $(2x,2y)$ v bodě $(x,y)$ míří směrem od počátku, tj ve směru spojnice se středem a tedy je kolmý k vrstevnici.
</div>

### Gradient funkce s paprskovitými vrstevnicemi

Určete gradient funkce $z=\mathop{\mathrm{arctg}} \frac yx$ a zkontrolujte, že je v každém bodě tečný ke kružnici se středem v počátku. Využijte toho, že tečna je kolmá na poloměr.

<div class=reseni>

$$
\begin{aligned}
  \pdv{z}{x} &= \frac1{1+\frac {y^2}{x^2}}y\frac {(-1)}{x^2}=-\frac{y}{x^2+y^2}\\
  \pdv{z}{y} &= \frac1{1+\frac {y^2}{x^2}}\frac 1x=\frac{x}{x^2+y^2}\\
  \nabla z &=  \left(-\frac{y}{x^2+y^2},\frac{x}{x^2+y^2}\right)= \frac{1}{x^2+y^2} (-y,x)
  \end{aligned}
$$

Vektor $(-y,x)$ v bodě $(x,y)$ je kolmý k vektoru $(x,y)$ a míří směrem od počátku, tj. k poloměru. Proto je tečný ke kružnici.
</div>

### Tečná rovina atd.

Pro funkci $f(x,y)=x^2+\frac x{y^2}-6$ najděte

1. gradient, 
1. gradient v bodě $(2,1)$,
1. lineární aproximaci v bodě $(2,1)$,
1. tečnou rovinu v bodě $(2,1)$,
1. rovnici vrstevnice bodem $(2,1)$ a rovnici tečny k vrstevnici tímto bodem,
1. explicitní vyjádření funkce dané v okolí bodu $(2,1)$ implicitně rovnicí $f(x,y)=0$,
1. lineární aproximace v okolí bodu $x=2$ pro funkci získanou v předchozím bodu.

<div class=reseni>

1. $\nabla f=\left(2x+\frac 1{y^2},-2\frac x{y^3}\right)$
1. $\nabla f(2,1)=(5,-4)$
1. $f(x,y)\approx 5(x-2)-4(y-1)$
1. $z= 5(x-2)-4(y-1)$
1. Rovnice vrstevnice je $$x^2+\frac x{y^2}-6=0$$
  a tečna $$5(x-2)-4(y-1)=0,$$ tj. $$5x-4y-6=0.$$
1. Postupnými úpravami a výběrem správného znaménka po vyřešení kvadratické rovnice vzhledem k $y$ dostáváme
  $$
  \begin{aligned}
    x^2+\frac x{y^2}-6&=0\\
        \frac x{y^2}&=6-x^2\\
        y^2&=\frac{x}{6-x^2}\\
        y&=\sqrt{\frac{x}{6-x^2}}\\
  \end{aligned}
$$
1. Z rovnice tečny k vrstevnici $$5(x-2)-4(y-1)=0$$
  dostáváme $$y=1+\frac 54 (x-2)$$
  a proto
  $$\sqrt{\frac{x}{6-x^2}}\approx 1+\frac 54 (x-2)$$ v okolí $x=2$.

</div>

### Linearizace vektorové funkce, Jacobiho matice

Jacobiho matice se používá k linearizaci vektorových funkcí, které
mají na vstupu i na výstupu vektor. Jsou to matice, kde gradienty
jednotlivých komponent vektorové funkce jsou zapsány do řádků matice.

Najděte Jacobiho matici pro funkci $$\vec F(x,y)=(x^2+xy+6y)\vec i + e^{3x}\vec j$$ a poté hodnotu této matice v bodě $(0,0)$.

<div class=reseni>

Platí
$$\begin{aligned}
  \frac{\partial }{\partial x}\left(x^2 +xy+6y\right) &=2x+y\\
  \frac{\partial }{\partial y}\left(x^2 +xy+6y\right) &=x+6\\
  \frac{\partial }{\partial x}\left(e^{3x}\right) &=3e^{3x}\\
  \frac{\partial }{\partial y}\left(e^{3x}\right) &=0\\
\end{aligned}$$
a proto má Jacobiho matice tvar
\begin{equation*}
  J(x,y)=
  \begin{pmatrix}
    2x+y & x+6\\ 3e^{3x} & 0
  \end{pmatrix}.
\end{equation*}
V bodě $(0,0)$ potom 
\begin{equation*}
  J(0,0)=
  \begin{pmatrix}
    0 & 6\\ 3 & 0
  \end{pmatrix}.
\end{equation*}

</div>

![Zdroj: Wood handbook](anatomicke_smery_dreva.png)

### Parciální derivace, gradient a násobení matic

Vypočtěte gradient funkce $$T=10-\sqrt{x^2+y^2}.$$ Ukažte, že vrstevnice
této funkce jsou kružnice se středem v počátku, nakreslete obrázek s
těmito vrstevnicemi a vyznačte do tohoto obrázku gradienty v bodech
$A=(0,1)$, $B=(1,0)$ a $C=(1,1)$

Uvažujte součinitel tepelné vodivosti $$\lambda =
\begin{pmatrix}
  2&0\\0&3
\end{pmatrix}$$
a vypočtěte tok tepla v bodech $A$, $B$, $C$. Porovnejte směr tohoto toku se směrem gradientu a vysvětlete svá pozorování. Snaží se matice usměrnit teplo do  směru osy $x$ nebo do  směru osy $y$? Odpovídá situace spíše dřevu s podélným směrem v ose $x$ nebo v ose $y$?

<div class=reseni>

Platí $$\pdv{T}{x}=-\frac 12 (x^2+y^2)^{-\frac 12}(2x)=-\frac{x}{\sqrt{x^2+y^2}}$$
a ze symetrie 
$$\pdv{T}{y}=-\frac{y}{\sqrt{x^2+y^2}}.$$
Odsud $$\nabla T=\qty(-\frac{x}{\sqrt{x^2+y^2}},-\frac{y}{\sqrt{x^2+y^2}})^T
=
-\frac 1{\sqrt{x^2+y^2}}(x,y)^T.$$
Tok tepla je
$$\vec q=-\lambda \nabla T=\frac 1{\sqrt{x^2+y^2}}\begin{pmatrix}
  2&0\\0&3
\end{pmatrix}
\begin{pmatrix}
  x\\y
\end{pmatrix}
=\frac 1{\sqrt{x^2+y^2}} \begin{pmatrix}
  2x\\3y
\end{pmatrix}
$$
Dosazením dostáváme $\vec q(A)=(0,3)^T$, $\vec q(B)=(2,0)^T$, $\vec q(C)=\frac 1{\sqrt{2}}(2,3)^T$. Porovnáním s gradientem $\nabla T(A)=-(0,1)^T$, $\nabla T(B)=-(1,0)^T$ a $\nabla T(C)=-\frac 1{\sqrt 2}(1,1)^T$ vidíme, že v bodech $A$  a $B$ je tok proti směru gradientu, v bodě $C$ se tok stáčí do směru osy $y$. Protože ve ose $y$ má dřevo větší vodivost, jedná se o podélný směr. To je ale vlastně vidět už ze zadané matice.

</div>

## Divergence, rovnice vedení tepla

### Divegrence vektorového pole

1. Vypočtěte divergenci vektorového pole
  $$\vec F=x^2y\vec \imath + (x+y^2)\vec \jmath.$$
1. Zakreslete do obrázku směr toku vektorového pole v bodě $(2,1)$. 
1. Vypočtěte divergenci vektorového pole v bodě $(2,1)$ a podle toho, zda je kladná nebo záporná rozhodněte, zda tok v daném bodě sílí nebo slábne.
1. Předpokládejme, že dané vektorové pole reprezentuje stacionární tok. Je v bodě $(2,1)$ zdroj nebo spotřebič?

<div class=reseni>

1. $\nabla \cdot \vec F=\pdv{x}(x^2y)+\pdv{y}(x+y^2)
=2xy+(0+2y)=2y(x+1)$
1. $\vec F(2,1)=2^2\cdot 1\vec \cdot \imath + (2+1^2)\vec \jmath=4\vec\imath+3\vec\jmath=(4,3)$, tj. vektorové pole teče směrem doprava nahoru směrem daným směrnicí $0.75$, tj. pod úhlem menším než $45^\circ$.
1. $\nabla\cdot\vec F(2,1)=2\cdot 1 \cdot(2+1)=6>0$. Divergence je kladná a proto se tok zahušťuje.
1. Zdroj (kladná divergence).

</div>

### Divegrence vektorového pole s parametrem

1. Vypočtěte divergenci vektorového pole
  $$\vec F=ax^3y^2\vec \imath + 3x^2y\vec \jmath,$$ kde
  $a\in\mathbb R$ je reálný parametr.
1. Určete hodnotu parametru $a$ tak, aby pole bylo v bodě $(-1,2)$ nezřídlové, tj. aby mělo nulovou divergenci v bodě $(-1,2)$.

<div class=reseni>

1. $\nabla \cdot \vec F=\pdv{x}(ax^3y^2)+\pdv{y}(3x^2y)
=3ax^2y^2+3x^2=3x^2(ay^2+1)$
1. $\nabla \cdot \vec F (-1,2)=3(-1)^2(a\cdot 2^2+1)=3(4a+1)$ a $\nabla \cdot \vec F (-1,2)=0$ pokud $3(4a+1)=0$, tj. $a=-\frac 14$.

</div>

![](drevo_textura.jpg)

### Rovnice vedení tepla v dvourozměrném materiálu

Teplota ve dvourozměrné desce pro $0\leq x\leq 10$ a $0\leq y\leq 10$ zachycené v určitém okamžiku termokamerou je popsána rovnicí
  $$T(x,y)=(2x-y)^2+x^4.$$
  Rozměry jsou v centimetrech, teplota ve stupních Celsia. (Formálně to nevychází, ale ke každému členu můžeme dodat konstantu, která jeho rozměr opraví. Pro jednoduchost tuto komplikaci vynecháme.)

1. Vypočtěte gradient $\nabla T$  a tok tepla $-k \cdot \nabla T.$
Součinitel tepelné vodivosti (v jednotkách kompatibilních se zadáním) je $k=
  \begin{pmatrix}
    4 & 1\\1&6
  \end{pmatrix}.$ 
1. Určete, zda na levém okraji desky teče teplo dovnitř desky nebo z desky ven.
1. Vypočtěte divergenci toku tepla, tj. $\nabla\cdot(-k \cdot \nabla T).$
1. V desce nejsou zdroje tepla. Ochlazuje se deska uprostřed, nebo otepluje?

<div class=reseni>

1. Gradient je vektor složený z parciálních derivací. $$\nabla T=\qty(
  4(2x-y)+4x^3,-2(2x-y))^T$$ Tok je tenzor vodivosti maticově vynásobený s gradientem teploty a faktorem $(-1)$.
  $$-k\cdot \nabla T=-
  \begin{pmatrix}
    4&1\\1&6
  \end{pmatrix}
  \begin{pmatrix}
    4(2x-y)+4x^3\\-2(2x-y)
  \end{pmatrix}
  =-
  \begin{pmatrix}
    14(2x- y)+16x^3\\-8(2x- y)+4x^3
  \end{pmatrix}
$$
1. Do vztahu pro tok dosadíme rovnici levého okraje desky, tj. $x=0$.
  $$-k\cdot \nabla T (x=0)=
  \begin{pmatrix}
    14y\\-8y
  \end{pmatrix}
  $$
  Na levém okraji desky je $y>0$ a proto $14y>0$. Tok míří doprava a teplo teče na tomto okraji do desky.
1.  Vypočteme divergenci toku určeného v prvním bodě. $$
  \begin{aligned}
\nabla \cdot (-k\cdot \nabla T )&=\pdv{x}(-14(2x- y)-16x^3)+\pdv{y}(8(2x- y)-4x^3)\\&=-48x^2-28-8\\&=-48x^2-36
\end{aligned}
$$
1. Do vztahu pro diveregenci dosadíme bod, který nás zajímá. $$\nabla \cdot (-k\cdot \nabla T )(x=5,y=5)=-1236$$ Tok tepla se zmenšuje a protože jde o stav bez zdrojů, teplo se v daném místě akumuluje a deska se proto otepluje. Z rovnice vedení tepla
  $$\rho c\pdv{T}{t}=\nabla\cdot(k \cdot \nabla T)$$
  plyne v daném bodě
  $$\rho c\pdv{T}{t}=1236$$
  a můžeme dokonce odhadnout, jak rychle teplota roste.

</div>

<!--
% var('x,y')
% k=matrix([[5,1],[1,4]])
% T(x,y)=(x+2*y)^2+x^3
% show(T.gradient())
% show(-k*T.gradient())
% show(-k*T.gradient()(x=0))
% show((-k*T.gradient())[0].diff(x)+(-k*T.gradient())[1].diff(y))
-->

### Vedení tepla v různých materiálech

1. Zapište rovnici vedení tepla v trojrozměrném izotropním a v
  trojrozměrném ortotropním materiálu. Ve druhém případě volte osy ve
  směru vlastních vektorů.
1. Napište, jak je možné zjednodušit rovnice z předchozího bodu,
  pokud jsou materiálové konstanty nezávislé na poloze (homogenní
  materiál) a na teplotě (lineární materiál).

<div class=reseni>

1. Izotropní: $\varrho c \pdv{T}{t} = \pdv{x}(k\pdv{T}{x})+\pdv{y}(k\pdv{T}{y})+\pdv{z}(k\pdv{T}{z})$

    Ortotropní: $\varrho c \pdv{T}{t} = \pdv{x}(k_x\pdv{T}{x})+\pdv{y}(k_y\pdv{T}{y})+\pdv{z}(k_z\pdv{T}{z})$
1. Izotropní: $\varrho c \pdv{T}{t} = k\left(\pdv[2]{T}{x} + \pdv[2]{T}{y} + \pdv[2]{T}{z}\right)$

     Ortotropní: $\varrho c \pdv{T}{t} = k_x\pdv[2]{T}{x}+k_y\pdv[2]{T}{y}+k_z\pdv[2]{T}{z}$

</div>

## Rotace, kmenová funkce gradientu

### Rotace vektorového pole v rovině

Vypočtěte rotaci funkce $\vec F=xy^2\vec \imath + 2xy\vec\jmath$.

<div class=reseni>

 $$
 \begin{aligned}
\curl \vec F=
 \begin{vmatrix}
   \vec\imath & \vec \jmath & \vec k\\
   \pdv{x} & \pdv{y} & \pdv{z} \\
   xy^2 & 2xy & 0
 \end{vmatrix}
 &=\vec k\qty({\pdv x{2xy}-\pdv y {xy^2}})\\&
 =\vec k(2y-2xy)\\&=2y(1-x)\vec k
\end{aligned}
 $$

</div>

### Rotace vektorového pole v prostoru

Vypočtěte rotaci funkce $\vec F=xyz\vec \imath + 5x^2y\vec\jmath-3x^2z\vec k$.

<div class=reseni>

 $$
 \begin{aligned}
\curl \vec F&=
 \begin{vmatrix}
   \vec\imath & \vec \jmath & \vec k\\[4pt]
   \pdv{x} & \pdv{y} & \pdv{z} \\[10pt]
   xyz& 5x^2y & -3x^2z
 \end{vmatrix}\\
 &=
\vec \imath \ \qty[\pdv x{-3x^2z}-\pdv z{5x^2y}]
 +\vec \jmath \ \qty[\pdv z{xyz}-\pdv x{-3x^2z}] 
 +\vec k\ \qty({\pdv x{5x^2y}-\pdv y{xyz}})\\
 &=(xy+6xz)\vec\jmath + (10xy-xz)\vec k
\\&=x(y+6z)\vec\jmath + x(10y-z)\vec k
\end{aligned}
 $$

</div>

### Divergence a rotace 2D funkce s parametrem
Vypočtěte divergenci a rotaci funkce $\vec F=ax^2y^3\vec \imath + (x^2+y)\vec\jmath$.

<div class=reseni>

$$\nabla\cdot \vec F=\pdv{x}(ax^2y^3)+\pdv{y}(x^2+y)=2axy^3+1$$

 $$\curl \vec F=
 \begin{vmatrix}
   \vec\imath & \vec \jmath & \vec k\\
   \pdv{x} & \pdv{y} & \pdv{z} \\
   ax^2y^3 & x^2+y & 0
 \end{vmatrix}
 =\vec k(2x-3ax^2y^2)
 $$

</div>

### Nalezení kmenové funkce 1/3

Pro vektorové pole $$\frac 45 x y^3\vec \imath + \frac 65x^2y^2\vec\jmath$$ najděte funkci $\varphi$ tak, že zadané vektorové pole je rovno gradientu $\nabla \varphi.$

<div class=reseni>

Platí $\pdv {\varphi}{x}=\frac 45 xy^3$ a $\pdv{\varphi}{y}=\frac 65 x^2y^2$.

Odsud
$$\varphi =\int \pdv{\varphi}{x} \,\mathrm dx=\int \frac 45 xy^3 \,\mathrm dx
=\frac 45 \frac {x^2}{2}y^3=\frac 25 x^2y^3+C_1(y)$$
a
$$\varphi =\int \pdv{\varphi}{y} \,\mathrm dy=\int \frac 65 x^2y^2 \,\mathrm dy
=\frac 65 {x^2}\frac{y^3}3=\frac 25 x^2y^3+C_2(x).$$
Porovnáním musí být $C_1(y)=C_2(x)=C\in\mathbb R$ a
$$\varphi(x,y)=\frac 25 x^2y^3+C,\quad C\in\mathbb R.$$

</div>

### Nalezení kmenové funkce 2/3

Pro vektorové pole $$\left(x^2+\frac 45 x y^3\right)\vec \imath + \left(\frac 65x^2y^2+y\right)\vec\jmath$$ najděte funkci $\varphi$ tak, že zadané vektorové pole je rovno gradientu $\nabla \varphi.$

<div class=reseni>

Platí $\pdv {\varphi}{x}=x^2+\frac 45 xy^3$ a $\pdv{\varphi}{y}=\frac 65 x^2y^2+y$.

Odsud
$$\varphi =\int \pdv{\varphi}{x} \,\mathrm dx=\int x^2+\frac 45 xy^3 \,\mathrm dx
=\frac {x^3}3+\frac 45 \frac {x^2}{2}y^3=\frac {x^3}3+\frac 25 x^2y^3+C_1(y)$$
a
$$\varphi =\int \pdv{\varphi}{y} \,\mathrm dy=\int \frac 65 x^2y^2 +y \,\mathrm dy
=\frac 65 {x^2}\frac{y^3}{3}+\frac 12 y^2=\frac 25 x^2y^3+\frac 12 y^2 + C_2(x).$$
Porovnáním musí být $C_1(y)=\frac 12 y^2+C$ a $C_2(x)=\frac {x^3}3+C$, $C\in\mathbb R$ a
$$\varphi(x,y)=\frac {1}{3}x^3+\frac 25 x^2y^3+\frac 12 y^2+C,\quad C\in\mathbb R.$$

</div>

### Nalezení kmenové funkce 3/3

Pro vektorové pole $$\left(y+\frac 45 x y^3\right)\vec \imath + \left(\frac 65x^2y^2+x^2\right)\vec\jmath$$ najděte funkci $\varphi$ tak, že zadané vektorové pole je rovno gradientu $\nabla \varphi.$

<div class=reseni>

Platí $\pdv {\varphi}{x}=y+\frac 45 xy^3$ a $\pdv{\varphi}{y}=\frac 65 x^2y^2+x^2$.

Odsud
$$\varphi =\int \pdv{\varphi}{x} \,\mathrm dx=\int y+\frac 45 xy^3 \,\mathrm dx
=xy+\frac 45 \frac {x^2}{2}y^3=xy+\frac 25 x^2y^3+C_1(y)$$
a
$$\varphi =\int \pdv{\varphi}{y} \,\mathrm dy=\int \frac 65 x^2y^2 +x^2 \,\mathrm dy
=\frac 25 {x^2}\frac{y^3}3+x^2y=\frac 25 x^2y^3+x^2y+ C_2(x).$$
Porovnáním musí být
$$xy+C_1(y)=x^2y+C_2(x),$$
což není možné splnit.

Ověříme, že parciální derivace
$\pdv {y} \qty(y+\frac 45 xy^3)$ a $\pdv{x}\qty(\frac 65 x^2y^2+x^2)$ jsou různé.
Platí
$$\pdv {y} \qty(y+\frac 45 xy^3)=1+\frac{12}5xy^2$$
a
$$\pdv{x}\qty(\frac 65 x^2y^2+x^2)=\frac {12}5 xy^2+2x$$
a protože obě parciální derivace jsou různé, kmenová funkce neexistuje.

</div>

## Křivkové integrály

### Křivkový integrál druhého druhu po třech různých křivkách

Vypočtěte $$\int_{C_i} \vec F \mathrm d\vec r$$ pro vektorové pole $$\vec F=-y\vec \imath + x\vec\jmath$$ po třech různých křivkách $C_1$, $C_2$ a $C_3$.
$$\begin{aligned}
  C_1&\colon \vec r=\cos(t)\vec \imath + \sin (t)\vec\jmath, \quad t\in\qty[0,\frac\pi 2]\\
  C_2&\colon \vec r=(1-t)\vec \imath + t\vec\jmath, \quad t\in\qty[0,1]\\
  C_3&\colon \vec r=(1-t^2)\vec \imath + t\vec\jmath, \quad t\in\qty[0,1]
\end{aligned}$$
Tj. počítáme
$$\int_{C_i} -y\,\mathrm dx + x\,\mathrm dy$$
po třech zadaných křivkách $C_1$, $C_2$ a $C_3$.

<div class=reseni>

Vektory budeme pro stručnost zapisovat jako uspořádané dvojice.

**Křivka $C_1$.**
Derivací křivky $\vec r=(\cos(t),\sin(t))$ podle $t$ dostáváme
$$\frac{\mathrm d\vec r}{\mathrm dt}=(-\sin (t),\cos (t)).$$
Rovnice vektorového pole podél křivky má tvar
$$\vec F(\vec r(t))=(-\sin t,\cos t).$$
Skalárním součinem dostáváme
$$\vec F \frac{\mathrm d\vec r}{\mathrm dt}=
(-\sin t,\cos t)\cdot (-\sin (t),\cos (t)) = \sin^2 t+\cos^2 t =1.
$$
Odsud formálně $$\vec F\mathrm d\vec r=1\mathrm dt$$
a integrál má tvar
$$\int_C\vec F\mathrm d\vec r=\int_0^{\frac \pi 2}1\,\mathrm dt=\frac \pi 2,$$
kde poslední Riemannův integrál není nutné počítat, protože integrál z jedničky je délka intervalu, přes který se integruje.

**Křivka $C_2$.**
Derivací křivky $\vec r=(1-t,t)$ podle $t$ dostáváme
$$\frac{\mathrm d\vec r}{\mathrm dt}=(-1,1).$$
Rovnice vektorového pole podél křivky má tvar
$$\vec F(\vec r(t))=(-t,1-t).$$
Skalárním součinem dostáváme
$$\vec F \frac{\mathrm d\vec r}{\mathrm dt}=
(-t,1- t)\cdot (-1,1) = (-t)(-1)+(1-t)\cdot 1 =1.
$$
Odsud formálně $$\vec F\mathrm d\vec r=1\mathrm dt$$
a integrál má tvar
$$\int_C\vec F\mathrm d\vec r=\int_0^{1}1\,\mathrm dt=1,$$
kde ani v tomto případě poslední Riemannův integrál není nutné počítat, protože integrál z jedničky je délka intervalu, přes který se integruje.

**Křivka $C_3$.**
Derivací křivky $\vec r=(1-t^2,t)$ podle $t$ dostáváme
$$\frac{\mathrm d\vec r}{\mathrm dt}=(-2t,1).$$
Rovnice vektorového pole podél křivky má tvar
$$\vec F(\vec r(t))=(-t,1-t^2).$$
Skalárním součinem dostáváme
$$\vec F \frac{\mathrm d\vec r}{\mathrm dt}=
(-t,1- t^2)\cdot (-2t,1) = (-t)(-2t)+(1-t^2)\cdot 1 =t^2+1.
$$
Odsud formálně $$\vec F\mathrm d\vec r=(t^2+1)\mathrm dt$$
a integrál má tvar
$$\int_C\vec F\mathrm d\vec r=\int_0^{1}(t^2+1)\,\mathrm dt=
\qty[\frac 13 t^3 + t]_0^1 = \frac 13 + 1 - 0 =\frac 43.
$$

![vlastní](priklad_5_1_prace.png)

**Interpretace jako práce, srovnání.**

Všechny křivky jsou z bodu $[1,0]$ do bodu $[0,1]$. Nejblíže k počátku je úsečka $C_2$, nejdále je čvrtkružnice $C_1$, křivka $C_2$ je mezi nimi.

Integrál fyzikálně znamená práci vektorového pole $(-y,x)$ po zadané křivce. Toto vektorové pole míří po kružnicích okolo počátku proti směru hodinových ručiček. Délka vektoru je rovna vzdálenosti od počátku.

Křivka $C_1$ je nejdále od počátku a vektorové pole je na ní nejsilnější. Navíc v každém bodě je síla ve směru křivky a proto se projeví ve výsledném příspěvku bez redukování. Díky tomu můžeme integrál po kružnici počítat stejně jako práci na přímce, tj. součinem délky  křivky $\frac \pi 2$ a velikosti síly $|\vec F|=1$. Po dalších křivkách je síla menší (křivky jdou blíže ke středu) a navíc se neuplatní celá velikost síly, protože síla svírá s křivkou nenulový úhel a při práci se projeví pouze tečná komponenta.

![vlastní](priklad_5_1.png)

<!--
%https://sagecell.sagemath.org/?z=eJx1kMFuwjAQRO-R8g8rgRRHMW3snH3iB3LgRmgUEkMNxo5sQ5u_r01SlbbhtCPN7hvN3hqDkiFJ40hcem0cqOulH-LIEXZXL1Io2zctRzkGhXrxSlNM8twfODqzQiZzTdh222qLRIqtUH7s4KANCBAKHNn5Deo3yEpg8ejQ4BSj80b_eyVhUlhX91I7tCYYgjhpoXjHNubKMUh-5KqrZbPnkplkua5J1WqpFSA_LThc2UBLl0laxVH2gKMzuHBqWGJ4l8yx6chGZOXwHLJ4jjwaztUstPiB-h_csXHku1MWWPWNt06b-iC47BD6xEOKwY8ckyCGSUwpe9m053Bv3_UHKklW-paN7T2jNo0TmpE7PI4WZTHHHzKK8zFhRb4jJvWriccsxpCsLP5mYHDCSe77bfQZei05LCsfBCc2JfiSX8c_x8Q=&lang=sage&interacts=eJyLjgUAARUAuQ==
-->

**Interpretace jako tok, srovnání.**

Všechny křivky jsou z bodu $[1,0]$ do bodu $[0,1]$. Nejblíže k počátku je úsečka $C_2$, nejdále je čvrtkružnice $C_1$, část paraboly $C_2$ je mezi nimi.

Integrál fyzikálně znamená tok vektorového pole $(x,y)$ křivkou. Toto vektorové pole míří směrem z počátku a zesiluje směrem od počátku, protože délka vektoru je rovna vzdálenosti od počátku.

Proto je hodnota po křivce nejblíže počátku nejmenší atd. Na křivce $C_1$ (kružnice) je tok v každém bodě kolmý ke křivce a stejně velký a proto je celkový tok snadné určit jako součin velikosti vektorového pole na křivce ($|\vec F|=1$) a délky křivky $\frac \pi 2$.

</div>

### Křivkový integrál druhého druhu po parabole

Vypočtěte $$\int_{C} \vec F \mathrm d\vec r$$ pro vektorové pole $$\vec F=x^2\vec \imath + (x+y)\vec\jmath$$ po části paraboly
$$\begin{aligned}
  C&\colon \vec r=t\vec \imath + t^2\vec\jmath, \quad t\in\qty[0,1]
\end{aligned}$$
tj. počítáme
$$\int_C x^2\,\mathrm dx + (x+y)\,\mathrm dy$$
po zadané křivce $C$.

<div class=reseni>

Vektory budeme pro stručnost zapisovat jako uspořádané dvojice.

Derivací křivky $\vec r=(t,t^2)$ podle $t$ dostáváme
$$\frac{\mathrm d\vec r}{\mathrm dt}=(1,2t).$$
Rovnice vektorového pole podél křivky má tvar
$$\vec F(\vec r(t))=(t^2,t+t^2).$$
Skalárním součinem dostáváme
$$\vec F \frac{\mathrm d\vec r}{\mathrm dt}=
(1,2t)\cdot (t^2,t+t^2) = 1\cdot t^2+2t\cdot(t+t^2)=3t^2+2t^3.
$$
Odsud formálně $$\vec F\mathrm d\vec r=(3t^2+2t^3)\mathrm dt$$
a integrál má tvar
$$\int_C\vec F\mathrm d\vec r=\int_0^{1}(3t^2+2t^3)\,\mathrm dt
=\qty[t^3+\frac 12 t^4]_0^1=1+\frac 12 - 0 = \frac 32.$$

</div>

### Křivkový integrál druhého druhu po kubické parabole

Vypočtěte $$\int_{C} \vec F \mathrm d\vec r$$ pro vektorové pole $$\vec F=2y\vec \imath + x^2y\vec\jmath$$ po části kubické paraboly
$$\begin{aligned}
  C&\colon \vec r=t\vec \imath + t^3\vec\jmath, \quad t\in\qty[0,1],
\end{aligned}$$
tj. počítáme
$$\int_C 2y\,\mathrm dx + x^2y\,\mathrm dy$$
po zadané křivce $C$.

<div class=reseni>

Vektory budeme pro stručnost zapisovat jako uspořádané dvojice.

Derivací křivky $\vec r=(t,t^3)$ podle $t$ dostáváme
$$\frac{\mathrm d\vec r}{\mathrm dt}=(1,3t^2).$$
Rovnice vektorového pole podél křivky má tvar
$$\vec F(\vec r(t))=(2t^3,t^2t^3)=(2t^3,t^5).$$
Skalárním součinem dostáváme
$$\vec F \frac{\mathrm d\vec r}{\mathrm dt}=
(1,3t^2)\cdot (2t^3,t^5) = 1\cdot 2t^3+3t^2\cdot t^5=2t^3+3t^7.
$$
Odsud formálně $$\vec F\mathrm d\vec r=(2t^3+3t^7)\mathrm dt$$
a integrál má tvar
$$\int_C\vec F\mathrm d\vec r=\int_0^{1}(2t^3+3t^7)\,\mathrm dt
=\qty[\frac 12 t^4 + \frac 38 t^8]_0^1=\frac 12 +\frac 38 - 0 = \frac 78.$$

</div>

\obrazek[vlastní]{priklad_5_4.png}

### Tok vektorového pole uzavřenou křivkou

Vypočtěte tok vektorového pole $$\vec \Phi_1=(x+2)\vec\imath$$ jednotkovou kružnicí se středem v počátku orientovanou proti směru hodinových ručiček, tj. $$C\colon \vec r=\cos(t)\vec \imath+\sin(t)\vec\jmath, \quad t\in[0,2\pi].$$

\textit{Návod:} $$\int_0^{2\pi}\sin^2 t\,\mathrm dt=\int_0^{2\pi}\cos^2 t\,\mathrm dt= \pi$$
a tento integrál je možno najít například grafickou cestou.

<div class=reseni>
Vektorové pole teče směrem doprava a směrem doprava i zesiluje. Dá se čekat, že tok ven pravou polovinou kružnice bude větší než tok dovnitř levou polovinou kružnice a celkový tok bude nenulový.

Vektorové pole je $$\vec \Phi_1=(x+2,0)$$ a pro výpočet toku musíme integrovat křivkovým integrálem druhého druhu vektorové pole $$\vec F=(0,x+2).$$
Vskutku, tok vektorového pole zadaného v komponentách $\Phi_1=(P,Q)$ je vyjádřen integrálem druhého druhu vektorového pole $\vec F=(-Q,P)$ a v našem případě je $P=x+2$ a $Q=0$. Derivací rovnice křivky obdržíme
$$\frac{\mathrm d\vec r}{\mathrm dt}=(-\sin (t),\cos (t)).$$
Rovnice vektorového pole $\vec F$ podél křivky $C$ má tvar
$$\vec F(\vec r(t))=(0,2+\cos t).$$
Skalárním součinem dostáváme
$$\vec F \frac{\mathrm d\vec r}{\mathrm dt}=
(-\sin t,\cos t)\cdot (0,2+\cos (t)) = 2\cos t+\cos^2 t .
$$
Odsud formálně $$\vec F\mathrm d\vec r=(2\cos t+\cos^2 t)\mathrm dt$$
a integrál má tvar
$$\oint_C\vec F\mathrm d\vec r=\int_0^{2\pi }(2\cos t+\cos^2 t)\,\mathrm dt= \pi ,$$
kde poslední Riemannův integrál není nutné počítat, protože integrál z první části je nulový díky geometrické interpretaci integrálu a periodicitě funkce $\cos t$ a integrál z druhého sčítance byl součástí zadání.

</div>

\obrazek[vlastní]{priklad_5_5.png}

### Tok vektorového pole uzavřenou křivkou

Vypočtěte tok vektorového pole $$\vec \Phi_2=(y+2)\vec\imath$$ jednotkovou kružnicí se středem v počátku orientovanou proti směru hodinových ručiček, tj. $$C\colon \vec r=\cos(t)\vec \imath+\sin(t)\vec\jmath, \quad t\in[0,2\pi].$$

\textit{Návod:} $$\int_0^{2\pi}\sin t\cos t\,\mathrm dt=0$$

<div class=reseni>
Vektorové pole teče směrem doprava. Kromě toho zesiluje směrem nahoru. Dá se čekat, že tok ven pravou polovinou kružnice bude v každý výšce stejný jako tok dovnitř levou polovinou kružnice a celkový tok bude nulový.

Vektorové pole je $$\vec \Phi_2=(y+2,0)$$ a pro výpočet toku musíme integrovat křivkovým integrálem druhého druhu vektorové pole $$\vec F=(0,y+2).$$
Vskutku, tok vektorového pole zadaného v komponentách $\Phi_2=(P,Q)$ je vyjádřen integrálem druhého druhu vektorového pole $\vec F=(-Q,P)$ a v našem případě je $P=y+2$ a $Q=0$. Derivací rovnice křivky obdržíme
$$\frac{\mathrm d\vec r}{\mathrm dt}=(-\sin (t),\cos (t)).$$
Rovnice vektorového pole $\vec F$ podél křivky $C$ má tvar
$$\vec F(\vec r(t))=(0,2+\sin t).$$
Skalárním součinem dostáváme
$$\vec F \frac{\mathrm d\vec r}{\mathrm dt}=
(-\sin t,\cos t)\cdot (0,2+\sin (t)) = 2\cos t+\cos t \sin t.
$$
Odsud formálně $$\vec F\mathrm d\vec r=(2\cos t+\cos t\sin t)\mathrm dt$$
a integrál má tvar
$$\oint_C\vec F\mathrm d\vec r=\int_0^{2\pi }(2\cos t+\cos t\sin t)\,\mathrm dt.$$

Integrál z prvního sčítance můžeme vypočítat pomocí primitivní funkce
$$\int_0^{2\pi} 2\cos x\,\mathrm dx=\qty[2\sin x]_0^{2\pi}=2\sin(2\pi)-2\sin 0 =0$$ a integrál z druhého sčítance je nulový, proto je nulový i celý integrál.
$$\int_C\vec F\mathrm d\vec r=0$$

</div>

\definecolor{zelena}{HTML}{0A5028}
## Dvojné integrály

### Integrál přes obdélník

\Tobrazek{\begin{tikzpicture}
  \draw[black,fill=green] (0,1) rectangle (3,2);
  \draw[->] (0,0)--(3.5,0) node[right]{$x$};
  \draw[->] (0,0)--(0,2.5) node[above]{$y$};
    \begin{scope}
    \clip (0,0) rectangle (3.5,2.5);
    \draw[thin, dashed, gray] (0,0) grid (4,3);
  \end{scope}
\end{tikzpicture}
}

Vypočtěte dvojný integrál $$\iint_\Omega xy^2\mathrm dx\mathrm dy$$
přes obdélník $$
\begin{gathered}
  0\leq x\leq 3\\1\leq y\leq 2.
\end{gathered}
$$

<div class=reseni>

$$
\begin{aligned}
  \iint_\Omega xy^2\mathrm dx\mathrm dy
  &=\int_0^3x\,\mathrm dx \int _1^2 y^2 \,\mathrm dy
\\&=\left[\frac {x^2}2\right]_0^3 \times \left[\frac 13 y^3 \right]_1^2
\\&=\left[\frac 92-0\right]\times \left [\frac 13 2^3 - \frac 13 \right]
=\frac 92 \times \frac 73 = \frac {21}2
\end{aligned}
$$

</div>

### Kvadratický moment pro obdélník

Vypočtěte integrál
$$
\begin{aligned}
 \iint_\Omega y^2\,\mathrm dx \mathrm dy,\\
\end{aligned}
$$
přes obdélník se stranami podél os, se středem v počátku a délkou stran $a$ a $b$, tj. přes množinu $\Omega$ danou nerovnostmi
$$
\begin{aligned}
  -\frac a2\leq &x\leq \frac a2,\\
  -\frac b2\leq &y \leq \frac b2.
\end{aligned}
$$

<div class=reseni>

$$
\begin{aligned}
  \iint_\Omega y^2\,\mathrm dx \mathrm dy
  = \int_{-\frac a2}^{\frac a2} \,\mathrm dx \times \int_{-\frac b2}^{\frac b2}y^2\,\mathrm dy=a\times \left[\frac 13 y^3\right]_{-\frac b2}^{\frac b2}=a\times \left(\frac 13 \times \frac {b^3}{8} + \frac 13 \times \frac {b^3}{8}\right)=
  \frac 1{12}ab^3
\end{aligned}
$$

</div>

### Integrál závislý na parametru

\Tobrazek{\begin{tikzpicture}
  \draw[black,fill=green] (0,0) rectangle (1,1);
  \draw[->] (0,0)--(1.5,0) node[right]{$x$};
  \draw[->] (0,0)--(0,1.5) node[above]{$y$};
    \begin{scope}
    \clip (0,0) rectangle (1.5,1.5);
    \draw[thin, dashed, gray] (0,0) grid (2,2);
  \end{scope}
\end{tikzpicture}
}

Vypočtěte dvojný integrál $$I_n=\iint_\Omega y^n\mathrm dx\mathrm dy$$
přes jednotkový čtverec $$
\begin{gathered}
  0\leq x\leq 1\\0\leq y\leq 1
\end{gathered}
$$
v závislosti na parametru $n\geq 0$.

<div class=reseni>

$$
\begin{aligned}
  \iint_\Omega y^n\mathrm dx\mathrm dy
  &=\int_0^1\,\mathrm dx \int _0^1 y^n \,\mathrm dy
  =1 \times \left[\frac 1{n+1} y^{n+1} \right]_0^1
  =\frac 1{n+1}
\end{aligned}$$

Správnost můžeme ověřit pomocí vzorců pro obsah  $$I_0=1$$ a polohu težiště $$\frac{I_1}{I_0}=\frac 12,$$
což porovnáme s očekávanými výsledky. Dalším využitím je působiště tlakové síly na přehradu (viz přednáška), které je při orientaci osy $y$ od hladiny směrem dolů v místě
$$\frac{I_2}{I_1}=\frac {\frac 13}{\frac 12}=\frac 23,$$
tj. ve dvou třetinách hloubky.

</div>

### Integrál přes trojúhelník

\Tobrazek{\begin{tikzpicture}[scale=3]
  \draw[black,fill=green, domain=0:1] (0,0) -- (0,1) -- plot ({\x},{1-\x})--cycle;
%  \draw[black,domain=0:1.2] plot ({\x},{1-\x}) node[right]{$y=1-x$};
  \draw[->] (0,0)--(1.5,0) node[right]{$x$};
  \draw[->] (0,0)--(0,1.5) node[above]{$y$};
    \begin{scope}
    \clip (0,0) rectangle (1.5,1.5);
    \draw[thin, dashed, gray] (0,0) grid (4,3);
  \end{scope}
\end{tikzpicture}
}

Vypočtěte integrál
$$  \iint_\Omega xy^2\,\mathrm dx \mathrm dy
$$
přes trojúhelník $\Omega$ s vrcholy v bodech $(0,0)$, $(1,0)$ a $(0,1)$.

<div class=reseni>

Rovnice přímky, ve které leží přepona trojúhelníka, je
$$y=1-x$$ a trojúhelník tedy je možno zapsat soustavou nerovností

$$
\begin{aligned}
  0\leq &x\leq 1,\\
  0\leq &y \leq 1-x.
\end{aligned}
$$

Použitím těchto nerovností můžeme dvojný integrál transformovat na dvojnásobný a vypočítat.
$$
\begin{aligned}
  \iint_\Omega xy^2\,\mathrm dx\mathrm dy
  &=\int_0^1 \int_0^{1-x} xy^2\,\mathrm dy\mathrm dx
  =\int_0^1 \left[\frac 13 xy^3\right]_0^{1-x}\,\mathrm dx
  =\int_0^1 \frac 13x(1-x)^3\,\mathrm dx
  \\&=\frac 13 \int_0^1 x-3x^2+3x^3-x^4\,\mathrm dx
  =\frac 13\left[\frac 12 x^2 - x^3 +\frac 34 x^4-\frac 15 x^5\right]_0^1
  \\&=\frac 13\left[\frac 12 -1 +\frac 34 -\frac 15\right] =\frac 1{60}
\end{aligned}
$$

</div> 

### Integrál pod parabolou

\Tobrazek{\begin{tikzpicture}[scale=3]
  \draw[black,fill=green, domain=0:1] (0,0) -- (0,1) -- plot ({\x},{1-\x^2})--cycle;
  \draw[black,domain=0:1.2] plot ({\x},{1-\x^2}) node[right]{$y=1-x^2$};
  \draw[->] (0,0)--(1.5,0) node[right]{$x$};
  \draw[->] (0,0)--(0,1.5) node[above]{$y$};
    \begin{scope}
    \clip (0,0) rectangle (1.5,1.5);
    \draw[thin, dashed, gray] (0,0) grid (4,3);
  \end{scope}
\end{tikzpicture}
}

Vypočtěte integrály
$$
\begin{aligned}
  I_1&=\iint_\Omega x\,\mathrm dx \mathrm dy,\\
  I_2&=\iint_\Omega y\,\mathrm dx \mathrm dy,\\
  I_3&=\iint_\Omega \,\mathrm dx \mathrm dy,\\
\end{aligned}
$$
přes množinu $\Omega$ danou nerovnostmi
$$
\begin{aligned}
  0\leq &x\leq 1,\\
  0\leq &y \leq 1-x^2.
\end{aligned}
$$
Určete obsah a polohu těžiště této množiny.

<div class=reseni>

$$
\begin{aligned}
  \iint_\Omega x\,\mathrm dx\mathrm dy
  &=\int_0^1 \int_0^{1-x^2} x\,\mathrm dy\mathrm dx
  =\int_0^1 \left[xy\right]_0^{1-x^2}\,\mathrm dx
  =\int_0^1 x(1-x^2)\,\mathrm dx
  =\int_0^1 x-x^3\,\mathrm dx
  \\&=\left[\frac 12 x^2 - \frac 14 x^4\right]_0^1=\frac 12-\frac 14 =\frac 14
\end{aligned}
$$
$$
\begin{aligned}
  \iint_\Omega y\,\mathrm dx\mathrm dy
  &=\int_0^1 \int_0^{1-x^2} y\,\mathrm dy\mathrm dx
  =\int_0^1 \left[\frac 12 y^2\right]_0^{1-x^2}\,\mathrm dx
  =\int_0^1 \frac 12 (1-x^2)^2\,\mathrm dx
  \\&=\frac 12 \int_0^1 1-2x^2+x^4\,\mathrm dx
  =\frac 12 \left[x-\frac 23 x^3 + \frac 15 x^5\right]_0^1=\frac 12\left[1-\frac 23 + \frac 15\right]=\frac 4{15}
\end{aligned}
$$

$$
\begin{aligned}
  \iint_\Omega \,\mathrm dx\mathrm dy
  &=\int_0^1 \int_0^{1-x^2} \,\mathrm dy\mathrm dx
%  =\int_0^1 \left[y\right]_0^{1-x^2}\,\mathrm dx
  =\int_0^1 1-x^2\,\mathrm dx
  =\left[x - \frac 13 x^3\right]_0^1=1-\frac 13 =\frac 23
\end{aligned}
$$

Obsah je $\frac 23$ a souřadnice těžiště jsou $\left[\frac 38,\frac 4{10}\right]$. Toto je možné porovnat s obsahem a souřadnicemi těžiště trojúhelníka, který vznikne nahrazením paraboly přímkou a tento trojúhelník má obsah $\frac 12$ a souřadnice těžiště $\left[\frac 13,\frac 13\right].$

</div> 
### Integrál přes čtvrtkružnici

\let\phi \varphi
\Tobrazek{\begin{tikzpicture}[scale=3]
  \draw[black,fill=green, domain=0:1] (0,0) -- (0,1) -- plot ({\x},{sqrt(1-\x^2)})--(1,0)--cycle;
  \draw[->] (0,0)--(1.5,0) node[right]{$x$};
  \draw[->] (0,0)--(0,1.5) node[above]{$y$};
    \begin{scope}
    \clip (0,0) rectangle (1.5,1.5);
    \draw[thin, dashed, gray] (0,0) grid (4,3);
  \end{scope}
\end{tikzpicture}
}

Vypočtěte integrály
$$
\begin{aligned}
  I_1&=\iint_\Omega x\,\mathrm dx \mathrm dy,\\
  I_2&=\iint_\Omega y\,\mathrm dx \mathrm dy,\\
  I_3&=\iint_\Omega \,\mathrm dx \mathrm dy,\\
\end{aligned}
$$
přes čtvrtkružnici na obrázku (čtvrtina jednotkové kružnice v prvním kvadrantu).
Určete obsah a polohu těžiště této čtvrtkružnice.

<div class=reseni>

V polárních souřadnicích daných rovnicemi $$
\begin{aligned}
  x&=r\cos\phi\\
  y&=r\sin\phi
\end{aligned}
$$
má čtvrtkružnice vyjádření $0\leq r\leq 1$, $0\leq \phi\leq \frac \pi2$.
$$
\begin{aligned}
  \iint_\Omega x\,\mathrm dx\mathrm dy
  &=\int_0^1 \int_0^{\frac \pi2} r\cos\phi \times r\,\mathrm d\phi\mathrm dr
  =\int_0^1 r^2 \,\mathrm dr \times \int_0^{\frac \pi2}\cos\phi \mathrm d \phi
  \\&=\left[\frac 13 r^3\right]_0^1\times \left[\sin\phi\right]_0^{\frac \pi2}=\frac 13 \times 1=\frac 13
\end{aligned}
$$$$
\begin{aligned}
  \iint_\Omega y\,\mathrm dx\mathrm dy
  &=\int_0^1 \int_0^{\frac \pi2} r\sin\phi \times r\,\mathrm d\phi\mathrm dr
  =\int_0^1 r^2 \,\mathrm dr \times \int_0^{\frac \pi2}\sin\phi \mathrm d \phi
  \\&=\left[\frac 13 r^3\right]_0^1\times \left[-\cos\phi\right]_0^{\frac \pi2}=\frac 13 \times 1=\frac 13
\end{aligned}
$$
$$
\begin{aligned}
  \iint_\Omega \,\mathrm dx\mathrm dy
  &=\int_0^1 \int_0^{\frac \pi2} 1 \times r\,\mathrm d\phi\mathrm dr
  =\int_0^1 r \,\mathrm dr \times \int_0^{\frac \pi2}\mathrm d \phi
  \\&=\left[\frac 12 r^2\right]_0^1\times {\pi2}=\frac 12 \times \frac \pi 2=\frac \pi 4
\end{aligned}
$$

Obsah je $\frac \pi 4$, což odpovídá čtvtině vzorce pro obsah jednotkového kruhu. Souřadnice težište jsou obě stejné, což odpovídá symetrii množiny.  Tyto souřadnice leží v bodě
$$\frac {4}{3\pi}\approx 0.42,$$
což odpovídá tomu, že těžište je posunuto doprava nahoru ve srovnání těžištěm trojúhelníka, který by vznikl nahrazením oblouku úsečkou.

</div>

### Kvadratický moment kruhu

Vypočtěte kvadratický moment kruhu o poloěmru $R$ vzhledem k ose procházející středem.

<div class=reseni>

Vypočteme kvadratický moment kruhu daného v polárních souřadnicích nerovnicemi
$$
\begin{aligned}
  0&\leq r\leq R,\\
  0&\leq \varphi\leq 2\pi.  
\end{aligned}
$$

Přímým výpočtem dostáváme
$$
\begin{aligned}
  \iint_{\Omega}y^2\,\mathrm dx\mathrm dy&=
  \int_{0}^R \int_0^{2\pi} r^2\sin^2\varphi \times r\,\mathrm d\varphi \mathrm dr
  =\int_{0}^R  r^3  \mathrm dr \int_0^{2\pi}\sin^2\varphi \,\mathrm d\varphi
  =\left[\frac {r^4}{4}\right]_0^R \pi
  =\frac {\pi}{4} R^4,
\end{aligned}
$$
kde při výpočtu integrálu přes proměnnou $\varphi$ využijeme nápovědu, kterou jsme měli již v sadě úloh s křivkovým integrálem.

Že je výsledkem veličina úměrná čtvrté mocnině poloměru je zřejmé i z rozměrové analýzy (resp. z Buckinghamova $\Pi$ teorému), uvedeným výpočtem však vidíme i konstantu úměrnosti.

To že kvadratický moment roste se čtvrtou mocninou poloměru značí, že snížení průměru tyče na polovinu vede k redukci tuhosti na přibližně $(0.5)^4$ tj. na šest procent. Devadesát šest procent tuhosti je v materiálu, který se při tomto odstraní. Proto jsou trubky při stejné spotřebě materiálu odolnější vůči ohnutí než tyče. Proto mají listy rostlin nebo listy vrtulí větrných elektráren materiál odpovídající za tuhost na povrchu. Proto máme kosti duté.

</div>

<!--
%

%## Jacobiho matice pro polární souřadnice

%  Najděte Jacobiho matici a její determinant pro transformaci 
% \begin{equation*}
%   \begin{aligned}
%     x&=r\cos \varphi\\
%     y&=r\sin \varphi
%   \end{aligned}
% \end{equation*}
% mezi polárními a kartézskými souřadnicemi.

-->

## Křivkový integrál pomocí potenciálu, Greenova věta, rovnice kontinuity

### Křivkový integrál pomocí kmenové funkce

Určete, pro jako hodnotu parametru $a\in \mathbb R$ křivkový integrál vektorového pole $$\vec F=ax^2y\vec\imath + (x^3+1)\vec\jmath$$ po křivce $C$, tj. $$\int_C ax^2y\,\mathrm dx+(x^3+1)\,\mathrm dy$$ nezávisí na integrační cestě v $\mathbb R^2$. Najděte kmenovou funkci příslušného vektorového pole a vypočtěte křivkový integrál po křivce z bodu $[0,0]$ do bodu $[1,2]$.

<div class=reseni>

Podmínka pro nezávislost na integrační cestě je $$
\begin{aligned}
0&=\nabla \times  \vec F
=\begin{vmatrix}
  \vec i & \vec j& \vec k \\
  \frac{\partial}{\partial x} &  \frac{\partial}{\partial y} &  \frac{\partial}{\partial z}\\
  ax^2y &  x^3+1 &  0
\end{vmatrix}
\\&=\vec k \left(  \frac{\partial}{\partial x} (x^3+1) - \frac{\partial }{\partial y} (ax^2y)\right)
  =\vec k(3x^2-ax^2y)=\vec k x^2(3-a)
\end{aligned}
  $$
  a odsud $a=3$. Totéž dokážeme určit pomocí věty, kterou jsme se ukázali již v souvislosti s pojmem gradient, ze které vyplývá podmínka na existenci kmenové funkce ve tvaru $$
\begin{aligned}
  \pdv{y}(ax^2y)&=\pdv{x}(x^3+1)\\
  ax^2&=3x^2\\
  a&=3
\end{aligned}
$$
Kmenová fukce $\varphi(x,y)$ vektorového pole $\vec F=(3x^2y,x^3+1)$ splňuje
$$
\begin{aligned}
  \pdv{\varphi}{x}&=3x^2y \\  \pdv{\varphi}{y}&=x^3+1.
\end{aligned}
$$
Integrací dostáváme
$$
\begin{aligned}
  \varphi &= \int 3x^2y\,\mathrm dx=x^3y+C_1(y)\\
  \varphi &= \int x^3+1\,\mathrm dy=x^3y+y+C_2(x)
\end{aligned}
$$
Porovnáním dostáváme kmenovou funkci $$\varphi (x,y)=x^3y+y+C,$$ kde $C$ je integrační konstanta. Integrál po křivce (tvar není důležitý, vzhledem k nezávislosti na integrační cestě stačí počáteční a koncový bod) je
$$\int _C \vec F\mathrm d\vec r=\varphi(1,2)-\varphi(0,0)=2+2-0=4.$$

</div>

### Křivkový integrál pomocí kmenové funkce 2

Pro jakou hodnotu parametru $m$ je křivkový integrál
$$\int (6x^2y+x+y)\,\mathrm dx+(mx^3+x)\,\mathrm dy$$ nezávislý na
integrační cestě v $\mathbb R^2$? Vypočtěte hodnotu tohoto integrálu
po křivce z bodu $(2,1)$ do bodu $(1,3)$.

<div class=reseni>

Podmínka pro nezávislost na integrační cestě je $$\pdv{y}\qty(6x^2y+x+y)=\pdv{x}\qty(mx^3+x).$$
Po výpočtu derivací dostáváme
$$6x^2+1=3mx^2+1$$
a odsud $m=2$.

Hledáme funkci, jejímž gradientem je vektorové pole $\vec F=(6x^2y+x+y,2x^3+x)$. 
Integrací podle $x$ a podle $y$ dostáváme
$$\int (6x^2y+x+y)\,\mathrm dx= 2x^3y+\frac 12 x^2+xy+C_1(y) $$
a
$$\int (2x^3+x)\,\mathrm dy=2x^3y+xy+C_2(x).$$
Porovnáním získáme kmenovou funkci
$$\varphi(x,y)=2x^3y+\frac 12 x^2+xy+C,
\quad C
\in
\mathbb R.$$

Integrál po křivce  z bodu $(2,1)$ do bodu $(1,3)$
má hodnotu
$$\varphi(1,3)-\varphi(2,1)=6+\frac 12 +3-\qty(16+2+2)=-\frac{21}2.$$

</div>

### Kmenová funkce pomocí křivkového integrálu

Ukažte, že vektorové pole
$\vec F=(6x^2y+x+y,2x^3+x)$ má kmenovou funkci. Vypočtěte z definice křivkový integrál v tomto vektorovém poli po křivce $\vec r(t)=(at,bt)$, $t\in[0,1]$, tj. po úsečce z počátku do bodu $(a,b)$ a ukažte, že tímto způsobem obdržíme kmenovou funkci.  

<div class=reseni>
Platí $$\pdv{y}\qty(6x^2y+x+y)=6x^2+1=\pdv{x}\qty(2x^3+x)$$
a proto kmenová funkce existuje.

Derivací křivky dostáváme rovnici tečného vektoru
$$\frac{\mathrm d\vec r}{\mathrm dt}=(a,b)$$
a dosazením křivky do vektorového pole
$$\vec F(\vec r(t))=(6a^2t^2bt+at+bt,2a^3t^3+at)=(6a^2bt^3+at+bt,2a^3t^3+at).$$
Skalární součin je daný vztahem
$$\vec F\frac{\mathrm d\vec r}{\mathrm dt}=a(6a^2bt^3+at+bt)+b(2a^3t^3+at)
=8a^3b t^3+a^2t+2abt.
$$
Křivkový integrál je tedy roven
$$\int_C \vec F\,\mathrm d\vec r=
\int_0^1 8a^3b t^3+a^2t+2abt\,\mathrm dt=
\qty[2a^3bt^4+\frac 12 a^2 t^2+abt^2]_0^1=2a^3b+\frac 12 a^2+ab.
$$
Podle věty o nezávislosti křivkového integrálu na integrační cestě máme
$$\varphi(a,b)-\varphi(0,0)=2a^3b+\frac 12 a^2+ab$$
a odsud
$$\varphi(a,b)=2a^3b+\frac 12 a^2+ab+\varphi(0,0),$$
neboli (po přejmenování proměnných a zavedení konstanty $C$ místo $\varphi(0,0)$)
$$\varphi(x,y)=2x^3y+\frac 12 x^2+xy+C.$$

</div>

### Greenova věta

Určete integrál $$\oint_C \vec F\,\mathrm d\vec r$$ po křivce, která je kladně orientovanou hranicí jednotkového čtverce s vrcholy v bodech $(0,0)$, $(1,0)$, $(0,1)$, $(1,1)$ pro vektorovou funkci $$\vec F=x^7\vec i+xy\vec j.$$

<div class=reseni>

$$
\begin{aligned}
  \oint_C \vec F\,\mathrm d\vec r
  &=
  \oint_C x^7\,\mathrm dx+ xy\,\mathrm dy\\&
  =\int_0^1 \int_0^1 \frac{\partial}{\partial x}(xy)-\frac{\partial}{\partial y}(x^7) \,\mathrm dy\mathrm dx\\
  &=\int_0^1 \int_0^1 y \,\mathrm dy\mathrm dx\\&
  =\int_0^1 y \,\mathrm dy \times \int_0^1 \,\mathrm dx \\&= \left[\frac 12 y^2\right]_0^1 \times 1\\&= \frac 12
\end{aligned}
$$

</div>

### Rovnice vedení tepla v materiálech různých vlastností

Rovnice vedení tepla v ortotropním materiálu umístěném do souřadné soustavy tak, aby vlastní směry tenzoru tepelné vodivosti (jako např. anatomické směry dřeva) má nejobecnější možné vyjádření
$$c\rho\pdv{T}{t}=\pdv{x}\qty(\lambda_x\pdv{T}{x} )+\pdv{y}\qty(\lambda_y\pdv{T}{y}) . $$
Za jakých okolností je možno veličiny $\lambda_x$ a $\lambda_y$ napsat před vnější derivaci tak, aby v rovnici vznikly druhé derivace? 

<div class=reseni>

V případě, že tyto veličiny nezávisí na poloze. Materiál tedy musí být homogenní. Závislost na poloze nesmí být ani zprostředkovaná přes teplotu. Tyto veličiny tedy nesmí být ani funkcemi teploty. Jinými slovy, konstanta úměrnosti ve Fourierově zákoně se nesmí měnit s teplotou, vztah z Fourierova zákona musí být opřesěn lineární a takové materiály se nazvají materiály s lineární materiálovou odezvou (zkráceně lineární materiály). Veličiny  $\lambda_x$ a $\lambda_y$  se dají napsat před vnější derivace pouze pokud je materiál homogenní a lineární.

</div>

\obrazek{chladic.jpg}
### Stacionární vedení tepla v žebru chladiče

Vyjímečně jsme nuceni do rovnice vedení tepla zahrnout i zdroje. 
Modelujte vedení tepla v žebru chladiče. Úlohu uvažujte jako
jednorozměrnou, materiál homogenní izotropní s konstantní tepelnou
vodivostí. Kolem chladiče proudí vzduch a teplotě $T_0$ a chladič
ztrácí teplo rychlostí úměrnou rozdílu teploty žebra v daném místě a
teploty okolního vzduchu. (Koeficient úměrnosti je dán koeficient přestupu tepla a šířkou žebra). Uvažujte stacionární děj.

<div class=reseni>

$$0=-h(T-T_0)+\frac{\mathrm d}{\mathrm dx}\left(\lambda \frac{\mathrm dT}{\mathrm dx}\right)$$

Ke stejnému závěru je možné dojít i přesnou analýzou ve 3D, viz Cengel, Heat transfer, kapitola 3–6 Heat transfer from finned surfaces.

</div>

## Diferenciální rovnice I

### Řešení ODE a IVP 

1. $\frac{\mathrm dy}{\mathrm dx}=xy^2$
1. $\frac{\mathrm dy}{\mathrm dt}=te^y$
1. $\frac{\mathrm dy}{\mathrm dx}=x\sqrt y$
1. $\frac{\mathrm dy}{\mathrm dx}=x\sqrt y,\ \ y(0)=1$
1. $\frac{\mathrm dr}{\mathrm dt}=kr^3,\ \ r(0)=r_0>0$
1. $\frac{\mathrm dm}{\mathrm dt}=m+2,\ \ m(0)=0$
1. $\frac{\mathrm dm}{\mathrm dt}=m+2,\ \ m(0)=-2$

_Umění najít řešení diferenciální rovnice je sympatické, není to však nic proti umění sestavit model (naučili jsme se již ve druhém týdnu, připomeneme si v následujícím modelu), umění posoudit jednoznačnost řešení (většina modelů se řeší numericky a musíme být přesvědčeni o smysluplnosti takové činnosti) a  stabilitu řešení (řešení, která nejsou stabilní, jsou sice v souladu s přírodními zákony, ale pravděpodobnost jejich spontánního výskytu je nulová). Jednoznačnost a zjednodušenou verzi stability řešení (stabilita konstantních řešení) jsme viděli na přednášce a připomeneme v dalších příkladech._

<div class=reseni>

1. $\frac{\mathrm dy}{\mathrm dx}=x\cdot y^2$
   *  Konstantní řešení jsou řešení rovnice $$ y^2=0,$$ tj. je jediné konstantní řešení $$ y=0.$$
    * Pro nekonstantní řešení dostaneme po separaci  $$ y^{-2}\mathrm dy=x\mathrm dx $$ a integrováním $$ -\frac 1y=\frac 12 x^2+C.$$
1. $\frac{\mathrm dy}{\mathrm dt}=t\cdot e^y$
    * Konstantní řešení jsou řešení rovnice $$ e^y=0.$$ Protože tato rovnice nemá řešení, zadaná diferenciální rovnice nemá konstantní řešení.
    * Pro nekonstantní řešení dostaneme po separaci  $$ e^{-y}\mathrm dy= t\mathrm dt$$ a integrováním $$ -e^{-y}=\frac 12 t^2 +C.$$
1. $\frac{\mathrm dy}{\mathrm dx}=x\cdot \sqrt y$
    * Konstantní řešení jsou řešení rovnice $$ \sqrt y=0,$$ tj. jediné řešení $$ y=0.$$
    * Pro nekonstantní řešení dostaneme po separaci  $$ \frac 1{\sqrt y}\mathrm dy=x\mathrm dx $$ a integrováním $$ 2\sqrt y=\frac 12 x^2+C.$$
1. $\frac{\mathrm dy}{\mathrm dx}=x\sqrt y,\ \ y(0)=1$
    * Konstantní řešení $$y=0$$ (viz předchozí příklad) nesplňuje počáteční podmínku a proto jej nemusíme uvažovat
    * Obecné řešení  $$ 2\sqrt y=\frac 12x^2 +C$$ dává po dosazení $x=0$ a $y=1$ rovnici $$2\sqrt 1=0+C.$$ Odsud dostáváme $C=2$ a řešení zadané počáteční úlohy je $$2\sqrt y=\frac 12 x^2+2.$$
1. $\frac{\mathrm dr}{\mathrm dt}=k\cdot r^3,\ \ r(0)=r_0>0$
    * Konstantní řešení jsou řešení rovnice $$ r^3=0,$$ tj. jediné konstantní řešení je $$ r=0$$ a toto řešení nesplňuje počáteční podmínku.
    * Pro nekonstantní řešení dostaneme po separaci  $$ r^{-3}\mathrm dr=k\mathrm dt $$ a integrováním $$ -\frac 12 r^{-2}=kt+C.$$ Dosazením počáteční podmínky $t=0$, $r=r_0$ dostáváme $$ -\frac 12 r_0^{-2}=C.$$ Tím je dána konstanta $C$ a po použití této konstanty v obecném řešení dostáváme řešení počáteční úlohy ve tvaru $$ -\frac 12 r^{-2}=kt-\frac 12 r_0^{-2}.$$
1. $\frac{\mathrm dm}{\mathrm dt}=m+2$, $m(0)=0$
    * Konstantní řešení jsou řešení rovnice $$ m+2=0,$$ tj. $$ m=-2$$ a toto řešení nesplňuje počáteční podmínku.
    * Pro nekonstantní řešení dostaneme po separaci  $$ \frac1{m+2}\mathrm dm=dt $$ a integrováním $$ \ln|m+2|=t+C.$$ Po dosazení počáteční podmínky $t=m=0$ dostáváme $$C=\ln 2$$ a počáteční úloha má řešení $$\ln(m+2)=t+\ln (2).$$ (Vzhledem k počáteční podmínce je $m$ kladné a nemusíme psát absolutní hodnotu.)
1. $\frac{\mathrm dm}{\mathrm dt}=m+2$, $m(0)=-2$
    * Konstantní řešení jsou řešení rovnice $$ m+2=0,$$ tj. $$ m=-2.$$ Toto řešení splňuje počáteční podmínku.
    * Pravá strana má ohraničenou (dokonce konstantní) derivaci podle $m$. Proto je řešení každé počáteční úlohy určeno jednoznačně. Řešení z předchozího bodu je jediné a další nemusíme hledat.

</div>

\obrazek{mladata.jpg}

### Model růstu úměrného velikosti chybějícího množství

Mnoho
živočichů roste tak, že mohou dorůstat jisté maximální délky a
rychlost jejich růstu je úměrná délce, která jim do této maximální
délky chybí (tj. kolik ještě musí do této maximální délky
dorůst). Sestavte matematický model popisující takovýto růst
(von Bertalanffy growth model).

_Jakmile vidíme, že v zadání figuruje rychlost změny veličiny,
  která nás zajímá, je jasné, že kvantitativní model bude obsahovat
  derivaci. Zatím se učíme model zapsat, později ho budeme umět i vyřešit._

<div class=reseni>
Je-li $L$ délka a $L_{\max}$ maximální délka, potom do maximální délky chybí  $L_{\max}-L$ a model má tvar
$$\dv {L}{t}=k (L_{\max}-L).$$
</div>

![](kontaminace.jpg)

### Kontaminace a čištění

Znečišťující látky se v kontaminované oblasti rozkládají tak, že za den se samovolně rozloží 
$8\%$ aktuálního znečištění. Kromě toho pracovníci odstraňují látky rychlostí $30$
galonů denně. Vyjádřete tento proces kvantitativně pomocí vhodného
modelu.

\textit{Tento příklad opět zmiňuje rychlost změny, tj. derivaci. Tentokrát se na změně podílejí dva procesy a jejich účinek se sčítá. Příklad navíc připomíná, jak se pracuje se změnou vyjádřenou procenty. Toto je používané například při úročení spojitým úrokem. Pokud pokles změníme na růst, tj. pokud změníme
  znaménka u derivace, máme okamžitě model růstu financí na účtu, na kterém se pravidelně připisuje úrok a k tomu se přidává fixní úložka.}

<div class=reseni> Je-li $y$ znečištění v galonech a $t$ čas ve dnech, má model tvar
$$\dv {y}{t}=-0.08y-30.$$

</div>

<!--
% \obrazek{lov.jpg}
% ## Logistická rovnice: model využívání přírodních zdrojů
% Při modelování růstu populace o velikosti $x(t)$ často pracujeme s populací žijící v prostředí s omezenou úživností (nosnou kapacitou). Často používáme model
% $$\frac{\mathrm d x}{\mathrm dt}=rx\left(1-\frac xK\right),$$
% kde $r$ a $K$ jsou parametry modelu (reálné konstanty).  Nakreslete
% graf funkce $f(x)=rx\left(1-\frac xK\right)$ a ověřte, že pro velká
% $x$ je $f(x)$ záporné a velikost populace proto klesá. Pokud populaci
% lovíme konstantní rychlostí, sníží se pravá strana o konstantu, kterou
% označíme $h$. Ukažte, že pro intenzivní lov bude pravá strana rovnice
% pořád záporná a intenzivní lov tak způsobí vyhubení populace. Dá se
% najít kritická hodnota lovu oddělující vyhynutí populace a její
% trvalé přežívání?

% \textit{Toto je asi nejdůležitější rovnice pro modelování biologických jevů. Používá se při modelování vývoje obnovitelných zdrojů a bývá modifikována pro konkrétní případy podle toho, jak populace interaguje s okolím.}

% <div class=reseni>
% Funkce $f(x)=rx\left(1-\frac xK\right)$ je kvadratická funkce s nulovými body $x=0$ a $x=K$, vrcholem uprostřed mezi nulovými body (tj. pro $x=\frac K2$) a parabola je otočená vrcholem nahoru. Proto je napravo od $x=K$ záporná. To odpovídá tomu, že populace s velikostí přesahující nosnou kapacitu v dlouhodobém horizontu vymírá.

% Funkce $f_h(x)=rx\left(1-\frac xK\right)-h$ vznikne posunutím funkce $f(x)=rx\left(1-\frac xK\right)$ o $h$ dolů. Pokud posuneme hodně, dostane se celá parabola pod osu $x$ a funkce bude pořád záporná. Kritická hodnota je v situaci, kdy mizí možnost, že $f_h(x)$ má body kde je kladná a populace se může rozvíjet. To nastane,  pokud se vrchol paraboly dostane na osu $x$, tj. $h$ je rovno funkční hodnotě funkce $f(x)$ v bodě $x=\frac K2.$
% </div>

-->

![pixabay.com, autor Free-Photos](deer.jpg)

### Populace jelenů

Populace jelenů v národním parku přibývá rychlostí 10\% za
rok. Správa parku každý rok odebere 50 jedinců. Napište
matematický model pro velikost populace jelenů v tomto parku.

<div class=reseni>
Je-li $x$ velikost populace jelenů, platí
$$ \dv {x}{t}=0.10 x-50, $$ kde $t$ je čas v letech.
</div>

### Hrubý model chřipkové epidemie

Rychlost s jakou roste počet nemocných chřipkou je úměrný současně
počtu nemocných a počtu zdravých jedinců. Sestavte model takového
šíření chřipky.

_Toto je současně model popisující šíření informace v populaci, stačí si místo chřipky představit nějakou informaci předávanou mezi lidmi (sociální difuze)._

<div class=reseni>
Je-li $M$ velikost populace a $y$ počet nemocných, je v populaci $M-y$ zdravých a model má tvar
$$\dv {y}{t}=ky(M-y).$$
</div>

![](olej.jpg)

### Ropná skvrna

Kruhová ropná skvrna na hladině se rozšiřuje tak, že její poloměr jako
funkce času roste rychlostí, která je nepřímo úměrná druhé mocnině
poloměru. Vyjádřete proces kvantitativně pomocí derivací.

<div class=reseni>
Je-li $r$ poloměr, je $r^2$ druhá mocnina a protože se jedná o nepřímou úměrnost, platí
$$\dv {r}{t}=\frac{k}{r^2}.$$
</div>

### Model učení

Rychlost učení (tj. časová změna objemu osvojené látky nebo procento z
maximální manuální zručnosti) je úměrná objemu dosud nenaučené
látky. Vyjádřete proces kvantitativně pomocí derivací.

<div class=reseni>
Je-li $L$ objem naučené látky a $L_{\max}$ maximální objem látky kterou je možné se naučit, je objem dosud nenaučené látky $L_{\max}-L$ a model má tvar
$$\dv {L}{t}=k (L_{\max}-L).$$
</div>

![](ledni_medved.jpg)

### Tloušťka ledu

Takzvaný Stefanův zákon (J. Stefan, Uber die Theorie der Eisbildung, insbesondere uber die Eisbildung im Polarmeere, 1891) vyjadřuje že tloušťka ledu na hladině moře roste ve
stabilních podmínkách rychlostí nepřímo úměrnou této tloušťce. Zapište
tento fakt pomocí vhodného matematického modelu a najděte řešení
vzniklé diferenciální rovnice.

<div class=reseni>

$$
\begin{aligned}
\frac{\mathrm dh}{\mathrm dt}&=\frac kh\\
h\,\mathrm dh&=k\, \mathrm dt\\
\int h\,\mathrm dh&=\int k\, \mathrm dt\\
\frac {h^2}{2}&=kt+C\\
\end{aligned}
$$

</div> 

![Zdroj: www.rodovystatek.cz](voda_plastovky.jpg)

### Model vypouštění nádrže

Z fyziky je známo, že rychlost s jakou
vytéká tekutina otvorem u dna nádoby je úměrná odmocnině výšky hladiny
(protože se mění potenciální energie úměrná výšce na kinetickou
energii úměrnou druhé mocnině rychlosti). Proto je i rychlost s jakou
se zmenšuje objem vody v nádrži úměrná odmocnině výšky
hladiny.

Ukažte, že matematickým popisem procesu je diferenciální rovnice.
Napište rovnici pro výšku hladiny vody v nádrži jako funkci času.
Uvažujte tři případy:
nádrž \textbf{cylindrického tvaru} (válec postavený na podstavu),
nádrž ve tvaru
\textbf{kvádru} 
a nádrž ve tvaru \textbf{kužele} otočeného vrcholem dolů (trychtýř). 

\textit{V tomto příkladě vystupuje derivace jak rychlost, ale po přepisu zadání do modelu máme v rovnici dvě různé veličiny, které se mění: objem vody a výšku hladiny. Musíme ještě najít a použít vztah mezi rychlostmi změn těchto veličin. Fyzikální zákon je formulován pro derivaci objemu a nás zajímá derivace výšky.}

<div class=reseni>
Buď $V$ objem vody a $h$ výška hladiny od dna.
Podle zadání ve všech případech platí $$\frac {\mathrm dV}{\mathrm dt}=-k_1\sqrt h$$ a musíme derivaci $\frac {\mathrm dV}{\mathrm dt}$ vyjádřit pomocí $\frac {\mathrm dh}{\mathrm dt}$.

Pro cylindr, kvádr nebo jakoukoliv nádrž se svislými stěnami je objem úměrný výšce hladiny, $V=k_2 h$, a proto $\frac {\mathrm dV}{\mathrm dt}=k_2\frac {\mathrm dh}{\mathrm dt}$. Odsud
$$k_2\frac {\mathrm dh}{\mathrm dt}=\frac {\mathrm dV}{\mathrm dt}=-k_1\sqrt h,$$
tj.
$$\frac {\mathrm dh}{\mathrm dt}=-\frac{k_1}{k_2}\sqrt h$$
a pro $k=\frac{k_1}{k_2}$ má model tvar
$$\frac {\mathrm dh}{\mathrm dt}=-k\sqrt h.$$

Pro kužel platí $V=k_3h^3$ (díky podobnosti je objem přímo úměrný třetí mocnině libovolného délkového parametru) a proto
$\frac {\mathrm dV}{\mathrm dt}=k_3 \times 3h^2 \frac {\mathrm dh}{\mathrm dt}$.
Odsud
$$3k_3 h^2 \frac {\mathrm dh}{\mathrm dt}=\frac {\mathrm dV}{\mathrm dt}=-k_1\sqrt h,$$
tj. 
$$\frac {\mathrm dh}{\mathrm dt}=-\frac{k_1}{3k_3}h^{-3/2}$$
a po přeznačení konstanty má model pro kuželovou nádrž tvar
$$\frac {\mathrm dh}{\mathrm dt}=-kh^{-3/2}.$$

</div>

![Zdroj: www.rodovystatek.cz](voda_plastovky.jpg)

### Problematika jednoznačnosti v modelu vypouštění nádrže

Dříve jsme odvodili rovnici
$$\dv {h}{t}=-k\sqrt h$$
popisující úbytek hladiny vody v nádrži tvaru kvádru, ze které vypouštíme vodu.

1. Zkontrolujte, že pro $h>0$ má každá počáteční úloha jediné řešení. Interpretujte tento výsledek prakticky.
1. Pro $h=0$ by řešení nemuselo být určeno jednoznačně. A opravdu
  není. Řešením je například $h(t)=0$ nebo $$h(t)=
  \begin{cases}
    \frac 14 k^2 t^2 & t<0\\
    0 & t\geq 0.
  \end{cases}
  $$
Zkontrolujte dosazením (pozor: pro $t<0$ platí $\sqrt {t^2}=|t|=-t$) a rozmyslete, jestli nejednoznačnost je jenom matematický trik, nebo jestli má
 fyzikální interpretaci.

<div class=reseni>

1. Nabídneme dvě  varianty, pro argumentaci je možno použít kteroukoliv z nich. 
    * _Podle obecné věty o jednoznačnosti:_ Stačí ověřit, že pravá strana má ohraničenou parciální derivaci podle $h$. Protože platí
    $$\frac{\partial }{\partial h}(k\sqrt h)=k\frac 12
    h^{-1/2}=\frac{k}{2\sqrt h}$$ a tato derivace je definovaná a
    ohraničená v nějakém okolí libovolného bodu splňujícího $h>0$.
    Podle věty o existenci a jednoznačnosti řešení obecné
    diferenciální rovnice má počáteční úloha právě jedno řešení.
    * _Podle věty o jednoznačnosti pro rovnici se separovanými proměnnými:_ Stačí ověřit,
    že část závislá na $h$ je nenulová. Toto jistě platí, protože pro
    $h>0$ je $\sqrt{h}\neq 0$.

    Pokud je tedy v nádrži nějaká voda, je jednoznačně dáno,
    jak bude vytékat a je možné vypočítat, jaká bude v libovolném
    okamžiku hladina.
1. Pro $h=\frac 14 k^2 t^2$ a $t<0$ dostáváme $$
    \begin{aligned}
      \dv {h}{t}&=\frac 14 k^2 \cdot 2t = \frac 12 k^2 t\\
      -k\sqrt h&=-k\sqrt{\frac 14 k^2 t^2} = - k \frac 12 |k| \cdot |t| =
      - k \frac 12 k (-t) = \frac 12 k^2 t
    \end{aligned}
    $$ a obě strany rovnice jsou stejné. Pro $h=0$ je dosazení triviální. Je-li $h(t_0)=0$, může to být proto, že voda v čase $t_0$ právě vytekla, nebo proto, že vytekla před hodinou nebo proto, že v nádrži nikdy voda nebyla. Proto je nejednoznačnost přirozená. Například $h(t)=0$ je řešení odpovídající tomu, že voda v nádrži nikdy nebyla. Funkce $h(t)=\frac 14 k^2t^2$ pro $t<0$ odpovídá tomu, že pro $t<0$ v nádrži voda byla a vytekla v čase $t=0$.

</div>

<!--

% \obrazek[vlastní]{pokros.jpg}

% ## Stavebniny vedle čebínského nádraží: model Hromada sypkého
% materiálu má tvar kužele. Úhel u vrcholu je konstantní, daný
% mechanickými vlastnostmi materiálu a je nezávislý na
% objemu. Předpokládejme, že personál stavebnin přisypává na hromadu
% materiál konstantní rychlostí (v jednotkách objemu za jednotku
% času). Tato hromada je však v poměrně otevřené krajině a vítr
% rozfoukává materiál po okolí. Je rozumné předpokládat, že rozfoukávání (opět v jednotkách objemu za jednotku
% času)
% se děje rychlostí úměrnou povrchu návětrné strany pláště. Vyjádřete proces kvantitativně pomocí derivací.
% Napište rovnici pro derivaci objemu hromady podle času. 

% \textit{Toto je podobný model jako model vypouštění nádrže, ale kratší. Opět máme po přepisu zadání do matematického modelu dvě veličiny měnící se s časem v jedné rovnici. Derivace objemu, která nás zajímá, již v rovnici přítomna naštěstí je. Stačí vyjádřit obsah pomocí objemu, nejlépe pomocí rozměrové analýzy.}

% <div class=reseni>
% Rychlost s jakou se mění objem je $\frac{\mathrm dV}{\mathrm dt}$, rychlost přisypávání označme $R$, povrch návětrné strany $S$.
% Podle zadání platí
% $$  \frac{\mathrm dV}{\mathrm dt} = R - k_0S.$$
% Protože kužel má stále stejný tvar, objem jednoznačně determinuje rozměry, povrch kužele, nebo i povrch poloviny pláště, tj. povrch návětrné strany. Z rozměrové analýzy na základě Buckinghamova Pi-teorému z přednášky je zřejmé, že musí platit úměrnost mezi takovými mocninami těchto veličin, pro které jednotky ``pasují'', Existuje tedy konstanta taková, že $$S=k_1V^{\frac 23}.$$ Spojením těchto dvou vztahů dostáváme
% $$  \frac{\mathrm dV}{\mathrm dt} = R - k V^{\frac 23},$$
% kde $r$ a $k=k_0k_1$ jsou konstanty.

% </div>

% \obrazek[vlastní]{pokros.jpg}[-30pt]

% ## Stavebniny vedle čebínského nádraží: stabilita řešení

% Hromada sypkého materiálu má tvar kužele. Úhel u vrcholu je konstantní, daný
% mechanickými vlastnostmi materiálu a je nezávislý na
% objemu. V předchozím příkladě jsme sestavili diferenciální rovnici popisující růst hromady ve tvaru
% $$\frac{\mathrm dV}{\mathrm dt}=R-kV^{\frac 23},$$
% kde $R$ je rychlost přisypávání a $k$ konstanta.
% \vspace*{25pt}
% \begin{itemize}
% 1. Existuje konstantní řešení? Pokud ano, je stabilní nebo nestabilní? Zdůvodněte.
% 1. Může hromada skončit i při neustálém přisypávání celá rozfoukaná?
% 1. Mohou pracovníci navršit hromadu do libovolné výšky anebo pro velkou hromadu je již rozfoukávání rychlejší než přisypávání?
% \end{itemize}

% <div class=reseni>
% Označme $f(V)=R-kV^{\frac 23}$.
% Konstantní řešení je řešením rovnice $f(V)=0$, tj. $$R-kV^{\frac 23}=0.$$ Odsud
% $$V_0=\left(\frac{R}{k}\right)^{3/2}.$$ Protože $f$ klesá v bodě $V_0$, je toto řešení stabilní.

% Protože $f(0)>0$, malá hromada vždy roste a proto nemůže skončit celá rozfoukaná. Pro malý objem je přisypávání intenzivnější než rozfoukávání.

% Protože $f$ je pro velké $V$ záporná, pro velkou hromadu objem ubývá (více se rozfouká než přisype) a hromadu není možné navršit libovolně velkou. 

% </div>

% 
% \obrazek[http://ecoursesonline.iasri.res.in]{aq.png}[-10pt]

% ## Pokles hladiny podzemní vody při ustáleném rovinném proudění

% \label{pokles}
% Stavovou veličinou pro popis podzemní vody je \textit{piezometrická
%   hladina} $h$ měřená v metrech (hrubá představa může být hladina
% spodní vody nebo, v případě že je shora ohraničení nepropustnou
% vrstvou, tak hladina, kam by vystoupila voda ve vrtu). Prostor, kde
% voda teče, se nazývá \textit{zvodeň} (aquifer).
% Proudění řídí \textit{Darcyho zákon}, který
%   vyjadřuje, že \textit{filtrační rychlost} $v_f$ podzemní vody je úměrná
%   sklonu piezometrické hladiny, tj. rychlosti, s jakou klesá
%   piezometrická hladina jako funkce $x$.

%   \vspace*{-15pt}
% \begin{enumerate}[A)]1.sep 0 pt
% 1. Zapište Darcyho zákon kvantitativně pomocí derivace piezometrické hladiny. 
% 1. Tok je dán součinem filtrační rychlosti a obsahu plochy kolmo na
%   rychlost. Uvažujte obdélníkovou plochu $h\times 1$, která je na výšku přes celou
%   zvodnělou vrstvu $h$ a na šířku má jednotkovou délku. Vynásobte její obsah 
%   filtrační rychlostí a dostanete \textit{průtok na jednotku šířky}, označovaný
%   $q$. Pro ustálené proudění je $q$ konstantní.
% 1. Výsledný vztah z předchozího bodu chápejte jako diferenciální rovnici s neznámou funkcí $h$ jako funkcí $x$ a řešením rovnice najdete křivku snížení hladiny podzemní vody v podélném profilu. 
% \end{enumerate}

% (\textit{Podle Dana Říhová a Jana Marková, Poznámky k přednáškám z Hydrauliky, přednáška č. 9.})

% <div class=reseni>

% \begin{enumerate}[A)]
%   1.  $$v_f=-k\derivace {h}x$$
%   1. $$q=-kh\derivace hx$$
%   1. $$
%     \begin{aligned}
%       q\,\mathrm{d}x&=-kh\,\mathrm dh\\
%       \int q\,\mathrm{d}x&=-k \int h\,\mathrm dh\\
%       qx&=-\frac k2 h^2+C
%     \end{aligned}
%     $$
%     V souřadnicích, kdy osa $x$ směřuje doprava a $h$ nahoru, se jedná
%     se o parabolu ``otočenou vrcholem směrem doprava''.
% \end{enumerate}
% </div>

% \obrazek[http://ecoursesonline.iasri.res.in]{well.png}[-25pt]

% ## Studna s volnou hladinou

% Uvažujme diferenciální rovnici
% \begin{equation}
% q=-kh\derivace hx \tag{*}\label{*}
% \end{equation}
% odvozenou v \ref{pokles} B. Tentokrát budeme studovat studnu s volnou hladinou\footnote{Zjednodušeně, voda ve studni je na úrovni hladiny podzemní vody. Studna nevznikla navrtáním nepropustné vrstvy, kdy by byla voda natlakovaná a vystoupila do výšky odpovídající tomuto tlaku.} Je-li studna čerpána konstantní rychlostí $Q$, je tok na jednotku délky na kružnici o poloměru $x$ roven $q=-\frac {Q}{2\pi x}$ (voda teče dovnitř, tj. ve směru ve kterém klesá $x$). Dosaďte tento vztah do rovnice \eqref{*} a rovnici vyřešte s počáteční podmínkou $h(R)=H$, kde $H$ odpovídá hladině vody ve studni a $R$ je poloměr studny (na obrázku $h_w$ a $r_w$). Dostanete rovnici \textit{snížení hladiny v okolí studny} čerpané rychlostí $Q$ (depresní křivka).
% (\textit{Volně podle Dana Říhová a Jana Marková, Poznámky k přednáškám z Hydrauliky, přednáška č. 9. Analogickým způsobem se počítají tepelné ztráty při prostupu tepla válcovou stěnou (viz \url{https://youtu.be/rvyogmaUmUQ}).})

% <div class=reseni>
% $$
% \begin{aligned}
%   -\frac{Q}{2\pi x}&=-kh\derivace hx\\
% %  \frac{Q }{2\pi x}\,\mathrm {d}x&=kh\,\mathrm d h\\
%   \frac{Q }{2\pi} \int \frac{\mathrm {d}x}{x}&=k\int h\,\mathrm d h\\
%   \frac{Q }{2\pi}\ln x&=k \frac {h^2}2 +c\\
% \text{obecné řešení: }  \frac{Q }{\pi}\ln x&=k {h^2} +C\\
% \text{z počáteční podmínky: }  \frac{Q }{\pi}\ln R&=k {H^2} +C\\
%   C&=\frac{Q }{\pi}\ln R-k {H^2}\\
% \text{po dosazení do obecného řešení: }   \frac{Q }{\pi}\ln x&=k {h^2} +\frac{Q }{\pi}\ln R-k {H^2}\\
% \text{po úpravě: }  \frac{Q }{k\pi}\ln \frac {x}{R}&={h^2} - {H^2}\\
% \end{aligned}
% $$
% Tento vztah umožňuje například navrhnout průměr studny, odhadnout
% vydatnost studny, nebo pomocí odčerpávaného vrtu a menších pomocných
% vrtů sledujících pokles hladiny v okolí odčerpávaného vrtu stanovit
% filtrační součinitel $k$. Využití vzorce
% \begin{equation*}
%   \frac{Q }{k\pi}\ln \frac {x}{R}={h^2} - {H^2}
% \end{equation*}
% je však mnohem rozmanitější,
% umožňuje vypočítat poměry ve stavebních jámách a v jejich okolí. To je
% užitečné například při odhadu, kolik vody se hromadí ve výkopu. Další
% využití je, že dokážeme odhadnout vliv stavební jámy na hydrologické
% poměry v okolí a tyto poměry dokážeme měnit a přizpůsobovat našim
% potřebám. Častou aplikací je například hydraulická clona (soustava
% prvků rozmístěných a provozovaných tak, aby nedocházelo k šíření kontaminace z chemické výroby do vodárensky využívaných vod).

% </div>

% ## Rovnice podzemní vody
% \def\raggedright{\rightskip 0 pt plus 1 em}
% \begin{minipage}[t]{0.44\linewidth}\raggedright
   
%   Stavovou veličinou pro popis podzemní vody je \textit{piezometrická
%     hladina} $h$ měřená v metrech (hrubá představa může být hladina
%   spodní vody nebo, v případě že je shora ohraničení nepropustnou
%   vrstvou, tak hladina, kam by vystoupila voda ve vrtu). Prostor, kde
%   voda teče, se nazývá \textit{zvodeň} (aquifer). Tok podzemní vody ve
%   dvoudimenzionální horizontální zvodni, kdy zanedbáváme vertikální
%   tok, popisuje \textit{průtok na jednotku šířky} $\vec q$, který má směr toku
%   a velikost vyjadřuje v metrech krychlových na metr za den, kolik
%   vody proteče za jednotku času jednotkovou délkou kolmo na směr toku.

% \bigskip
% Zdroj obrázků: Jacob Bear, https://www.interpore.org/

% \end{minipage}\hfill
% \begin{minipage}[t]{0.5\linewidth}
%   \kern -40 pt
%   \raggedright
%   Řez zvodní s napjatou hladinou (výška zavodněné části je dána vzdáleností mezi nepropustnými vrstvami).
% \includegraphics[width=0.99\linewidth]{conaq.jpg}

%   Řez zvodní s volnou hladinou (výška zavodněné části je rovna rozdílu mezi piezometrickou výškou a dolní nepropustnou vrstvou).

% \includegraphics[width=0.99\linewidth]{phraq.jpg}
  
% \end{minipage}

% Zapište pomocí vhodných veličin, operátorů a rovnic následující vztahy, zákony nebo pozorování,
% odpovězte na otázky a splňte úkoly.
% \begin{enumerate}[A)]
% 1. \textit{Darcyho zákon vyjádřený pro celou zvodeň (od povrchu k nepropustnému podloží)}:
%   Průtok na jednotku šířky, $\vec q$, má v izotropním prostředí směr
%   maximálního poklesu piezometrické hladiny a co do velikosti je
%   úměrný tomuto poklesu. Koeficient úměrnosti se nazývá koeficient
%   průtočnosti nebo transmisivita a označuje se $T$.
% 1. Jak zpravidla modifikujeme předchozí odpověď, pokud zvodeň není
%   izotropní a má v různých směrech různé vlastnosti?
% 1. Často pracujeme s veličinou \textit{filtrační rychlost} $\vec v_f$, která
%   udává, jaký objem proteče jednotkovou plochou kolmo na směr proudění
%   za jednotku času. Jaký bude vztah mezi $\vec v_f$ a $\vec q$? Uvažujte pouze
%   speciální případ, kdy je $\vec v_f$ konstantní v celé tloušťce zvodnělé
%   vrstvy $b$. (Tloušťka zvodnělé vrstvy $b$ je u proudění s volnou hladinou rovna vzdálenosti piezometrické hladiny od dolní nepropustné vrstvy a u proudění mezi nepropustnými vrstvami rovna vzdálenosti těchto vrstev.) 
%   
% 1. \textit{Zákon zachování pro vodu}: Množství vody v daném místě (v metrech krychlových vody na metr čtvereční povrchu zvodně) označte $v$. Rychlost s jakou se kumuluje voda v daném místě v kubických
%   metrech (vody) na čtvereční metr (povrchu zvodně) za den, tj. derivace $v$ podle času, je
%   součtem
%   \begin{itemize}1.sep 0 pt
%   1. vydatnosti zdrojů v tomto místě ($\sigma$, v kubických
%     metrech vody na metr čtvereční povrchu zvodně za den, může se jednat například o zasakování srážek) a
%   1. rychlosti, s jakou v daném místě klesá tok $\vec q$.
% \end{itemize}
%   Vyjádřete tento zákon kvantitativně pomocí vhodné rovnice.
% 1. Objem vody v podzemí souvisí s hladinou podzemní
%   vody. \textit{Zásobnost} $S_s$ udává, jaký objem vody se uvolní na
%   metru čtverečním povrchu zvodně, pokud se piezometrická hladina
%   v tomto místě sníží o jednotku. U zvodně s volnou hladinou je tato
%   veličina dána zejména pórovitostí půdy nebo horniny, u zvodně s
%   napjatou hladinou souvisí se stlačitelností a proto je v tomto
%   případě zásobnost velmi malá. Jaká je jednotka takto definované
%   zásobnosti a jak souvisí rychlost s jakou roste objem vody v daném
%   místě zvodně s rychlostí, s jakou roste piezometrická hladina
%   v tomto místě?
% 1. Předchozí odpovědi spojte do rovnice 
%   podzemní vody v anizotropním prostředí.
% \end{enumerate}

% \textit{Podle Jacob Bear, Modeling Groundwater Flow and Pollution a Charles Fitts, Groundwater Science.}

% <div class=reseni>

% \begin{enumerate}[A)]
% 1. $\vec q=-T \nabla h$ kde $T$ je koeficient průtočnosti a $-\nabla h$
%   je vektor mířící ve směru nejrychlejšího poklesu piezometrické
%   hladiny $h$ a vyjadřující rychlost tohoto poklesu.
% 1. $T$ je  $2\times 2$ matice
% 1. $\vec q=b\vec v_f$
% 1. $\frac{\partial v}{\partial t}=\sigma-\mathop{\mathrm{div}}\vec q$
% 1. Zásobnost je vlastně změna objemu (vody) na jednotkovou plochu
%   (zvodně) vyvolaná  jednotkovou změnou délky (změna piezometrické hladiny),
%   tj. derivace $v$ podle $h$ a jednotkově vychází bez rozměru. Platí tedy
%   \begin{equation*}
%     \derivace vh=S_s \end{equation*}
%   kde $v$ je objem vody na
%   metr čtvereční povrchu zvodně v daném místě. Po vynásobení rychlostí s jakou se
%   mění piezometrická výška dostáváme
%   \begin{equation*}
%     \derivace vh \derivace ht=S_s\derivace ht
%   \end{equation*}
%    a po využití derivace složené funkce
%   \begin{equation*}
%     \derivace vt=S_s\derivace ht.
%   \end{equation*}
%   Toto se děje v libovolném místě zvodně. Protože $v$ a $h$ jsou i funkcemi proměnných $x$ a $y$ a protože souřadnice $x$ a $y$ jsou nezávislé na čase, stačí pro korektní zápis použít parciální derivace namísto obyčejné derivace, tj.
%   \begin{equation*}
%        \frac{\partial v}{\partial t} = S_s \frac {\partial h}{\partial t}.
%      \end{equation*}
% 1.
%   \begin{equation*}
%     S_s\frac{\partial h}{\partial t}=\sigma - \mathop{\mathrm{div}} \left(-T\nabla h\right)
%   \end{equation*}
%   tj. 
%   \begin{equation*}
%     S_s\frac{\partial h}{\partial t}=\sigma + \mathop{\mathrm{div}} \left(T\nabla h\right)
%   \end{equation*}

% \end{enumerate}
% </div>
% 

% ## Rovinné proudění podzemní vody podruhé

% Prozkoumáme podruhé rovinné proudění, kterému jsme se věnovali v
% příkladě \ref{pokles}.

% \begin{enumerate}[A)]
% 1. Rovnici podzemní vody ve 2D rozepište do složek. Uvažujte pro jednoduchost izotropní prostředí (transmisivita je skalární veličina, tj. ne matice a voda teče ve směru spádu piezometrické hladiny).
% 1. Napište rovnici z předchozího bodu pro \textit{stacionární} případ \textit{bez zdrojů} a pro případ, že funkce $h$ nezávisí na $y$. Uvažujte homogenní prostředí a zvodeň s volnou hladinou a vodorovnou dolní nepropustnou vrstvou, kde volíme nulovou hladinu $h$ (tj. transmisivita je tvaru $$T=kh,$$ kde $k$ je reálné číslo, ne funkce proměnných $x$ a $y$)
% 1. Ukážeme, že rovnice se dá vyřešit i bez znalosti řešení diferenciálních rovnic. Upravte vztah z předchozího bodu použitím zřejmé identity
%   $(h^2)'=2 h h'$
%   pro $h$ jako funkci proměnné  $x$, kde čárka značí derivaci podle $x$. Výsledkem bude podmínka, kterou musí splňovat funkce $h^2$ a odsud již najdete hledanou křivku snížení piezometrické hladiny. (Pokud je $h$ závislé jenom na $x$, plocha ohraničující zvodnělou vrstvu se z bočního pohledu promítne do křivky.)
% \end{enumerate}

% <div class=reseni>
% \begin{enumerate}[A)]
% 1. $$S_s\frac{\partial h}{\partial t}=\sigma + \frac{\partial }{\partial x}\left (T \frac{\partial h}{\partial x} \right)
%   +
%   \frac{\partial }{\partial y}\left (T \frac{\partial h}{\partial y} \right)
%   $$
% 1. Protože máme uvažovat stacionární případ, funkce $h$ nezávisí na $t$. Podle předpokladu $h$ nemá záviset ani na $y$. Proto platí $h=h(x)$, tj. derivace $h$ podle $t$ a podle $y$ jsou nulové.
%   Protože nemáme uvažovat zdroje, je $\sigma$ také nulové. Protože máme uvažovat homogenní případ a $T=kh$, můžeme konstantu $k$ a dát před derivaci.  Rovnice má tvar
%   $$0=k\frac{\partial }{\partial x}\left ( h\frac{\partial h}{\partial x} \right)
%   $$
%   anebo (využitím stručnějšího zápisu pro derivace funkce jedné proměnné)
%   $$0=k(h h')'.$$
% 1. Dostáváme $h h' = \frac12 (h^2)'$ a po dosazení
% $$0=k\left(\frac 12 (h^2)'\right )'.$$ Po vydělení rovnice konstantou $k$ a vynásobení faktorem $2$ dostaneme 
%   $$0=(h^2)''.$$
%   Druhá derivace funkce $h^2$ tedy musí být nula. Proto je $h^2$ nutně lineární funkcí proměnné $x$, tj. existují konstanty $C_1$ a $C_2$ tak, že platí $$h^2=C_1x+C_2.$$
%   Křivka odpovídá výsledku příkladu  \ref{pokles}, kde je
%   $$h^2=\frac{-2q}k x + \text{const.}$$
% \end{enumerate}
% </div>

-->

## Diferenciální rovnice II

## Autonomní rovnice a systémy

![Zdroj: vlastní](pokros.jpg)

### Stavebniny vedle čebínského nádraží: model

Hromada sypkého
materiálu má tvar kužele. Úhel u vrcholu je konstantní, daný
mechanickými vlastnostmi materiálu a je nezávislý na
objemu. Předpokládejme, že personál stavebnin přisypává na hromadu
materiál konstantní rychlostí (v jednotkách objemu za jednotku
času). Tato hromada je však v poměrně otevřené krajině a vítr
rozfoukává materiál po okolí. Je rozumné předpokládat, že rozfoukávání (opět v jednotkách objemu za jednotku
času)
se děje rychlostí úměrnou povrchu návětrné strany pláště.

1. Napište rovnici pro derivaci objemu hromady podle času. 
1. Existuje konstantní řešení? Pokud ano, je stabilní nebo nestabilní? Zdůvodněte.
1. Může hromada skončit i při neustálém přisypávání celá rozfoukaná?
1. Mohou pracovníci navršit hromadu do libovolné výšky anebo pro velkou hromadu je již rozfoukávání rychlejší než přisypávání?

<div class=reseni>
Rychlost s jakou se mění objem je $\frac{\mathrm dV}{\mathrm dt}$, rychlost přisypávání označme $R$, povrch návětrné strany $S$.
Podle zadání platí
$$  \frac{\mathrm dV}{\mathrm dt} = R - k_0S.$$
Protože kužel má stále stejný tvar, objem jednoznačně determinuje rozměry, povrch kužele, nebo i povrch poloviny pláště, tj. povrch návětrné strany. Z podobnosti víme, že plochy rostou s druhou mocninnou a objemy se třetí mocninou délkových rozměrů. Proto je zřejmé, že musí platit úměrnost mezi takovými mocninami těchto veličin, pro které jednotky ``pasují'', Existuje tedy konstanta taková, že $$S=k_1V^{\frac 23}.$$ Spojením těchto dvou vztahů dostáváme
$$  \frac{\mathrm dV}{\mathrm dt} = R - k V^{\frac 23},$$
kde $r$ a $k=k_0k_1$ jsou konstanty.

Označme $f(V)=R-kV^{\frac 23}$.
Konstantní řešení je řešením rovnice $f(V)=0$, tj. $$R-kV^{\frac 23}=0.$$ Odsud
$$V_0=\left(\frac{R}{k}\right)^{3/2}.$$ Protože $f$ klesá v bodě $V_0$, je toto řešení stabilní.

Protože $f(0)>0$, malá hromada vždy roste a proto nemůže skončit celá rozfoukaná. Pro malý objem je přisypávání intenzivnější než rozfoukávání.

Protože $f$ je pro velké $V$ záporná, pro velkou hromadu objem ubývá (více se rozfouká než přisype) a hromadu není možné navršit libovolně velkou. 

</div>

![Zdroj: vlastní](trolejbus.jpg)

### Časový rozestup mezi trolejbusy

Uvažujme dva trolejbusy jedoucí za sebou po stejné trati. Označme
$x(t)$ jejich časový odstup. Pokud první trolejbus zastaví na určité
zastávce v čase $t$, druhý trolejbus na tuto zastávku dorazí v čase
$x(t)$. Naším úkolem je zjistit, jak se $x(t)$ mění s\ rostoucím $t$.

Předpokládejme, že **(1)** pokud žádní pasažéři nečekají na druhý vůz, druhý vůz se
  pohybuje rychleji než první vůz a oba vozy se "sjedou", tj. $x(t)$
  klesá konstantní rychlostí, pokud na druhý vůz nečekají žádní pasažéři
**(2)** rychlost druhého vozu klesá (a rozestup roste) s rostoucím počtem pasažérů, kteří
  čekají na zastávce 
**(3)** počet pasažérů kteří čekají na zastávce roste s rostoucím
  intervalem mezi oběma vozy.

Navrhněte model pro rozestup trolejbusů, najděte stacionární řešení a posuďte jeho stabilitu.

<div class=reseni>

Situaci je možno modelovat diferenciální rovnicí
$$ 
  \frac{\mathrm dx}{\mathrm  dt}=\beta x-\alpha,
$$
kde $\alpha$ a $\beta$ jsou kladné reálné konstanty. Tato rovnice má konstantní řešení $x=\frac \alpha\beta$. Toto řešení je nestabilní, protože 
$$\frac{\mathrm d}{\mathrm dx}(\beta x-\alpha)=\beta>0.$$ Žádné jiné
konstantní řešení neexistuje a proto všechna řešení klesají na nulu
nebo neohraničeně rostou.

Vzhledem k nestabilitě stacionárního řešení nemůžeme nechat řidiče
veřejné dopravy jezdit ``jak jim to vyjde''. Situace by směřovala k
tomu, že cestující budou nejprve dlouho čekat na trolejbus a nakonec
přijede několik trolejbusů těsně za sebou. (Podle knihy P.  Blanchard,
R. L. Devaney, G.  R. Hall: Differential equations, Cengage Learning
(2006), 828 pp.)

</div>

![](kost.jpg)

### Propeptid kolagenu

Kolagen je klíčový protein pojivových tkání. Jeden z kroků při syntéze
kolagenu spočívá v reakci tří molekul propeptidu kolagenu, zkráceně
propeptidu. Tento propeptid se formuje konstantní rychlostí a kromě
toho, že je surovinou pro produkci kolagenu, se ještě rozpadá
rychlostí úměrnou koncentraci. Napište matematický model pro množství
(koncentraci) propeptidu kolagenu.

_Podle Alan Garfinkel, Jane Shevtsov, Yina Guo: Modeling Life_

<div class=reseni>

$$\frac{\mathrm dP}{\mathrm dt}=-k_1 P^3 +k_2-k_3 P$$

</div>

![Jelen a los](moose.jpg)

### Jelen a los

Uvažujme populaci jelenů a losů. Tyto populace spolu soupeří o potravu. \textbf{(1)} Bez konkurence by populace jelena rostla rychlostí $3$ a  populace losa rychlostí $2$ na jeden kus. \textbf{(2)} Vnitrodruhová konkurence se projevuje v obou populacích stejně a je rovna druhé mocnině příslušné velikosti populace. \textbf{(3)} Mezidruhová konkurence je vyjádřena členem rovným součinu velikosti populací a tato konkurence se projeví s koeficientem 0.5 v populaci losa a s koeficientem 1 v populaci jelena.

Sestavte matematický model a otestujte jej numerickým experimentem na stabilitu stacionárních bodů. Poté zdvojnásobte parametry mezidruhové konkurence a sledujte změnu odezvy. 

<div class=reseni>

$$
\begin{aligned}
  \frac{\mathrm dx}{\mathrm dt}&=3x-xy-x^2\\
    \frac{\mathrm dy}{\mathrm dt}&=2y-0.5xy-y^2
\end{aligned}
$$

[Sage](https://homepages.bluffton.edu/~nesterd/apps/slopefields.html?flags=2&dxdt=3*x%20-%20x%5E2%20-%20x*y&dydt=2*y%20-%20y%5E2%20-%200.5%20*%20x%20*%20y&x=0,4,20&y=0,3,15&method=rk4&h=0.1&f1=80-30cos(2pi%20x/24)&f2=exp(2x)&f3=zeta(x)&f4=gamma(x)&pts1=%5B0.3,0.28328571428571436%5D,%5B0.20714285714285716,0.6434928229665071%5D,%5B2.664285714285714,2.158851674641148%5D,%5B3.1714285714285713,0.7533014354066987%5D,%5B1.7785714285714285,0.2115789473684213%5D)

</div>

<!--

% \obrazek{les.jpg}

% ## Model konkurence

% Konkurence je častý jev v přírodě. Například v lese si konkurují listnaté a jehličnaté stormy z hlediska prostoru, slunečního světla a vody. Stromy se liší rychlostí růstu, nosnou kapacitou prostředí a tím, jak ovlivňují své konkurenty. Předpokládejte logistický růst v obou konkurujících si populacích, předpokládejte člen vyjadřující zbrždění vlivem konkurenta přímo úměrný velikosti obou populací  a namodelujte čtyři možné východiska modelu ()

% %https://homepages.bluffton.edu/~nesterd/apps/slopefields.html?flags=2&dxdt=0.1*x*(1-x/10000)-5*0.00001*x*y&dydt=0.25*y*(1-y/6000)-3*0.00001*x*y&x=0,10000,20&y=0,6000,15&method=rk4&h=0.1&f1=80-30cos(2pi%20x/24)&f2=exp(2x)&f3=zeta(x)&f4=gamma(x)&pts1=%5B4907.407407407408,5229.428571428572%5D,%5B7444.444444444444,3746.6985645933014%5D,%5B8407.407407407407,2633.9712918660284%5D,%5B9259.25925925926,1111.2918660287078%5D,%5B9648.148148148148,423.1578947368416%5D,%5B3240.740740740741,306.0287081339711%5D,%5B1407.4074074074074,935.5980861244016%5D,%5B4611.111111111111,203.5406698564584%5D,%5B5518.518518518518,57.129186602870504%5D
-->

![wikimedia](pustik.jpg)

### Puštík obecný

Puštík obecný se téměř výhradně živí malými hlodavci. Předpokládejme následující vztahy.
\textbf{(1)} Populace hlodavců má porodnost 0.1 na jedince a úmrtnost 0.025 na jedince za jednotku času.
\textbf{(2)} Rychlost s jakou jeden puštík konzumuje hlodavce je úměrná počtu hlodavců s kostantou úměrnosti 0.01.
\textbf{(3)} Porodnost v populaci puštíka je úměrná množství zkonzumované potravy s konstantou úměrnosti 0.05.
\textbf{(4)} Úmrtnost v populaci puštíka je 0.1 na jedince za jednotku času.

Vyjádřete tyto vztahy matematickým modelem.

_Podle Alan Garfinkel, Jane Shevtsov, Yina Guo: Modeling Life. Doslova přeloženo. Porodnost je ve skutečnosti společný efekt zvýšené porodnosti a snižené úmrtnosti v případě, že puštík má přístup k potravě._

<div class=reseni>

$$
\begin{aligned}
  \frac{\mathrm dx}{\mathrm dt}&=0.1 x-0.025x-0.01xy\\
  \frac{\mathrm dy}{\mathrm dt}&=-0.1y+0.05xy  
\end{aligned}
$$

[Sage](https://homepages.bluffton.edu/~nesterd/apps/slopefields.html?flags=2&dxdt=0.1*x%20-%200.025*x-0.01*x*y&dydt=-0.1*y+0.05*x*y&x=0,10,20&y=0,40,15&method=rk4&h=0.1&f1=80-30cos(2pi%20x/24)&f2=exp(2x)&f3=zeta(x)&f4=gamma(x)&pts1=%5B0.7894736842105263,10.577142857142857%5D,%5B1.795774647887324,12.09377990430622%5D,%5B0.7394366197183099,22.830622009569378%5D)

</div>

![Kůň Převalského](prevalski.jpg)

### Kůň Převalského

Kůň Převalského je divoký kůň ze střední Asie, jediný druh koně, který nebyl domestikován. V divočině jsou tyto koně loveni vlky. Napište matematický model založený na následujících předpokladech.
\textbf{(1)} Porodnost v populaci koní je  0.15 na jedince. \textbf{(2)} Úmrtnost v populaci koní je  0.01 na jedince.
\textbf{(3)} Vlci se živí i jinou potravou, mají tedy kladnou porodnost. Ta je 0.1 na jedince.
\textbf{(4)} Vlci mají konstantní úmrtnost 0.05 na jedince.
\textbf{(5)} Pravděpodobnost s jakou je kůň uloven vlkem je úměrná počtu vlků s konstantou úměrnosti 0.02.

_Podle Alan Garfinkel, Jane Shevtsov, Yina Guo: Modeling Life_

_Podle Wikipedie kůň Převalského přežil jenom díky péči zoologických zahrad a z rodokmenu je zřejmé, že 70 procent jedinců tohoto druhu má původní předky ze zoologické zahrady v Praze._

<div class=reseni>

$$
\begin{aligned}
  \frac{\mathrm dx}{\mathrm dt}&=0.15 x-0.01x-0.05xy\\
  \frac{\mathrm dy}{\mathrm dt}&=0.1y-0.05y  
\end{aligned}
$$

[Sage](https://homepages.bluffton.edu/~nesterd/apps/slopefields.html?flags=2&dxdt=x-x*y&dydt=-y+x*y&x=0,4,20&y=0,3,15&method=rk4&h=0.1&f1=80-30cos(2pi%20x/24)&f2=exp(2x)&f3=zeta(x)&f4=gamma(x)&pts1=%5B0.6714285714285717,0.6442105263157893%5D,%5B1.1571428571428575,0.6002870813397125%5D,%5B0.9857142857142858,1.155933014354067%5D,%5B0.7142857142857143,2.1442105263157893%5D,%5B2.992857142857143,2.01244019138756%5D,%5B2.7,1.382870813397129%5D)

</div>

<!--

% Holling
% https://homepages.bluffton.edu/~nesterd/apps/slopefields.html?flags=2&dxdt=x*(1-x/2)-y*%20x/(1+x)&dydt=-0.2*y%20+%200.7%20*%20y%20*%20x/(1+x)&x=0,1.5,15&y=0,2,15&method=rk4&h=0.05&f1=80-30cos(2pi%20x/24)&f2=exp(2x)&f3=zeta(x)&f4=gamma(x)&pts1=%5B0.19553571428571428,0.7085714285714286%5D,%5B0.23839285714285716,0.8731100478468901%5D,%5B0.38571428571428573,0.477799043062201%5D

%
% Jezera
% https://homepages.bluffton.edu/~nesterd/apps/compartmentalanalysis.html?O&S,29,F,80,10;H,0,T,290,100;M,0,T,130,200;R,0,T,325,280;O,0,T,490,230&S,H,S*15/2900;M,H,M*38/1180;H,R,H*68/850;R,O,R*85/116;O,s,O*99/393&The%20compartments%20represent%20levels%20of%20some%20pollutant%20in%20the%20Great%20Lakes.%20%28R%20%3D%20Erie%2C%20because%20E%20is%20not%20an%20allowed%20variable%20name.%29%20The%20model%20assumes%20that%20the%20initial%20concentration%20of%20the%20pollutant%20is%20the%20same%20in%20all%20the%20lakes%2C%20so%20the%20initial%20value%20is%20proportional%20to%20the%20lake%27s%20volume.%20No%20more%20of%20that%20pollutant%20is%20being%20introduced%2C%20and%20pure%20%28rain%29%20water%20flows%20in%20to%20the%20lakes%2C%20with%20the%20resulting%20mixture%20flowing%20from%20each%20lake%20into%20the%20next%2C%20and%20eventually%20to%20the%20ocean.%20From%20Fundamentals%20of%20Differential%20Equations%20%28Nagle%20and%20Saff%2C%201996%29%2C%20page%20317.

-->

### Analýza pomocí vlastních čísel

Autonomní systém
$$
\begin{aligned}
  \frac{\mathrm dx}{\mathrm dt}&= 4x^2y+y^3-5\\
  \frac{\mathrm dy}{\mathrm dt}&= 3xy^2-3y
\end{aligned}
$$
má stacionární bod $(1,1)$. Najděte Jacobiho matici v tomto bodě, vlastní čísla této matice a určete typ stacioárního bodu.

<div class=reseni>

Platí
$$
\begin{aligned}
  \frac{\partial }{\partial x}(4x^2y+y^3-5)&=8xy\\
  \frac{\partial }{\partial y}(4x^2y+y^3-5)&=4x^2+3y^2\\
  \frac{\partial }{\partial x}(3xy^2-3y)&=3y^2\\
  \frac{\partial }{\partial y}(3xy^2-3y)&=6xy-3\\
\end{aligned}
$$
a odsud
$$J(x,y)=
\begin{pmatrix}
  8xy& 4x^2+3y^2 \\ 3y^2 & 6xy-3
\end{pmatrix}.
$$
Ve stacionárním bodě dostáváme $$J(1,1)=
\begin{pmatrix}
  8 & 7\\3&3
\end{pmatrix}.
$$
Výpočtem determinantu dostáváme
$$|J-\lambda I|=
\begin{vmatrix}
  8-\lambda & 7 \\ 3 & 3-\lambda
\end{vmatrix}
=(8-\lambda)(3-\lambda)-21=\lambda^2-11\lambda +3.
$$
Kořeny jsou
$$\lambda_{1,2}=\frac{11\pm\sqrt{121-12}}{2}$$
 a oba jsou kladné. Ve stacionárním bodě proto je nestabilní uzel.

</div>

## Diferenciální rovnice druhého řádu

## Více integrálů

## Více diferenciálních rovnic

## Shrnutí


