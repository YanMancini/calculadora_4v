import os

os.system("cls")

choose=int(input("Escolha a operação:('+ =1; - =2; * =3; / =4')\n"))

if choose ==1:
    a=int(input("Digite o primeiro valor: \n"))
    b=int(input("Digite o segundo valor: \n"))

    soma=(a+b)
    os.system("cls")
    print("Soma: ",soma)

elif choose ==2:
    a=int(input("Digite o primeiro valor: \n"))
    b=int(input("Digite o segundo valor: \n"))

    subtra=(a-b)
    os.system("cls")
    print("Subtração: ",subtra)

elif choose ==3:
    a=int(input("Digite o primeiro valor: \n"))

    b=int(input("Digite o segundo valor: \n"))
    
    mult=(a*b)
    os.system("cls")
    print("multiplicação: ",mult)
elif choose ==4:
    b=0
    a=int(input("Digite o primeiro valor: \n"))

    while b==0:
          os.system("cls")
          b=int(input("Digite o segundo valor: \n"))
          os.system("cls")
    div=(a/b)
    print("divisão: ",div)
else:
    print("A operação selecionada é inválida!")
