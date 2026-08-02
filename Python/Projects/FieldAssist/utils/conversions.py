"""
Conversion Utilities

Contains reusable helper functions used throughout
the FieldAssist project.

Keeping common conversions here avoids repeating code
across multiple collector modules.
"""

def bytes_to_gb(value):

    """
    Convert bytes into gigabytes.

    Args:
        value (int):
            Value stored in bytes.

    Returns:
        float:
            Value converted to gigabytes,
            rounded to two decimal places.
    """
    
    return round(value / (1024 ** 3), 2)