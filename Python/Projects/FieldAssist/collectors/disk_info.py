import pathlib
import psutil
from utils.conversions import bytes_to_gb

"""
Disk Information Collector

Collects information about the current Windows system drive.

Current Information:
- Drive Letter
- Total Space
- Used Space
- Free Space
- Usage Percentage

Future Improvements:
- Support multiple drives.
- Include filesystem type.
- Add SMART health information.
"""
def get_disk_info():

    """
    Collect disk usage statistics.

    Returns:
        dict:
            A dictionary containing information about
            the primary Windows drive.
    """

    # Determine which drive contains the current user's profile.
    # This is typically the Windows system drive (e.g. C:).

    drive = pathlib.Path.home().drive


    # Retrieve disk usage statistics from the operating system.

    disk = psutil.disk_usage(drive)

    return{
        "Drive": drive,
        "Total Space": f"{bytes_to_gb(disk.total)} GB",
        "Used Space": f"{bytes_to_gb(disk.used)} GB",
        "Free Space": f"{bytes_to_gb(disk.free)} GB",
        "Usage": disk.percent
    }