from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

operadoras_df = pd.read_csv('dados_operadoras.csv')

@app.route('/busca', methods=['GET'])
def busca():
    termo = request.args.get('q', '').lower()
    resultado = operadoras_df[operadoras_df['nome'].str.lower().str.contains(termo)]
    dados = resultado.to_dict(orient='records')
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
