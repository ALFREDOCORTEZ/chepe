#para realizar la suma de dos numeros

a = 0
b = 0
c = 0

a = float (input("ingresa el primer numero: "))

b = float (input("ingresar el sugundo numero: "))

if a > 0 or b > 0:
  print ("suma de numeros")
  c = a + b
else :
  print ("multiplicacion de resultados ")
  c = a * b

print("El resultado de la operacion: " , c)