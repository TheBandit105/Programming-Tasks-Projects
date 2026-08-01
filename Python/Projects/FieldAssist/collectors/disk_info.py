import pathlib
import psutil
def get_disk_info():

    drive = pathlib.Path.home().drive
    disk = psutil.disk_usage(drive)

    return{
        "Drive": drive,
        "Total Space": f"{disk.total / (1024 ** 3):.2f} GB",
        "Used Space": f"{disk.used / (1024 ** 3):.2f} GB",
        "Free Space": f"{disk.free / (1024 ** 3):.2f} GB",
        "Usage": disk.percent
    }