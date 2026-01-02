import requests

BASE_URL = "http://localhost:8080"
ENDPOINT = "/api/telefonia"


def buscar_ramal_por_nome(nome: str):
    try:
        response = requests.get(
            f"{BASE_URL}{ENDPOINT}",
            params={"nome": nome},
            timeout=5
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print("Erro ao chamar a API:", e)
        return None


if __name__ == "__main__":
    resultado = buscar_ramal_por_nome("joao")

    if resultado is None:
        print("Erro na requisição")
    elif len(resultado) == 0:
        print("Nenhum ramal encontrado")
    else:
        for item in resultado:
            print(
                f"Nome: {item['nome']} | "
                f"Ramal: {item['ramal']}"
            )
