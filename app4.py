import os

os.system("cls")

choose=int(input("escolha a operação:('+ =1; - =2; * =3')"))
if choose ==1:
    a=int(input("Digite o primeiro valor: "))
    b=int(input("Digite o segundo valor: "))
    soma=(a+b)
    print(soma)
elif choose ==2:
    a=int(input("Digite o primeiro valor: "))
    b=int(input("Digite o segundo valor: "))
    subtra=(a-b)
    print("Subtração: ",subtra)
elif choose ==3:
    a=int(input("Digite o primeiro valor: "))
    b=int(input("Digite o segundo valor: "))
    mult=(a*b)
    print("multiplicação: ",mult)
elif choose ==4:
    b=0
    a=int(input("Digite o primeiro valor: "))
    while b==0:
          os.system("cls")
          b=int(input("Digite o segundo valor: "))
    div=(a/b)
    print("divisão: ",div)