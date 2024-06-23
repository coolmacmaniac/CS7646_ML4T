# https://stackoverflow.com/a/52556384

import pytest


class TimeLine:
    def __init__(self, instances):
        # print('•••', instances)
        self.instances = instances


@pytest.fixture
def instances():
    # print('• dummy instances called')
    return [0, 0, 0]


@pytest.fixture
def timeline(instances):
    # print('\n••', instances)
    return TimeLine(instances)
