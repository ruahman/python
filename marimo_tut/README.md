marimo is a reactive notebook for Python,
- reproducible, 
- git-friendly 
- SQL built-in
- executable as an app

run a basic tutorial
`marimo tutorial intro`

run one cell and marimo reacts by running all affected cells.
- eliminating the error-prone chore of managing notebook state.

marimo's UI elements

marimo notebooks are pure python and stored as .py files

notebooks are executed in a deterministic order

a marimo notebook is powered by WASM:
it's running enirely in your browser

to see all tutorial 
`marimo tutorial --help`


# key concepts

marimo lets you interact with data using Python, SQL, and interactive elements

marimo notebooks can be shared as interactive web apps

marimo notebooks are reactive: they automaticaly react to your code changes and UI interactions
kinda like spreadsheets

if you dont want cells to run automatically, the runtime can be configured to be lazy,
only running cells when you ask them to and marking affected cells as stale.

you can create a note book this way 
`marimo edit my_notebook.py`

we recommend starting each marimo notebook with a cell containing a single line of code,
`import marimo as mo`
- the marimo library lets you use interactive UI elements, layout elements, dynamic markdown, and more
  in you marimo notebook

a marimo notebook is made up of small blocks of Python code called cells.

when you run a cell, marimo automatically runs all cells that read any global variables defined by that cell.

the order of cells has no bearing on the order cells are executed.
execution order is determined by the variables cells define and the variables they read.

see **reactivity guide** and `marimo tutorial dataflow`

## visializing outputs 

marimo visualizs the last expression of each cell as its output

try these tutorials 

marimo tutorial markdown
marimo tutorial plots
marimo tutorial layout

to use a UI element, create it with mo.ui and assign it to a global variable.
when you interact with the UI element, marimo sends the new value back to Python 
and reactively runs all cells that use the element

for UI examples 
marimo tutorial ui  

# Query dataframes and databases with SQL 
marimo has built-in support for SQL
- you can query Python dataframes, databases, CSVs, Google Sheets, etc

marimo tutorial sql 


# run notebooks as applications 

marimo run my_notebook.py






