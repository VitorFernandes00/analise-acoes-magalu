#Bibliotecas para Modelagem e Matrizez
import numpy as np
import pandas as pd

#Bibliotecas para analises gráficas
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

#Biblioteca ignorar avisos
import warnings

#Desabilitando avisos
warnings.filterwarnings('ignore')

#Lendo os dados
Base_Dados = pd.read_excel(r'C:\Users\Camily Abreu\OneDrive\Desktop\Python\MercadoFinanceiro\FinanceiroPerformance.xlsx')

#Verificando
Base_Dados.head()

#Verificando o Tamanho de linhas e colunas
Base_Dados.shape

#Verificando os formatos tipos de campo
Base_Dados.info()

#Verificando Descrição
Base_Dados.describe()

#Series Temporais
Dados = Base_Dados.set_index('Data')
Base_Dados.head()

#Grafico Fechamento
plt.style.use('seaborn-v0_8-dark')
plt.figure(figsize=(16,5))
plt.title('Analise das ações da Magalu - Fechamento', fontsize=14, loc='left')
plt.plot(Dados.index, Dados['Fechamento'])

plt.xlabel('Período da Cotação')
plt.ylabel('Valor da Ação (R$)')
plt.show()

#Mostrar os ultimos valores
Dados.tail()

#Grafico Comparativo
Media_Movel= Dados['Fechamento'].rolling(5).mean()
Media_Tendencia = Dados['Fechamento'].rolling(30).mean()

plt.style.use('seaborn-v0_8-dark')
plt.figure(figsize=(16,5))
plt.title('Analise das ações da Magalu - Fechamento', fontsize=14, loc='left')

plt.plot(Dados.index, Dados['Fechamento'])
plt.plot(Dados.index, Media_Movel)
plt.plot(Dados.index, Media_Tendencia)

plt.xlabel('Período da Cotação')
plt.ylabel('Valor da Ação (R$)')
plt.show()

#Boxplot Mensal
Base_Dados['Mes'] = Base_Dados['Data'].dt.month

plt.figure(figsize=(16,5))
sns.boxplot(data=Base_Dados, x='Mes', y='Fechamento')
plt.show(block=True)

#Descrição pra analisar o Boxplot detalhado
Base_Dados.groupby(['Mes']).describe()['Fechamento']

#Grafico Final Comparando abertura, maior valor, menor valor e fechamento
Grafico = go.Figure(
    data=[
        go.Candlestick(
            x= Dados.index,
            open= Dados['Abertura'],
            high= Dados['Maior'],
            low= Dados['Menor'],
            close= Dados['Fechamento']
        )
    ]
)

Grafico.update_layout( xaxis_rangeslider_visible=False)
Grafico.show()