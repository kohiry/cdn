# tests/test_nearest_cities.py
def test_get_nearest_cities(client):
    # Arrange
    cities = [
        {'name': 'Moscow', 'latitude': 55.7558, 'longitude': 37.6173},
        {'name': 'Saint Petersburg', 'latitude': 59.9343, 'longitude': 30.3351},
        {'name': 'Novosibirsk', 'latitude': 55.0084, 'longitude': 82.9357}
    ]
    for city in cities:
        client.post('/cities', json={'name': city['name']})

    # Точка близкая к Москве
    point = {'latitude': 55.7550, 'longitude': 37.6175}

    # Act
    response = client.get('/cities/nearest', params=point)

    # Assert
    assert response.status_code == 200
    nearest = response.json()
    assert len(nearest) == 2
    assert nearest[0]['name'] == 'Moscow'
    assert nearest[1]['name'] == 'Novosibirsk'  # В зависимости от алгоритма расстояний

def test_get_nearest_cities_insufficient_data(client):
    # Arrange
    client.post('/cities', json={'name': 'Moscow'})

    point = {'latitude': 55.7550, 'longitude': 37.6175}

    # Act
    response = client.get('/cities/nearest', params=point)

    # Assert
    assert response.status_code == 400
    assert response.json()['detail'] == 'Not enough cities in the database to find nearest neighbors'

