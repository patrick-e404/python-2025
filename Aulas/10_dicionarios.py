#%%
#DICIONARIO

dados_patrick = {
    "nome": "Patrick",
    "sobre":"Sousa",
    "filho": True,
    "formacao":["ADS", "Cybersecurity","Analise de Dados"],
    "cargos":[
        {"nome": "Vendedor", "empresa": "Saraiva"},
        {"nome": "Suporte Técnico", "empresa": "Bitcom"},
    ],
}

print(dados_patrick)
#%%
print(dados_patrick["cargos"][-1]["empresa"])
print(dados_patrick["cargos"][-1]["nome"])
# %%
dados_patrick.keys()
print(dados_patrick.values())
print(dados_patrick.items())
#%%
for chave, valor in dados_patrick.items():
    print(chave, valor)