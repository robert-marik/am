# Diferenciální rovnice druhého řádu

<!--
https://youtu.be/a308Zs_6bq0
-->

## Okrajová úloha

Ukažte, že úloha
$$y''-my=0, \quad y(0)=0=y(1), \ m>0$$
má pouze nulové řešení.

```{prf:example} Řešení
:class: dropdown
:nonumber:

Charakteristcká rovnice je $$\lambda^2-m=0$$ s reálnými kořeny $\lambda_{1,2}=-\sqrt m$.
Obecným řešením je funkce 
$$y(t)=C_1 e^{\sqrt m t} + C_2 e^{-\sqrt m t}$$
a dosazením získáváme
$$y(0)=C_1  + C_2 =0$$
a
$$y(1)=C_1 e^{\sqrt m} + C_2 e^{-\sqrt m}=0.$$
Z první rovnice dostáváme $C_2=-C_1$ a druhá rovnice má tvar
$$C_1 e^{\sqrt m} - C_1 e^{-\sqrt m}=0.$$
Odsud
$$C_1 (e^{\sqrt m} - e^{-\sqrt m})=0 $$
a
$C_1=0$. Poto však $C_2=-C_1=0$ a řešení se redukuje na 
$$y(t)=0 e^{\sqrt m t} + 0 e^{-\sqrt m t}=0$$
tj. na konstantní nulovou funkci.
```

## Okrajová úloha pro rovnici žebra chladiče

*V určitých speciálních případech má smysl formulovat i jiné typy okrajových podmínek, než podmínky na funkční hodnotu (Dirichletova) nebo derivaci (Neumannova) případně na jejich kombinace. Například může být přirozené požadovat ohraničenost.*

Ve cvičení věnovaném difuzní rovnici jsme se zabývali problematikou žebra chladiče z materiálu s koeficientem tepelné vodivosti $\lambda$ v prostředí o teplotě $T_0$. Naformulovali jsme rovnici pro stacionární rozložení teploty ve tvaru $$\lambda \frac{\mathrm d^2T}{\mathrm dx^2} -h (T-T_0) =0,  $$ kde $h$ je koeficient úměrnosti, popisující přestup tepla z chladiče do vnějšího prostředí. 

* Uvažujte dlouhý chladič a ukažte, že teplota klesá exponenciálně s polohou k teplotě okolí. 
* Ze zkušenosti očekáváme, že pro materiál, který lépe vede teplo, bude konec chladiče více horký. Teplota jako funkce polohy bude klesat pomaleji. Je to splněno pro případ z předchozího bodu? Vysvětlete, odkud to vidíme, nebo zdůvodněte, v jaké situaci tomu tak být nemusí. 
* Ze zkušenosti očekáváme, že pokud bude teplo intenzivněji vyzařováno do okolí, bude teplota na konci nižší. Při pomalejším vyzařování (například světlá barva chladiče a izolující nános prachu) bude teplota na konci vyšší. Je to splněno pro případ z předchozího bodu? Vysvětlete, odkud to vidíme, nebo zdůvodněte, v jaké situaci tomu tak být nemusí. 

```{prf:example} Řešení
:class: dropdown
:nonumber:

Jedná se o nehomogenní rovnici 
$$\frac{\mathrm d^2T}{\mathrm dx^2} - \frac {h}{\lambda} T = -\frac {h}{\lambda} T_0.$$ 
Tato rovnice má evidentně konstantní řešení, protože pokud je teplota ochlazované součástky stejná jako teplota okolí, bude teplota žebra chladiče v každém bodě rovna hodnotě $T_0$. Tuto skutečnost můžeme ověřit i dosazením. 

Asociovaná homogenní rovnice má tvar
$$\frac{\mathrm d^2T}{\mathrm dx^2} - \frac {h}{\lambda} T = 0.$$ 
Charakteristický polynom (v proměnné $z$)
$$z^2 - \frac {h}{\lambda}  = 0$$ 
má kořeny $$z_{1,2}=\pm\sqrt{\frac{h}\lambda}$$ a obecné řešení rovnice je
$$ T (x) = T_0 + C_1 e^{\sqrt{\frac{h}\lambda} x} + C_2 e^{-\sqrt{\frac{h}\lambda} x}.$$

* Pro dlouhý chladič musí být teplota ohraničená, proto platí $C_1=0.$ 
* Teplota chladiče je větší než teplota okolí. Proto dále platí $C_2>0$. 

Stacionární teplota jako funkce polohy je tedy dána vztahem $$ T (x) = T_0 + C e^{-\sqrt{\frac{h}\lambda} x},$$ kde $C$ je kladná konstanta. Teplota podél žebra klesá exponenciálně s polohou k hodnotě $T_0$.

Pokles je exponenciální funkce $e^{-z x}$ je rychlejší, pokud je numericky větší hodnota $z$. 

Pokud materiál lépe vede teplo, je hodnota $\lambda$ větší. Protože je tato hodnota ve jmenovateli zlomku, je hodnota $$ \sqrt{\frac h\lambda} $$ menší. To znamená, že exponenciální faktor se mění pomaleji a funkce klesá pomaleji. Pro hodně dobrý vodič tepla je teplota podél žebra prakticky konstantní. 

Pokud je teplo intenzivněji vyzařováno do okolí, je vyšší hodnota $h$. Proto je i vyšší hodnota $$ \sqrt{\frac h\lambda}.$$ To znamená, že koeficient v exponentu je zápornější a exponenciální část klesá rychleji k nule. 

Pro zadané pevné $x$ a kladné $C$ je funkce $$T=T_0+C e^{-\sqrt{\frac h\lambda}x}$$ rostoucí funkcí proměnné $\lambda$ a klesající funkcí proměnné $h$. Řešení úlohy se tedy chová v souladu s očekáváním.

```

