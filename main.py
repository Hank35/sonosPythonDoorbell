import soco

devices = {device.player_name: device for device in soco.discover()}

for device in devices:
    print(device.by_name())