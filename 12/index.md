# Numerické metody pro diferenciální rovnice

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


<div class="shorten" data-text="Konečné diference je možné použít k převedení parciální diferenciální rovnice (úloha v počítači obtížně řešitelná) na soustavu lineárních rovnic (úloha snadno řešitelná na počítačích).">

Rovnice obsahující parciální derivace jsou přirozeným jazykem, kterým modelujeme fyzikální děje. To jsme viděli na rovnici vedení tepla výše a setkáme se s tím i dále. Bohužel tyto rovnice umíme ručně vyřešit jenom v poměrně speciálních případech a ani v těchto případech to není snadná práce. Proto v inženýrské praxi dáváme přednost numerickému řešení rovnice. To je založeno na numerické aproximaci derivací a převádí řešení rovnic s parciálními derivacemi na řešení lineárních rovnic. Možnosti si naznačíme na příkladu rovnice vedení tepla. Tato ukázka je důležitá pro pochopení, co nám z rovnic vlastně může vyplývat a jaké jsou zhruba požadavky na výpočetní prostředky.

#### Diskretizace rovnice vedení tepla pomocí konečných diferencí

<div class='obtekat'>

```{figure} finite_differences_heat.png
 Konečné diference umožňují převést parciální diferenciální rovnici na soustavu lineárních rovnic. Červený rámeček označuje neznámé hodnoty v dalším časovém kroku.
```
</div>

