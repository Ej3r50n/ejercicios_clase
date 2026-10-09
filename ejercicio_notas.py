print ("\n ACONTINUACIÓN CONOCERÁS EL ESTADO DE TU NOTA \n ")
num = float(input("Por favor ingrese su nota: \n"))
if num < 0:
    print (" su nota es incorrecta")

if num >= 0 and num <5:
    print (" su nota es insuficiente")

if num >= 5 and num < 6:
    print (" su nota es suficiente")

if num >= 6 and num < 7:
    print (" su nota es bien")

if num >= 7 and num < 9:
    print (" su nota es notable")

if num >= 9 and num <= 10:
    print (" su nota es sobresaliente")

if num > 10 :
    print (" su nota es incorrecta")

print ("\n Gracias! vuelva pronto \n ")

