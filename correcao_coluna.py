import pandas as pd

acoes = pd.read_excel("Cotacoes_final.xlsx")
# display(acoes)
acoes.columns = ['Data', 'High', 'Low',
                 'Open', 'Close', 'Volume', 'Adj Close', 'Empresa']
print(acoes)
# display(acoes)
