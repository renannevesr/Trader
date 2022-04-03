import pandas as pd


balanco = pd.read_excel("balancos/BBAS3.xls")
print(balanco)
datas = balanco.loc[0]
datas = pd.DataFrame(datas)
datas.columns = ['Data']
datas['Data'] = pd.to_datetime(datas['Data'])
#print(datas)
#datas.to_excel(f'datas.xlsx', header=True, index=False)
acoes = pd.read_excel("Cotacoes_BBAS3.xlsx")

#print(cota)
acoes.columns = ['Data', 'High', 'Low','Open', 'Close', 'Volume', 'Adj Close', 'Empresa']

cota =pd.concat([acoes, datas]).sort_values(by='Data')
cota.to_excel(f'teste.xlsx',
                    sheet_name='Acoes', header=True, index=False)
#acoes.to_excel(f'teste1.xlsx', header=True, index=True)
#df.loc[df['Veículo'] == 'Fiat', 'Veículo'] = 0
