def compute(a, b):
    result = a + b
    breakpoint()  # program stops here, open interactive debugger
    return result * 2

print(compute(3, 4))