from student_app.logger import logger

def calculate_grade(marks: float) -> str:
    """Calculates letter grade based on marks."""
    logger.debug(f"Calculating grade for marks: {marks}")
    
    if marks >= 85:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 65:
        grade = "C"
    elif marks >= 55:
        grade = "D"
    else:
        grade = "F"
        
    logger.info(f"Calculated grade '{grade}' for score {marks}")
    return grade