import pytest
from utils.driver_factory import get_driver

@pytest.fixture
def driver(get_driver):
    return get_driver
