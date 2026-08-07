import psutil
from utils.conversions import bytes_to_gb
def get_memory_info():

    memory = psutil.virtual_memory()

    return{
        "Total Memory": f"{bytes_to_gb(memory.total)} GB",
        "Used Memory": f"{bytes_to_gb(memory.used)} GB",
        "Available Memory": f"{bytes_to_gb(memory.available)} GB",
        "Usage": bytes_to_gb(memory.percent)
    }