Po převedení derivací z rovnice vedení tepla 
\dm $$\rho c\frac{\partial T}{\partial t}=k \frac{\partial ^2 T}{\partial x^2}$$ 
na konečné diference
bychom dostali 
\dm $$\rho c\frac{T(x,t+\Delta t)-T(x,t)}{\Delta t}= k\frac{T(x-\Delta x,t)-2T(x,t)+T(x+\Delta x,t)}{\Delta x^2},$$ 
kde $\Delta x$ a $\Delta t$ jsou intervaly oddělující body a časy, ve kterých aproximujeme teplotu. Odsud 
\dm $$T(x,t+\Delta t)=T(x,t)+\frac{k\Delta t}{\rho c (\Delta x)^2}\Bigl[T(x-\Delta x,t)-2T(x,t)+T(x+\Delta x,t)\Bigr]$$ 
a teplotu $T(x,t+\Delta t)$ v následujícím časovém okamžiku v libovolném bodě $x$ dokážeme vypočítat ze současné teploty v tomto bodě a z teploty v sousedních bodech $x+\Delta x$ a $x-\Delta x$. Toto je vzorec pro takzvanou _explicitní_ metodu řešení rovnice vedení tepla a tuto metodu je snadné implementovat [programovým kódem](https://gist.github.com/robert-marik/bbd7677bcf876403dcd454ab25cea681). Pokud teploty v čase $t$ uspořádáme do sloupcového vektoru $\vec T(t)$, je dokonce možno předchozí vztah zapsat pro všechny body současně jedinou maticovou rovnicí $$\vec T(t+\Delta t)=\vec T(t)+\frac{k \Delta t}{\rho c (\Delta x)^2} A \vec T(t),$$ kde $A$ je matice, která má v hlavní diagonále čísla $-2$, podél diagonály má čísla $1$ a jinak nuly s výjimkou prvního a posledního řádku, které jsou nulové. Viz [výsledný kód](https://gist.github.com/robert-marik/afa6114fe765b607ddd0c3733840e40a), kde je jenom jeden cyklus pro posun v čase a namísto cyklu přes všechny body v tyči je zde maticové násobení. 
>
>
Ještě existuje metoda [_implicitní_ metoda řešení](https://en.wikipedia.org/wiki/Finite_difference_method#Example:_The_heat_equation) založená na zpětné diferenci v čase namísto dopředné, tj. 
\dm $$\frac{\partial T(x,t)}{\partial t}=\frac{T(x,t)-T(x,t-\Delta t)}{\Delta t}$$
a odsud 
\dm $$T(x,t) = T(x,t-\Delta t) +\frac{k\Delta t}{\rho c (\Delta x)^2}\Bigl[T(x-\Delta x,t)-2T(x,t)+T(x+\Delta x,t)\Bigr].$$
Toto vztah umožňující výpočet teplot v čase $t$ z teplot v čase $t-\Delta t$. Programová realizace je založena na řešení rovnice a může vypadat [následovně.](https://gist.github.com/robert-marik/8b898a66ee7018b4a72dc40dc20e1a94)

Rozdíl mezi implicitní a explicitní metodou je v tom, že u explicitní metody máme v rovnici jednou neznámou a tuto neznámou je snadné určit. Formálně tedy metoda vede na soustavu rovnic, ale řešení této soustavy je triviální. U implicitní metody však máme v každém vztahu tři neznámé a řešení soustavy rovnic je již komplikovanější. Zdá se tedy, že explicitní metoda je výhodnější. Bohužel v praxi explicitní metoda vyžaduje dostatečně jemný časový krok, což může vést k nutnosti použít velmi jemnou časovou diskretizaci a tato skutečnost navyšuje výpočetní náročnost jak z hlediska času, tak i z hlediska paměťových nároků. Implicitní metoda je sice komplikovanější na výpočet, ale dovoluje použít větší časové kroky a v praxi se ukazuje jako výhodnější. Často se pro zvýšení přesnosti používá i kombinace obou metod, kdy je v diferenčním schematu použita dopředná i zpětná diference pro derivaci podle času.

</div>

<!--

% Rovnice vedeni tepla pro jednorozmernou tyc s fixovanymi teplotami na koncich a konstantni pocatecni teplotou.
% Teplota se v tyci rozlozi rovnomerne (linearni profil).
% Teplotni profil pred dosazenim rovnovazenho stavu pro ruzne casy ziskame z rovnice vedeni tepla.
% Nize je aproximace reseni pomoci konecnych diferenci explicitni metodou - jednoducha na implementaci, ale nestabilni, pokud neni casovy krok dostatecne maly

% 
%  Nastaveni
%

L = 1;       % delka tyce

nx = 50;     % pocet bodu v tyci, ve kterych budeme pocitat teplotu
nt = 500;    % pocet kroku v case
dx = L/nx;   % prostorovy krok (vzdalenost dvou sousednbich bodu)
dt = .0001;  % casovy krok, interval s jakzm budeme v danem bode sledovat zmeny teplo
             % casovy krok musi byt dostatecne maly, jinak model neni stabilni

u = zeros(nt+1,nx+1);      % inicializace promenne, do ktere budeme ukladat teploty

T = 0*ones(1,nx+1);  % nastaveni pocatecnich hodnot, nulove teploty vsude krome na nakonci
T(end) = 100;      % nastaveni pocatecnich hodnot, teplota 100 na konci

u(1,1:nx+1) = T;    % vychozi stav

A = toeplitz([-2,1,zeros(1,nx-1)]);  % vytvoreni matice pro iterace
A(1,:) = zeros(1,nx+1);              % vynulovani prvniho radku matice A
A(end,:) = zeros(1,nx+1);            % vynulovani posledniho radku matice A

%
%  Vlastní výpočet a uložení do paměti
%

for j = 2:nt        % jednotlive kroky v case
   T = T + dt/(dx^2) * (A * T')';  % iteracni vzorec pouziva dvakrat transpozice, protoze pracujeme s radkovym vektorem, ale maticove nasobeni funguje pro sloupcove vektory
   u(j+1,1:nx+1) = T;    % ulozeni pro pozdejsi vykresleni
end
 

%
% Vykreslení řešení
%

[X1,T1] = meshgrid(0:dx:nx*dx,0:dt:nt*dt);
colormap hot
pcolor(X1,T1,u)

shading interp
colorbar
title('Vyvoj prubehu teploty v tyci')
xlabel('x')
ylabel('t')

-->

<!--

% Rovnice vedeni tepla pro jednorozmernou tyc s fixovanymi teplotami na koncich a konstantni pocatecni teplotou.
% Teplota se v tyci rozlozi rovnomerne (linearni profil).
% Teplotni profil pred dosazenim rovnovazenho stavu pro ruzne casy ziskame z rovnice vedeni tepla.
% Nize je aproximace reseni pomoci konecnych diferenci explicitni metodou - jednoducha na implementaci, ale nestabilni, pokud neni casovy krok dostatecne maly

% 
%  Nastaveni
%

L = 1;       % delka tyce

nx = 50;     % pocet bodu v tyci, ve kterych budeme pocitat teplotu
nt = 500;    % pocet kroku v case
dx = L/nx;   % prostorovy krok (vzdalenost dvou sousednbich bodu)
dt = .0001;  % casovy krok, interval s jakzm budeme v danem bode sledovat zmeny teplo
             % casovy krok musi byt dostatecne maly, jinak model neni stabilni

u = zeros(nt+1,nx+1);      % inicializace promenne, do ktere budeme ukladat teploty

T = 0*ones(1,nx+1);  % nastaveni pocatecnich hodnot, nulove teploty vsude krome na nakonci
T(end) = 100;      % nastaveni pocatecnich hodnot, teplota 100 na konci

u(1,1:nx+1) = T;    % vychozi stav

A = toeplitz([-2,1,zeros(1,nx-1)]);  % vytvoreni matice pro iterace
A(1,:) = zeros(1,nx+1);              % vynulovani prvniho radku matice A
A(end,:) = zeros(1,nx+1);            % vynulovani posledniho radku matice A

%
%  Vlastní výpočet a uložení do paměti
%

for j = 2:nt        % jednotlive kroky v case
   T = T + dt/(dx^2) * (A * T')';  % iteracni vzorec pouziva dvakrat transpozice, protoze pracujeme s radkovym vektorem, ale maticove nasobeni funguje pro sloupcove vektory
   u(j+1,1:nx+1) = T;    % ulozeni pro pozdejsi vykresleni
end
 

%
% Vykreslení řešení
%

[X1,T1] = meshgrid(0:dx:nx*dx,0:dt:nt*dt);
colormap hot
pcolor(X1,T1,u)

shading interp
colorbar
title('Vyvoj prubehu teploty v tyci')
xlabel('x')
ylabel('t')

-->


## Variační metody

### Slabá formulace parciálních diferenciálních rovnic

### Souvislost řešení rovnice a minima funkcionálu

### Metoda konečných prvků

## Separace proměnných u parciálních diferenciálních rovnic

https://youtu.be/wfvY6bwlxaw

Budeme se zabývat jednorozměrnou rovnicí vedení tepla ve tvaru
$$\frac{\partial u}{\partial t}=\frac{\partial^2 u}{\partial x^2}.$$ V
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




