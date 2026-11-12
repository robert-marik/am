# Případová studie: metoda konečných prvků

```{admonition} Anotace.
Metodou konečných prvků (MKP, angl. _finite element method_, FEM) spočítáme, jak
se zatížené těleso zdeformuje a jaké v něm vznikne napětí. Projdeme celou
statickou úlohu od zadání po výsledek: co do výpočtu vstupuje, co z něj
vystupuje, jaká matematika za ním stojí a jak moc se dá výsledku věřit. Nakonec
si metodu naprogramujeme na necelých sto řádcích a spočítáme dřevěný nosník
v tříbodovém ohybu.
```

```{admonition} Prerekvizity.
Navazujeme na tenzor malých deformací (přednáška 2), Greenovu větu (přednáška
7) a na Hookův zákon, slabou formulaci a Galerkinovu metodu (přednáška 12).
Z lineární algebry potřebujeme násobení matic a soustavy lineárních rovnic.
```

## O co se jedná

Pro tažený prut nebo ohýbaný nosník stálého průřezu existují vzorce. Pro
konzolu s otvorem, tesařský spoj nebo židli vzorce nejsou: rovnice pružnosti
jsou parciální diferenciální rovnice a na obecném tvaru je přesně vyřešit
neumíme. Metoda konečných prvků je řeší přibližně a je dnes standardním
nástrojem pro pevnostní výpočty.

Myšlenka má tři kroky.

1. Těleso rozdělíme na malé kousky jednoduchého tvaru, _prvky_ (trojúhelníky,
   čtyřstěny, kvádry). Vrcholy prvků jsou _uzly_ a všechny prvky dohromady
   tvoří _síť_.
2. Neznámou funkci, tedy posunutí bodů tělesa, nahradíme v každém prvku
   jednoduchou funkcí, která je určena hodnotami v uzlech. Místo neznámé funkce
   tak hledáme konečně mnoho čísel: posunutí uzlů.
3. Pro tato čísla sestavíme soustavu lineárních rovnic $K\vec U=\vec b$
   a vyřešíme ji. Z posunutí uzlů dopočítáme deformaci a napětí.

```{figure} postup.png
Postup výpočtu na úloze, kterou budeme v této kapitole řešit: dřevěný nosník na
dvou podporách zatížený uprostřed silou. Barvy v dolním obrázku ukazují napětí
ve směru osy nosníku: horní vlákna jsou stlačená (modrá), dolní tažená (červená).
```

Slovo _statická_ v názvu úlohy znamená, že zatížení se v čase nemění a těleso je
v klidu. Hledáme rovnovážný stav, čas v úloze nevystupuje. Budeme navíc
předpokládat, že deformace jsou malé a že materiál je lineárně pružný, tedy že se
řídí Hookovým zákonem. Takové úloze se říká _lineární statická analýza_ a je to
nejčastější a nejjednodušší typ výpočtu.

## Vstupy a výstupy

Výpočet potřebuje pět druhů údajů.

| Vstup | Co zadáváme | V našem příkladu |
|--|--|--|
| Geometrie | tvar tělesa, obvykle z CAD modelu | obdélník 280 × 20 mm, tloušťka 20 mm |
| Materiál | pružné konstanty; pro izotropní materiál $E$ a $\nu$, pro dřevo moduly a Poissonova čísla v anatomických směrech | smrk: $E_L$, $E_R$, $\nu_{LR}$, $G_{LR}$ |
| Uchycení | kde a ve kterých směrech se těleso nemůže posunout | dvě podpory na spodní straně |
| Zatížení | síly v bodech, tlak na plochu, vlastní tíha | síla 1000 N uprostřed nahoře |
| Síť | typ a velikost prvků | trojúhelníky o hraně 2,5 mm |

Výstupem je především **posunutí** každého uzlu. To je jediná veličina, kterou
metoda počítá přímo. Všechno ostatní se z posunutí dopočítává:

* **deformace** $\varepsilon$ derivováním posunutí,
* **napětí** $\sigma$ z deformace Hookovým zákonem,
* **reakce** v místech uchycení,
* odvozené veličiny pro posouzení pevnosti, například hlavní napětí nebo von
  Misesovo napětí.

Derivováním se přesnost ztrácí, a proto jsou napětí vždy méně přesná než
posunutí. Uvidíme to už na prvním příkladu.

Výpočet odpovídá na otázky typu: o kolik se konstrukce prohne, kde je nejvíce
namáhaná, jaké síly přenášejí podpory, co se změní při jiném tvaru nebo
materiálu. Neodpovídá na otázku, zda je správně zadání. Výsledek platí pro
model, který jsme popsali, a model se od skutečnosti liší uchycením, zatížením
i vlastnostmi materiálu. U dřeva, kde se vlastnosti mění kus od kusu, s vlhkostí
i s polohou suků, je to rozdíl podstatný.

## Rozcvička v jedné dimenzi: tažená tyč

Všechny kroky metody si nejprve ukážeme na úloze, kterou umíme vyřešit přesně.
Tyč délky $L$ s průřezem o ploše $A$ z materiálu s Youngovým modulem $E$ je na
konci $x=0$ upnutá a po délce ji zatěžuje osová síla $f$ na jednotku délky
(například vlastní tíha svisle zavěšené tyče). Konec $x=L$ je volný. Hledáme
posunutí $u(x)$ jednotlivých průřezů.

```{figure} tyc_zadani.png
Vlevo zadání úlohy. Vpravo síly působící na kousek tyče mezi průřezy $x$
a $x+\Delta x$: osové síly v obou průřezech a zatížení připadající na tento kousek.
```

