import pandas as pd

# Carregar os dados
df = pd.read_csv('Titanic-Dataset.csv')

# Excluir coluna com muitos valores ausentes
df.drop(columns=['Cabin'], inplace=True)

# Preencher valores ausentes em 'Age' com a mediana
df['Age'].fillna(df['Age'].median(), inplace=True)

# Preencher valores ausentes em 'Embarked' com a moda
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Remover espaços em branco extras nos nomes
df['Name'] = df['Name'].str.strip()

# Converter 'Sex' e 'Embarked' para minúsculas (padronização)
df['Sex'] = df['Sex'].str.lower()
df['Embarked'] = df['Embarked'].str.lower()

# Verificar se ainda há valores nulos
print(df.isnull().sum())

# Visualizar as primeiras linhas limpas
print(df.head())

# Salvar o dataset limpo (opcional)
df.to_csv('Titanic-Dataset-Cleaned.csv', index=False)
