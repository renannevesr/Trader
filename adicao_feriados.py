import pandas as pd
from IPython.display import display


balanco = pd.read_excel("balancos/BBAS3.xls")
display(balanco)
datas = balanco.loc[0]
datas = pd.DataFrame(datas)
datas.columns = ['Data']
print(datas)
datas.to_excel(f'datas.xlsx', header=True, index=False)

#acoes = pd.read_excel("Cotacoes_BBAS3.xlsx")

#acoes = acoes.append(datas)
# display(acoes)
#acoes.to_excel(f'teste1.xlsx', header=True, index=True)
#df.loc[df['Veículo'] == 'Fiat', 'Veículo'] = 0
