import requests

# ======================
# CONFIGURAÇÃO
# ======================

CONTEXT_SERVER_BASE_URL = "http://localhost:8080"
CONTEXT_TELEFONIA_ENDPOINT = "/api/telefonia"

# ======================
# CLIENTE CONTEXTO
# ======================

def _consultar_servidor_contexto(nome: str):
    response = requests.get(
        f"{CONTEXT_SERVER_BASE_URL}{CONTEXT_TELEFONIA_ENDPOINT}",
        params={"nome": nome},
        timeout=5
    )
    response.raise_for_status()
    return response.json()

# ======================
# TOOL MCP
# ======================

def tool_buscar_ramal_por_nome(nome: str):
    """
    Consulta o Servidor de Contexto (API Spring Boot) para obter
    o ramal telefônico associado a um nome.
    """
    try:
        return _consultar_servidor_contexto(nome)
    except requests.exceptions.RequestException as e:
        return {
            "erro": "Falha ao consultar o servidor de contexto",
            "detalhe": str(e)
        }

# ======================
# TESTE LOCAL
# ======================

if __name__ == "__main__":
    resultado = tool_buscar_ramal_por_nome("joao")

    if isinstance(resultado, dict) and "erro" in resultado:
        print("Erro:", resultado)
    elif len(resultado) == 0:
        print("Nenhum ramal encontrado")
    else:
        for item in resultado:
            print(
                f"Nome: {item['nome']} | "
                f"Ramal: {item['ramal']}"
            )
