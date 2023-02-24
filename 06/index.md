# Dvojný integrál

> Anotace.
>
> * V předchozí přednášce jsme si ukázali rozšíření integrálu, které nám umožnilo počítat integrál nejenom po úsečce, ale i po libovolné křivce. V této přednášce se naučíme integrovat přes dvourozměrný obrazec v rovině. Seznámíme se s dvojným integrálem.
> * Mezi aplikace spadá střední hodnota na dvourozměrné oblasti.
> * Pomocí dvojného integrálu je definován kvadratický moment průřezu nosníku, což je zásadní veličina ovlivňující tuhost a chování těchto nosníků při deformaci.
> * Pomocí dvojného integrálu je možné určit množství veličiny ze znalosti její plošné hustoty. To využijeme později při makroskopické formulaci bilance stavové veličiny a při odvození difuzní rovnice v integrálním tvaru.

> Prerekvizity.
>
> * Dvojný integrál počítáme převodem na dva jednorozměrné Riemannovy integrály. Je proto tedy dobré ovládat výpočet neurčitého a určitého Riemannova integrálu.

<!-- [Motivace pro dvojný integrál](http://user.mendelu.cz/marik/aromamath/Dvojny_integral.html) - ve výpočetním prostředí Jupyter notebooku numericky určíme parametry, jaké zdroje tepla je potřeba dodat do rovinné desky vedoucí teplo tak, aby teplotní profil byl takový, jaký požadujeme. Vyjde, že výkon zdrojů se liší podle toho, v jakém bodě je zdroj umístěn. Pokud chceme celkový výkon, musíme sečíst příspěvky k celkovému výkonu. Tyto příspěvky jsou spojitě rozloženy na dvourozměrné množině a prostý součet konečného počtu sčítanců nestačí. Nástrojem, který takové příspěvky umí sečíst je dvojný integrál. -->

V praxi pracujeme s řadou veličin, které se počítají tak, že se parametr systému násobí obsahem. 

* Z plošné hustoty desky a jejího obsahu násobením obdržíme hmotnost desky. 
* Z hloubky nádrže (se svislými stěnami) a obsahu hladiny obdržíme násobením objem. 
* Z tlaku a obsahu stěny obdržíme násobením tlakovou sílu působící na stěnu nádrže. 

Je však otázka, jak tento přístup použít v případě, že daný parametr není po celé ploše konstantní. Deska může být nehomogenní, nádrž nemusí mít vodorovné dno a tlak působící na stěnu nádrže není ve všech místech stejný, protože různé části stěny jsou v různé hloubce. 

U křivkového integrálu jsme se setkali s momentem setrvačnosti. Ukázali jsme si, jak stanovit moment setrvačnosti množiny, která má hmotnost rozloženu na křivce a třeba i nerovnoměrně. Při výpočtu namáhání nosníků, trámů, polic nebo stromů řešíme podobnou úlohu, ale pro množiny v rovině namísto křivek. Potřebujeme zohlednit, že  při deformaci nosníků se pro jednotlivé body průřezu liší vzdálenost od neutrální osy. 

Řešení uvedených nesnází je stejné: další rozšíření integrálního počtu a zavedení  dvojného integrálu. Ten si nyní představíme.

https://youtu.be/DYySq6o6WTk

\def\maxwidth{5cm}

\iffalse

## Motivace 1 (hmotnost nehomogenní desky)

<div class='obtekat'>

![Deska s nekonstantní plošnou hustotou. Zdroj:  https://www.flickr.com/photos/svacher, licence CC BY-NC-ND  2.0](table.jpg)

</div>

* Hmotnost $m$ desky $\Omega$ je možno vypočítat jako součin plošné
  hustoty $\sigma$ (hmotnost na jednotku obsahu) a obsahu $S$ desky podle vzorce $$m=\sigma S.$$
* Toto funguje pro desky s konstantní plošnou hustotou, kdy má deska
  ve všech místech stejné fyzikální vlastnostmi.
* Pokud je deska slepená z konečného počtu malých homogenních desek o
  různých plošných hustotách, určíme hmotnost každé jednotlivé desky
  samostatně a výsledky potom sečteme.
  $$m=\sigma_1 S_1+\sigma_2 S_2+\cdots + \sigma_n S_n$$
* Pokud není možné nebo vhodné použít předchozí bod, musíme
  předpokládat, že hustota je obecnou funkcí. Potom namísto součtu
  konečného počtu sčítanců následuje nekonečný počet sčítanců a
  vybudujeme aparát, který nám umožní psát
  $$m=\iint_\Omega \sigma \,\mathrm dS.$$

## Motivace 2 (objem vody v jezeře)

<div class='obtekat'>

![Nádrž s proměnnou hloubkou. Zdroj: https://www.pixabay.com](lake.jpg)

</div>

* Objem vody $V$ v nádrži nebo bazénu (se svislými stěnami, ale jinak
  i nepravidelného půdorysu $\Omega$) vypočteme jako součin obsahu
  hladiny $S$ a hloubky vody $h$ podle vzorce $$V=Sh.$$ To ovšem platí jenom,
  pokud je v každém místě stejná hloubka.
* Pokud má jedna část bazénu jinou hloubku než část druhá, vypočteme
  objem u každé hloubky samostatně a příspěvky sečteme. Objem je tedy dán vztahem $$V=S_1h_1+S_2h_2.$$
* Předchozí postup je možné aplikovat pro konečně mnoho hloubek, ale
  někdy to je nevhodné nebo, v případě spojitě se měnící hloubky,
  dokonce nemožné. Potom místo součtu konečně mnoha příspěvků
  použijeme dvojný integrál a dostáváme $$V=\iint_\Omega h\mathrm dS.$$

## Motivace 3 (průtok)

<div class='obtekat'>

![Průtok potrubím je ovlivněn tím, že u stěny teče tekutina pomaleji  než ve středu, potrubí na Aljašce. Zdroj: https://www.pixabay.com](pipe.jpg)

</div>

* Teče-li průřezem $\Omega$ tekutina kolmo na průřez rychlostí $v$, je
  celkový průtok $Q$ (objem, který proteče průřezem za jednotku času)
  dán součinem $$Q=vS,$$ kde $S$ je plošný obsah průřezu.
* Teče-li různými místy průřezu voda různou rychlostí, sečteme
  jednotlivé příspěvky podle vzorce  $$Q=v_1S_1+v_2S_2+\dots +v_nS_n.$$
* Myšlenku z předchozího bodu není snadné udělat, pokud se rychlost
  mění spojitě. Například v potrubí je rychlost rozdělena parabolicky
  a ubývá se vzdáleností od středu. Situaci zachraňuje dvojný integrál
  $$Q=\iint_\Omega v\,\mathrm dS.$$

\fi

## Dvojný integrál

https://youtu.be/tPf-7dZ4Il0

<div class='obtekat'>

\def\maxfactor{0.3}

\iffalse

![](dvojny_integral.png)

\fi

</div>

Pro dvojný integrál použijeme podobnou myšlenkovou konstrukci jako
u\ křivkového integrálu prvního druhu, pouze místo drátu s\ danou
lineární hustotou budeme uvažovat rovinnou ohraničenou desku s\ danou
plošnou hustotou.

* Pokud je hustota desky konstantní, je možno její hmotnost získat
  jednoduše jako součin plošné hustoty a obsahu.
* Pokud se hustota desky mění a v\ obecném bodě $(x,y)$ je dána funkcí
  $f(x,y)$, můžeme myšlenkově rozdělit desku na malé kousky, v\ rámci
  každého malého kousku hustotu aproximovat konstantou, vypočítat
  hmotnost každého kousku jako součin hustoty a obsahu a všechny
  hmotnosti sečíst.
* Získaná veličina je aproximací celkové hmotnosti.

V\ limitním přechodu kdy rozměry všech kousků na něž je deska dělena
jdou k\ nule dostáváme **dvojný integrál** 
$$ \iint_\Omega f(x,y)\mathrm{d}x \mathrm{d}y , $$ 
kde $\Omega$ je oblast v\ rovině $(x,y)$ definovaná uvažovanou deskou. V aplikacích je častý též zápis
$$ \iint_\Omega f(x,y)\mathrm{d}A$$ 
nebo 
$$ \iint_\Omega f(x,y)\mathrm{d}S.$$ 

## Linearita a aditivita

Dvojný integrál je odvozen (tak jako všechny integrály) pro aditivní
veličiny a proto se "dobře snáší" se sčítáním (ať už integrovaných
funkcí, nebo integračních oborů) a s násobení integrované funkce
konstantou. Přesněji, platí následující věty.

```{prf:theorem} linearita dvojného integrálu
:nonumber:
   Buď $f_1$, $f_2$ funkce integrovatelné v $\Omega$ a $c_1$, $c_2$   libovolná reálná čísla. Platí \dm$$     \iint_{\Omega} \bigl[c_1f_1(x,y)+c_2f_2(x,y)\bigr]\mathrm dx\mathrm dy     =     c_1\iint_{\Omega} f_1(x,y)\mathrm dx\mathrm dy+     c_2\iint_{\Omega} f_2(x,y)\mathrm dx\mathrm dy $$
```


```{prf:theorem} aditivita vzhledem k oboru integrace
:nonumber:
  Nechť je množina $\Omega$ rozdělena na dvě oblasti $\Omega_1$   a $\Omega_2$, které mají společné nejvýše hraniční body. Platí $$     \iint_\Omega f(x,y)\mathrm dx\mathrm dy=     \iint_{\Omega_1} f(x,y)\mathrm dx\mathrm dy+     \iint_{\Omega_2} f(x,y)\mathrm dx\mathrm dy. $$
```


## Výpočet dvojného integrálu

https://youtu.be/ItTWxJGD3sY

Výpočet dvojného integrálu se provádí převodem, na integrály funkcí jedné proměnné.

#### Výpočet (oblast mezi funkcemi proměnné $x$)

<div class='obtekat'>

![Oblast mezi funkcemi proměnné $x$.](fub_1.png)

</div>

V\ závislosti na tom, jakými nerovnostmi množinu $\Omega$ definujeme,
můžeme pro výpočet dvojného integrálu použít následující věty. Tyto
věty udávají, jak je možno dvojný integrál přepsat jako dvojnásobný
integrál. Mají název **Fubiniovy věty**.

```{prf:theorem} Fubiniova věta
:nonumber:
 Nechť $f$ je funkce spojitá v\ uzavřené oblasti
$$  
\Omega=\{(x,y)\in\mathbb{R}^2:{a\leq x\leq b}\text{ a }
{\varphi (x)\leq y\leq \psi (x)}\}.$$ 
Potom 
$$
\iint_{\Omega}f(x,y)\mathrm{d}x \mathrm{d}y ={\int_{a}^{b}}
\Bigl[ \int_{\varphi (x)}^{\psi(x)}   
f(x,y){\mathrm{d}y }\Bigr]{\mathrm{d}x }.
$$
```


#### Výpočet (oblast mezi funkcemi proměnné $y$)

<div class='obtekat'>
![Oblast mezi funkcemi proměnné $y$.](fub_2.png)

</div>

```{prf:theorem} Fubiniova věta pro jiné pořadí integrace
:nonumber:
 Nechť $f$ je funkce spojitá v\ uzavřené oblasti
$$  \Omega=\{(x,y)\in\mathbb{R}^2:{a\leq y\leq b}\text{ a }
{\varphi (y)\leq x\leq
\psi (y)}\}.
$$
Potom 
$$
\iint_{\Omega}f(x,y)\mathrm{d}x \mathrm{d}y ={\int_a^b}\Bigl[ 
{\int_{\varphi (y)}^{\psi(y)}}
f(x,y){\mathrm{d}x }\Bigr]{\mathrm{d}y }.
$$

```


#### Záměna pořadí integrace

<div class='obtekat'>

![Oblast, pro kterou jsou možná obě pořadí integrace.](fub_4.png)

</div>

Často je možné oblast integrace zapsat pomocí obou možností uvedených
na předchozích slidech. Například oblast na obrázku je možno zapsat
buď jako
$$\begin{gathered}
0\leq x \leq 2\\
0\leq y\leq x^2
\end{gathered}$$
nebo
$$\begin{gathered}
0\leq y \leq 4\\
\sqrt{y}\leq x\leq  2.
\end{gathered}$$

Pro integrál funkce $f(x,y)$ přes takovou množinu tedy máme dvě alternativy. Buď
$$\int_0^2 \int _0^{x^2} f(x,y)\;\mathrm{d}y\;\mathrm{d}x$$
anebo
$$\int_0^4 \int _{\sqrt y}^{2} f(x,y)\;\mathrm{d}x\;\mathrm{d}y.$$

Všimněte si, že nestačí prosté prohození integrálů. Je nutno přepočítávat meze a hraniční křivky je nutno vyjádřit jednou jako funkce proměnné $x$ a jednou jako funkce proměnné $y$. V důsledku tohoto dochází v průběhu výpočtu dvěma různými způsoby k\ tomu, že pracujeme se dvěma různými integrály. Výsledky jsou samozřejmě stejné, ale nemusí být dosažitelné srovnatelnou námahou. Jedna z cest může být snazší.

## Výpočet (obdélníková oblast)

https://youtu.be/o38mi3tTAvw

<div class='obtekat'>
![Integrál přes obdélník.](fub_3.png)

</div>

Výše uvedené problémy se stanovením a případným přepočítáváním mezí
při záměně pořadí integrace se nevyskytují při integrování přes
obdélníkovou oblast.

```{prf:theorem} Fubiniova věta na obdélníku
:nonumber:
 Nechť $R=[a,b]\times[c,d]$ je uzavřený obdélník v $\mathbb{R}^2$ a
$f$ funkce definovaná a spojitá na $R$. Pak platí
$$    \begin{aligned}\iint_R f(x,y)\mathrm{d}x \mathrm{d}y 
&=\int_a^b\Bigl[\int_c^d f(x,y)\mathrm{d}y \Bigr]\mathrm{d}x 
\\&=\int_c^d\Bigl[\int_a^b f(x,y)\mathrm{d}x \Bigr]\mathrm{d}y .\end{aligned}
$$

Platí-li dokonce rovnost $f(x,y)=g(x)h(y)$, pak
$$
\iint_R f(x,y)\mathrm{d}x \mathrm{d}y  =     \int_a^b g(x) \mathrm{d}x  \int_c^d h(y)\mathrm{d}y .
$$

```


## Aplikace dvojného integrálu

https://youtu.be/8YS2Fn8st5I

#### Matematické aplikace dvojného integrálu

* **Obsah** $\mu(\Omega)$ množiny $\Omega$ vypočteme jako integrál
    $$\mu(\Omega)=\iint_\Omega \mathrm{d}x \mathrm{d}y.$$
* **Integrální střední hodnota** funkce $f(x,y)$ definované na množině
  $\Omega$ je 
  $$ \frac{\iint_\Omega f(x,y)\mathrm{d}x \mathrm{d}y }{\mu (\Omega)},$$ 
  kde $\mu (\Omega)=\iint_\Omega\mathrm{d}x\mathrm{d}y$ je obsah
  množiny $\Omega$.

#### Objem kopce nebo jezera pomocí vrstevnic

\iffalse

<div class='obtekat'>

![Posvátná hora Japonska. Objem se dá určit pomocí obsahů vrstevnic. Zdroj: https://www.pixabay.com](fuji.jpg)

</div>

\fi

* Obsah množiny ohraničené vrstevnicí na mapě vynásobený rozestupem
mezi vrstevnicemi je přibližně roven objemu vrstvy mezi dvěma
vrstevnicemi.
* Pokud sečteme obsahy všech vrstevnic a vynásobíme rozestupem mezi
těmito vrstevnicemi, dostaneme odhad pro objem kopce. Vlastně je to
jako bychom kopec rozřezali na stejně tlusté plátky, naskládali je
vedle sebe, sečetli obsahy postav takto vzniklých těles a vynásobili
výškou.
* Podobně je možné odhadnout objem jezera.
* V tomto případě je dvojný integrál pouze koncept. Samozřejmě nemáme
ambice vyjadřovat vrstevnice v analytickém tvaru a integrovat pomocí
Fubiniovy věty. Ke slovu přijde spíše numerický výpočet integrálu.
  
#### Fyzikální aplikace dvojného integrálu

* **Hmotnost** množiny $M$ je $$m=\iint_M \sigma(x,y)\mathrm{d}x
  \mathrm{d}y,$$ kde $\sigma(x,y)$ je **plošná hustota** (hmotnost
  vztažená na jednotku povrchu).
* Je-li plošná $u$ hustota kinetické energie molekul (což je veličina úměrná
  termodynamické teplotě), je $\iint_M u\,\mathrm dx\mathrm dy$ celková kinetická
  energie částic. Tato energie se může měnit tepelnou
  výměnou. Rychlost, s jakou se mění část vnitřní energie související
  s teplotou, je $$\frac{\mathrm d}{\mathrm d t}\left(\iint_M u\,\mathrm
  dx\mathrm dy\right)$$
  a odsud odvozujeme rovnici vedení tepla.
* **Lineární momenty** hmotné množiny $M$ vzhledem k\ osám $y$ a $x$
  jsou rovny $$\iint_M x\sigma(x,y)\mathrm{d}x \mathrm{d}y$$ a
  $$\iint_M y\sigma(x,y)\mathrm{d}x \mathrm{d}y.$$
* **Moment setrvačnosti** hmotné množiny $M$ vzhledem k\ ose je
  $$J=\iint_M \rho^2(x,y)\sigma(x,y)\mathrm{d}x \mathrm{d}y ,$$ kde
  $\rho(x,y)$ je vzdálenost bodu $(x,y)$ od osy otáčení. Například pro
  osu $x$ je $\rho(x,y)=y$ a pro osu $y$ je $\rho (x,y)=x$. Pro osu
  procházející kolmo počátkem je $\rho(x,y)=\sqrt{x^2+y^2}$.

#### Technické aplikace dvojného integrálu

\iffalse

<div class='obtekat'>

![Dřevostavba realizovaná pomocí I-nosníků. I-nosníky mají vysoký kvadratický moment při nízké spotřebě materiálu. Proto jsou tuhé a silné i při nízké hmotnosti. Ve strojařině se používají odedávna, první dřevostavba z nosníků tohoto typu byla v ČR [realizována 2011](https://stavba.tzb-info.cz/7551-prvni-rodinny-dum-v-cr-s-konstrukcnim-systemem-i-nosniku-fermacell-steico). Zdroj: https://www.taus.eu](I-nosniky.jpg)

![Větrné turbíny jsou konstruovány podobně jako I nosníky, pevný materiál na vnějších stranách a materiál s menší pevností uvnitř. Například balzové dřevo. A podobně jsou "konstruovány" například listy rostlin. Zdroj: pixabay.com, tpsdave](vetrna_turbina.jpg)

</div>

manimp:beam|Odvození ohybové rovnice nosníku.

\fi

* **Souřadnice těžiště** množiny jsou podílem lineárních momentů a
  celkové hmotnosti množiny.
* **Kvadratický moment průřezu** (což je moment setrvačnosti pro
  $\sigma(x,y)=1$, anglicky *second moment of area*) je veličina,
  která hraje podstatnou roli v\ mechanice (nábytek, stavby) při
  dimenzování (polic, nosných tyčí, nosníků).
* V technické praxi zpravidla neuvažujeme nekonstantní plošnou hustotu. Potom je možné je bez újmy na obecnosti nahradit jedničkou. Vzorce pro obsah, $x$-ovou souřadnici těžiště ($x_0$), $y$-ovou
  souřadnici těžiště ($y_0$), kvadratický moment vzhledem k\ ose $x$
  ($I_x$) a kvadratický moment vzhledem k\ ose $y$ ($I_y$) (pro množinu $M$ s plošnou hustotou $1$) jsou
  $$
  \begin{alignedat}{2}
	  %  S&=\iint_M\mathrm{d}x \mathrm{d}y \\
	  x_0&=\frac 1S \iint_M x\mathrm{d}x \mathrm{d}y ,&\qquad    I_x&= \iint_M y^2\mathrm{d}x \mathrm{d}y, \\
	  y_0&=\frac 1S \iint_M y\mathrm{d}x \mathrm{d}y , &    I_y&= \iint_M x^2\mathrm{d}x \mathrm{d}y, \\
  \end{alignedat}
  $$
  kde $S=\mu (M)$ je obsah množiny $M$.
  Poloha těžiště je tedy střední hodnotou funkcí $x$ a $y$.

#### Tuhost nosníků, stabilita stromů

\iffalse

<div class='obtekat'>

![Tuhost a nosnost nosníků nebo podpěr souvisí s kvadratickým momentem průřezu. Zdroj: pixabay.com](beam.jpg)

![Poloviční poloměr znamená u homogenního materiálu šestnáctkrát menší tuhost. Tedy jenom šest procent původní tuhosti! U stromu je tento poměr ještě horší díky různým druhům dřeva uprostřed a na kraji. Vánoční strom pro Prahu na Vánoce 2019. Zdroj: Taiko, Pražský deník](vanocni_strom.jpg)

</div>

\fi

Tuhost (odolnost vůči deformaci) pro nosník obdélníkového průřezu o výšce $b$ a
šířce $a$ je dána kvadratickým momentem obdélníkového průřezu vzhledem
k vodorovné ose procházející těžištěm. 
$$\begin{aligned}I_x&=\iint_{\left[-\frac a2,\frac a2\right]\times \left[-\frac b2,\frac b2\right]} y^2\,\mathrm dx\mathrm dy\\
&=\int_{-\frac a2}^{\frac a2} \,\mathrm dx\int_{-\frac b2}^{\frac b2}
y^2 \,\mathrm dy=a\left[\frac 13 y^3\right]_{-\frac b2}^{\frac b2}=\frac 1{12}ab^3
\end{aligned}
$$
Odsud máme okamžitě několik pozorování

* Pokud šířka vzroste dvakrát, tuhost vzroste také dvakrát. Pokud ale
  dvakrát vzroste výška, tuhost vzroste dokonce osmkrát. Pro nosník s
  poměrem stran 1:2 je poměr tuhostí při poloze naplacato a nastojato roven 1:4.
* Pro nosník čtvercového průřezu ($a=b$) roste tuhost se čtvrtou
  mocninou rozměrů. Obsah (a tedy i hmotnost) roste s druhou
  mocninou. Uvažujme tři nosníky. První má čtvercový průřez. Druhý také, ale průřez má dvojnásobný obsah. (Strana je tedy $\sqrt 2$-krát delší.) Třetí nosník bude krabicový nosník. Bude mít vnější rozměry stejné jako větší nosník, ale uvnitř bude čtvercová dutina o rozměrech prvního nosníku. Tuhost prvního nosníku bude referenční, označme ji $I$. Tuhost druhého nosníku bude čtyřnásobná, tj. $4I$ a za toto navýšení tuhosti "platíme" použitím dvojnásobného množství materiálu. Tuhost třetího nosníku najdeme jako rozdíl prvních dvou, tj. $3I$, protože i geometricky největší nosník vznikne zasunutím prvního nosníku do dutiny ve třetím krabicovém nosníku. Nyní porovnjeme původní nosník a krabicový nosník. Oba používají stejné množství materiálu, ale tuhost krabicového nosníku je trojnásobná. To proto, že část materiálu je dál od osy symetrie průřezu. Podobně se dá zdůvodnit a výpočtem ukázat, že profil ve tvaru písmene I, známé íčko, je tužší než tyč vykovaná ze stejného množství materiálu.
* Pro čtvercový průřez roste tuhost se čtvrtou mocninou délky
  strany. Podobná závislost musí být u\ každého průřezu
  jednoparametrického tvaru, například pro kruh. Jako na nosník s\ kruhovým průřezem můžeme pohlížet i\ na stromy. Například strom, ve
  kterém je dutina o\ velikosti poloviny průměru kmene většinou vyvolá
  obavy ze stability. I když taková dutina vypadá obrovská, tuhost se
  sníží o\ původní tuhost vynásobenou koeficientem
  $$(0.5)^4=0.0625\approx 6\%.$$ 
  Vidíme, že i s hrozivě vypadající dutinou má kmen pořád tuhost 
  $94\%$ původní tuhosti (za předpokladu dutiny uprostřed
  kmene). Pevnost roste jenom s třetí
  mocninou a proto odolnost vůči zlomení neklesne tak dramaticky jako tuhost.

\iffalse 

#### Těžiště složeného obrazce

Uvažujme množinu $M$ s jednotkovou plošnou hustotou, rozdělenou na dvě
disjunktní části $M_1$ a $M_2$. Tyto množiny mají $x$-ovou polohu
těžiště v bodě
$$x_{0i}=\frac1{S_i}{\iint_{M_i}x\,\mathrm dx\mathrm dy}, \qquad S_i=\iint_{M_i}\,\mathrm dx\mathrm dy,\qquad i=1,2.$$
Poloha těžiště není aditivní veličinou. Dvojný integrál však aditivní veličinou je. Platí
$$
\begin{aligned}
\iint _{M} x\,\mathrm dx\mathrm dy&=\iint _{M_1} x\,\mathrm dx\mathrm dy + \iint _{M_2} x\,\mathrm dx\mathrm dy\\
&=S_1 x_{01} + S_2 x_{02}
\end{aligned}
$$
a těžiště množiny $M$ je
$$
\begin{aligned}
x_0&=\frac 1{S_1+S_2}\iint _{M} x\,\mathrm dx\mathrm dy\\
&=\frac 1{S_1+S_2}(S_1 x_{01} + S_2 x_{02})\\
&=\frac {S_1 x_{01} + S_2 x_{02}}{S_1+S_2}.
\end{aligned}
$$
Totéž je možné provést pro $y$-ovou souřadnici, nebo pro libovolný
konečný počet částí. Podobně je možné odvodit vzorec s\ obecnou
nekonstantní plošnou hustotou.  Poloha těžiště složeného obrazce je
tedy *váženým průměrem* těžišť jednotlivých složek, kde váha každé
složky je určena její hmotností. Protože se jedná o vážený průměr,
tj. vlastně o lineární kombinaci bodů, kdy součet koeficientů je roven
jedné, okamžitě vidíme, že těžiště složeného obrazce je na úsečce mezi
těžišti jednotlivých částí.

Zobecnění výše uvedených myšlenek na množinu rozdělenou na více částí
je již snadné.

#### Steinerova věta

Nechť je dána množina $M$ s plošnou hustotou $\sigma(x,y)$. *Ukážeme,
že vzhledem k ose procházející těžištěm je nejmenší moment
setrvačnosti.* Nechť $m=\iint \sigma(x,y)\,\mathrm dx\mathrm dy$, $y_0=\frac
1{m}\iint_M y\sigma(x,y)\,\mathrm dx\mathrm dy$ a $I_{xT}=\iint_M
(y-y_0)^2\sigma(x,y)\,\mathrm dx\mathrm dy$ jsou hmotnost, $y$-ová poloha těžiště
a moment setrvačnosti vzhledem k ose jdoucí těžištěm rovnoběžně s osou
$x$. Moment setrvačnosti vhledem k ose  $x$ je
$$I_{x0}=\iint y^2\sigma(x,y)\,\mathrm dx\mathrm dy.$$
Platí
$$\begin{aligned}
I_{xT}&=\iint_M
(y-y_0)^2\sigma(x,y)\,\mathrm dx\mathrm dy\\
&=\iint_M
(y^2-2yy_0+y_0^2)\sigma(x,y)\,\mathrm dx\mathrm dy\\
&=\iint_M
y^2\sigma(x,y)\,\mathrm dx\mathrm dy
-2y_0
\iint_M
y\sigma(x,y)\,\mathrm dx\mathrm dy+y_0^2
\iint_M
\sigma(x,y)\,\mathrm dx\mathrm dy\\
&=I_{x0}
-2y_0 m y_0+y_0^2 m
\\
&=I_{x0}
-m y_0^2.
\end{aligned}
$$
Odsud dostáváme
$$I_{x0}=I_{xT}+my_0^2,$$
což lze interpretovat tak, že *moment setrvačnosti vhledem k ose $o$
je součtem momentu setrvačnosti vzhledem k ose procházející těžištěm rovnoběžně s $o$
a momentu setrvačnosti hmotného bodu ležícího
v těžišti množiny a o stejné hmotnosti jako je hmotnost množiny vzhledem k ose $o$.*

\fi

#### Tlak na svislou plochu

\iffalse

<div class='obtekat'>

![Bobři v ZOO v Brně jsou za skleněnou stěnou obdélníkového tvaru.](bobri.jpeg)

</div>

\fi

Vzorec pro tlakovou sílu $F=pS$ není možné použít například pro
výpočet celkové síly působící na svislou hráz, protože tlak $p$ se
mění s hloubkou a není tedy konstantní na celém průřezu o obsahu
$S$. Ukážeme, jak tuto nesnáz překonat.

Uvažujme svislou rovinnou hráz $M$. Hrází je přitom myšlena rovinná
množina s jednotkovou plošnou hustotou, ne postavený trojrozměrný
objekt. Počátek kartézské soustavy souřadnic volíme u hladiny, osa $y$
směřuje dolů, osa $x$ vodorovně. Tlak v hloubce $y$ je roven $p=y\rho
g$, kde $\rho$ je hustota vody a $g$ tíhové zrychlení. Na plochu o
rozměrech $\Delta S$ v hloubce $y$ působí tlaková síla
$$\Delta F=y\rho g \Delta S.$$
Tato tlaková síla má ve všech bodech hráze stejný směr a celkovou sílu
na hráz je možno zjistit sečtením sil v jednotlivých bodech. Podobná
myšlenková úvaha jako v úvodu pro hmotnost desky, nebo přesný
matematický popis, nás dovedou k tomu, že celková síla na hráz je dána
integrálem
$$F=\iint _M y\rho g \,\mathrm d x\mathrm dy.$$
Protože $g$ a $\rho$ jsou konstanty, je možno psát
$$F=\rho g\iint _M y \,\mathrm d x\mathrm dy.$$
Využijeme-li vzorec pro $y$-ovou souřadnici těžiště, má výsledný vztah tvar
$$F=\rho g y_0 S,$$
kde $S$ je obsah hráze. Formálně tento vztah odpovídá vzorci
$$F=p_0 S,\tag{H1}\label{H1}$$
kde $p_0=\rho g y_0$ je tlak v těžišti. *Proto v praxi stačí znát těžiště
hráze a pro výpočet síly na hráz použít celkovou plochu hráze a tlak
v\ těžišti.* Protože jsme pracovali s obecnou množinou $M$, není tento
poznatek nijak vázán na konkrétní tvar hráze. Musí být však splněna
podmínka, že všechny body hráze leží v\ jedné rovině.

\iffalse

Ve výpočtu výše jsme uvažovali svislou rovinu, ale zobecnění na šikmou
rovinu je snadné. Stačí opravit vztah pro hloubku, protože když svislou množinu
i s kartézskými souřadnicemi pootočíme okolo osy procházející
hladinou, hloubka všech bodů se sníží faktorem $\sin \alpha$, kde
$\alpha$ je úhel mezi vodorovnou hladinou a rovinou hráze. Formálně
tato operace dopadne stejně, jako kdybychom tekutinu nahradili tekutinou
s hustotou $\sin\alpha$-krát nižší. Protože však vztah $\eqref{H1}$
nezávisí na hustotě, nic se na něm nezmění. Také zobecnění na několik rovin
je snadné. Zobecnění na zakřivenou plochu je náročnější a vyžaduje
jiný typ integrálu.

\fi

V předchozím textu jsme proměnnou veličinu popisující tlak na hráz
jako funkci hloubky nahradili konstantní veličinou, udávající tlak v
těžišti. Výsledný účinek na hráz se nezměnil. To je přesně smysl
střední hodnoty. V matematických pojmech je možno říci, že střední
hodnota tlaku na svislou hráz je rovna tlaku v těžišti hráze. (Protože
hrází myslíme spíše rovinnou plochu, tak by přesnější terminologie
měla používat raději pojem geometrický střed. Budeme se však držet
ustálené terminologie.)

Nikde ve výpočtu jsme nepoužili konkrétní meze pro integraci. Výsledek
tedy platí nejenom pro hráz dosahující k hladině, ale například i pro
poklop výpusti, který je celý pod vodou.

#### Působiště tlakové síly

Budeme pokračovat v předchozím příkladě a hledat působiště výsledné
tlakové síly.

Tlaková síla působící na svislou hráz má celkový nulový moment
vzhledem k ose procházející působištěm. Je-li hráz definována množinou
$M$ a je-li $y_c$ působiště výsledné tlakové síly, je v hloubce $y$
tlak na plošku o velikosti $\Delta S$ roven $y\rho g \Delta S$ a
součin $(y_c-y)y\rho g\Delta S$ je příspěvek k\ otáčivému momentu
vzhledem k\ ose, procházející vodorovně působištěm tlakové
síly. Součet všech těchto příspěvků se nuluje, tedy musí platit
$$\iint_M (y_c-y)y\rho g\,\mathrm dx\mathrm dy=0.$$
Odsud po vydělení konstantami $\rho g$ dostáváme
$$\iint_M (y_c-y)y\,\mathrm dx\mathrm dy=0$$
a po roznásobení závorky, rozdělení integrálu na dva a vytknutí konstanty
$$y_c\iint_M y\,\mathrm dx\mathrm dy = \iint_M y^2\,\mathrm dx\mathrm dy.$$
Nyní již snadno dostaneme výsledný vztah
$$y_c=\frac{\iint_M y^2\,\mathrm dx\mathrm dy}{\iint_M y\,\mathrm dx\mathrm dy}.\tag{H2}\label{H2}$$
Pokud je množina $M$ obdélník, je možné ji (po vhodné změně jednotek) brát jako jednotkový čtverec. Protože platí
$$\iint_{[0,1]\times [0,1]}y\,\mathrm dx\mathrm dy=\frac 12, \quad
\iint_{[0,1]\times [0,1]}y^2\,\mathrm dx\mathrm dy=\frac 13,
$$
dostáváme $y_c=\frac{\frac 13}{\frac 12}=\frac 23$
a působiště na obdélníkovou hráz je v hloubce odpovídající dvěma třetinám celkové hloubky.

Formálně vztah pro $y_c$ odpovídá vztahu pro těžiště množiny s plošnou
hustotou $y$. Na tomto pozorování a na skutečnosti, že u pravidelných
množin umíme těžiště najít geometricky, je založena metoda nalezení
působiště tlakové síly pomocí [zatěžovacího obrazce](https://en.wikipedia.org/wiki/Pressure_prism).

\iffalse

Kvadratický moment v čitateli zlomku $\eqref{H2}$ vyjadřujícího $y_c$ je často
výhodnější rozepsat pomocí Steinerovy věty. Ve jmenovateli je součin
obsahu $S$ a $y$-ové souřadnice těžiště $y_0$. Tím dostaneme
$$y_c=\frac{I_{x0}+Sy_0^2}{Sy_0}=\frac{I_{x0}}{Sy_0}+y_0,$$
kde $I_{x0}$ je kvadratický moment vzhledem k ose procházející vodorovně těžištěm.
Působiště tlakové síly $y_c$ je tedy posunuto směrem dolů od těžiště
$y_0$ o hodnotu odpovídající kvadratickému momentu vzhledem k
vodorovné ose těžištěm $I_{x0}$ vyděleném součinem obsahu hráze $S$ a
$y$-ové polohy těžiště $y_0$.

\fi

## Dvojný integrál v\ polárních souřadnicích

https://youtu.be/lEObYHpX72w

#### Polární souřadnice

<div class='sloupce'>

Dosud jsme používali pouze kartézské souřadnice: dvojici čísel
udávající vzdálenost bodu od osy $y$ a od osy $x$, která jednoznačně
určuje polohu bodu v\ rovině. V\ praxi je někdy výhodnější použít
i\ jiný způsob jak pomocí dvojice čísel charakterizovat polohu bodu
v\ rovině - takové souřadnice potom nazýváme **křivočaré** souřadnice.

Z\ křivočarých souřadnic jsou nejdůležitější **polární
souřadnice**. Při jejich použití polohu bodu $A$ zadáváme tak, že
určíme vzdálenost $r$ bodu od počátku soustavy souřadnic $O$ a úhel
$\varphi$, který svírá spojnice bodů $O$ a $A$ s\ kladnou částí osy
$x$.

\def\maxfactor{0.3}

![Polární souřadnice.](polarni_souradnice.png)

\def\maxfactor{0.6}

</div>

\newpage

#### Množiny s jednoduchým vyjádřením v polárních souřadnicích

Nejsnáze se při výpočtu dvojného integrálu pracuje s obdélníkovými
množinami, tj. s množinami charakterizovanými nerovnostmi pro jednotlivé
proměnné a konstantním omezením pro tyto proměnné. Analogicky se bude
snadno pracovat v polárních souřadnicích s množinami, které by se staly
obdélníky pro překreslení do souřadné soustavy $r$ a $\varphi$. Takové
množiny jsou zobrazeny na následujících obrázcích.

<style>
table, th, td {
   border: 2px solid green;
} 
table {width:97%;}
td {padding:10px}
tr td:nth-child(2) {color:green; background: #E9E9E9;}
table {
    border-collapse: collapse;
}
</style>

<style>
table, th, td {
   border: 2px solid green;
} 
table {width:97%;}
td {padding:10px}
tr td:nth-child(2) {color:green; background: #E9E9E9;}
table {
    border-collapse: collapse;
}

th {
    background-color: green;
    color: white;
    border-color: gray;
}

th {text-align: center;}
</style>

\iffalse

\maxwidthdefault
\def\velkatabulka{\begin{table*}\setlength{\columnwidth}{18cm}}
\def\velkatabulkakonec{\caption{Množiny s jednoduchým zápisem v polárních souřadnících}\end{table*}}

\velkatabulka

|Obrázek        | Popis v polárních souřadnicích | Popis v kartézských souřadnicích |
|----------------|-----------------------|-----------------------|
| \vspace*{0pt} ![](polarni_2.png)   | $$\begin{gathered}0\leq r\leq 1 \\ 0\leq \varphi\leq 2\pi\end{gathered}$$  | $$\begin{gathered}-1\leq x\leq 1\\ -\sqrt{1-x^2}\leq y\leq \sqrt{1-x^2}\end{gathered}$$  |
|  \vspace*{0pt} ![](polarni_1.png)   | $$\begin{gathered}1\leq r\leq 2 \\ 0\leq \varphi\leq \frac \pi2\end{gathered}$$  | Nelze zapsat pomocí jedné dvojice nerovností |
|  \vspace*{0pt} ![](polarni_3.png)  | $$\begin{gathered}0\leq r\leq 1 \\ \frac\pi 4\leq \varphi\leq \frac\pi 2\end{gathered}$$  | $$\begin{gathered}0\leq x\leq \frac {\sqrt 2}2 \\ x\leq y\leq \sqrt{1-x^2}\end{gathered}$$ |

\velkatabulkakonec

\fi

#### Převod dvojného integrálu do polárních souřadnic

\def\maxwidth{5cm}

<div class='obtekat'>

![Element plochy v polárních souřadnicích](jakobian.png)

</div>

Chceme-li převést dvojný integrál do polárních souřadnic, provádíme v\ něm vlastně substituci $x=r\cos \varphi$ a $y=r\sin \varphi$. Přitom
se transformují i\ diferenciály $\mathrm{d}x$ a $\mathrm{d}y$.  Při
změně úhlu o $\mathrm{d}\varphi$ a změně vzdálenosti o $\mathrm{d}r$
má odpovídající část roviny rozměry $\mathrm{d}r$ a
$r\mathrm{d}\varphi$ a její obsah je $r\mathrm{d}\varphi\mathrm{d}r$
(viz obrázek). Platí tedy, že obsah elementární oblasti $\mathrm{d}
A=\mathrm{d} x\mathrm{d}y$ se transformuje na $\mathrm{d}
A=r\mathrm{d}\varphi\mathrm{d}r$. Podíl
$\frac{\mathrm{d}\varphi\mathrm{d}r }{\mathrm{d}x \mathrm{d}y }$
udává, kolikrát se změní obsah elementární oblasti při změně souřadnic
a nazývá se **jakobián**. V\ případě polárních souřadnic je jakobián
jak vidíme roven $r$ a platí tedy
$$
  \iint_{\Omega}f(x,y){\mathrm{d}x \mathrm{d}y }=\iint_{\Omega}f(r\cos \varphi ,
  r\sin\varphi ){r\mathrm{d}\varphi\mathrm{d}r }.
$$
  
V\ diferenciálním počtu polární souřadnice používáme především tam, kde
má problém radiální symetrii. Například při studiu ochlazování nebo
kmitů kruhových desek či válcovitých součástek. V\ integrálním počtu
tyto souřadnice použijeme zejména v\ případě, kdy integrujeme přes
kružnici nebo její část (např. mezikruží či kruhová výseč). V\ takovém
případě mají totiž integrály které vzniknou po transformaci dvojného
integrálu na dvojnásobný pevné meze a výpočet druhého integrálu je
zpravidla jednodušší. 

## Z ptačí perspektivy

\iffalse

<div class='obtekat'>

![Ještě pohled s trochou nadhledu. Zdroj: pixabay.com](../falcon.jpg)

</div>

\fi

* Dvojný integrál využijeme tam, kde nás zajímá celková hodnota aditivní veličiny, jejíž příspěvky jsou rozloženy ve dvourozměrné ploše. Například celková tlaková síla na stěnu akvária. 
* Dvojný integrál počítáme jako integrál z integrálu aparátem integrálního počtu funkcí jedné proměnné. V řadě případů se však problém dá zjednodušit. Například při integrování funkcí se separovanými proměnnými přes obdélníkové množiny se integrál dá zapsat jako součin integrálů. Podobně, při integrování přes množiny které jsou částmi kruhu se dá v mnoha případech integrál přepsat pomocí polárních souřadnic na integrál přes obdélník (v polárních souřadnicích). 

