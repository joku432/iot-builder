from devices.devicenetwork import GenericDeviceNetwork

class CGenerator:
    def __init__(self, network: GenericDeviceNetwork):
        self.network = network

    def gen(self, output_dir: str) -> None:
        for device in self.network.devices:
            # each device will get their own file
            with open(f"iotb_{device.name}.c", "w") as f:
                self._gen_base_code(f)
                f.write()


    def _gen_base_code(self, file):
        file.writelines([
            "/* Automatically generated by IoT builder*/",
            "\n\n",
            ]
        )
