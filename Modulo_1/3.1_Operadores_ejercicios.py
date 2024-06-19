"""
Escribir un programa que solicite dos números y luego imprima:
    1. La suma de los dos números
    2. La resta del primer número menos el segundo
    3. El producto de los dos números
    4. El cubo de la suma de los dos números
    5. El cociente de la división del primer número por el segundo
"""
num1 = float(input("Ingrese el primer número por favor"))
num2 = float(input("Ingrese el segundo número por favor"))
print("Suma:", num1+num2)
print("Resta:", num1-num2)
print("Producto:", num1*num2)
print("Cubo:", (num1+num2)**3)
print("División:", num1/num2)