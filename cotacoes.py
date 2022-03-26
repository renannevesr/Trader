from IPython.display import display
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
                                  start="01-01-2013", end="03-24-2022")
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
                       sheet_name='Acoes', header=True, index=True)
cota_a = 0
cota_b = 0
i = 0
for empresa in empresas['Empresas']:
    print(empresa)
    cota_a += 1
    cota_a = pd.read_excel(f"Cotacoes_{empresa}.xlsx")
    cota_b = cota_a

    if i == 0:
        resultado = cota_a
    if empresa == 'BBAS3':
        i = cota_a[cota_a.columns[0]].count()
    else:
        resultado = cota_a.append(cota_b)


resultado.to_excel(f'Cotacoes_final.xlsx',
                   sheet_name='Acoes', header=True, index=True)
