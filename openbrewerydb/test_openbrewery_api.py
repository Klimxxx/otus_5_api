import pytest
from requests import sessions


def openbrewery_api(method, url, **kwargs):
    new_url = 'https://api.openbrewerydb.org/v1' + url
    with sessions.Session() as session:
        response = session.request(method=method, url=new_url, **kwargs)
    return response


def test_list_of_breweries_status_code_is_ok():
    response = openbrewery_api('get', url='/breweries?per_page=3')

    assert response.status_code == 200


def test_get_a_single_brewery_status_code_is_ok():
    response = openbrewery_api('get', url='/breweries/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0')

    assert response.status_code == 200


def test_get_a_single_brewery_name_is_ok():
    response = openbrewery_api('get', url='/breweries/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0')

    assert response.json()['name'] == 'MadTree Brewing 2.0'


@pytest.mark.parametrize("city, per_page", [('san_diego', 3), ('los_angeles', 10)])
def test_get_list_of_breweries_by_city_status_code_is_ok(city, per_page):
    response = openbrewery_api('get', url=f'/breweries?by_city={city}&per_page={per_page}')

    assert response.status_code == 200


@pytest.mark.parametrize("type, per_page", [('nano', 5), ('bar', 18)])
def test_get_list_of_breweries_by_type_status_code_is_ok(type, per_page):
    response = openbrewery_api('get', url=f'/breweries?by_type={type}&per_page={per_page}')

    assert response.status_code == 200
