# Mayoría de edad

def mayoria_edad(edad):
    if edad > 18:
        return "El usuario es mayor de edad"
    else:
        return "El usuario es menor de edad"

# Es par o impar?

def espar(num):
    calculo = num % 2
    if calculo == 0:
        return "El número es par"
    else:
        return "El número es impar"
    
# Palindromo

def palindromo(txt):
    txt = txt.replace(" ", "").lower()
    return txt == txt[::-1]