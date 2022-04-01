import pandas as pd
from IPython.display import display


balanco = pd.read_excel("balancos/BBAS3.xls")
display(balanco)
datas = balanco.loc[0]
# display(datas)
# datas.to_excel(f'datas.xlsx', sheet_name='datas balancos',
#               header=False, index=False)
acoes = pd.read_excel("Cotacoes_BBAS3.xlsx")
acoes.merge(balanco, on=)
