from geomove import Bearing, haversine, move
import pytest


def test_move_point():
    """
    Test move point with some defined cases.
    """
    # Define cases (origin, bearing, distance, expected)
    cases = [
        ((51.9624, 7.6256), 0, 1, (51.97139320367762, 7.625600000000001)),
        ((51.9624, 7.6256), 90, 1, (51.95836966175978, 7.638646822807718)),
        (
            (0, -179.999999),
            Bearing.WEST,
            10,
            (0.0885274726594929, 179.98416881686882),
        ),
    ]
    # Run test cases
    for case in cases:
        moved = move(case[0], case[1], case[2])
        assert moved == pytest.approx(case[3], abs=1e-12)
        assert haversine(case[0], moved) == pytest.approx(case[2], abs=1e-12)


if __name__ == "__main__":
    test_move_point()
    print("Everything passed")
