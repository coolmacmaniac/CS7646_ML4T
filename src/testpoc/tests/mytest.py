####
# How to run this file --
# 1.
# cd ~/.../src/testpoc
# pytest -vvs tests/mytest.py
# or
# 2.
# cd ~/.../src/testpoc/tests
# pytest -vvs --rootdir='../' mytest.py


import pytest
from code.add import add


def test_number_is_integer(number):
    assert isinstance(number, int)


@pytest.mark.parametrize('instances', [
    [[1, 2, 3]],
    [[2, 4, 6]],
    [[6, 8, 14]],
])
def test_timeline(timeline):
    for instance in timeline.instances:
        # print('••••', instance)
        assert add(instance[0], instance[1]) == instance[2]


@pytest.mark.parametrize(
    "fruits", 
    [
        "Apple",                          # request.param # 1
        ["Apple", "Orange", "Banana"],    # request.param # 2
        ("Pear", "Pineapple")             # request.param # 3
    ], 
    indirect=True
)
def test(fruits):
    print(fruits)
    assert True
