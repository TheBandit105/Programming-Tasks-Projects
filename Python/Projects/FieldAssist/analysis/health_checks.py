def check_disk_usage(disk):
    usage = disk["Usage"]

    if usage >= 90:
        return "Critical"
    elif usage >= 80:
        return "Warning"
    else:
        return "OK"