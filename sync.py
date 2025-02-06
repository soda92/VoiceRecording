import win32api

def get_disk_name(path):
    return win32api.GetVolumeInformation(f"{path[0]}:\\")[0]

