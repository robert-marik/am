# Metody řešení diferenciálních rovnic 1

````{admonition} Anotace
Ukážeme si některé metody pro numerické řešení obyčejných i parciálních 
diferenciálních rovnic. Probereme metody jako Eulerova metoda, Runge-Kuttovy metody, metody konečných diferencí, metodu konečných prvků a další. Jako doplněk si ukážeme řešení parciálních diferenciálních rovnic Fourierovou metodou separace proměnných, která umožňuje odseparovat časovou a prostorovou složku řešení a tím lépe pochopit některé vlastnosti řešení, zejména u rovnic popisujících vlnění.
````

## Metody pro obyčejné diferenciální rovnice


### Numerické řešení IVP

manim:Diference|r_Ae2mGnfFs|Numerické řešení diferenciální rovnice je zpravidla založeno na aproximaci derivace konečnou diferencí a postupným prodlužováním řešení od počáteční podmínky směrem dopředu nebo dozadu v čase.

<div class='obtekat'>

```{figure} euler.png
 Eulerova metoda s velmi dlouhým krokem (modrou barvou) zaostává za přesným řešením (šedou  barvou). Pro lepší výsledek můžeme zmenšit krok nebo vylepšit metodu.
```

```{figure} rk.png
 Metoda Runge Kutta s velmi dlouhým krokem (modrou barvou, jde jasně  vidět aproximace lomenou čarou). Přesné řešení je nakresleno šedou  barvou.
```

</div>

