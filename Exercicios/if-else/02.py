# %%
texto = """"Escolha a sua agua para comprar
(1) Água natual - R$1,50
(2) Água com gás - R$2,50
"""

opcao = input(texto)
valor_item = 0

if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Com todo respeito, entre com a porra do valor correto")

else:
    qtde = input("Quantas garrafas? ")
    qtde = int(qtde)
    valor_total = valor_item * qtde
    print("Sua conta deu: R$:", valor_total)