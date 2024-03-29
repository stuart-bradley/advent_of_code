import pytest

from year_2019.challenge_5 import run_intcode


@pytest.mark.parametrize(
    "string, result",
    [
        ("1,0,0,0,99", "2,0,0,0,99"),
        ("2,3,0,3,99", "2,3,0,6,99"),
        ("2,4,4,5,99,0", "2,4,4,5,99,9801"),
        ("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99"),
    ],
)
def test_run_intcode(string, result):
    assert ",".join([str(x) for x in run_intcode(string)[0]]) == result
