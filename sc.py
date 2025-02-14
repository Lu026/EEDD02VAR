#Sentencia de control: bifurcación
a=50
if a%2==0:
    print(f"El valor{a} es un numero par")
else:
    print(f"El valor {a} es un numero impar")    



if a>50:
    print(f"El valor {a} es mayor que 50")
elif a<50:
     print(f"El valor {a} es menor que 50")
else:
    print(f"El valor {a} es 50")

num= input("Introduce un valor...")
print("Valor introducido",num)

#bucle while
#devuelve la cadena de carácteres
num=int(num)
a=0
while a<num:
    print("a:",a)
    a+=1
#bucle que solicite numeros al usuario hasta que se introduzca un numero par
#recorre estructuras
sum = 0  
for a in range(10):
    sum += a
    print("a:", a, ", sum:", sum)

while a<num:
    print("a:",a)
    a+=1

#Solicita numeros al usuario hasta que introduzca numero par
while True:  
    num = int(input("Introduce un número: "))  #Scanner en java
    if num % 2 == 0:  # Verifica si el número es par  
        print("Número par detectado. Fin del programa.")  
        break  # Sale del bucle si el número es par 

#Solicita numeros al usuario hasta que introduzcan 2 numeros pares
num1 = None
num2 = None

while num1 is None or num2 is None:
    num = int(input("Introduce un número: "))
    if num % 2 == 0:
        if num1 is None:
            num1 = num
        elif num2 is None:
            num2 = num

print("Números pares introducidos:", num1, num2)
