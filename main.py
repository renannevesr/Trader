import pandas as pd
import os
from IPython.display import display

empresas = ["BBAS3", "BBDC4", "BIDI11", "CASH3",
            "CIEL3", "MGLU3", "ITSA4", "PETR4", "SEER3", "SHOW3"]
# criando dicionario
fundamentos = {}
arquivos = os.listdir("balancos")
for arquivo in arquivos:
    nome = arquivo[0:-4]
    if nome in empresas:
        print(nome)
        balanco = pd.read_excel(f'balancos/{arquivo}', sheet_name=0)
        # colocando o nome da empresa
        balanco.iloc[0, 0] = nome
        # pega a 1ª linha e transforma ela em cabeçalho
        balanco.columns = balanco.iloc[0]
        # tirando a 1ªlinha que duplicou
        balanco = balanco[1:]
        # alterando a coluna de index
        balanco = balanco.set_index(nome)
        dre = pd.read_excel(f'balancos/{arquivo}', sheet_name=1)
        # colocando o nome da empresa
        dre.iloc[0, 0] = nome
        # pega a 1ª linha e transforma ela em cabeçalho
        dre.columns = dre.iloc[0]
        # tirando a 1ªlinha que duplicou
        dre = dre[1:]
        # alterando a coluna de index
        dre = dre.set_index(nome)
        # display(balanco)
        # display(dre)
        # criando dicionario de cada empresa colocando balanco e dre
        fundamentos[nome] = balanco.append(dre)
        print(len(fundamentos))
