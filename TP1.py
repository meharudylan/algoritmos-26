#Ejercicio 5
def romano_a_decimal(s):
    valores = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    def rec(i):
        if i >= len(s):
            return 0
        if i == len(s) - 1:
            return valores[s[i]]
        if valores[s[i]] < valores[s[i+1]]:
            return -valores[s[i]] + rec(i+1)
        return valores[s[i]] + rec(i+1)

    return rec(0)

#Ejercicio 6
def invertir(cadena):
    if cadena == "":
        return ""
    return invertir(cadena[1:]) + cadena[0]

#Ejercicio 7
def serie(n):
    if n == 1:
        return 1
    return 1/n + serie(n-1)

#Ejercicio 8
def decimal_a_binario(n):
    if n < 2:
        return str(n)
    return decimal_a_binario(n//2) + str(n%2)

#Ejercicio 9
def log_entero(n, b):
    if n < b:
        return 0
    return 1 + log_entero(n//b, b)

#Ejercicio 10    
def contar_digitos(n):
    if n < 10:
        return 1
    return 1 + contar_digitos(n//10)

#Ejercicio 11    
def invertir_num(n, res=0):
    if n == 0:
        return res
    return invertir_num(n//10, res*10 + n%10)
                     
#Ejercicio 12
def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

#Ejercicio 13
def mcm(a, b):
    return (a * b) // mcd(a, b)

#Ejercicio 14
def suma_digitos(n):
    if n == 0:
        return 0
    return n % 10 + suma_digitos(n//10)

#Ejercicio 15
def raiz_entera(n, i=0):
    if i*i > n:
        return i-1
    return raiz_entera(n, i+1)

#Ejercicio 16
def sucesion_geo(a1, r, n):
    if n == 1:
        return a1
    return r * sucesion_geo(a1, r, n-1)

#Ejercicio 17
def mostrar_reves(vec, i):
    if i < 0:
        return
    print(vec[i])
    mostrar_reves(vec, i-1)

#Ejercicio 18
def recorrer_matriz(mat, i=0, j=0):
    if i >= len(mat):
        return
    if j >= len(mat[0]):
        recorrer_matriz(mat, i+1, 0)
        return
    print(mat[i][j])
    recorrer_matriz(mat, i, j+1)

#Ejercicio 19

def f(n):
    if n == 1:
        return 2
    return n + 1 / f(n-1)

#Ejercicio 20
def busqueda(lista, x, i=0):
    if i >= len(lista):
        return False
    if lista[i] == x:
        return True
    return busqueda(lista, x, i+1)

#Ejercicio 21
def busqueda_binaria(lista, x, ini, fin):
    if ini > fin:
        return False
    mid = (ini + fin) // 2
    if lista[mid] == x:
        return True
    elif x < lista[mid]:
        return busqueda_binaria(lista, x, ini, mid-1)
    else:
        return busqueda_binaria(lista, x, mid+1, fin)
    
#Ejercicio 22
def usar_la_fuerza(mochila, i=0):
    if i >= len(mochila):
        return False, i
    if mochila[i] == "sable de luz":
        return True, i+1
    return usar_la_fuerza(mochila, i+1)