Numerické řešení diferenciálních rovnic je základním nástrojem pro ukázku průběhu simulací pro dané hodnoty parametrů a počátečních podmínek. Jedná se o velice užitečnou a široce používanou činnost při inženýrských simulacích. Neprofesionálům často musí stačit použít hotové postupy, procedury a nástroje. Například [Python](https://gist.github.com/robert-marik/db46ca470720b32028e9a83da807a37c) je jednou z nejvhodnějších voleb.

<div class="volitelne">
Řešení počáteční úlohy lze numericky aproximovat poměrně snadno:
začneme v bodě zadaném počáteční podmínkou a v okolí tohoto bodu
nahradíme integrální křivku její tečnou. Tím se dostaneme do dalšího
bodu, odkud opět integrální křivku aproximujeme tečnou.  Směrnici
tečny zjistíme z diferenciální rovnice, buď přímo z derivace (Eulerova
metoda).

Vyjdeme-li z počáteční úlohy $$y'=\varphi(x,y), \quad y(x_0)=y_0,$$
má lineární aproximace řešení v bodě $[x_0,y_0]$ tvar $$y=y_0+\varphi(x_0,y_0)(x-x_0).$$
Funkční hodnotu v bodě $x=x_1$ označíme $y_1$ a tento bod bude dalším  body lomené čáry, tj. $$y_1=y_0+\varphi(x_0,y_0)(x_1-x_0).$$
Hodnota $x_1-x_0$ je krok Eulerovy metody označovaný $h$. Tento postup opakujeme s počáteční podmínkou $y(x_1)=y_1$.
Iterační formule Eulerovy metody má potom následující tvar. $$\begin{aligned}x_{n+1}&=x_n+h, \\ y_{n+1}&=y_n+\varphi(x_n,y_n)h.\end{aligned}$$

Stačí tedy mít zvolen *krok* numerické
metody (délku intervalu, na kterém aproximaci tečnou použijeme) a
výstupem metody bude aproximace integrální křivky pomocí lomené čáry.

**Vylepšení**

* Pro přesnější aproximaci je možné zjemnit krok $h$ (buď všude, nebo
  jenom tam, kde "je to potřeba").
* Pro přesnější aproximaci je možné použít místo $\varphi(x_n,y_n)$
  lepší směrnici, která dokáže zohlednit, jestli se růst zrychluje
  nebo zpomaluje (metoda Runge Kutta druhého nebo čtvrtého řádu, ...).
* Modely obsahující diferenciální rovnice obsahují zpravidla sadu
  parametrů charakterizujících fyzikální vlastnosti studovaných
  objektů. Pro numerické řešení musíme těmto parametrům dát konkrétní
  hodnoty a přicházíme tak o cennou informaci, jak řešení závisí na
  těchto parametrech. Vhodnou úpravou rovnice dokážeme počet parametrů
  eliminovat. Jednoduchým a často dostatečným způsobem je volba
  jednotek, obecnější metodou je transformace diferenciální rovnice
  uvedená v úvodní kapitole věnované diferenciálním rovnicím.

</div>

**Online řešiče ODE (numericky):**

* [Sage](https://sagecell.sagemath.org/?z=eJyFj0EKgzAQRfdC7pCdSTsVTbudO2RfREQjDY1GErXm9nU8QLv5zB_mP-YPYockMV3EfkuSZSxLo52Ap7HdOfISuKKl7WKFzxLKoqpPp8jRzDKtsDfRu8004f0Qw0mEBMcVUg7s1gbcwUx9M3s7LZGy9xr8uszrgnl0fjbNYI3r8-MFXf3kqb-82fklB9555wPmwZxUlgldXbWSRXz5j6B-SALUF0nkF_PaU9U=&lang=sage&interacts=eJyLjgUAARUAuQ==)
* [Python](https://gist.github.com/robert-marik/db46ca470720b32028e9a83da807a37c)


### Malá odbočka - zaokrouhlovací chyby v numerických výpočtech

<div class='obtekat'>

```{figure} patriot.jpg
 Součást protiraketového systému Patriot. Raketu Scud vystřelenou 25.2.1991 systém nesestřelil vinou zaokrouhlovací chyby. Zdroj: U.S. Army.
```

</div>

Uvedli jsme, že počáteční úlohu umíme vyřešit numericky. Ukázali jsme
si základní algoritmus (Eulerův) a řekli, že existují algoritmy
pokročilejší. Na tomto místě upozorníme na záludnosti skryté v
numerických výpočtech. Je iluzorní se domnívat, že zjemněním kroku při
numerickém řešení diferenciální rovnice vždy dostaneme přesnější
řešení. Toto platí jenom dokud se nedostaneme ke kritické hodnotě
kroku, kdy další snižování vede k tomu, že zpřesnění díky kratšímu
kroku se přebije akumulovanou chybou z velkého množství výpočtů nutně
zatížených zaokrouhlováním a dalším zjemňováním přesnost ztrácíme.

Zajímavá léčka je v samé podstatě výpočtů na počítači a to v
reprezentaci desetinných čísel ve dvojkové soustavě. Například číslo
0.1 je ve dvojkové soustavě periodické! Proto desetinásobným sečtením
tohoto čísla ve dvojkové soustavě nedostaneme (překvapivě) jedničku! Je to podobné, jako
bychom v námi běžně používané desítkové soustavě třikrát sečetli jednu třetinu v desetinném tvaru
reprezentovaném konečným počtem desetinných míst, tj. například
třikrát sečetli číslo $0.33333333$. Nedostaneme přesně jedničku. 

Tento efekt měl i tragický důsledek. Software protiraketového
systému Patriot počítal čas postupným přičítáním desetiny
sekundy. Protože systém byl vytvořen a testován na mobilním zařízení,
které se často restartovalo a běželo krátkou dobu, ničemu to
nevadilo. Dlouhodobé nasazení systému Patriot
ve válečné operaci na osvobození Kuvajtu   však odhalilo závažný nedostatek. Při ostrém
nasazení systém běžel dlouho a  zaokrouhlovací chyba se kumulovala
například 100 hodin. I když za tu dobu chyba dosáhla pouze zlomku
sekundy, raketa letící vysokou rychlostí již byla jinde, než systém
Patriot propočítal.  Dne 25.2.1991 systém Patriot během operace
Pouštní bouře na osvobození Kuvajtu od irácké okupace nesestřelil
útočící raketu Scud a ta zabila 28 vojáků osvobozující armády a okolo
100 osob zranila.

S chybami plynoucími ze zaokrouhlování se setkáme i při výpočtech mimo modelování diferenciálních rovnic. Viz například [Floating-point arithmetic may give
inaccurate results in
Excel](https://support.microsoft.com/en-us/help/78113/floating-point-arithmetic-may-give-inaccurate-results-in-excel).


## Metoda konečných diferencí

### Diskretizace rovnice vedení tepla pomocí konečných diferencí

Rovnice obsahující parciální derivace jsou přirozeným jazykem, kterým modelujeme fyzikální děje. To jsme viděli na rovnici vedení tepla výše a setkáme se s tím i dále. Bohužel tyto rovnice umíme ručně vyřešit jenom v poměrně speciálních případech a ani v těchto případech to není snadná práce. Proto v inženýrské praxi dáváme přednost numerickému řešení rovnice. To je založeno na numerické aproximaci derivací a převádí řešení rovnic s parciálními derivacemi na řešení lineárních rovnic. Možnosti si naznačíme na příkladu rovnice vedení tepla. Tato ukázka je důležitá pro pochopení, co nám z rovnic vlastně může vyplývat a jaké jsou zhruba požadavky na výpočetní prostředky.


<div class='obtekat'>

```{figure} finite_differences_heat.png
 Konečné diference umožňují převést parciální diferenciální rovnici na soustavu lineárních rovnic. Červený rámeček označuje neznámé hodnoty v dalším časovém kroku. U explicitní metody je tato hodnota jediná a je snadné ji vypočítat. U implicitní metody jsou neznámé hodnoty tři, každá z nich figuruje ve třech rovnicích a je nutné řešit soustavu rovnic s tridiagonální maticí.
```
</div>

Po převedení derivací z rovnice vedení tepla 
\dm $$\rho c\frac{\partial T}{\partial t}=k \frac{\partial ^2 T}{\partial x^2}$$ 
na konečné diference
bychom dostali 
\dm $$\rho c\frac{T(x,t+\Delta t)-T(x,t)}{\Delta t}= k\frac{T(x-\Delta x,t)-2T(x,t)+T(x+\Delta x,t)}{\Delta x^2},$$ 
kde $\Delta x$ a $\Delta t$ jsou intervaly oddělující body a časy, ve kterých aproximujeme teplotu. Odsud 
\dm $$T(x,t+\Delta t)=T(x,t)+\frac{k\Delta t}{\rho c (\Delta x)^2}\Bigl[T(x-\Delta x,t)-2T(x,t)+T(x+\Delta x,t)\Bigr]$$ 
a teplotu $T(x,t+\Delta t)$ v následujícím časovém okamžiku v libovolném bodě
$x$ dokážeme vypočítat ze současné teploty v tomto bodě a z teploty v sousedních
bodech $x+\Delta x$ a $x-\Delta x$. Konkrétní tvar vzorce není v této chvíli až
tak důležitý, podstatné je, že teplotu v dalším časovém okamžiku dokážeme vypočítat 
z teplot v současném čase. Proto se tato metoda nazývá explicitní metoda.

Explicitní  metodu je snadné implementovat [programovým kódem](https://gist.github.com/robert-marik/bbd7677bcf876403dcd454ab25cea681). Pokud teploty v čase $t$ uspořádáme do sloupcového vektoru $\vec T(t)$, je dokonce možno předchozí vztah zapsat pro všechny body současně jedinou maticovou rovnicí $$\vec T(t+\Delta t)=\vec T(t)+\frac{k \Delta t}{\rho c (\Delta x)^2} A \vec T(t),$$ kde $A$ je matice, která má v hlavní diagonále čísla $-2$, podél diagonály má čísla $1$ a jinak nuly s výjimkou prvního a posledního řádku, které jsou nulové. Viz [výsledný kód](https://gist.github.com/robert-marik/afa6114fe765b607ddd0c3733840e40a), kde je jenom jeden cyklus pro posun v čase a namísto cyklu přes všechny body v tyči je zde maticové násobení. 


Ještě existuje metoda [_implicitní_ metoda řešení](https://en.wikipedia.org/wiki/Finite_difference_method#Example:_The_heat_equation) založená na zpětné diferenci v čase namísto dopředné, tj. 
\dm $$\frac{\partial T(x,t)}{\partial t}=\frac{T(x,t)-T(x,t-\Delta t)}{\Delta t}$$
a odsud 
\dm $$T(x,t) = T(x,t-\Delta t) +\frac{k\Delta t}{\rho c (\Delta x)^2}\Bigl[T(x-\Delta x,t)-2T(x,t)+T(x+\Delta x,t)\Bigr].$$
Toto vztah umožňující výpočet teplot v čase $t$ z teplot v čase $t-\Delta t$.
Programová realizace je založena na řešení rovnice a může vypadat
[následovně.](https://gist.github.com/robert-marik/8b898a66ee7018b4a72dc40dc20e1a94)
Obsahuje pro každý časový krok řešení soustavy lineárních rovnic s tridiagonální maticí (nenulová
čísla jsou na hlavní diagonále a vedle ní).

Rozdíl mezi implicitní a explicitní metodou je v tom, že u explicitní metody
máme v každé rovnici jednu neznámou a tuto neznámou je snadné určit. Formálně
metoda vede na soustavu rovnic, ale řešení této soustavy je triviální. Oproti
tomu u 
implicitní metody máme v každém vztahu tři neznámé a řešení soustavy rovnic
je komplikovanější. Zdá se tedy, že explicitní metoda je výhodnější. Bohužel
v praxi explicitní metoda vyžaduje dostatečně jemný časový krok, což může vést k
nutnosti použít velmi jemnou časovou diskretizaci a tato skutečnost navyšuje
výpočetní náročnost jak z hlediska času, tak i z hlediska paměťových nároků.
Implicitní metoda je sice komplikovanější na výpočet, ale dovoluje použít větší
časové kroky a v praxi se ukazuje jako výhodnější. Často se pro zvýšení
přesnosti používá i kombinace obou metod, kdy je v diferenčním schematu použita
dopředná i zpětná diference pro derivaci podle času a obě jsou vhodně
zkombinovány ([Crank-Nicolsonova metoda](https://en.wikipedia.org/wiki/Crank%E2%80%93Nicolson_method)).

## Metoda konečných prvků

Metoda konečných prvků je jedna z nejběžnějších numerických metod pro řešení
diferenciálních rovnic v inženýrských aplikacích. Ukážeme si základní myšlenky
této metody na jednoduchém příkladu
rovnice 
$$-\frac{\mathrm d^2 u}{\mathrm dx^2}=f(x)\tag{E}$$
s okrajovými podmínkami $u(0)=u(1)=0.$
Tato rovnice může vystupovat například při modelování teplotního pole v tyči, ve
které jsou zdroje tepla popsané funkcí $f(x)$. Z praktického hlediska je snadné
rovnici vyřešit přímo integrací, ale pro ilustraci metody konečných prvků je
tento příklad vhodný. Metoda je obecná a použitelná i pro složitější rovnice ve
vícedimenzionálním prostoru, kde analytické metody selhávají: buď jsou
nepoužitelné, nebo vedou na řešení zapsané pomocí komplikovaných speciálních
funkcí a nekonečných řad, s nimiž se v praxi špatně pracuje.

### Slabá formulace rovnice

Nejprve převedeme rovnici na tzv. slabou formulaci. To je formulace, kde
nevystupuje druhá derivace funkce $u$, ale jenom derivace první. To umožní
pracovat například s úlohami vedení tepla, kde se materiálové vlastnosti mění
skokem. Kromě toho slabá formulace převádí úlohu na úlohu integrální, což je
výhodné pro numerické metody. Na tuto výhodu se zaměříme a proto nebudeme
rozebírat aspekty spojené s hladkostí funkcí. Budeme předpokládat, že funkce, se
kterými pracujeme, jsou dostatečně hladké.

Použijeme základní poznatky z integrálního počtu a derivaci součinu
funkcí $u'$ a $v$
$$(u'v)'=u''v+u'v',$$
která má po integraci na intervalu $[a,b]$ podobu
$$u'(b)v(b)-u'(a)v(a)=\int_a^b u''v\,\mathrm dx +\int_a^b u'v'\,\mathrm dx.$$
Pokud funkce $v$ splňuje okrajové podmínky $v(a)=v(b)=0$, dostaneme
$$-\int_a^b u''v\,\mathrm dx = \int_a^b u'v'\,\mathrm dx.\tag{*}$$

Nyní přistoupíme k převodu rovnice (E) na obecnější formulaci. Rovnici napíšeme pro jednoduchost s derivacemi vyjádřenými čárkami a s
vynechanou závislostí na $x$
$$-u''=f$$
a tuto rovnici vynásobíme funkcí $v$, která splňuje okrajové podmínky
$v(0)=v(1)=0$. Výslednou rovnici 
$$-u''v=fv$$
integrujeme přes interval $[0,1]$.
Tím dostaneme
$$-\int_0^1 u''v\,\mathrm dx = \int_0^1
fv\,\mathrm dx.$$
Ze vztahu (*) poté plyne, že získanou rovnost můžeme přeformulovat na tvar
$$\int_0^1 u'v'\,\mathrm dx = \int_0^1
fv\,\mathrm dx. \tag{W}$$
Pokud nějaká funkce $u$ splňuje tuto rovnost pro každou hladkou funkci $v$
s okrajovými podmínkami $v(0)=v(1)=0$, říkáme, že $u$ je _slabým řešením_
rovnice (E) (s uvažovanými okrajovými podmínkami). Rovnice (W) se nazývá _slabá
formulace_  (angl. _weak form_) rovnice (E). Slabá formulace rovnice úzce
souvisí s hledáním minima energie nebo obecněji nějaké vhodné veličiny
související s úlohou a proto ji řadíme mezi _variační metody_. Proto se slabá
formulace někdy nazývá _variační formulace_.

### Galerkinova metoda

Vyjdeme ze slabé variační formulace (W) a budeme hledat přibližné řešení ve tvaru
$$u(x)=\sum_{i=1}^n u_i \varphi_i(x),$$
kde funkce $\varphi_i(x)$ jsou zvolené hladké funkce splňující okrajové podmínky
$\varphi_i(0)=\varphi_i(1)=0$ a $u_i$ jsou neznámé koeficienty, které budeme
určovat. 
To vlastně znamená, že hledáme řešení v podprostoru generovaném funkcemi
$\varphi_i(x)$. Funkce $\varphi_i(x)$ se proto nazývají _bázové funkce_.
Pro snadné odlišení funkcí a koeficientů už nebudeme vynechávat závislost
na $x$.

Derivace funkce $u(x)$ je
$$u'(x)=\sum_{j=1}^n u_j \varphi_j'(x).$$
Dosadíme-li toto vyjádření do slabé formulace (W), dostaneme
$$\int_0^1 \Bigl(\sum_{j=1}^n u_j \varphi_j'(x)\Bigr) v'(x)\,\mathrm dx = \int_0^1 
f(x)v(x)\,\mathrm dx.$$
Využitím linearity integrálu je možné rovnici přepsat do tvaru
$$\sum_{j=1}^n u_j \int_0^1 \varphi_j'(x) v'(x)\,\mathrm dx = \int_0^1
f(x)v(x)\,\mathrm dx.$$

Galerkinova metoda spočívá v tom, že za funkci $v(x)$ volíme postupně jednotlivé bázové funkce, tedy $v(x)=\varphi_i(x)$ pro $i=1,2,\ldots,n$. Tím dostaneme soustavu rovnic
$$\sum_{j=1}^n u_j \int_0^1 \varphi_j'(x) \varphi_i'(x)\,\mathrm dx = \int_0^1
f(x)\varphi_i(x)\,\mathrm dx, \quad i=1,2,\ldots,n$$
nebo po přeznačení 
$$a_{ij}=\int_0^1 \varphi_i'(x) \varphi_j'(x)\,\mathrm dx$$
a
$$b_j=\int_0^1 f(x)\varphi_j(x)\,\mathrm dx$$
ve tvaru $$\sum_{j=1}^n a_{ij} u_j = b_i, \quad i=1,2,\ldots,n.$$
Nyní už je patrné, že se jedná o soustavu lineárních rovnic a po zavedení matice
$A=(a_{ij})$ a vektoru $\vec b=(b_i)$ můžeme tuto soustavu psát v maticovém
tvaru $$A\vec u=\vec b.$$
Matice $A$ se nazývá (z historických důvodů) _matice tuhosti_ a vektor $\vec b$
se nazývá _vektor zatížení_.


<div class='obtekat'>

```{figure} konecne_prvky.png
Bázové funkce pro metodu konečných prvků na intervalu [0,1] s dělením na deset dílčích intervalů.  V obrázku jsou vybrány tři bázové funkce a lineární kombinace bázových funkcí aproximující parabolu $y=2x(1-x)$.
```

</div>


Je účelné volit bázové funkce tak, aby na jednu stranu generovaly dostatečně
širokou škálu funkcí, ale také aby byla matice $A$ vhodná pro numerické řešení &mdash; například, aby byla řídká.
Vhodnou volbou jsou trojúhelníkové funkce dle připojeného obrázku. Pomocí lineární kombinace těchto funkcí je možné
vyjádřit libovolnou po částech lomenou funkci splňující nulové okrajové
podmínky. Při takto zvolených funkcích je $a_{ij}$ nulové, pokud se $i$ a $j$
liší více než o jedničku a
matice $A$ má nenulové prvky jenom na hlavní diagonále a na dvou přilehlých
diagonálách (je tridiagonální). Výpočet integrálů pro $a_{ij}$ vede k následující matici.

$$
A = \frac 1h\begin{pmatrix}
2 & -1 & 0 & 0 & \cdots & 0 \\
-1 & 2 & -1 & 0 & \cdots & 0 \\
0 & -1 & 2 & -1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & -1 & 2 & -1 \\
0 & 0 & 0 & 0 & -1 & 2
\end{pmatrix}
$$

### Metoda konečných prvků (FEM)

<div class='obtekat'>

```{figure} nosnik_3bodovy.png
 Ukázka programu pro modelování pomocí metody konečných prvků (FEM). V tomto případě je modelován tříbodově podepřený nosník zatížený silou uprostřed. Program umožňuje měnit parametry nosníku a zatížení a okamžitě vidět výsledky a identifikovat kritická místa konstrukce.
```

```{figure} beam_smyk.png
  Smykové namáhání není symetrické, ale antisymetrické.
```

</div>

Výše uvedený postup tvoří jádro metody konečných prvků (angl. _finite element
method_, FEM). Problém je nejprve
naformulován obecněji než v původní diferenciální rovnici (*slabá variační formulace*) a
poté je hledáno přibližné řešení v podprostoru generovaném zvolenými bázovými
funkcemi. Dosazením tohoto tvaru řešení do slabé formulace a volbou testovacích
funkcí
je získána soustava lineárních rovnic pro neznámé 
koeficienty v rozvoji řešení podle bázových funkcí. Tuto soustavu je
poté možné vyřešit běžnými numerickými metodami pro řešení soustav lineárních
rovnic.

Uvedený postup je možné zobecnit na složitější rovnice a úlohy. Na rozdíl od
analytických metod si metoda konečných poradí i s komplikovanějšími geometrickými tvary a
nespojitými materiálovými vlastnostmi, kdy na sebe navazují dva odlišné
materiály. Je možné metodu použít i pro nelineární rovnice, i když v
tomto případě je výpočet numericky náročnější.

Výhodou metody konečných prvků oproti metodě konečných diferencí je větší
volnost diskretizaci. Metoda konečných diferencí vyžaduje pravidelnou síť bodů,
kdežto metoda konečných prvků umožňuje využít nepravidelnou síť a přizpůsobit
hustotu bodů místním potřebám. To je výhodné například při zjemnění
diskretizace v místech, kde se očekávají velké změny řešení.

Matematicky se například při řešení úlohy statické rovnováhy používá popis stavu
napjatosti a deformace pomocí tenzorů napětí ($\sigma$) a deformace ($\varepsilon$). 

<div class='obtekat'>

```{figure} stress.svg
  Tenzor napětí $\sigma$ popisuje vnitřní síly v tělese. Komponenty jsou síly působící na jednotku plochy a rozlišujeme normálové a smykové síly.
```

</div>

Tenzor napětí udává normálovou nebo tečnou sílu působící v tělese na jednotku
plochy. Zpravidla tyto síly modelujeme na reprezentativním elementu tělesa ve
tvaru krychle.

$$
\sigma = \begin{pmatrix}
\sigma_x & \sigma_{xy} & \sigma_{xz}\cr
\sigma_{xy} & \sigma_y & \sigma_{yz}\cr
\sigma_{xz} & \sigma_{xy} & \sigma_{z}
\end{pmatrix}
$$

Tenzor deformace popisuje, jak těleso mění tvar. I zde sledujeme normálové a
smykové komponenty. Ty jsou definovány pomocí vektoru posunutí $\vec u(x,y,z)$
vztahem 

$$\varepsilon_{ij} = \frac{1}{2}\left(\frac{\partial u_i}{\partial x_j} +
\frac{\partial u_j}{\partial x_i}\right)$$

$$
\varepsilon = \begin{pmatrix}
\varepsilon_x & \varepsilon_{xy} & \varepsilon_{xz}\cr
\varepsilon_{xy} & \varepsilon_y & \varepsilon_{yz}\cr
\varepsilon_{xz} & \varepsilon_{xy} & \varepsilon_{z}
\end{pmatrix}
$$

Vztah mezi napětím a deformací (Hookův zákon) je pro lineární materiály dán vztahem
$$\sigma_{ij} = \sum_{k,l}C_{ijkl} \varepsilon_{kl},$$
kde $C_{ijkl}$ jsou materiálové konstanty, které charakterizují materiálové
vlastnosti tělesa. Pro praktické účely je vhodnější tenzory přepsat použitím
Voigtovy notace na vektory 

$$\varepsilon = \left(
    \begin{matrix}
    \varepsilon_x \\
    \varepsilon_y \\
    \varepsilon_z \\
    \varepsilon_{yz} \\
    \varepsilon_{xz} \\
    \varepsilon_{xy}
     \end{matrix} 
\right)
\quad \text{a} \quad
\sigma = \left(
     \begin{matrix}
    \sigma_x \\
    \sigma_y \\
    \sigma_z \\
    \sigma_{yz} \\
    \sigma_{xz} \\
    \sigma_{xy} 
     \end{matrix}
\right).
$$

Hookův zákon potom zpravidla píšeme ve tvaru obsahujícím dobře měřitelné
materiálové parametry, jako jsou Youngův modul pružnosti $E$, smykový modul $G$ a Poissonův poměr
$\nu$.

$$
\left(
    \begin{matrix}
    \varepsilon_x \\
    \varepsilon_y \\
    \varepsilon_z \\
    \varepsilon_{yz} \\
    \varepsilon_{xz} \\
    \varepsilon_{xy}
     \end{matrix} 
\right)
=
\left(
    \begin{matrix}
    \frac 1{E_x} & -\frac{\nu_{yx}}{E_y} & -\frac{\nu_{zx}}{E_z} & 0 & 0 & 0 \\
     & \frac 1{E_y} & -\frac{\nu_{zy}}{E_z} & 0 & 0  & 0 \\
     &  & \frac 1{E_z} & 0 & 0 & 0 \\
     &  & & \frac 1{G_{yz}} & 0 & 0 \\
     \rlap{\text{symmetric}} & & &  & \frac 1{G_{xz}} & 0 \\
     &  &  &  &  & \frac 1{G_{xy}} \\
     \end{matrix} 
\right)
\left(
     \begin{matrix}
    \sigma_x \\
    \sigma_y \\
    \sigma_z \\
    \sigma_{yz} \\
    \sigma_{xz} \\
    \sigma_{xy} 
     \end{matrix}
\right)
$$

Poznamenejme, diagonálnost pravého dolního rohu plyne z poznatku, že pro většinu
materiálů se smykové namáhání projevuje pouze smykovou deformací v rovině, ve
které působí.

Při vhodné volbě souřadné soustavy se smykové namáhání neprojevuje normálovou
deformací a normálové namáhání se neprojevuje smykovou deformací. Proto
zpravidla předpokládáme, že pravý horní a levý dolní blok matice v Hookově
zákonu je nulový. 

Pro statickou rovnováhu platí, že vnitřní síly musí být v rovnováze s vnějšími
silami, což se matematicky vyjadřuje pomocí rovnic kontinuity. Tyto rovnice mají
tvar $$\sum_{j}\frac{\partial \sigma_{ij}}{\partial x_j} + f_i = 0,$$ kde $f_i$ jsou
$i$-té komponenty objemové síly působící na těleso. Pro řešení této rovnice
pomocí metody konečných prvků je nutné převést ji na slabou formulaci, což
zahrnuje integraci a použití vhodných testovacích funkcí. Po diskretizaci pomocí
bázových funkcí a volbě testovacích funkcí se získá soustava lineárních rovnic
pro neznámé koeficienty v rozvoji řešení podle bázových funkcí, kterou je možné
numericky vyřešit.




````{admonition} Poznámka.
:nonumber:
Metodu podrobněji rozebereme a zařadíme do širšího kontextu numerických metod při studiu numerických metod pro parciální diferenciální rovnice v poslední přednášce semestru.
````

