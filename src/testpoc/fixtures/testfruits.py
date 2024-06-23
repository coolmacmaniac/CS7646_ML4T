# https://stackoverflow.com/a/77067340

import pytest

@pytest.fixture
def fruits(request):
    # request.param may also be a datasource name
    return f'fruits {request.param}'
