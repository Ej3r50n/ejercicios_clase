name = float(input("\n Ingrese su nota: \n"))
if num > 10 or num < 0:
    print("la nota es incorrecta")

if num < 5:
    print("la nota es insuficiente")
elif num < 6:
    print("la nota es suficiente")
elif num < 7:
    print("la nota es bien")
elif num < 9:
    print("la nota es notable")
else:
    print("la nota es sobresaliente")
