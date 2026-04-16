# %%
import numpy as np
import matplotlib.pyplot as plt

def phi(i,x):
    """Triangle basis function, equal to 1 at node i and 0 at other nodes."""
    if i-1 <= x <= i:
        return (x - (i - 1)) / (1)
    elif i <= x <= i + 1:
        return ((i + 1) - x) / (1)
    else:
        return 0

x = np.linspace(0, 1, 11)
y = np.array([[phi(j,10*i) for i in x] for j in range(1,10)]).T
# combine columns of y with weights

weights = np.array([2*i/10*(1 - i / 10) for i in range(1, 10)])
yy = y @ weights

fig, ax = plt.subplots()

for i in [2,5,6]:
    ax.plot(x, y[:,i-1], label=r'$\varphi_{%d}(x)$'% (i))

ax.plot(x, yy, label=r'$\sum_{i=1}^{9}{2i(1-i)}\varphi_i(x)$')
ax.legend()
ax.set(title='Bázové funkce v metodě konečných prvků',
    xlabel='x',ylabel='Hodnota funkce')
ax.grid()
ax.set_xticks(np.arange(0, 1.1, 0.1))
plt.savefig('konecne_prvky.png')


# %%
