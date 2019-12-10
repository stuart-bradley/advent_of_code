import pytest
from challenge_1.one import fuel_requirements
from challenge_1.two import fuel_requirements_fuel_inclusive


@pytest.mark.parametrize(
    'mass, fuel',
    [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583)
    ]
)
def test_fuel_requirements(mass, fuel):
    assert fuel_requirements(mass) == fuel

@pytest.mark.parametrize(
    'mass, fuel',
    [
        (14, 2),
        (1969, 966),
        (100756, 50346)
    ]
)
def test_fuel_requirements_fuel_inclusive(mass, fuel):
    assert fuel_requirements_fuel_inclusive(mass) == fuel