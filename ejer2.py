import math

def axb_extraccion(expr):
    expr = expr[::-1]
    partes = expr.split('+', 1)
    if len(partes) != 2:
        partes = expr.split('-', 1)
        partes[0] += '-'

    a_str = partes[1]
    a_str = a_str[1:]
    a_str = a_str[::-1]
    if a_str == '' or a_str == '-':
        a_str += '1'

    a = int(a_str)
    x = partes[1][0]
    b = int(partes[0][::-1])

    return a, x, b

def binom_coeficiente(n):
    top = list(range(n, math.floor((n+1)/2), -1))
    bot = list(range(1, math.ceil((n+1)/2), 1))

    for i in range(1, len(top)):
        top[i] *= top[i-1]
        bot[i] *= bot[i-1]

    coeficiente = [1]
    for i in range(len(top)):
        coeficiente.append(top[i]//bot[i])

    coeficiente2 = coeficiente if n % 2 == 1 else coeficiente[:-1]
    coeficiente += coeficiente2[::-1]

    return coeficiente

def expand(expr):
    partes = expr.split('^', 1)
    exponente = int(partes[1])

    if exponente == 0:
        return '1'
    elif exponente == 1:
        return partes[0][1:-1]

    a, x, b = axb_extraccion(partes[0][1:-1])

    coeficiente = binom_coeficiente(exponente)

    qa = 1
    qb = 1
    for i in range(exponente+1):
        coeficiente[exponente-i] *= qb
        coeficiente[i] *= qa
        qb *= b
        qa *= a

    elementos = []

    for i in range(exponente, -1, -1):
        sign = '+' if coeficiente[i] > 0 else '-'
        coeficiente_elemento = abs(coeficiente[i]) if abs(coeficiente[i]) > 1 else ''
        if i > 1:
            elementos.append('{}{}{}^{}'.format(sign, coeficiente_elemento, x, i))
        elif i == 1:
            elementos.append('{}{}{}'.format(sign, coeficiente_elemento, x))
        else:
            elementos.append('{}{}'.format(sign, coeficiente_elemento))

    if elementos[0][0] == '+':
        elementos[0] = elementos[0][1:]

    if len(elementos[-1]) == 1:
        elementos[-1] += '1'

    return ''.join(elementos)

print(expand("(2f+4)^6"))