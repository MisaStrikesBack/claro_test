import pytest
from app.prueba import app as base_app


@pytest.fixture
def client():
    app = base_app
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


# definiendo las pruebas
def test_pokemon_list(client):
    response_keys = ["control", "resultados", "total"]
    # revisando que solo el método get sea aceptado
    response = client.post('/api/pokemon')
    assert response.status_code == 405
    response = client.put('/api/pokemon')
    assert response.status_code == 405
    response = client.patch('/api/pokemon')
    assert response.status_code == 405
    response = client.delete('/api/pokemon')
    assert response.status_code == 405
    # evaluando las respuestas
    response = client.get('/api/pokemon')
    assert response.status_code == 200
    response = response.json
    # evaluando la respuesta default
    # evaluando los keys del json
    assert all([key_name in response.keys() for key_name in response_keys])
    # evaluando el número default de 20 resultados esperados
    assert len(response["resultados"]) == 20
    # evaluando el query param limit para cambiar el número de resultados
    response = client.get('/api/pokemon?limit=30')
    response = response.json
    assert len(response["resultados"]) == 30
    # evaluando que todos los resultados sean diccionarios y
    # que todos tengan "id" y "nombre"
    assert all(
        [isinstance(element, dict) for element in response["resultados"]])
    assert all([
        all(
            [
                key_name in element.keys() for key_name in [
                    "id",
                    "nombre"
                ]
            ]
        ) for element in response["resultados"]])
    # Evaluando el query param offset
    response = client.get('/api/pokemon?offset=10')
    response = response.json
    assert response["resultados"][0]["id"] == 11
    # evaluando que ambos parámetros se puedan utilizar al mismo tiempo
    response = client.get('/api/pokemon?offset=35&limit=50')
    response = response.json
    assert response["resultados"][0]["id"] == 36
    assert len(response["resultados"]) == 50


def test_pokemon_detail(client):
    # revisando que solo el método get sea aceptado
    response = client.post('/api/pokemon/1')
    assert response.status_code == 405
    response = client.put('/api/pokemon/1')
    assert response.status_code == 405
    response = client.patch('/api/pokemon/1')
    assert response.status_code == 405
    response = client.delete('/api/pokemon/1')
    assert response.status_code == 405
    # evaluando la respuesta de una petición correcta
    response = client.get('/api/pokemon/1')
    assert response.status_code == 200
    # evaluando la respuesta de una petición con error
    # petición con id alfanumérico
    response = client.get('/api/pokemon/sdk')
    assert response.status_code == 404
    # petición con id inexistente
    response = client.get('/api/pokemon/100000')
    assert response.status_code == 404