nome = "Patrick"

for letra in nome:
    print(letra)

# %%
numero = 2
max_numero = 100

for i in range(1, max_numero+1):
    print(numero, "x", i, "=", numero *i)
# %%
for i in range(4, 101):
    if i % 4 == 0:
        print(i)

# %%
soma = 0
qtde_entradas = 4

for i in range (qtde_entradas):
    altura = float(input("Entre com a altura: "))
    soma += altura
print("A soma das alturas é: ", soma)