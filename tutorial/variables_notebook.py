import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    message = "Hello, World!"
    print(message)
    return (message,)


@app.cell
def _():
    _message = "Helltdddo, Python Crash Course world!"
    print(_message)

    return


@app.cell
def _():
    _fruits = ["apple", "banana", "cherry"]
    _x, _y, _z = _fruits
    print(_x)
    print(_y)
    print(_z)
    return


@app.cell
def _():
    _x, _y, _z = "Orange", "Banana", "Cherry"
    print(_x)
    print(_y)
    print(_z)
    return


if __name__ == "__main__":
    app.run()
