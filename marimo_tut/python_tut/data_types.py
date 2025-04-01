import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    _x = 5
    print(type(_x))
    _x = int(20)
    _x
    return


@app.cell
def _():
    _x = "Hello World"	
    print(_x)
    _x = str("Hello World")
    _x
    return


@app.cell
def _():
    _x = 20.5
    print(_x)
    x = float(20.5)
    _x
    return (x,)


@app.cell
def _():
    _x = ["apple", "banana", "cherry"]
    print(_x)
    _x = list(("apple", "banana", "cherry"))
    _x
    return


@app.cell
def _():
    _x = ("apple", "banana", "cherry")
    print(_x)
    _x = tuple(("apple", "banana", "cherry"))
    _x
    return


@app.cell
def _():
    _x = range(6)	
    print(_x)
    _x = range(6)
    _x
    return


@app.cell
def _():
    _x = {"name" : "John", "age" : 36}
    print(_x)
    _x = dict(name="John", age=36)
    _x
    return


@app.cell
def _():
    _x = {"apple", "banana", "cherry"}
    print(_x)
    _x = set(("apple", "banana", "cherry"))
    _x
    return


@app.cell
def _():
    _x = bool(5)
    print(_x)
    _x = True
    _x
    return


@app.cell
def _():
    _x = b"Hello"
    print(_x)
    _x = bytes(5)
    _x
    return


@app.cell
def _():
    _x = None
    print(_x)
    return


if __name__ == "__main__":
    app.run()
