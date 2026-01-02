from flask import Flask, request, jsonify
import unicodedata

app = Flask(__name__)

def normalizar(texto: str) -> str:
    return (
        unicodedata
        .normalize("NFD", texto)
        .encode("ascii", "ignore")
        .decode("utf-8")
        .lower()
    )

TELEFONIA_FAKE = [
    {"nome": "João Silva", "setor": "Financeiro", "ramal": "1234"},
    {"nome": "Maria Souza", "setor": "RH", "ramal": "5678"},
    {"nome": "João Pedro", "setor": "TI", "ramal": "4321"},
]

@app.route("/api/telefonia", methods=["GET"])
def buscar_ramal():
    nome_busca = normalizar(request.args.get("nome", ""))

    resultado = [
        {
            "nome": t["nome"],
            "ramal": t["ramal"]
        }
        for t in TELEFONIA_FAKE
        if nome_busca in normalizar(t["nome"])
    ]

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(port=8080)
