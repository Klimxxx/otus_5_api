import pytest
from requests import sessions


def jsonplaceholder_api(method, url, **kwargs):
    new_url = 'https://jsonplaceholder.typicode.com' + url
    with sessions.Session() as session:
        response = session.request(method=method, url=new_url, **kwargs)
    return response


def test_post_creating_a_resource_status_code_is_ok():
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = {'title': 'foo', 'body': 'bar', 'userId': 1}

    response = jsonplaceholder_api('post', url='/posts', headers=headers, json=body)

    assert response.status_code == 201


def test_post_creating_a_resource_status_id_is_ok():
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = {'title': 'foo', 'body': 'bar', 'userId': 1}

    response = jsonplaceholder_api('post', url='/posts', headers=headers, json=body)

    assert response.json()['id'] == 101


def test_post_creating_a_resource_status_headers_is_ok():
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = {'title': 'foo', 'body': 'bar', 'userId': 1}

    response = jsonplaceholder_api('post', url='/posts', headers=headers, json=body)

    assert response.headers['Content-type'] == 'application/json; charset=utf-8'


@pytest.mark.parametrize("userId", [1, 2])
def test_get_filtering_resources_status_code_is_ok(userId):
    response = jsonplaceholder_api('get', url=f'/posts?userId={userId}')

    assert response.status_code == 200


@pytest.mark.parametrize("routes", ['comments', 'photos', 'albums', 'todos', 'posts'])
def test_get_Listing_nested_resources_status_code_is_ok(routes):
    response = jsonplaceholder_api('get', url=f'/posts/1/{routes}')

    assert response.status_code == 200
