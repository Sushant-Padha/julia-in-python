# julia-in-python

Examples on how to use Julia in Python.

## Tutorial

### Installation

- If using a python virtual environment, do this before following further steps:
    Activate the environment
    
Set the environment variable `PYCALL_JL_RUNTIME_PYTHON` and `PYTHON` to the path of the `python` executable (set it to env executable if environment is activated).  
For more info, see [PyCall.jl](https://github.com/JuliaPy/PyCall.jl).

Note that these steps will have to be repeated again or each different environment.


1. Install [Julia](https://julialang.org/downloads/) for your OS.

2. Install PyJulia with:
    ```bash
    python3 -m pip install -U julia
    ```

3. Install the required Julia packages by running this in the Python REPL:
    ```python
    import julia
    julia.install()
    ```

4. Just to be sure, rebuild the package in Julia by opening the Julia REPL:
    ```julia
    using Pkg
    Pkg.build("PyCall")
    ```

To test if the installation works, run `from julia import Main` in a python REPL.  
If an error is returned, delete/remove everything and follow these steps again.

Remove python `julia` package using `python3 -m pip uninstall julia`, and remove julia `PyCall` package using `rm PyCall` by starting `julia` and entering package manager by typing `]`.

### Usage

Run the following lines of code in a REPL or add them to your code file:

```python
from julia.api import Julia  # these two lines take a long time to execute
from julia import Main

jl = Julia(compiled_modules=False)

# run any one of the following two lines
jl.eval('include("test.jl")')
Main.include("test.jl")
```

### Useful Information

`Julia` is the object representing julia.  
`Main` is the default Julia namespace (used to define and access variables, functions etc.).  
`jl.eval(...)` is used to execute Julia. `include("test.jl")` is used in Julia to include `test.jl` file.

To pass on your variables to the Julia namespace, define them like:
```python
Main.var_in_julia = var_in_python
```
You can now use the variable `var_in_julia` inside your Julia code.  
To execute a function or method defined in the .jl file, use either:

1. `jl.eval('my_func(var_in_julia)')` - to run it in the julia namespace using its defined objects.
2. `Main.my_func(var_in_python)` - to run it by directly accessing it in python.


- In Julia, the `Pkg` package is used to add new packages, remove packages, create packages, activate environments etc.  
  Add new packages using:  
    ```julia
    using Pkg
    Pkg.add("PackageName")
    ```
    The first line adds `Pkg` to the namespace, and second line installs package `PackageName`.  

- For bigger projects, where including one or two scripts isn't enough, you can create a Julia package in current directory using: (run in Julia REPL)
    ```julia
    using Pkg
    Pkg.generate("MyPackage")
    ```  
    Main file is created as `MyPackage.jl` in `src` folder inside `MyPackage`.  
    Create more files in the `src` folder.  
    Export the necessary objects in the `MyPackage.jl` file with `export my_class, my_func, my_var`.  

    Folder structure for `MyPackage`:
    ```text
    PATH/TO/
    |
    +-- MyPackage/
        |
        +-- src/
        |   |
        |   +-- MyPackage.jl
        |   +-- SomeCode.jl
        |   +-- SomeMoreCode.jl
        |
        +-- Project.toml
        +-- Manifest.toml
    ```


- Import the package in python using:
    ```python
    from julia import Pkg
    Pkg.activate("PATH/TO/MyPackage")
    from julia import MyPackage
    ```  
    Objects defined in `MyPackage` can be used directly using `MyPackage.my_class`, `MyPackage.my_func`, `MyPackage.my_var`.
