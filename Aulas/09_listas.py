# %%%
idades = [28, 42, 43, 35, 39, 28, 38, 42, 34, 72]

print("qtde idades: ", len(idades))

print("soma das idades: ", sum(idades))

print("media das idades: ", sum(idades) / len(idades))

print("menor idade: ", min(idades))

print("maior idade: ", max(idades))

#LISTA
#%%
patrick = ["Patrickão", 
           28, 
           True, 
           "Dev", 
           ["Python", "JavaScript","C#"]]

#ACESSANDO ULTIMO ITEM DA LISTA
tamanho = len(patrick)
pos = tamanho - 1
lang = patrick[pos]

patrick[pos][len(lang)-1]

# MODO SIMPLES
patrick[-1][-1]
#%%
#FATIAMENTO DE LISTA
patrick[0:4]

patrick[4][1:3]
#%%
patrick[4][-2:]

#%%
#ORDEM INVERSA DA LISTA

linguagens = patrick[4]
linguagens[::-1]