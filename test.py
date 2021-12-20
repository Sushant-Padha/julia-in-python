from julia.api import Julia
from julia import Main

jl = Julia(compiled_modules=False)

# `jl.eval()` runs jl code
# `Main` is the default Julia namespace

jl.eval('include("test.jl")')
Main.include("test.jl")

# test.jl defines functions `sphere_vol`, `quadratic`, `quadratic2`

# initialize variables
radius = 10.0
a1, b1, c1 = 1.0, -5.0, 6.0

# define those variables in the julia namespace
Main.radius = radius
Main.a1, Main.b1, Main.c1 = a1, b1, c1

# run functions
unit_volume = Main.unit_volume
volume = Main.sphere_vol(radius)  # running it in python
x1, x2 = jl.eval('quadratic2(a1, b1, c1)')  # running it in julia

print(f'Volume of unit sphere will be {unit_volume}')
print(f'Volume of sphere with radius {radius} is {volume}.')
print(f'Solutions of the quadratic with coefficients {a1}, {b1}, {c1} are ' +
      f'{x1}, {x2}.')
