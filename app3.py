import os

os.system("cls")

choose=int(input("escolha a operação:('+=1 ou -=2')"))
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