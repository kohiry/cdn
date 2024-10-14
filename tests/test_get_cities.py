# tests/test_get_cities.py
def test_get_all_cities(client):
    # Arrange
    cities = [
        {'name': 'Moscow', 'latitude': 55.7558, 'longitude': 37.6173},
        {'name': 'Saint Petersburg', 'latitude': 59.9343, 'longitude': 30.3351}
    ]
    for city in cities:
        client.post('/cities', json={'name': city['name']})

    # Act
    response = client.get('/cities')

    # Assert
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json() == cities

def test_get_single_city(client):
    # Arrange
    city = {'name': 'Moscow', 'latitude': 55.7558, 'longitude': 37.6173}
    client.post('/cities', json={'name': city['name']})

    # Act
    response = client.get(f"/cities/{city['name']}")

    # Assert
    assert response.status_code == 200
    assert response.json() == city

def test_get_single_city_not_found(client):
    # Act
    response = client.get('/cities/NonExistentCity')

    # Assert
    assert response.status_code == 404
    assert response.json()['detail'] == 'City not found'

