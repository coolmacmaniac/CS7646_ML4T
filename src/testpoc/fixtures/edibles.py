import pytest
from model.data_model import DataModel

@pytest.fixture
def test_data(request):
    # request.param may also be a datasource name
    return DataModel(request.param)

@pytest.fixture
def fruits(test_data):
    # aliasing a fixture: a specific fixture to yield the generic fixture
    yield test_data

@pytest.fixture
def vegetables(test_data):
    # aliasing a fixture: a specific fixture to yield the generic fixture
    yield test_data
