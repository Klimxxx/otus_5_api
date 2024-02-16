import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="URL to test")
    parser.addoption("--status_code", action="store", default="200", help="Expected status code")


@pytest.fixture
def url(request):
    return request.config.getoption("--url", default="https://ya.ru")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code", default="200")


def test_url_status(url, status_code):
    response = requests.get(url)
    assert response.status_code == int(
        status_code), f"Expected status code {status_code}, but got {response.status_code}"
