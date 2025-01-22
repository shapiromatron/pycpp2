import bloop


def test_bloop():
    # test calling cpp extension directly
    assert bloop.core.add(2, 2) == 4
    assert bloop.core.sub(2, 2) == 0

    # test python package around c extension
    assert bloop.double_add(2, 2) == 8

    # version -> python == cpp == expected value
    assert bloop.__version__ == bloop.core.__version__ == "0.0.2"
