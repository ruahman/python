import marimo

__generated_with = "0.12.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sympy as sym
    import numpy as np
    from IPython.display import display, Math 
    return Math, display, mo, np, sym


@app.cell
def _(Math, display, np, sym):
    A = np.array([[1,2],[3,4]])

    display(Math(sym.latex(sym.sympify(A))))
    return (A,)


@app.cell
def _(np):
    mat = np.zeros([4,6])
    mat[0,1] = 2
    mat[2,4] = 7
    mat
    return (mat,)


@app.cell
def _(Math, display, np, sym):
    x,y = sym.symbols('x y')
    Fxy = (4+ x)*(2 - y)
    xyset = range(0,3)

    outmat = np.zeros([len(xyset),len(xyset)])
    outmat

    for i in xyset:
        for j in xyset:
            outmat[i,j] = Fxy.subs({x:i,y:j})

    display(Math(sym.latex(sym.sympify(outmat))))
    return Fxy, i, j, outmat, x, xyset, y


@app.cell
def _(Math, display, np, sym):
    nums = range(1,11)
    matmult = np.zeros((len(nums),len(nums)), dtype=int)
    for row in nums:
        for col in nums:
            matmult[row - 1, col - 1] = row*col

    display(Math(sym.latex(sym.sympify(matmult))))
    return col, matmult, nums, row


if __name__ == "__main__":
    app.run()
