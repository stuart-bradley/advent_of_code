import pytest

from year_2019.challenge_3 import best_intersection, closest_distance


@pytest.mark.parametrize(
    "wire_1, wire_2, distance",
    [
        ("R8,U5,L5,D3", "U7,R6,D4,L4", 6),
        ("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83", 159),
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            135,
        ),
    ],
)
def test_closest_distance(wire_1, wire_2, distance):
    assert closest_distance(wire_1, wire_2) == distance


@pytest.mark.parametrize(
    "wire_1, wire_2, distance",
    [
        ("R8,U5,L5,D3", "U7,R6,D4,L4", 30),
        ("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83", 610),
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            410,
        ),
    ],
)
def test_best_intersection(wire_1, wire_2, distance):
    assert best_intersection(wire_1, wire_2) == distance
