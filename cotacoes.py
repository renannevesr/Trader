from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt


empresas = pd.read_excel("empresas.xlsx")
df = []
df = pd.DataFrame(df)
cota_final = []
cota_final = pd.DataFrame(df)
df_emp = [(('Empresa'))]
df_emp = pd.DataFrame(df_emp, columns=['Empresa'])

for empresa in empresas['Empresas']:
    try:
        cotacoes = web.DataReader(f'{empresa}.SA', data_source='yahoo',
                                  start="01-01-2013", end="03-30-2022")
        df = df.append(cotacoes)
        df['Data'] = df.index
        balanco = pd.read_excel(f"balancos/{empresa}.xls")
        datas = balanco.loc[0]
        datas = pd.DataFrame(datas)
        datas.columns = ['Data']
        datas['Data'] = pd.to_datetime(datas['Data'])
        df['Data'] = pd.to_datetime(df['Data'])
        cota = pd.concat([df, datas]).sort_values(by='Data').drop_duplicates()
        # cota.to_excel(f'Cotacoes_{empresa}.xlsx',
        #              sheet_name='Acoes', header=True)
        nova_cota = cota.assign(Nome=empresa)
        cota_final = cota_final.append(cota)
    except:
        print(f"Não foi possível localizar os dados da {empresa}")

# for empresa in empresas['Empresas']:
#    cota = pd.read_excel(f"Cotacoes_{empresa}.xlsx")
#    nova_cota = cota.assign(Nome=empresa)
#    nova_cota.to_excel(f'Cotacoes_{empresa}.xlsx',
#                       sheet_name='Acoes', header=True, index=False)
#cota_final = pd.DataFrame()
# for empresa in empresas['Empresas']:
#    cota_final = cota_final.append(pd.read_excel(f"Cotacoes_{empresa}.xlsx"))
high = ['High']
cota_final = cota_final.drop(cota_final[cota_final['High'].isin(high)].index)
# cota_final.columns = ['Duplicada', 'High', 'Low', 'Open',
#                      'Close', 'Volume', 'Adj Close', 'Data', 'Empresa']
# cota_final.drop(columns=['Duplicada'])
cota_final.to_excel(f'Cotacoes_final.xlsx',
                    sheet_name='Acoes', header=True, index=False)
