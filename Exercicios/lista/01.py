#ESCREVA UM PROGRAMA QUE RECEBA UMA LISTA DE NÚMEROS DO USUARIO
#DO USUÁRIO E CONTE QUANTAS VEZES UM NÚMERO
#ESPECÍFICO APARECE NA LISTA
#SOLICITE AO USUÁRIO UM NÚMERO E EXIBA A CONTAGEM.
#%%
lista = [1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

numero = int(input("Entre com um número: "))
contador = 0

for i in lista:
    if i == numero:
        contador += 1

print("Quantidade de", numero, ":", contador)
