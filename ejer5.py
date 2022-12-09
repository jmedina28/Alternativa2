from itertools import cycle

def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])

def codificar_rail_fence_cipher(string, n):
    p = rail_pattern(n)
    return ''.join(sorted(string, key=lambda i: next(p)))

def decodificar_rail_fence_cipher(string, n):
    p = rail_pattern(n)
    indices = sorted(range(len(string)), key=lambda i: next(p))
    resultado = [''] * len(string)
    for i, c in zip(indices, string):
        resultado[i] = c
    return ''.join(resultado)

print(codificar_rail_fence_cipher("Hola Mundo", 4))
print(decodificar_rail_fence_cipher("HuoMnl dao", 4))