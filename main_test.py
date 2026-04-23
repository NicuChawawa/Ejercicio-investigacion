from main import mayoria_edad

def test_mayoria_edad():
    assert mayoria_edad(21) == "El usuario es mayor de edad"

from main import espar

def test_espar():
    assert espar(4) == "El número es par"

from main import palindromo

def test_palindromo():
    assert palindromo("Radar") == True