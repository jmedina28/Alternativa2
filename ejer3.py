valores = [0,1,2,5,6,7,10,11,12]
def contarpatrones(puntoinicial, longitud, left=set(valores)):
    if longitud<1 or longitud>len(left): return 0
    if longitud==1: return 1
    n = valores[ord(puntoinicial)-65] if type(puntoinicial)==str else puntoinicial
    return sum(contarpatrones(m,longitud-1,left-{n}) for m in left-{n} if (m+n)/2 not in left)

print(contarpatrones('E',4))