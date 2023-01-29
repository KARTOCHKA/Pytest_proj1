import pytest

from utils import arrs
from utils import dicts


@pytest.fixture
def data():
    return {"vcs": "mercurial"}


def test_dicts(data):
    assert dicts.get_val({}, "vcs") == "git"
    assert dicts.get_val(data, "vcs") == "mercurial"
    assert dicts.get_val(data, "HHS") == "git"


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1, 2) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -2) == [4, 5]
    assert arrs.my_slice([1, 2], -3) == [1, 2]
