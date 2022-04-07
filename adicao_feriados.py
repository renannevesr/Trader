import pandas as pd


balanco = pd.read_excel("balancos/BBAS3.xls")
<<<<<<< HEAD
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
=======
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
>>>>>>> 66f528eea6595ae87d3dd96299a012019979639e
#acoes.to_excel(f'teste1.xlsx', header=True, index=True)
#df.loc[df['Veículo'] == 'Fiat', 'Veículo'] = 0
