import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(np, plt):
    # leave these parameters as-is
    n = 1000000
    t = np.logspace(np.log10(10),np.log10(500),n)

    # try chaning these parameters
    A = [  1, 1, 1.5, 1.5 ]
    d = [ .004, .001, .002, .0015 ]
    f = [   3, 1, 2, 2.5 ]

    # generate XY value pairs
    x = A[0]*np.sin(t*f[0])*np.exp(-d[0]*t) + A[1]*np.sin(t*f[1])*np.exp(-d[1]*t)
    y = A[2]*np.sin(t*f[2])*np.exp(-d[2]*t) + A[3]*np.sin(t*f[3])*np.exp(-d[3]*t)

    # plot them!
    plt.plot(x,y,'k',linewidth=.1)
    plt.axis('off')
    plt.show()
    return A, d, f, n, t, x, y


@app.cell
def _(d, f, np, plt, t):
    # what are the elementary components of the plots above? Let's have a look!
    plt.plot(np.sin(t*f[0])*np.exp(-d[0]*5*t),linewidth=.5)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
