import pytest
from services.calculator import calculate_grade

@pytest.mark.parametrize("marks, expected_grade", [
    (88.0, "A"),  # Grade A test
    (78.0, "B"),  # Grade B test
    (68.0, "C"),  # Grade C test
    (58.0, "D"),  # Grade D test
    (40.0, "F"),  # Grade F test
])
def test_calculate_grade(marks, expected_grade):
    assert calculate_grade(marks) == expected_grade

def test_grade_boundary_edge_cases():
    assert calculate_grade(85.0) == "A"
    assert calculate_grade(75.0) == "B"
    assert calculate_grade(65.0) == "C"
    assert calculate_grade(55.0) == "D"
    assert calculate_grade(54.9) == "F"