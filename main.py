from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Carrega os dados do CSV para um DataFrame do Pandas
df = pd.read_csv('Cronograma.csv')

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à sua API de CSV!"}

@app.get("/dados")
def get_data():
    # Converte o DataFrame para um formato JSON
    return df.to_dict(orient='records')

@app.get("/dados/{item_id}")
def get_item(item_id: int):
    # Filtra os dados pelo ID fornecido
    item = df[df['id'] == item_id]
    if not item.empty:
        return item.to_dict(orient='records')[0]
    return {"error": "Item não encontrado"}