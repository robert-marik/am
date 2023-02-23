% Rotace, kmenová funkce gradientu

> Anotace.
>
> * V úvodu si zkusíme vypočítat několik rotací pro získání určité míry jistoty při práci s tímto operátorem. 
> * V další části se budeme věnovat hledání kmenové funkce vektorového pole. Rotace informuje o tom, zda tato úloha má řešení, k nalezení tohoto řešení však už nijak nepřispívá. Protože však vzhledem k výše uvedenému problematika k rotaci logicky patří, jsou tyto úlohy zařazeny pospolu. Protože ve dvourozměrném poli se rotace výrazně zjednodušuje, může být nulovost rotace nahrazena rovností mezi jistými dvěma parciálními derivacemi.


# Rotace vektorového pole v rovině

https://youtu.be/IRjknyO2_yo


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
 &=\vec k\qty({\pdv {2xy}{x}-\pdv {xy^2}{y}})\\&
 =\vec k(2y-2xy)\\&=2y(1-x)\vec k
\end{aligned}
 $$



</div>

# Rotace vektorového pole v prostoru


https://youtu.be/U_USLTQF5fM

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
\vec \imath \ \qty[\pdv {(-3x^2z)}{y}-\pdv {5x^2y}{z}]
 +\vec \jmath \ \qty[\pdv {xyz}{z}-\pdv {(-3x^2z)}{x}] 
 +\vec k\ \qty[{\pdv {5x^2y}{x}-\pdv {xyz}{y}}]\\
 &=(xy+6xz)\vec\jmath + (10xy-xz)\vec k
\\&=x(y+6z)\vec\jmath + x(10y-z)\vec k
\end{aligned}
 $$



</div>

# Divergence a rotace 2D funkce s parametrem


https://youtu.be/ZRIHxmBzf5s

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


# Nalezení kmenové funkce 1/3

https://youtu.be/cjN80-0M77Q

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

# Nalezení kmenové funkce 2/3

https://youtu.be/Km-_WWQi_kg

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

# Nalezení kmenové funkce 3/3

https://youtu.be/mgZl8AScBgI

Pro vektorové pole $$\left(y+\frac 45 x y^3\right)\vec \imath + \left(\frac 65x^2y^2+x^2\right)\vec\jmath$$ najděte funkci $\varphi$ tak, že zadané vektorové pole je rovno gradientu $\nabla \varphi.$



<div class=reseni>

Platí $\pdv {\varphi}{x}=y+\frac 45 xy^3$ a $\pdv{\varphi}{y}=\frac 65 x^2y^2+x^2$.

Odsud
$$\varphi =\int \pdv{\varphi}{x} \,\mathrm dx=\int y+\frac 45 xy^3 \,\mathrm dx
=xy+\frac 45 \frac {x^2}{2}y^3=xy+\frac 25 x^2y^3+C_1(y)$$
a
$$\varphi =\int \pdv{\varphi}{y} \,\mathrm dy=\int \frac 65 x^2y^2 +x^2 \,\mathrm dy
=\frac 65 {x^2}\frac{y^3}3+x^2y=\frac 25 x^2y^3+x^2y+ C_2(x).$$
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


