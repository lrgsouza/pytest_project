import requests
import pytest

# Função para buscar dados da API Random Data
def get_random_data(resource, size=1):
    base_url = "https://random-data-api.com/api/v2/"
    url = f"{base_url}{resource}?size={size}"
    response = requests.get(url)
    status_code = requests.get(url).status_code
    return status_code, response.json()

# [Teste de unidade] Teste para verificar se a resposta da API contém a chave 'id'
def test_response_contains_id():
    status_code, data = get_random_data("users")
    assert "id" in data

# [Teste de Integração] Teste para verificar se o status da resposta da API é 200 (OK)
def test_response_status_code():
    status_code, data = get_random_data("users")
    assert status_code == 200

# [Teste de Aceitação] Teste para verificar se o tamanho da resposta da API é igual a 5 (esperado)
@pytest.mark.parametrize("resource", ["users", "addresses", "banks"])
def test_acceptance(resource):
    status_code, result = get_random_data(resource, size=5)
    assert isinstance(result, list)
    assert len(result) == 5


# [Teste de Carga] Teste os recursos da API especificados para um grande volume de dados
@pytest.mark.parametrize("resource", ["users", "addresses", "banks"])
def test_load(resource):
    status_code, result = get_random_data(resource, size=100)
    assert isinstance(result, list)
    assert len(result) == 100