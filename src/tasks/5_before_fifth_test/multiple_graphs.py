import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x + 1

def g(x):
    return x**2 - 3

def h(x):
    return 2**x

def i(x):
    return x/3

x_verdier = np.linspace(0, 25, 251)

# I have chosen a 2x2 frame, where the axl objects are in two tuples
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)

# Make padding within both graphs
fig.tight_layout(pad=2)

#graf 1
y_verdier = f(x_verdier)
ax1.plot(x_verdier, y_verdier, color="blue")
ax1.grid()
ax1.set_title("Function: $f(x)=2x+1$")
ax1.set_xlim(0,5)
ax1.set_ylim(0,15)

#graf 2
y_verdier = g(x_verdier)
ax2.plot(x_verdier, y_verdier, color="blue")
ax2.grid()
ax2.set_title("Function: $f(x)=x^2-3$")
ax2.set_xlim(0,5)
ax2.set_ylim(0,25)

#graf 3
y_verdier = h(x_verdier)
ax3.plot(x_verdier, y_verdier, color="blue")
ax3.grid()
ax3.set_title("Function: $f(x)=2^x$")
ax3.set_xlim(0,5)
ax3.set_ylim(0,25)

#graf 4
y_verdier = i(x_verdier)
ax4.plot(x_verdier, y_verdier, color="blue")
ax4.grid()
ax4.set_title("Function: $f(x)=\\frac{x}{3}$")
ax4.set_xlim(0,5)
ax4.set_ylim(0,3)

plt.savefig("5/4graf-plot.png",dpi=300)
plt.show()