import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    print("Hello")
    print('Hello')
    return


@app.cell
def _():
    print("It's alright")
    print("He is called 'Johnny'")
    print('He is called "Johnny"')
    return


@app.cell
def _():
    a = """Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua."""
    print(a)
    return (a,)


@app.cell
def _(a):
    _a = '''Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.'''
    print(a)
    return


@app.cell
def _():
    _a = "Hello, World!"
    print(_a[1])
    return


@app.cell
def _():
    for x in "banana":
      print(x)
    return (x,)


@app.cell
def _():
    _a = "Hello, World!"
    print(len(_a))
    return


@app.cell
def _():
    txt = "The best things in life are free!"
    print("free" in txt)
    return (txt,)


@app.cell
def _():
    _txt = "The best things in life are free!"
    if "free" in _txt:
      print("Yes, 'free' is present.")
    return


@app.cell
def _():
    _txt = "The best things in life are free!"
    print("expensive" not in _txt)
    return


@app.cell
def _():
    _txt = "The best things in life are free!"
    if "expensive" not in _txt:
      print("No, 'expensive' is NOT present.")
    return


@app.cell
def _():
    b = "Hello, World!"
    print(b[2:5])
    return (b,)


@app.cell
def _():
    _b = "Hello, World!"
    print(_b[:5])
    return


@app.cell
def _():
    _b = "Hello, World!"
    print(_b[2:])
    return


@app.cell
def _():
    _b = "Hello, World!"
    print(_b[-5:-2])
    return


@app.cell
def _():
    _a = "Hello, World!"
    print(_a.upper())
    return


@app.cell
def _():
    _a = "Hello, World!"
    print(_a.lower())
    return


@app.cell
def _():
    _a = " Hello, World! "
    print(_a.strip()) # returns "Hello, World!"
    return


@app.cell
def _():
    _a = "Hello, World!"
    print(_a.replace("H", "J"))
    return


@app.cell
def _():
    age = 36
    txt = "My name is John, I am " + str(age)
    print(txt)
    return age, txt


@app.cell
def _():
    _age = 36
    _txt = f"My name is John, I am {_age}"
    print(_txt)
    return


@app.cell
def _():
    _txt = "We are the so-called \"Vikings\" from the north."
    print(_txt)
    return


if __name__ == "__main__":
    app.run()
