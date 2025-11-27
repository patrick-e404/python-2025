#%%
nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)

#ABRE O ARQUIVO EM FORMATO DE LEITURA
# open_file = open(nome_arquivo)

#LÊ OS DADOS DO ARQUIVO
# conteudo = open_file.read()
# print(conteudo)

#FECHA O ARQUIVO
# open_file.close()