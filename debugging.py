import pdb

def square(n):
    return n*n

x = 20
y = 10
pdb.set_trace()
print(square(x))
print(square(y))

# n(next), c(complete execution), display -var-, p(print), pp(pretty-print), cl(clear all breakpoints), b(create breadkpt. b 12), w(directory location), l (lists -3, +3 line from current line of execution of code), unt(until the line with a number greater than the current one is reached), etc..