from .prime_factors import prime_factors
import pytest

@pytest.mark.parametrize("number, expected", [
    (2, [2]),
    (7, [7]),
    (8, [2, 2, 2]),
    (18, [2, 3, 3]),
    (108, [2, 2, 3, 3, 3]),
])
def test_prime_factors(number, expected):
    assert prime_factors(number) == expected


@pytest.mark.parametrize("number", [2, 7, 13, 17])
def test_prime_numbers(number):
    assert len(prime_factors(number)) == 1


@pytest.mark.parametrize("number", [
    2.5, 
    pytest.param(1, marks=[pytest.mark.xfail]),
    pytest.param(0, marks=[pytest.mark.skip])
    ])
def test_prime_factors_raises(number):
    with pytest.raises(ValueError):
        prime_factors(number)
