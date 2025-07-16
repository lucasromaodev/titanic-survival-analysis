import os

# Define o diretório do kaggle.json e o destino do download
os.environ['KAGGLE_CONFIG_DIR'] = r'C:\Users\luckh\Desktop\Automações\titanic-project'
destino = r'C:\Users\luckh\Desktop\Automações\titanic-project'

# Caminho completo do arquivo CSV que deve ser apagado se existir
arquivo_csv = os.path.join(destino, 'Titanic-Dataset.csv')

# Apaga o arquivo CSV antigo se existir
if os.path.isfile(arquivo_csv):
    print(f"Arquivo existente encontrado, apagando: {arquivo_csv}")
    os.remove(arquivo_csv)

# Cria a pasta destino se não existir
os.makedirs(destino, exist_ok=True)

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

print("Baixando dataset Titanic...")
api.dataset_download_files('yasserh/titanic-dataset', path=destino, unzip=True)
print("Download finalizado!")
