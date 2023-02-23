# Křivkový integrál pomocí potenciálu, Greenova věta, rovnice kontinuity

> Anotace.
>
> * V úvodních příkladech ilustrujeme výpočet křivkového integrálu pomocí kmenové funkce. Příkladů je několik, aby se zapsalo do paměti to nejdůležitější: že se křivkový integrál dá v některých případech vypočítat snadno pomocí kmenové funkce. Jak konkrétně postupovat je již dovednost navazující.
> * Greenova věta pro nás bude mít spíše teoretický význam. Umožňuje přepis křivkového integrálu na dvojný. Vlastní použití není těžké a osaháme si jej i v domácích úlohách. I zde je důležité v první řadě vědět, že to jde a teprve potom přemýšlet nad tím, jak konkrétně se to dělá.
> * V příkladě se vrátíme i k difuzní rovnici.


## Křivkový integrál pomocí kmenové funkce

https://youtu.be/-VCnGpRz3K0

Určete, pro jakou hodnotu parametru $a\in \mathbb R$ křivkový integrál vektorového pole $$\vec F=ax^2y\vec\imath + (x^3+1)\vec\jmath$$ po křivce $C$, tj. $$\int_C ax^2y\,\mathrm dx+(x^3+1)\,\mathrm dy$$ nezávisí na integrační cestě v $\mathbb R^2$. Najděte kmenovou funkci příslušného vektorového pole a vypočtěte křivkový integrál po křivce z bodu $[0,0]$ do bodu $[1,2]$.

```{prf:example} Řešení
:class: dropdown
:nonumber:


Podmínka pro nezávislost na integrační cestě je $$
\begin{aligned}
0&=\nabla \times  \vec F=\begin{vmatrix}
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
Kmenová funkce $\varphi(x,y)$ vektorového pole $\vec F=(3x^2y,x^3+1)$ splňuje
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


```

## Křivkový integrál pomocí kmenové funkce 2

https://youtu.be/WtLoQ79wUdo

Pro jakou hodnotu parametru $m$ je křivkový integrál
$$\int (6x^2y+x+y)\,\mathrm dx+(mx^3+x)\,\mathrm dy$$ nezávislý na
integrační cestě v $\mathbb R^2$? Vypočtěte hodnotu tohoto integrálu
po křivce z bodu $(2,1)$ do bodu $(1,3)$.

```{prf:example} Řešení
:class: dropdown
:nonumber:


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

```


## Kmenová funkce pomocí křivkového integrálu


https://youtu.be/y-gTOlGVRXI

Ukažte, že vektorové pole
$\vec F=(6x^2y+x+y,2x^3+x)$ má kmenovou funkci. Vypočtěte z definice křivkový integrál v tomto vektorovém poli po křivce $\vec r(t)=(at,bt)$, $t\in[0,1]$, tj. po úsečce z počátku do bodu $(a,b)$ a ukažte, že tímto způsobem obdržíme kmenovou funkci.

Toto je metoda, jak určit skalární potenciál z numerických dat. Pokud je vektorové pole dáno numericky, je hledání skalárního potenciálu integrováním těžce realizovatelné. Ale derivováním a výpočtem rotace je jednoduché zkontrolovat podmínku existence skalárního potenciálu a poté se dá hodnota skalárního potenciálu v libovolném bodě počítat pomocí křivkového integrálu vedoucího z počátku do daného bodu.


```{prf:example} Řešení
:class: dropdown
:nonumber:

Platí $$\pdv{y}\qty(6x^2y+x+y)=6x^2+1=\pdv{x}\qty(2x^3+x)$$
a proto kmenová funkce existuje.

Derivací křivky dostáváme rovnici tečného vektoru
$$\frac{\mathrm d\vec r}{\mathrm dt}=(a,b)$$
a dosazením křivky do vektorového pole
$$\vec F(\vec r(t))=(6a^2t^2bt+at+bt,2a^3t^3+at)=(6a^2bt^3+at+bt,2a^3t^3+at).$$
Skalární součin je daný vztahem
$$\vec F\frac{\mathrm d\vec r}{\mathrm dt}=a(6a^2bt^3+at+bt)+b(2a^3t^3+at)=8a^3b t^3+a^2t+2abt.
$$
Křivkový integrál je tedy roven
$$\int_C \vec F\,\mathrm d\vec r=\int_0^1 8a^3b t^3+a^2t+2abt\,\mathrm dt=\qty[2a^3bt^4+\frac 12 a^2 t^2+abt^2]_0^1=2a^3b+\frac 12 a^2+ab.
$$
Podle věty o nezávislosti křivkového integrálu na integrační cestě máme
$$\varphi(a,b)-\varphi(0,0)=2a^3b+\frac 12 a^2+ab$$
a odsud
$$\varphi(a,b)=2a^3b+\frac 12 a^2+ab+\varphi(0,0),$$
neboli (po přejmenování proměnných a zavedení konstanty $C$ místo $\varphi(0,0)$)
$$\varphi(x,y)=2x^3y+\frac 12 x^2+xy+C.$$

```

