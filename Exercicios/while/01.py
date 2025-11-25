soma = 0
qtde_entradas = 4

while qtde_entradas >0:
    altura = float(input("Entre com a altura: "))
    soma += altura
    qtde_entradas -= 1

print("Soma das alturas:", soma)