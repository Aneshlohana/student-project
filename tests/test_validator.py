import pytest
from utils.validation import validate_marks

@pytest.mark.parametrize("valid_input", [0, 50, 75.5, 100])
def test_validate_marks_valid(valid_input):
    assert validate_marks(valid_input) == float(valid_input)

@pytest.mark.parametrize("invalid_input", [-1, 100.1, 150])
def test_validate_marks_out_of_bounds(invalid_input):
    with pytest.raises(ValueError, match="Marks must be between 0 and 100"):
        validate_marks(invalid_input)

@pytest.mark.parametrize("bad_type_input", ["abc", None, ""])
def test_validate_marks_invalid_type(bad_type_input):
    with pytest.raises(ValueError, match="Marks must be a numeric value"):
        validate_marks(bad_type_input)