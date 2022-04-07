
from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt


empresas = pd.read_excel("empresas.xlsx")
# display(empresas)
df = [(('High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'))]
df = pd.DataFrame(df, columns=['High', 'Low',
                  'Open', 'Close', 'Volume', 'Adj Close'])
df_emp = [(('Empresa'))]
df_emp = pd.DataFrame(df_emp, columns=['Empresa'])

for empresa in empresas['Empresas']:
    # print(empresa)

    try:
        cotacoes = web.DataReader(f'{empresa}.SA', data_source='yahoo',
                                  start="01-01-2013", end="03-30-2022")
        df = df.append(cotacoes)
        # display(cotacoes)
        # print(empresa)
        #pd.concat([df, df_emp])
        # display(df)
        df.to_excel(f'Cotacoes_{empresa}.xlsx',
                    sheet_name='Acoes', header=True, index=True)
    except:
        print(f"Não foi possível localizar os dados da {empresa}")
    #cotacoes["Adj Close"].plot()
    # plt.show()
for empresa in empresas['Empresas']:
    cota = pd.read_excel(f"Cotacoes_{empresa}.xlsx")
    nova_cota = cota.assign(Nome=empresa)
    # display(nova_cota)
    nova_cota.to_excel(f'Cotacoes_{empresa}.xlsx',
                       sheet_name='Acoes', header=True, index=False)
cota_final = pd.DataFrame()
for empresa in empresas['Empresas']:
    #print("ultimo for ", empresa)
    cota_final = cota_final.append(pd.read_excel(f"Cotacoes_{empresa}.xlsx"))
    # display(cota_final)
high = ['High']
cota_final = cota_final.drop(cota_final[cota_final['High'].isin(high)].index)
cota_final.columns = ['Data', 'High', 'Low', 'Open',
                      'Close', 'Volume', 'Adj Close', 'Empresa']
cota_final.to_excel(f'Cotacoes_final.xlsx',
                    sheet_name='Acoes', header=True, index=False)
