import logging
import sys

def setup_logger():
    """Configures and returns the application logger."""
    logger = logging.getLogger("student_app")
    logger.setLevel(logging.DEBUG)
    
    # Prevent adding multiple handlers if setup is called more than once
    if not logger.handlers:
        # Console Handler
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        
        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger

logger = setup_logger()