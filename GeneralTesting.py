import bluetooth

devices = bluetooth.discover_devices(20)

for device in devices:
    print(device, bluetooth.lookup_name(device))
