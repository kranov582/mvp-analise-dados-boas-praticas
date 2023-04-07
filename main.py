# Imports
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

# Para mostrar todas as linhas do pandas
pd.set_option('display.max_rows', None)

# Para mostrar todas as colunas do pandas
pd.set_option('display.max_columns', None)

# %%

# Caminho do arquivo
file_path = R"C:\Users\PedroB\PycharmProjects\MPV_1\analise_de_dados.csv"

dataset = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1')

# %%
# Gerar report para uma análise mais facil:
'''
profile = ProfileReport(dataset, title="Profiling Report")
profile.to_file("your_report.html")
'''
# %%

# Para saber o tamanho do array de dados
print(dataset.shape)

print(dataset.info())

print(dataset.isnull().sum())
# %%

# salvando um novo dataset para tratamento de missings

# Laço for para remover colunas com dados faltantes que correspondem a mais de 90% do dataset
thresh = len(dataset) * 0.9  # Define o limiar para 90% de valores não-nulos
dataset_limpo = dataset.dropna(thresh=thresh, axis=1)  # Remove as colunas que não atingem o limiar
dataset_limpo = dataset_limpo.dropna(how='all')  # Remove as linhas com valores faltantes

print(dataset_limpo.shape)
# %%
print(dataset.info())
print(dataset_limpo.info())

# %%

dataset_limpo_2 = dataset_limpo.drop(columns=['Centro', 'Divisão ord.cliente', 'Empresa', 'Moeda'])
print(dataset_limpo_2.shape)
# %%

print(dataset_limpo_2.info())

dataset_limpo_2['Depósito'].fillna(value='Sem depósito', inplace=True)
print(dataset_limpo_2.head())


# %%
# Função para comparar colunas, com o objetivo de determinar se são iguais:

# obtenha as colunas em forma de lista

def verificar_colunas(coluna1, coluna2):
    col1 = dataset_limpo_2[f"{coluna1}"].values
    col2 = dataset_limpo_2[f"{coluna2}"].values


    # inicialize a variável de contagem
    count = 0

    # percorra as duas listas simultaneamente e compare os valores
    for item1, item2 in zip(col1, col2):
        if item1 == item2:
            count += 1

    # calcule o percentual de similaridade
    percentual_similaridade = (count / len(col1)) * 100

    # imprima o resultado
    print(f"Os valores das colunas são {percentual_similaridade:.2f}% iguais.")
# %%

verificar_colunas('Unid.medida básica', 'UM registro')
'''
De acordo com a função, as duas colunas são praticamente iguais (99,61% iguais), e como "Unid.medida básica" contém valores 
 faltantes, será a escolhida para ser removida.
'''

verificar_colunas('Data de entrada', 'Data do documento')
verificar_colunas('Data de entrada', 'Data de lançamento')
verificar_colunas('Data de lançamento', 'Data do documento')

'''
Neste caso, as tres colunas de datas possuem uma 
diferença razoavel entre seus valores,
 e por isso serão todas mantidas.
'''

# %%

'''
Verificação das colunas que sobraram:
Deposito: Deposito onde ocorreu a movimentação
Tipo de movimento: Código do movimento
Doc.Material: Código único da movimentação
Item doc.material: "linha" correspondente do item transferido no doc.Material


'''


dataset_limpo_3 = dataset_limpo_2.drop(columns=['Unid.medida básica'])

print(dataset_limpo_3.head)
