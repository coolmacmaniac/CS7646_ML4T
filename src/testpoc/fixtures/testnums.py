# https://stackoverflow.com/a/74144573

import pytest

@pytest.fixture(params=[1, 2, 3, 4, 5])
def number(request):
    yield request.param
