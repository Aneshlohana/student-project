from student_app.logger import logger

def validate_marks(marks) -> float:
    """Validates that marks are numbers between 0 and 100."""
    logger.debug(f"Validating marks input: {marks}")
    
    try:
        numeric_marks = float(marks)
    except (ValueError, TypeError):
        logger.error(f"Invalid input type detected: '{marks}' is not a valid number.")
        raise ValueError(f"Marks must be a numeric value. Got: '{marks}'")
        
    if not (0 <= numeric_marks <= 100):
        logger.warning(f"Boundary violation: Marks value {numeric_marks} is out of bounds (0-100).")
        raise ValueError("Marks must be between 0 and 100.")
        
    logger.info(f"Marks validated successfully: {numeric_marks}")
    return numeric_marks