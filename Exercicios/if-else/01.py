# %%
texto = """"Escolha a sua agua para comprar
(1) Água natual
(2) Água com gás
"""

opcao = input(texto)
conta = 0

if opcao == "1":
    conta = 1.5
elif opcao == "2":
    conta = 2.5

if conta == 0:
    print("Opção inválida")
else:
    print("Sua conta é: R$", conta)