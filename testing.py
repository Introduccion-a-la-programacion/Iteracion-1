import Portafolio1;
import pytest;

def test_divisores_1():
    assert Portafolio1.divisores(24) == [24, 12, 8, 6, 4, 3, 2, 1]
      
###########################################################################

def test_potencia_1():
    assert Portafolio1.potencia(5, 2) == 25
    
###########################################################################    

def test_division_1():
    assert Portafolio1.division(25, 5) == 5
    
def test_division_2():
    assert isinstance(str(Portafolio1.division(25, 0)), str) == isinstance('Error: División entre cero', str)
    
###########################################################################       

def test_indiceNumero_1():
    assert Portafolio1.indiceNumero(1235, 3) == 3
    
def test_indiceNumero_2():
    assert isinstance(str(Portafolio1.indiceNumero(1335, 8)), str) == isinstance('Error: Indice fuera del rango del número', str)
    
###########################################################################    

def test_cortarNumero_1():
    assert Portafolio1.cortarNumero(1235, 2, 3) == 23

def test_cortarNumero_2():
    assert isinstance(Portafolio1.cortarNumero(1335, 8, 2), str) == isinstance('Error: Indices fuera del rango del número', str)  
