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


#Ejercicio 22    
def usar_la_fuerza(mochila, i=0):
    # Caso base: se vació la mochila, no había sable
    if i >= len(mochila):
        print(f"Se revisaron todos los objetos. No hay sable de luz.")
        return False, 0

    # Simulamos "sacar" el objeto actual
    print(f"Sacando objeto {i+1}: {mochila[i]}")

    # Caso base: encontramos el sable
    if mochila[i] == "sable de luz":
        print(f"¡Encontrado el sable de luz!")
        return True, i+1   # i+1 = cantidad de objetos que se sacaron

    # Caso recursivo: seguimos buscando
    return usar_la_fuerza(mochila, i+1)