## Separace proměnných ve vlnové rovnici, kmity struny

Rovnice kmitů struny je (po eliminaci konstant)
$$\frac{\partial^2 u}{\partial t^2}=\frac{\partial^2 u}{\partial x^2}$$
s nulovými okrajovými podmínkami na koncích. Je-li délka struny $l$, platí  pro
výchylku $u(x,t)$ podmínky $u(0,t)=u(l,t)$ v libovolném čase $t$.

Budeme řešení hledat ve tvaru $u(x,t)=\varphi(x)\psi(t)$, kde $\varphi$ a $\psi$ jsou funkcemi jedné proměnné.
Platí
$$\frac{\partial^2 u}{\partial t^2}=\varphi(x)\psi''(t), \quad \frac{\partial^2 u}{\partial x^2}=\varphi''(x) \psi(t)$$
a rovnice má tvar
$$\varphi(x)\psi''(t)=\varphi''(x)\psi (t).$$
Vydělením této rovnice součinem $\varphi(x)\psi(t)$ dostáváme
$$\frac {\psi''(t)}{\psi(t)}=\frac{\varphi''(x)}{\varphi (x)}.$$
Toto je rovnice, kde levá strana je funkcí proměnné $t$ a pravá strana funkcí proměnné $x$. Obě proměnné jsou však nezávislé a uvedená rovnost může být splněna jen tehdy, když se rovnají společné konstantě. Označme tuto konstantu $-\lambda^2$. Platí tedy
$$\frac {\psi''(t)}{\psi(t)}=-\lambda ^2,\quad \frac{\varphi''(x)}{\varphi (x)}=-\lambda ^2.$$

* První rovnice představuje lineární diferenciální rovnici druhého řádu $$\psi''+\lambda^2\psi=0.$$ Její charakteristická rovnice  $$z^2 +\lambda^2=0$$ má řešení $$z_{1,2}=\pm i\lambda$$ a proto platí $$\psi(t)=C_1\cos(\lambda t) + C_2\sin(\lambda t).$$ Konstanta $C_1$ souvisí s počáteční výchylkou, konstanta $C_2$ s počáteční rychlostí  a konstanta $\lambda$ s frekvencí kmitů.
* Druhá rovnice představuje lineární diferenciální rovnici druhého řádu $$\varphi''+\lambda^2\varphi=0$$ a okrajové podmínky si  vynucují platnost vztahů $\varphi(0)=\varphi(l)=0$. Máme tedy Dirichletovu úlohu na vlastní čísla a vlastní funkce, jak jsme ji použili [v přednášce](http://user.mendelu.cz/marik/am/slidy/11/). Řešením je funkce $\varphi(x)=\sin\left (k\frac{\pi}l x\right)$, kde $k\in\mathbb N$.
* Spojením obdržených výsledků dostáváme rovnici popisující kmity na $k$-té vlastní frekvenci ve tvaru $$u_k(x,t)=\psi(t)\varphi(x)=\left[C_1\cos\left(k\frac{\pi}l t\right) + C_2\sin\left(k\frac{\pi}l t\right)\right]\sin\left (k\frac{\pi}l x\right).$$ 
* Spojením kmitů na všech frekvencích dostaneme řešení rovnice ve tvaru $$u(x,t) = \sum_{k=1}^\infty \left[C_1\cos\left(k\frac{\pi}l t\right) + C_2\sin\left(k\frac{\pi}l t\right)\right]\sin\left (k\frac{\pi}l x\right).$$ Tento vzorec je dostatečně flexibilní, abychom dokázali splnit libovolné počáteční podmínky a proto v sobě obsahuje všechna řešení. Praktická využitelnost vzorce v reálných případech je diskutabilní, proto často používáme numerické simulace využívající numerické řešení zadané rovnice za daných počátečních a okrajových podmínek. 


