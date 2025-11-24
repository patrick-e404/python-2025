# %%
numero = 2
count = 1

while count <= 100:
    print(numero, "X", count, "=", numero * count)
    count = count + 1

print("acabou")
# %%
count = 4

while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count)
    
    count += 1