### Rovnice

Deformace je $\varepsilon=\frac{\mathrm du}{\mathrm dx}$, napětí podle Hookova
zákona $\sigma=E\varepsilon$ a osová síla v průřezu $N=\sigma A=EA\frac{\mathrm
du}{\mathrm dx}$. Kousek tyče mezi $x$ a $x+\Delta x$ je v rovnováze, pokud
$N(x+\Delta x)-N(x)+f\Delta x=0$. Po vydělení $\Delta x$ a limitním přechodu
dostáváme
$$-\frac{\mathrm d}{\mathrm dx}\left(EA\frac{\mathrm du}{\mathrm dx}\right)=f,
\qquad u(0)=0,\qquad EA\frac{\mathrm du}{\mathrm dx}(L)=0.\tag{T}$$
Druhá okrajová podmínka říká, že na volném konci nepůsobí žádná síla. Pro
konstantní $E$, $A$ a $f$ je to až na konstanty rovnice (E) z přednášky 12
a přesné řešení najdeme dvojí integrací,
$$u(x)=\frac{f}{EA}\left(Lx-\frac{x^2}2\right),\qquad
\sigma(x)=\frac{f(L-x)}{A}.$$

### Slabá formulace

Postupujeme stejně jako v přednášce 12. Rovnici (T) vynásobíme funkcí $v$, která
splňuje $v(0)=0$, integrujeme přes $[0,L]$ a derivaci přesuneme z $u$ na $v$
pomocí vzorce pro derivaci součinu:
$$\int_0^L EA\,u'v'\,\mathrm dx-\Bigl[EA\,u'v\Bigr]_0^L=\int_0^L fv\,\mathrm dx.$$
Hranatá závorka je nulová: v bodě $0$ díky $v(0)=0$ a v bodě $L$ díky okrajové
podmínce na volném konci. Zbývá
$$\int_0^L EA\,u'v'\,\mathrm dx=\int_0^L fv\,\mathrm dx
\qquad\text{pro každou funkci $v$ s $v(0)=0$.}\tag{W1}$$

```{prf:remark} dva druhy okrajových podmínek
:nonumber:
Podmínka $u(0)=0$ předepisuje posunutí a musíme ji splnit výběrem funkcí,
mezi kterými řešení hledáme. Podmínka na volném konci předepisuje sílu a je ve
slabé formulaci obsažena sama: nic pro ni dělat nemusíme. Kdyby na konci tyče
působila síla $F$, přibyl by na pravé straně (W1) člen $Fv(L)$. To je obecný
rys metody: uchycení se vnucuje, zatížení se přičítá na pravou stranu.
```

Rovnice (W1) má mechanický význam. Chápeme-li $v$ jako myšlené malé posunutí
(virtuální posunutí), je vlevo práce vnitřních sil, protože $EAu'=N$ je osová
síla a $v'$ deformace, a vpravo práce zatížení. Slabá formulace je tedy _princip
virtuálních prací_: těleso je v rovnováze, pokud se při každém myslitelném
posunutí práce vnitřních a vnějších sil rovnají.

### Prvky a jejich matice

Tyč rozdělíme uzly $x_0=0<x_1<\dots<x_n=L$ na $n$ prvků. Přibližné řešení
hledáme jako lomenou čáru,
$$u(x)=\sum_{j=0}^n u_j\varphi_j(x),$$
kde $\varphi_j$ jsou trojúhelníkové bázové funkce z přednášky 12 a $u_j$ jsou
posunutí uzlů. Uzly i prvky číslujeme od nuly, stejně jako později v programu.

```{figure} tyc_prvky.png
Dělení tyče na tři prvky a bázové funkce příslušné uzlům. Funkce $\varphi_0$
a $\varphi_3$ krajních uzlů jsou jen poloviční. Na každém prvku jsou nenulové
právě dvě bázové funkce, jedna klesající a jedna rostoucí.
```

Dosazením do (W1) a volbou $v=\varphi_i$ dostaneme soustavu
$K\vec u=\vec b$ s
$$k_{ij}=\int_0^L EA\,\varphi_i'\varphi_j'\,\mathrm dx,\qquad
b_i=\int_0^L f\varphi_i\,\mathrm dx.$$

Integrály nepočítáme pro každou dvojici $i$, $j$ zvlášť, ale po prvcích. Na
prvku délky $h$ mezi uzly $x_e$ a $x_{e+1}$ jsou nenulové jen dvě bázové funkce.
Jedna tam klesá z 1 na 0 a má derivaci $-\frac 1h$, druhá roste z 0 na 1 a má
derivaci $\frac 1h$. Příspěvek prvku k matici $K$ a k vektoru $\vec b$ proto je
$$K_e=\frac{EA}{h}\begin{pmatrix}1&-1\cr -1&1\end{pmatrix},\qquad
\vec b_e=\frac{fh}2\begin{pmatrix}1\cr 1\end{pmatrix}.$$
Matici $K_e$ říkáme _matice tuhosti prvku_ a název je zde doslovný: prvek se
chová jako pružina o tuhosti $\frac{EA}h$. Síly, kterými působí na své dva
uzly, jsou $K_e$ krát posunutí těchto uzlů. Vektor $\vec b_e$ říká, že zatížení
prvku $fh$ se rozdělí napůl mezi oba jeho uzly.

### Sestavení a řešení

Globální matici dostaneme tak, že příspěvky prvků sečteme na místech
odpovídajících číslům jejich uzlů. Pro $n=3$ prvky stejné délky $h$:
$$
K=\frac{EA}h\begin{pmatrix}
1&-1&0&0\cr 
-1&1+1&-1&0\cr 
0&-1&1+1&-1\cr 
0&0&-1&1
\end{pmatrix},
\qquad
\vec b=\frac{fh}2\begin{pmatrix}1\cr 1+1\cr 1+1\cr 1\end{pmatrix}.
$$
Uzel 1 patří prvkům 0 a 1, a proto se na jeho diagonálním místě sešly dvě
tuhosti. Je to stejné jako u pružin spojených za sebou.

```{figure} tyc_sestaveni.png
Vlevo mechanický model, který soustava $K\vec u=\vec b$ popisuje: uzly spojené
pružinami o tuhosti $\frac{EA}h$ a zatížené silami. Vpravo skládání matice
tuhosti: každý prvek přispívá blokem $2\times2$ na místě svých dvou uzlů
a v místech překryvu se příspěvky sčítají.
```

Tato matice je singulární: součet prvků v každém řádku je nula, takže
$K(1,1,1,1)^T=\vec 0$. Mechanicky to znamená, že tyč, která není nikde upnutá,
se může posunout jako celek, aniž by v ní vzniklo napětí, a rovnováha proto
posunutí neurčuje jednoznačně. Teprve uchycení $u_0=0$ dá jediné řešení. Vnutíme
ho tak, že vyškrtneme první řádek a sloupec a řešíme soustavu tří rovnic pro
$u_1,u_2,u_3$. Vyškrtnutý řádek nezahodíme: po vyřešení z něj spočítáme
reakci v upnutí.

Celý výpočet v Pythonu:

```{literalinclude} mkp_tyc.py
:language: python
:start-after: "# [zadani]"
:end-before: "# [konec zadani]"
```

```{literalinclude} mkp_tyc.py
:language: python
:start-after: "# [sestaveni]"
:end-before: "# [konec sestaveni]"
:dedent: 4
```

```{literalinclude} mkp_tyc.py
:language: python
:start-after: "# [reseni]"
:end-before: "# [konec reseni]"
:dedent: 4
```

Pro zadané hodnoty je $\frac{EA}h=100\,\mathrm{MN/m}$ a $\frac{fh}2=10\,\mathrm{kN}$.
Program vrátí

```text
u [mm] = [0.  0.5 0.8 0.9]
sigma [MPa] = [5. 3. 1.]
reakce [kN] = -60.0
```

Reakce $-60\,\mathrm{kN}$ přesně vyrovnává celkové zatížení $fL=60\,\mathrm{kN}$.

```{figure} tyc.png
Tažená tyč: řešení metodou konečných prvků se třemi prvky a přesné řešení.
Posunutí je lomená čára, napětí je v každém prvku konstantní.
```

Obrázek ukazuje dvě věci, které platí obecně.

* Posunutí je spojité a vystihuje přesné řešení dobře. V této jednoduché úloze
  jsou hodnoty v uzlech dokonce přesné, což je zvláštnost jedné dimenze.
* Napětí je derivací lomené čáry, je tedy po částech konstantní a na hranicích
  prvků skáče. Přesné hodnotě odpovídá uprostřed prvku. Největší napětí
  $6\,\mathrm{MPa}$ v místě upnutí výpočet se třemi prvky podhodnotil
  o šestinu.

Program {download}`mkp_tyc.py` je možné stáhnout a vyzkoušet s jiným počtem prvků.

## Rovnice pružnosti v rovině

Skutečná tělesa jsou trojrozměrná. Postup je ve dvou i ve třech rozměrech
stejný, a proto zůstaneme v rovině, kde se vše dá nakreslit. Budeme uvažovat
tenkou desku tloušťky $t$ zatíženou jen ve své rovině. Její střednicová plocha
je oblast $\Omega$ v rovině $x$, $y$.

**Neznámou** je vektorové pole posunutí
$\vec u(x,y)=\bigl(u_x(x,y),u_y(x,y)\bigr)$, které říká, kam se přesune bod
$(x,y)$.

**Deformaci** popisuje tenzor malých deformací z přednášky 2. Jeho tři různé
složky zapíšeme do sloupce (Voigtův zápis z přednášky 12)
$$\varepsilon=\begin{pmatrix}\varepsilon_x\cr \varepsilon_y\cr \gamma_{xy}\end{pmatrix}
=\begin{pmatrix}
\dfrac{\partial u_x}{\partial x}\cr
\dfrac{\partial u_y}{\partial y}\cr
\dfrac{\partial u_x}{\partial y}+\dfrac{\partial u_y}{\partial x}
\end{pmatrix}.\tag{G}$$
První dvě složky jsou poměrná prodloužení ve směru os. Třetí složka
$\gamma_{xy}$ je _zkos_: změna pravého úhlu mezi vlákny, která původně mířila
ve směru os.

```{prf:remark} zkos a smyková složka tenzoru
:nonumber:
Zkos je dvojnásobkem smykové složky tenzoru deformace,
$\gamma_{xy}=2\varepsilon_{xy}$. V inženýrských výpočtech se používá zkos,
protože právě pro něj má Hookův zákon ve smyku tvar $\tau_{xy}=G_{xy}\gamma_{xy}$
se smykovým modulem $G_{xy}$ měřeným při zkouškách.
```

**Napětí** má v rovině rovněž tři složky,
$\sigma=(\sigma_x,\sigma_y,\tau_{xy})^T$, kde $\tau_{xy}=\sigma_{xy}$ je smykové
napětí. U tenké desky s volnými povrchy jsou složky napětí mířící kolmo k desce
nulové. Tomuto stavu se říká _rovinná napjatost_.

**Hookův zákon.** Ortotropní materiál s hlavními směry podél os má při rovinné
napjatosti podle přednášky 12
$$\varepsilon_x=\frac{\sigma_x}{E_x}-\frac{\nu_{yx}}{E_y}\sigma_y,\qquad
\varepsilon_y=-\frac{\nu_{xy}}{E_x}\sigma_x+\frac{\sigma_y}{E_y},\qquad
\gamma_{xy}=\frac{\tau_{xy}}{G_{xy}},$$
kde $\frac{\nu_{xy}}{E_x}=\frac{\nu_{yx}}{E_y}$. Tyto vztahy vyjadřují deformaci
pomocí napětí. Pro výpočet potřebujeme opak, a proto je vyřešíme vzhledem
k napětím:
$$\sigma=C\varepsilon,\qquad
C=\frac{1}{1-\nu_{xy}\nu_{yx}}\begin{pmatrix}
E_x&\nu_{yx}E_x&0\cr 
\nu_{xy}E_y&E_y&0\cr 
0&0&(1-\nu_{xy}\nu_{yx})G_{xy}
\end{pmatrix}.\tag{H}$$
Matice $C$ se nazývá _matice tuhosti materiálu_ a je symetrická. Pro izotropní
materiál se zjednoduší na
$$C=\frac{E}{1-\nu^2}\begin{pmatrix}1&\nu&0\cr \nu&1&0\cr 0&0&\frac{1-\nu}2\end{pmatrix}.$$

**Rovnováha.** Podle přednášky 12 platí v každém bodě
$$\frac{\partial\sigma_x}{\partial x}+\frac{\partial\tau_{xy}}{\partial y}+f_x=0,
\qquad
\frac{\partial\tau_{xy}}{\partial x}+\frac{\partial\sigma_y}{\partial y}+f_y=0,
\tag{R}$$
kde $\vec f=(f_x,f_y)$ je objemová síla, například tíha.

**Okrajové podmínky.** Hranici $\partial\Omega$ rozdělíme na dvě části. Na
části $\Gamma_u$ je těleso uchyceno a posunutí je předepsáno, $\vec u=\vec 0$.
Na zbytku $\Gamma_p$ je předepsáno zatížení $\vec p$, tedy síla na jednotku
plochy povrchu. Je-li $\vec n=(n_x,n_y)$ jednotkový vektor kolmý k hranici
a mířící ven z tělesa, pak tam platí
$$\sigma_xn_x+\tau_{xy}n_y=p_x,\qquad\tau_{xy}n_x+\sigma_yn_y=p_y.\tag{P}$$
Nezatížený volný povrch je zvláštním případem s $\vec p=\vec 0$.

Dosadíme-li (G) do (H) a výsledek do (R), dostaneme dvě parciální diferenciální
rovnice druhého řádu pro dvě neznámé funkce $u_x$ a $u_y$. To je úloha, kterou
metoda konečných prvků řeší.

## Slabá formulace

Postupujeme jako u tyče, jen místo derivace součinu použijeme její obdobu
v rovině, Greenovu větu z přednášky 7. V tokovém tvaru říká, že tok vektorového
pole $\vec F$ hranicí oblasti je roven integrálu jeho divergence,
$$\oint_{\partial\Omega}\vec F\cdot\vec n\,\mathrm ds=\iint_\Omega\nabla\cdot\vec F\,\mathrm dA.$$

Zvolíme libovolné virtuální posunutí $\vec v=(v_x,v_y)$, které je nulové na
uchycené části hranice $\Gamma_u$. První rovnici (R) vynásobíme $v_x$, druhou
$v_y$, sečteme a integrujeme přes $\Omega$:
$$\iint_\Omega\left[\left(\frac{\partial\sigma_x}{\partial x}+\frac{\partial\tau_{xy}}{\partial y}\right)v_x
+\left(\frac{\partial\tau_{xy}}{\partial x}+\frac{\partial\sigma_y}{\partial y}\right)v_y\right]\mathrm dA
+\iint_\Omega\vec f\cdot\vec v\,\mathrm dA=0.\tag{1}$$
Greenovu větu použijeme na pole
$$\vec F=\bigl(\sigma_xv_x+\tau_{xy}v_y,\ \tau_{xy}v_x+\sigma_yv_y\bigr).$$
Jeho divergence je podle pravidla pro derivaci součinu
$$\begin{aligned}\nabla\cdot\vec F={}&
\underbrace{\left(\frac{\partial\sigma_x}{\partial x}+\frac{\partial\tau_{xy}}{\partial y}\right)v_x
+\left(\frac{\partial\tau_{xy}}{\partial x}+\frac{\partial\sigma_y}{\partial y}\right)v_y}_{\text{výraz z rovnice (1)}}
\cr &+\underbrace{\sigma_x\frac{\partial v_x}{\partial x}+\sigma_y\frac{\partial v_y}{\partial y}
+\tau_{xy}\left(\frac{\partial v_x}{\partial y}+\frac{\partial v_y}{\partial x}\right)}_{\varepsilon(\vec v)^T\sigma}.
\end{aligned}$$
Druhá skupina členů je skalární součin napětí s deformací $\varepsilon(\vec v)$,
kterou podle (G) vyvolá virtuální posunutí. Na hranici je díky (P)
$$\vec F\cdot\vec n=(\sigma_xn_x+\tau_{xy}n_y)v_x+(\tau_{xy}n_x+\sigma_yn_y)v_y=\vec p\cdot\vec v$$
na $\Gamma_p$, kdežto na $\Gamma_u$ je $\vec v=\vec 0$. Greenova věta tedy dává
$$\int_{\Gamma_p}\vec p\cdot\vec v\,\mathrm ds
=\iint_\Omega\bigl(\text{výraz z rovnice (1)}\bigr)\,\mathrm dA
+\iint_\Omega\varepsilon(\vec v)^T\sigma\,\mathrm dA.$$
Odtud vyjádříme první integrál v (1), dosadíme $\sigma=C\varepsilon(\vec u)$
a vynásobíme tloušťkou $t$:

$$\boxed{\iint_\Omega\varepsilon(\vec v)^T\,C\,\varepsilon(\vec u)\,t\,\mathrm dA
=\iint_\Omega\vec f\cdot\vec v\,t\,\mathrm dA+\int_{\Gamma_p}\vec p\cdot\vec v\,t\,\mathrm ds}
\tag{W2}$$

pro každé $\vec v$ nulové na $\Gamma_u$. Je to přesná obdoba (W1): vlevo práce
vnitřních sil na virtuální deformaci, vpravo práce objemových a povrchových
sil. Jako u tyče se uchycení promítlo do výběru funkcí a zatížení do pravé
strany. Ve (W2) vystupují jen první derivace posunutí, a proto do ní můžeme
dosadit i funkce, které jsou jen po částech hladké.

```{prf:remark} minimum energie
:nonumber:
Na slabou formulaci se dá dívat i jinak. Zdeformované těleso má potenciální
energii
$$\Pi(\vec u)=\frac12\iint_\Omega\varepsilon(\vec u)^TC\,\varepsilon(\vec u)\,t\,\mathrm dA
-\iint_\Omega\vec f\cdot\vec u\,t\,\mathrm dA-\int_{\Gamma_p}\vec p\cdot\vec u\,t\,\mathrm ds,$$
kde první člen je energie pružné deformace a zbylé dva potenciální energie
zatížení. Rovnice (W2) je podmínkou, že derivace $\Pi$ ve směru každého $\vec v$
je nulová. Rovnovážný stav je tedy ten, ve kterém má energie minimum. Je to
stejný princip jako u kuličky v důlku, jen místo polohy kuličky hledáme
celé pole posunutí.
```

## Diskretizace: od funkcí k číslům

### Trojúhelníkový prvek

Oblast $\Omega$ pokryjeme trojúhelníky. Každému uzlu $i$ přiřadíme bázovou
funkci $\varphi_i(x,y)$, která je v tomto uzlu rovna jedné, ve všech ostatních
uzlech nule a v každém trojúhelníku je lineární. Jejím grafem je jehlan nad
trojúhelníky, které se v uzlu $i$ stýkají. Je to dvojrozměrná obdoba
trojúhelníkových funkcí z přednášky 12.

```{figure} tvarove_funkce.png
Vlevo bázová funkce příslušná jednomu uzlu sítě. Vpravo lineární funkce na
jednom prvku, určená hodnotami ve třech vrcholech.
```

Obě složky posunutí hledáme jako kombinace těchto funkcí,
$$u_x(x,y)=\sum_iU_{2i}\,\varphi_i(x,y),\qquad
u_y(x,y)=\sum_iU_{2i+1}\,\varphi_i(x,y).$$
Čísla $U_{2i}$ a $U_{2i+1}$ jsou vodorovné a svislé posunutí uzlu $i$. Síť
s $n$ uzly má $2n$ neznámých, kterým se říká _stupně volnosti_, a sestavíme je
do vektoru $\vec U$.

Podívejme se na jeden prvek s vrcholy $(x_1,y_1)$, $(x_2,y_2)$, $(x_3,y_3)$
číslovanými proti směru hodinových ručiček a s plochou $S$. Uvnitř prvku jsou
nenulové jen tři bázové funkce, a to funkce příslušné jeho vrcholům. Jsou to
lineární funkce
$$N_i(x,y)=\frac{a_i+b_ix+c_iy}{2S},\qquad
b_1=y_2-y_3,\quad c_1=x_3-x_2$$
a ostatní koeficienty $b_i$, $c_i$ dostaneme cyklickou záměnou indexů. Jejich
derivace jsou konstanty, $\frac{\partial N_i}{\partial x}=\frac{b_i}{2S}$
a $\frac{\partial N_i}{\partial y}=\frac{c_i}{2S}$. Dosazením do (G) dostaneme
deformaci v prvku jako součin matice a vektoru šesti posunutí jeho vrcholů:
$$\varepsilon=B\,\vec U_e,\qquad
B=\frac1{2S}\begin{pmatrix}
b_1&0&b_2&0&b_3&0\cr 
0&c_1&0&c_2&0&c_3\cr 
c_1&b_1&c_2&b_2&c_3&b_3
\end{pmatrix},\qquad
\vec U_e=\begin{pmatrix}u_{x1}\cr u_{y1}\cr u_{x2}\cr u_{y2}\cr u_{x3}\cr u_{y3}\end{pmatrix}.$$
Matice $B$ závisí jen na poloze vrcholů. Deformace, a tedy i napětí
$\sigma=CB\vec U_e$, je v celém prvku konstantní, stejně jako u tyče.

### Matice tuhosti prvku

Do levé strany (W2) dosadíme $\varepsilon(\vec u)=B\vec U_e$
a $\varepsilon(\vec v)=B\vec V_e$. Integrand je na prvku konstantní, takže
integrál je součin s plochou:
$$\iint_{\text{prvek}}\varepsilon(\vec v)^TC\,\varepsilon(\vec u)\,t\,\mathrm dA
=\vec V_e^T\,\underbrace{t\,S\,B^TCB}_{K_e}\,\vec U_e.$$
Matice
$$K_e=t\,S\,B^TCB\tag{K}$$
typu $6\times6$ je matice tuhosti prvku. Udává síly ve vrcholech trojúhelníka,
které odpovídají daným posunutím vrcholů. V programu je to jediný řádek.

```{literalinclude} mkp_2d.py
:language: python
:start-after: "# [prvek]"
:end-before: "# [konec prvek]"
```

### Sestavení

Integrál přes $\Omega$ je součet integrálů přes prvky. Globální matice $K$ typu
$2n\times2n$ proto vznikne stejně jako u tyče: matici každého prvku přičteme na
místa daná čísly jeho stupňů volnosti.

```text
K ← nulová matice 2n × 2n
pro každý prvek e s uzly (i, j, k):
    spočítej B, plochu S a K_e = t · S · Bᵀ C B      (matice 6 × 6)
    sv ← (2i, 2i+1, 2j, 2j+1, 2k, 2k+1)               (čísla neznámých)
    pro p = 1..6, q = 1..6:
        K[sv[p], sv[q]] ← K[sv[p], sv[q]] + K_e[p, q]
```

```{figure} sestaveni.png
Vlevo malá síť. Uprostřed její matice tuhosti: číslo udává, kolik prvků do
daného místa přispívá, prázdná místa jsou nuly. Řádky a sloupce jsou označeny
číslem uzlu a směrem posunutí. Vpravo rozložení nenulových prvků matice pro síť
nosníku z úvodního obrázku.
```

Z obrázku je vidět důležitá vlastnost. Na místě, které odpovídá dvojici uzlů,
je nenulové číslo jen tehdy, když oba uzly patří k témuž prvku. Uzly 0 a 5
žádný společný prvek nemají, a proto je na jejich místě nula. Ve velké síti
sousedí každý uzel jen s několika dalšími, a matice je proto _řídká_: téměř
celou ji tvoří nuly. Jen díky tomu lze řešit úlohy s miliony neznámých, protože
ukládat a zpracovávat stačí nenulové prvky.

```{literalinclude} mkp_2d.py
:language: python
:start-after: "# [sestaveni]"
:end-before: "# [konec sestaveni]"
```

Pravou stranu $\vec b$ tvoří síly v uzlech. Osamělou sílu zapíšeme přímo na
místo příslušného stupně volnosti. Spojité zatížení se na uzlové síly
přepočítá integrály z pravé strany (W2), podobně jako jsme u tyče rozdělili
zatížení prvku mezi jeho dva uzly.

### Uchycení a řešení

Matice $K$ má tyto vlastnosti.

* Je symetrická, protože $C$ je symetrická.
* Bez uchycení je singulární. Těleso se v rovině může jako celek posunout ve
  dvou směrech a pootočit, aniž by se zdeformovalo. Uchycení proto musí
  zabránit všem třem těmto pohybům, jinak řešič skončí chybou. V praxi je to
  nejčastější chyba v zadání.
* Po vyškrtnutí řádků a sloupců uchycených stupňů volnosti je pozitivně
  definitní, soustava má právě jedno řešení a existují pro ni rychlé
  a spolehlivé algoritmy.

```{literalinclude} mkp_2d.py
:language: python
:start-after: "# [reseni]"
:end-before: "# [konec reseni]"
```

### Zpětný výpočet napětí

Z posunutí uzlů spočítáme v každém prvku deformaci $\varepsilon=B\vec U_e$
a napětí $\sigma=C\varepsilon$. Napětí je v prvku konstantní a mezi sousedními
prvky skáče. Pro kreslení a čtení hodnot se proto obvykle vyhlazuje: uzlu se
přiřadí průměr hodnot z prvků, které se v něm stýkají. Programy to dělají
automaticky. Je dobré vědět, že hladké barevné obrázky napětí jsou výsledkem
tohoto vyhlazení.

```{literalinclude} mkp_2d.py
:language: python
:start-after: "# [napeti]"
:end-before: "# [konec napeti]"
```

## Výpočet: dřevěný nosník v tříbodovém ohybu

Spočítáme zkoušku, která se u dřeva běžně provádí a jejíž model z komerčního
programu je na obrázku v přednášce 12. Smrkový hranolek délky 280 mm s průřezem
20 × 20 mm leží na dvou podporách vzdálených 240 mm a uprostřed je shora
zatížen silou 1000 N. Vlákna míří podél nosníku, osa $x$ je tedy podélný směr
$L$ a osa $y$ radiální směr $R$. Počítáme v milimetrech, newtonech
a megapascalech.

```{literalinclude} mkp_2d.py
:language: python
:start-after: "# [zadani]"
:end-before: "# [konec zadani]"
```

Materiálové konstanty jsou zaokrouhlené hodnoty typické pro smrk. Matici $C$
sestavíme podle (H).

```{literalinclude} mkp_2d.py
:language: python
:start-after: "# [material]"
:end-before: "# [konec material]"
```

Síť vytvoříme nejjednodušším způsobem: obdélník rozdělíme na čtverce a každý
čtverec úhlopříčkou na dva trojúhelníky.

```{literalinclude} mkp_2d.py
:language: python
:start-after: "# [sit]"
:end-before: "# [konec sit]"
```

Zbývá popsat uchycení a zatížení. Levá podpora brání posunutí v obou směrech,
pravá jen ve svislém směru, aby se nosník mohl volně prodlužovat. Tím jsou
vyloučeny všechny tři pohyby tělesa jako celku. Síla působí v jednom uzlu.

```{literalinclude} mkp_2d.py
:language: python
:start-after: "# [nosnik]"
:end-before: "# [konec nosnik]"
```

To je celý program. Soubor {download}`mkp_2d.py` obsahuje řešič, soubor
{download}`obrazky.py` kreslí obrázky v této kapitole.

### Výsledky

Na síti 112 × 8 čtverců, tedy s 1792 prvky, 1017 uzly a 2034 neznámými, trvá
výpočet zlomek sekundy.

```{figure} nosnik_deformace.png
Deformovaný nosník. Posunutí jsou desetkrát zvětšena, šedě je původní tvar.
```

První kontrolou je rovnováha. Svislé reakce v podporách vyjdou 500 N a 500 N,
dohromady právě tolik, kolik činí zatížení, a vodorovná reakce je nulová.

Průhyb uprostřed rozpětí vychází 1,98 mm. Nosníková teorie, kterou znáte
z pružnosti a pevnosti, dává pro nosník s rozpětím $l$, kvadratickým momentem
průřezu $I$ a plochou průřezu $A$
$$w=\frac{Fl^3}{48E_LI}+\frac{Fl}{4\kappa G_{LR}A}
=1{,}80\,\mathrm{mm}+0{,}26\,\mathrm{mm}=2{,}06\,\mathrm{mm},
\qquad\kappa=\frac56.$$
První člen je průhyb od ohybu, druhý od smyku. U oceli se druhý člen běžně
zanedbává. U dřeva je smykový modul oproti $E_L$ velmi malý a smyk zde přidává
14 % průhybu. Metoda konečných prvků žádný z těchto vzorců nepoužila, a přesto
smykový příspěvek zachytila. K rozdílu mezi 1,98 a 2,06 mm se vrátíme
v následující části.

```{figure} nosnik_napeti.png
Složky napětí v jednotlivých prvcích. Barevné stupnice jsou oříznuty, v okolí
síly a podpor jsou hodnoty vyšší.
```

Pole napětí odpovídají tomu, co o ohybu víme.

* Napětí $\sigma_x$ je nahoře tlakové, dole tahové, uprostřed výšky nulové
  a roste směrem ke středu rozpětí, kde je největší ohybový moment.
* Smykové napětí $\tau_{xy}$ je v levé a pravé polovině nosníku stejně velké
  s opačným znaménkem a největší je uprostřed výšky. Za podporami, kde nosník
  nic nenese, je nulové.
* Napětí $\sigma_y$ napříč vlákny je téměř všude nulové, kromě okolí síly
  a podpor. Tam nosníková teorie neříká nic, ale u dřeva jsou to důležitá
  místa, protože pevnost v tlaku napříč vlákny je malá.

```{figure} nosnik_rez.png
Napětí v řezu uprostřed mezi levou podporou a silou na síti 224 × 16 čtverců
a srovnání s nosníkovou teorií.
```

V řezu dostatečně daleko od síly i od podpory se výsledky shodují s nosníkovou
teorií: $\sigma_x$ je po výšce lineární s krajní hodnotou
$\frac{M}{I}\frac h2=22{,}5\,\mathrm{MPa}$ a $\tau_{xy}$ parabolické s maximem
$\frac{3}{2}\frac{F/2}{A}=1{,}9\,\mathrm{MPa}$. Odchylka krajních bodů je
důsledkem vyhlazení: uzel na povrchu má sousední prvky jen z jedné strany.

```{prf:remark} posouzení pevnosti
:nonumber:
U izotropních kovů se napjatost shrnuje do jednoho čísla, von Misesova napětí,
které se při rovinné napjatosti spočítá jako
$\sqrt{\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2}$ a porovnává se
s mezí kluzu. Pro dřevo tento postup nelze použít, protože má v různých směrech
řádově různou pevnost. Jednotlivé složky napětí se porovnávají s pevností
v příslušném směru nebo se používají kritéria navržená pro ortotropní materiály.
```

## Jak moc výsledku věřit

Program vrátí čísla a barevné obrázky vždy, i když je síť hrubá nebo zadání
nesmyslné. Základním nástrojem pro posouzení výsledku je opakovat výpočet
s jemnější sítí a sledovat, co se mění.

| Síť | Neznámých | Průhyb [mm] | $\sigma_x$ dole v $x=80$ mm [MPa] | Největší $\lvert\sigma_y\rvert$ pod silou [MPa] |
|--|--|--|--|--|
| 28 × 2 | 174 | 1,40 | 7,5 | 2,8 |
| 56 × 4 | 570 | 1,82 | 15,0 | 5,6 |
| 112 × 8 | 2 034 | 1,98 | 19,1 | 11,1 |
| 224 × 16 | 7 650 | 2,02 | 21,0 | 22,0 |
| 448 × 32 | 29 634 | 2,03 | 21,8 | 44,0 |
| 896 × 64 | 116 610 | 2,04 | 22,2 | 87,9 |

```{figure} konvergence.png
Tři veličiny při postupném zjemňování sítě. Průhybem se rozumí pokles střednice
uprostřed rozpětí vůči střednici nad podporami.
```

Z tabulky a obrázku plynou tři poučení.

**Hrubá síť je příliš tuhá.** Nejhrubší síť dává průhyb o 31 % menší než
nejjemnější. Není to náhoda. Metoda hledá minimum energie jen mezi funkcemi,
které síť umí vyjádřit, tedy po částech lineárními. Skutečný ohnutý tvar mezi
nimi není a nejbližší náhrada je vždy tužší. Lineární trojúhelníky jsou v ohybu
obzvlášť nepoddajné, a proto komerční programy používají jako výchozí prvky
s kvadratickými funkcemi, které mají uzly i uprostřed hran a na stejnou
přesnost potřebují mnohem méně prvků.

**Posunutí konverguje rychleji než napětí.** Průhyb se od sítě 224 × 16 mění
o méně než 1 %, kdežto napětí ve spodním vlákně se k hodnotě 22,5 MPa blíží
pomaleji. Je to důsledek derivování, které jsme viděli už u tyče. Výsledek
považujeme za použitelný, když se sledovaná veličina při dalším zjemnění mění
méně, než kolik činí požadovaná přesnost. Průhyb se ustálí na 2,04 mm. Od
nosníkové teorie se liší o 1 %, což je v pořádku: i ona je jen přiblížením.

**Některá čísla nekonvergují nikdy.** Napětí $\sigma_y$ pod silou se při každém
zjemnění sítě zdvojnásobí. Chyba není ve výpočtu, ale v zadání. Síla působící
v jediném bodě působí na nulovou plochu a přesné řešení rovnic pružnosti má
v tom bodě nekonečné napětí. Síť jen určuje, na jak malou plochu se síla
rozloží: napětí je řádově $\frac{F}{t\cdot\text{velikost prvku}}$. Totéž platí
pro bodové podpory a také pro ostré vnitřní rohy. Takovému místu se říká
_singularita_.

```{figure} ../12/nosnik_3bodovy.png
Model tříbodového ohybu z komerčního programu (obrázek z přednášky 12). Krajní
hodnoty stupnice, −7000 MPa a +1558 MPa, leží v místě dotyku se zatěžovacím
trnem a mnohonásobně převyšují pevnost jakéhokoli dřeva. Je to příbuzný jev:
zatížení soustředěné na malou dotykovou plochu, které lineárně pružný model
nemá čím omezit. O únosnosti nosníku tyto hodnoty nevypovídají.
```

Se singularitami se zachází dvojím způsobem. Pokud nás okolí zatížení nezajímá,
hodnoty v něm ignorujeme. Ve vzdálenosti srovnatelné s výškou nosníku už na
způsobu, jakým je síla vnesena, nezáleží, jak ukázal řez v $x=80$ mm. Pokud nás
naopak zajímá právě otlačení dřeva pod trnem, musíme zatížení modelovat
realisticky, tedy rozložit ho na skutečnou dotykovou plochu.

Shrnutí kontrol, které stojí za to udělat u každého výpočtu:

* součet reakcí se rovná zatížení,
* deformovaný tvar vypadá tak, jak čekáme, a posunutí mají rozumnou velikost,
* výsledek se při zjemnění sítě podstatně nemění,
* řádově souhlasí s ručním odhadem, například s nosníkovým vzorcem,
* největší napětí neleží v singularitě.

## Silné a slabé stránky

| Silné stránky | Slabé stránky |
|--|--|
| Libovolný tvar tělesa, síť lze zjemnit jen tam, kde je to potřeba. | Výsledek je přibližný a jeho chybu musí odhadnout uživatel. |
| Různé materiály v jednom modelu, anizotropie, skokové změny vlastností. | Odpovídá zadanému modelu. Chybné uchycení, zatížení nebo konstanty dají věrohodně vypadající, ale špatný výsledek. |
| Okrajové podmínky se zadávají přirozeně: uchycení a síly. | Napětí jsou méně přesná než posunutí a v singularitách nemají smysl. |
| Řídká symetrická matice, a proto zvládne miliony neznámých. | Jeden výpočet dá čísla pro jedno zadání, ne vzorec. Závislost na parametru znamená výpočet opakovat. |
| Stejný postup pro pružnost, vedení tepla, proudění i jejich kombinace. | Tvorba kvalitní sítě ve 3D je pracná a nelineární úlohy jsou výpočetně náročné. |
| Pevný matematický základ: jemnější síť dává přesnější řešení. | Pro dřevo je potřeba znát devět pružných konstant, které se obtížně měří a kus od kusu se liší. |

## Co jsme vynechali

Program z této kapitoly a komerční systémy jako ANSYS nebo Abaqus či volně
dostupné CalculiX a FEniCS dělají v jádru totéž: sestaví $K$ a $\vec b$,
vyřeší soustavu a dopočítají napětí. Velké programy navíc nabízejí:

* **trojrozměrné prvky** (čtyřstěny, šestistěny), kde má každý uzel tři
  posunutí, deformace i napětí šest složek a Hookův zákon se zapisuje
  maticí typu $6\times6$ jako v přednášce 12; vzorec (K) zůstává stejný, jen místo plochy
  a tloušťky v něm vystupuje objem prvku,
* **prvky vyššího řádu** a také nosníkové a skořepinové prvky pro štíhlé
  konstrukce,
* **automatickou tvorbu sítě** na obecné geometrii,
* **nelineární úlohy**: velké deformace, plasticitu, dotyk těles; soustava
  rovnic pak není lineární a řeší se opakovaně,
* **dynamiku**: vlastní frekvence a kmity, děje proměnné v čase.

Matematický základ je ve všech případech ten, který jsme prošli: slabá
formulace, po částech jednoduché funkce na síti a soustava rovnic pro hodnoty
v uzlech.
