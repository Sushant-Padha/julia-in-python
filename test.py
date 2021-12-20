from julia.api import Julia
from julia import Main

jl = Julia(compiled_modules=False)

# `jl.eval()` runs jl code
test_jl = jl.eval('include("test.jl")')

# test.jl defines functions `sphere_vol`, `quadratic`, `quadratic2`

# initialize variables
radius = 10.0
a1, b1, c1 = 1.0, -5.0, 6.0

# define those variables in the julia namespace (referred to by Main)
Main.radius = radius
Main.a1, Main.b1, Main.c1 = a1, b1, c1

# run functions
volume = jl.eval('sphere_vol(radius)')
x1, x2 = jl.eval('quadratic2(a1, b1, c1)')

print(f'Volume of sphere with radius {radius} is {volume}.')
print(f'Solutions of the quadratic with coefficients {a1}, {b1}, {c1} are ' +
      f'{x1}, {x2}.')
