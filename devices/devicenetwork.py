class GenericDeviceNetwork:
    def __init__(self, kind: str, devices = [], communication_protocol = ""):
        self.devices = devices
        self.communication_protocol = communication_protocol

    def __len__(self):
        return len(self.devices)