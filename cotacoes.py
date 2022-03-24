from IPython.display import display
from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt


empresas = pd.read_excel("empresas.xlsx")
# display(empresas)
df = [(('Date', 'High',
        'Low', 'Open', 'Close', 'Volume', 'Adj Close', 'Empresa'))]
df = pd.DataFrame(df, columns=['Date', 'High',
                  'Low', 'Open', 'Close', 'Volume', 'Adj Close', 'Empresa'])
for empresa in empresas['Empresas']:
    print(empresa)

    try:
        cotacoes = web.DataReader(f'{empresa}.SA', data_source='yahoo',
                                  start="01-01-2013", end="03-24-2022")

        # display(cotacoes)
        df = df.append(cotacoes)
        # print()
        df.assign(Empresa=f'{empresa}')
    except:
        print(f"Não foi possível localizar os dados da {empresa}")
    #cotacoes["Adj Close"].plot()
    # plt.show()
df.to_excel('Cotacoes_empresas.xlsx',
            sheet_name='Acoes', header=True, index=False)
