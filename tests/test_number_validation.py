from src.number_validation import is_positive_int


def test_positive_int():
    assert is_positive_int(3)


def test_zero_is_not_positive():
    assert not is_positive_int(0)


def test_non_int_is_false():
    assert not is_positive_int("3")
