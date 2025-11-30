#%%
import requests
import json
from tqdm import tqdm
import pandas as pd

ceps = [
    "95034160",
    "95034140",
    "95034150",
    "95034110",
    "95034180",
    "95034170",
]

url = "https://viacep.com.br/ws/{cep}/json"
dados = []
for i in tqdm(ceps):
    res = requests.get(url.format(cep=i))
    if res.status_code == 200:
        dados.append(res.json())

dados
#%%

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

#%%
with open("ceps.json", "w", encoding="utf-8") as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)