## Greenova věta

https://youtu.be/J6BVkOzg0mg

Určete integrál $$\oint_C \vec F\,\mathrm d\vec r$$ po křivce, která je kladně orientovanou hranicí jednotkového čtverce s vrcholy v bodech $(0,0)$, $(1,0)$, $(0,1)$, $(1,1)$ pro vektorovou funkci $$\vec F=x^7\vec i+xy\vec j.$$

```{prf:example} Řešení
:class: dropdown
:nonumber:


$$
\begin{aligned}
  \oint_C \vec F\,\mathrm d\vec r
  &=  \oint_C x^7\,\mathrm dx+ xy\,\mathrm dy\\&  =\int_0^1 \int_0^1 \frac{\partial}{\partial x}(xy)-\frac{\partial}{\partial y}(x^7) \,\mathrm dy\mathrm dx\\
  &=\int_0^1 \int_0^1 y \,\mathrm dy\mathrm dx\\& =\int_0^1 y \,\mathrm dy \times \int_0^1 \,\mathrm dx \\&= \left[\frac 12 y^2\right]_0^1 \times 1\\&= \frac 12
\end{aligned}
$$

```

## Rovnice vedení tepla v materiálech různých vlastností

https://youtu.be/CKZNkuyDd5Y

Rovnice vedení tepla v ortotropním materiálu umístěném do souřadné soustavy tak,
aby vlastní směry tenzoru tepelné vodivosti (jako např. anatomické směry dřeva)
byly ve směru souřadnicových os má nejobecnější možné vyjádření
$$c\rho\pdv{T}{t}=\pdv{x}\qty(\lambda_x\pdv{T}{x} )+\pdv{y}\qty(\lambda_y\pdv{T}{y}) . $$
Za jakých okolností je možno veličiny $\lambda_x$ a $\lambda_y$ napsat před vnější derivaci tak, aby v rovnici vznikly druhé derivace? 


```{prf:example} Řešení
:class: dropdown
:nonumber:


V případě, že tyto veličiny nezávisí na poloze. Materiál tedy musí být homogenní. Závislost na poloze nesmí být ani zprostředkovaná přes teplotu. Tyto veličiny tedy nesmí být ani funkcemi teploty. Jinými slovy, konstanta úměrnosti ve Fourierově zákoně se nesmí měnit s teplotou, vztah z Fourierova zákona musí být přesně lineární a takové materiály se nazývají materiály s lineární materiálovou odezvou (zkráceně lineární materiály). Veličiny  $\lambda_x$ a $\lambda_y$  se dají napsat před vnější derivace pouze pokud je materiál homogenní a lineární.

```


## Stacionární vedení tepla v žebru chladiče

https://youtu.be/zvs3TsvBrho

![pixabay.com](chladic.jpg)

Někdy jsme nuceni do rovnice vedení tepla zahrnout i zdroje.
Modelujte vedení tepla jednom v žebru chladiče.

Úlohu uvažujte jako jednorozměrnou, materiál homogenní izotropní s
konstantní tepelnou vodivostí. Kolem chladiče proudí vzduch o teplotě
$T_0$ a tím se chladič ochlazuje. V místě, kde je teplota chladiče
vysoká je proces odevzdávání tepla do okolí intenzivnější. Obvykle se
předpokládá, že v každém místě chladič ztrácí teplo rychlostí úměrnou
rozdílu teploty v daném místě a teploty okolního vzduchu. (Koeficient
úměrnosti je dán koeficientem přestupu tepla a šířkou žebra). Uvažujte
stacionární děj.

```{prf:example} Řešení
:class: dropdown
:nonumber:


$$0=-h(T-T_0)+\frac{\mathrm d}{\mathrm dx}\left(\lambda \frac{\mathrm dT}{\mathrm dx}\right)$$

Protože máme konstantní tepelnou vodivost (a homogenita je v kovech splněna přirozeně), je možné místo kvaziderivace použít druhou derivaci.

$$0=-h(T-T_0)+\lambda \frac{\mathrm d^2T}{\mathrm dx^2}$$

Ke stejnému závěru je možné dojít i přesnou analýzou ve 3D, viz Cengel, Heat transfer, kapitola 3–6 Heat transfer from finned surfaces.

Máme rovnici, kde neznámou je funkce a v rovnici figuruje druhá derivace této funkce. Takové rovnice se naučíme řešit na konci semestru. To nám odpoví na otázku, zda teplota bude podél chladiče klesat lineárně, nebo exponenciálně či nějak jinak.

```

