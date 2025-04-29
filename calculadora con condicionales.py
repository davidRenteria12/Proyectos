num1 = float(input("ingresa primer numero: "))
operador = input("ingresa el operador (+, - , /, *):  ")
num2 = float(input("ingresa segundo numero: " ))

if operador == " + ":
    print("Resultado:", num1 + num2)
    
elif operador == "-":
    print("Resultado",  num1- num2)
elif operador == "*":
    print("Resultado",  num1* num2)
elif operador == "/":
    if num2 == 0:
        print("no se puede divir por 0")
    else:
        ("Resultado", num1 / num2)
else:
    print("ERROR: No has elegido un operador valido")
