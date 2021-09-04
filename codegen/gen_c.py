from devices.devicenetwork import GenericDeviceNetwork

class CGenerator:
    def __init__(self, network: GenericDeviceNetwork):
        self.network = network

    def gen(self, output_dir: str) -> None:
        for device in self.network.devices:
            # each device will get their own file
            with open("devicename.c", "w"):
                pass

