import pytest
from requests import sessions


def dog_api(method, url, **kwargs):
    new_url = 'https://dog.ceo/api' + url
    with sessions.Session() as session:
        response = session.request(method=method, url=new_url, **kwargs)
    return response


def test_list_all_breeds_status_code_is_ok():
    response = dog_api('get', url='/breeds/list/all')

    assert response.status_code == 200


def test_get_random_image_status_code_is_ok():
    response = dog_api('get', url='/breeds/image/random')

    assert response.status_code == 200


@pytest.mark.parametrize("breed, num_images", [("hound", 1), ("husky", 3), ("beagle", 2)])
def test_get_multiple_random_dog_image_from_a_breed_status_code_is_ok(breed, num_images):
    response = dog_api('get', url=f'/breed/{breed}/images/random/{num_images}')

    assert response.status_code == 200


@pytest.mark.parametrize("breed", ["hound", "husky", "beagle"])
def test_get_Browse_breed_list(breed):
    response = dog_api('get', url=f'/breed/{breed}/images/random')

    assert response.status_code == 200
