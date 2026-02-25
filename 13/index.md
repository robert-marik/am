# Metody řešení diferenciálních rovnic 2


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





