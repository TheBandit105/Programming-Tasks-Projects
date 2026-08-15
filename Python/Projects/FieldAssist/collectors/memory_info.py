"""
Memory Information Collector

Collects information about the computer's physical memory (RAM)
using psutil.

Current information:
- Total memory
- Used memory
- Available memory
- Memory usage percentage

Future improvements:
- Analyse memory usage and provide health warnings.
- Identify processes using large amounts of memory.
"""

import psutil
from utils.conversions import bytes_to_gb

def get_memory_info():

    """
    Collect system memory usage statistics.

    Returns:
        dict:
            A dictionary containing total, used and available
            memory, along with the current memory usage percentage.
    """

    # Retrieve current system memory statistics from the operating system.
    memory = psutil.virtual_memory()

    return{
        "Total Memory": f"{bytes_to_gb(memory.total)} GB",
        "Used Memory": f"{bytes_to_gb(memory.used)} GB",
        "Available Memory": f"{bytes_to_gb(memory.available)} GB",
        "Usage": f"{memory.percent} %"
    }