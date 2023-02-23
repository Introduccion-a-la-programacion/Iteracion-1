import Practica;
import pytest;

def test_1():
    assert Practica.sumatoria(5) == 15
    
def test_2():
    assert Practica.factorial(0) == 1
    
def test_3():
    assert Practica.factorial(3) == 6
    
def test_4():
    assert Practica.sumatoriaDescendente(5) == 15
    
def test_5():
    assert Practica.sumatoriaParcial(3, 6) == 18
    
def test_6():
    assert Practica.contarDigitos(306) == 3
    
def test_7():
    assert Practica.contarDigitos(0) == 1
    
def test_8():
    assert Practica.contarDigitosImpares(305) == 2
    
def test_9():
    assert Practica.contarDigitosImpares(0) == 0
