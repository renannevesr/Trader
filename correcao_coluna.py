import pandas as pd
from IPython.display import display

acoes = pd.read_excel("Cotacoes_BBAS3.xlsx")
# display(acoes)
acoes.columns = ['Data', 'High', 'Low',
                 'Open', 'Close', 'Volume', 'Adj Close', 'Empresa']
print(acoes)
# display(acoes)

