from utils import arrs
from utils import dicts

data = {"vcs": "mercurial"}
data1 = {}
data2 = {"vcs": "mercurial"}


def test_dicts():
    assert dicts.get_val(data, "vcs") == "mercurial"
    assert dicts.get_val(data1, "vcs") == "git"
    assert dicts.get_val(data2, "vhc") == "git"


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1, 2) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -2) == [4, 5]
    assert arrs.my_slice([1, 2], -3) == [1, 2]
