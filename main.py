# main.py - VERSÃO CORRIGIDA

from fastapi import FastAPI
# Importe o CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# =================================================================
# ADICIONE ESTA SEÇÃO PARA CONFIGURAR O CORS
# =================================================================
# Defina as origens que terão permissão.
# Usar ["*"] permite que QUALQUER origem acesse sua API.
# É seguro para começar, especialmente para projetos públicos.
origins = [
    "*", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, etc)
    allow_headers=["*"], # Permite todos os cabeçalhos
)
# =================================================================


# Carrega os dados do CSV para um DataFrame do Pandas
df = pd.read_csv('Cronograma.csv')

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à sua API de CSV! CORS está habilitado."}

@app.get("/dados")
def get_data():
    # Converte o DataFrame para um formato JSON
    return df.to_dict(orient='records')

@app.get("/dados/{item_id}")
def get_item(item_id: int):
    # Filtra os dados pelo ID fornecido
    # (É importante converter o tipo do ID no dataframe para int se ele for lido como string)
    df['id'] = df['id'].astype(int)
    item = df[df['id'] == item_id]
    if not item.empty:
        return item.to_dict(orient='records')[0]
    return {"error": "Item não encontrado"}
