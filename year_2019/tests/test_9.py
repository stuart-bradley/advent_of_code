import pytest

from year_2019.challenge_9 import IntCodeComputer


@pytest.mark.parametrize(
    "program, result",
    [
        (
            "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99",
            "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99",
        ),
        (
            "104,1125899906842624,99",
            "1125899906842624",
        ),
        ("1102,34915192,34915192,7,4,7,99,0", "1219070632396864"),
    ],
)
def test_relative_intcode(program, result):
    c = IntCodeComputer(program)
    c.run_intcode()
    assert ",".join([str(x) for x in c.outputs]) == result
