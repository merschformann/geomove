from geomove import Bearing, haversine, move
import pytest


def test_move_point():
    """
    Test move point with some defined cases.
    """
    # Define cases (origin, bearing, distance, expected)
    cases = [
        ((51.9624, 7.6256), 0, 1, 1, (51.97139320367762, 7.625600000000001)),
        ((51.9624, 7.6256), 90, 1, 1, (51.96239909784941, 7.640195127867031)),
        ((0, -179.999999), Bearing.WEST, 10, 10, (0.0, 179.9100689632238)),
        ((0, 0), 127, 100, 100, (-0.54121033307446, 0.7182505431627817)),
        # Move through north pole to other side of earth
        ((45, 0), Bearing.NORTH, 8966.6, 8966.6, (54.361539904282665, -180.0)),
        # Move around earth (using EARTH_RADIUS_KM for circumference) to land at the same point
        ((45, 0), Bearing.NORTH, 40030.228704373, 0, (45, 0)),
    ]
    # Run test cases
    for case in cases:
        moved = move(case[0], case[1], case[2])
        assert moved == pytest.approx(case[4], abs=1e-10)
        dist = haversine(case[0], moved)
        assert dist == pytest.approx(case[3], abs=1e-9)


if __name__ == "__main__":
    test_move_point()
    print("Everything passed")
