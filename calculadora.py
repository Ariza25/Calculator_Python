#from tkinter import *
#from tkinter import ttk

a = 0
b = 0

def soma(a, b):
    return a + b

def subtração(a, b):
    return a - b

def multiplicação(a, b):
    return a * b

def divisão(a, b):
    if b == 0:
        return "Impossível dividir por zero!"
    else:
        return a / b

while True:
    print("Selecione a operação desejada:\n ")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão\n")
    
    opcao = input("Digite sua opção: ")
    
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if opcao == '1':
        print(f'{a} + {b} = {soma(a,b)}')
    elif opcao == '2':
        print(f'{a} - {b} = {subtração(a,b)}')
    elif opcao == '3':
        print(f'{a} * {b} = {multiplicação(a,b)}')
    elif opcao == '4':
        print(f'{a} / {b} = {divisão(a,b)}')
    else:
        print("Opção inválida.")
        break
    
   


