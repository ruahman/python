# Modules in Python are just Python files with a .py extension.
# The name of the module will be the name of the file.
# Modules are imported from other modules using the import command.

# You may have noticed that when importing a module, a .pyc file is created.
# This is a compiled Python file.
# Python compiles files into Python bytecode so that it won't have to parse the files each time modules are loaded.
# If a .pyc file exists, it gets loaded instead of the .py file.

# Module initialization
# The first time a module is loaded into a running Python script,
# it is initialized by executing the code in the module once.
# If another module in your code imports the same module again,
# it will not be loaded again, so local variables inside the module act as a "singleton,"
# meaning they are initialized only once.

# We can look for which functions are implemented in each module by using the dir function:
# When we find the function in the module we want to use, we can read more about it with the help function

# Packages are namespaces containing multiple packages and modules.
# They're just directories, but with certain requirements.

# Each package in Python is a directory which MUST contain a special file called __init__.py.
# This file, which can be empty, indicates that the directory it's in is a Python package

# The __init__.py file can also decide which modules the package exports as the API,
# while keeping other modules internal, by overriding the __all__ variable like so:

