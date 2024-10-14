# tests/test_add_city.py
def test_add_city_success(client, mock_external_api):
    """
    Тест успешного добавления города.
    """
    # Arrange
    mock_external_api.return_value = {'latitude': 55.7558, 'longitude': 37.6173}  # Координаты Москвы
    city_data = {'name': 'Moscow'}

    # Act
    response = client.post('/cities', json=city_data)

    # Assert
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == 'Moscow'
    assert data['latitude'] == 55.7558
    assert data['longitude'] == 37.6173
    mock_external_api.assert_called_once_with('Moscow')


def test_add_city_duplicate(client, mock_external_api):
    """
    Тест добавления дублирующегося города.
    """
    # Arrange
    mock_external_api.return_value = {'latitude': 55.7558, 'longitude': 37.6173}
    city_data = {'name': 'Moscow'}
    client.post('/cities', json=city_data)

    # Act
    response = client.post('/cities', json=city_data)

    # Assert
    assert response.status_code == 400
    assert response.json()['detail'] == 'City already exists'
    mock_external_api.assert_called_once_with('Moscow')  # Внешний API вызывается только один раз

