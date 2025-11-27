#Construa um programa que realiza o sorteio de um número entre 1 e 15.
#O usuário terá 3 chances de acertar o valor.
#A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado.
#Caso o usuário acerte, dê os parabéns.

import random

def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com seu numero de sorte (entre 1 e 15): "))

        except ValueError as err:
            print("Valor inválido!")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario

        print("Valor inválido! o valor deve ser entre 1 e 15.")

def check_numbers(sorteio, usuario):
    if sorteio == usuario:
        print("Parabéns! você acertou na loto ipotetica!")
        return True

    elif usuario > sorteio:
        print("Tente um número menor!")
        return False
    else:
        print("Tente um número maior!")
        return False

numero_sorteio = random.randint(1,15)

for i in range(3):
    numero_usuario = get_input()
    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario):
        break

else:
    print("Suas tentativas acabaram. O número sorteado era:", numero_sorteio)
