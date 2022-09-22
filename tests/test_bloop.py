import bloop

def test_bloop():
    # test calling cpp extension directly
    assert bloop.bleep.add(2, 2) == 4
    assert bloop.bleep.sub(2, 2) == 0

    # test python package around c extension
    assert bloop.double_add(2, 2) == 8

