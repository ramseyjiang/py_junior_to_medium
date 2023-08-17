import inc_dec


def test_increment():
    assert inc_dec.increment(3) == 4


def test_decrement():
    assert inc_dec.decrement(4) == 3


# Following codes are the evidence for test run correct.
test_increment()
test_decrement()
