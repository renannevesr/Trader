import pandas as pd
from IPython.display import display


balanco = pd.read_excel("balancos/BBAS3.xls")
display(balanco)
df = balanco.loc[0]
df = pd.DataFrame(df)
df.columns = ['Data']
# print(df)
#df.to_excel(f'datas.xlsx', header=True, index=False)

df['Data'] = pd.to_datetime(df['Data'])
print(df.dtypes)
print(df)

ac = pd.read_excel("Cotacoes_final.xlsx")
print(ac.dtypes)
#acoes = pd.read_excel("Cotacoes_BBAS3.xlsx")

#acoes = acoes.append(df)
# display(acoes)
#acoes.to_excel(f'teste1.xlsx', header=True, index=True)
#df.loc[df['Veículo'] == 'Fiat', 'Veículo'] = 0
