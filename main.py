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


# =================================================================
# CONFIGURAÇÃO DE CORS - BASEADO NA SUA ANÁLISE
# =================================================================
# Sua pesquisa mostrou que precisamos permitir a origem 'http://127.0.0.1:5500'.
# Vamos criar uma lista de origens permitidas.
# O "*" é um curinga que permite QUALQUER origem, o que é ótimo para garantir que funcione.

origins = [
    # Permite a origem exata que o seu console reportou
    "http://127.0.0.1:5500", 
    # É uma boa prática também permitir a origem 'null', que ocorre
    # quando você abre um arquivo HTML localmente (file:///)
    "null",
    # Você pode adicionar outras origens aqui se precisar no futuro
    # "https://meu-outro-projeto.com"
]

# Esta é a "tradução" para Python/FastAPI do app.use(cors()) que você encontrou.
app.add_middleware(
    CORSMiddleware,
    # A linha abaixo é a mais importante. Se quiser simplificar e permitir TUDO,
    # pode trocar 'allow_origins=origins' por 'allow_origins=["*"]'.
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, etc)
    allow_headers=["*"], # Permite todos os cabeçalhos
)
# =================================================================


# O resto do seu código permanece o mesmo.
df = pd.read_csv('Cronograma.csv')

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à sua API de CSV!"}

@app.get("/dados")
def get_data():
    return df.to_dict(orient='records')

@app.get("/dados/{item_id}")
def get_item(item_id: int):
    # Filtra os dados pelo ID fornecido
    item = df[df['id'] == item_id]
    if not item.empty:
        return item.to_dict(orient='records')[0]
    return {"error": "Item não encontrado"}
