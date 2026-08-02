import pathlib
import psutil
from utils.conversions import bytes_to_gb
def get_disk_info():

    drive = pathlib.Path.home().drive
    disk = psutil.disk_usage(drive)

    return{
        "Drive": drive,
        "Total Space": f"{bytes_to_gb(disk.total)} GB",
        "Used Space": f"{bytes_to_gb(disk.used)} GB",
        "Free Space": f"{bytes_to_gb(disk.free)} GB",
        "Usage": disk.percent
    }