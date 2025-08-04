import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

# O nome do seu arquivo Excel
EXCEL_FILE = "disciplinas.xlsx"

# A gente vai carregar o Excel uma vez e guardar os dados
# Isso evita que a API precise ler o arquivo a cada requisição
try:
    df = pd.read_excel(EXCEL_FILE)
    # Aqui, a gente limpa e organiza os dados.
    # Exemplo: só pega a coluna 'disciplina' e remove duplicadas
    disciplinas_unicas = df['Disciplina'].dropna().unique().tolist()
except FileNotFoundError:
    disciplinas_unicas = []
    print(f"Erro: O arquivo {EXCEL_FILE} não foi encontrado. A API retornará uma lista vazia.")

@app.route('/disciplinas', methods=['GET'])
def get_disciplinas():
    """
    Endpoint que retorna a lista de disciplinas.
    """
    if not disciplinas_unicas:
        return jsonify({"message": "Nenhuma disciplina encontrada."}), 404
        
    return jsonify({"disciplinas": disciplinas_unicas})

if __name__ == '__main__':
    # Roda a API no seu computador
    app.run(debug=True)