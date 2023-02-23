# 2022 S2 Portafolio #1

El archivo debe llamarse **Portafolio1.py**, además respetar el nombre de las funciones que más adelante se describen
Recordar hacer las validaciones de cada una de las restricciones

Recordar los comentarios, validaciones y el hacer uso de las estructuras ***IF, WHILE o FOR***

## divisores(num)
Imprimir los divisores de un número de manera descendente.
Solo números enteros positivos.

```python
>>>divisores(24)
[24, 12, 8, 6, 4, 3, 2, 1]
```

## potencia(base, exponente)  
Potencia de un número base elevado a un número exponente sin utilizar el operador de potencia.
Para ambos parámtros solo números enteros positivos.

```python
>>>potencia(5, 2)
25
```

## division(dividendo, divisor)
Resultado de la división entera un número “dividendo” entre un número “divisor” sin utilizar el operador de división.
Para ambos parámtros solo números enteros positivos.
Tomar en cuenta la divisón entre cero no es permitido.

```python
>>>division(25, 5)
5
>>>division(25, 0)
'Error: División entre cero'  
```

## indiceNumero(num, indice)
Retorna el dígito del número según índices.
Para ambos parámtros solo números enteros positivos.
La lectura debe ser de izquiera a derecha, iniciando desde desde 1
```python
>>>indiceNumero(1235, 3)  	
3
>>>indiceNumero(1335, 8)
'Error: Indice fuera del rango del número'
```

## cortarNumero(num, ini, fin)
Construir una función que reciba un número y ordenados de manera ascendente.
Para ambos parámtros solo números enteros positivos.
Verificar que los parámtros ini y fin no sobre pasen el largo del número.
```python
>>>cortarNumero(1235, 2, 3)
23
>>>cortarNumero(1335, 8, 2)
'Error: Indices fuera del rango del número'
```

