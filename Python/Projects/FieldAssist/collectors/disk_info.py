import pathlib
import psutil
def get_disk_info():
    return{
        "Drive": pathlib.Path.home().drive,
        "Total Space": psutil.disk_usage(pathlib.Path.home().drive)
        ## "Used Space":
        ## "Free Space":
        ## "Usage":
    }