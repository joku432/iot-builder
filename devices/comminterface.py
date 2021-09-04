class GenericCommunicationInterface:
    """Defines a common interface for 
    several possible communication protocols
    available for use in the IOT builder application"""
    def __init__(self, protocol_name: str):
        pass

class BluetoothConnection(GenericCommunicationInterface):
    def __init__(self, device1: str, device2: str, btversion: int = 4):
        super().__init__(f"Bluetooth v{4}")

class I2CConnection(GenericCommunicationInterface):
    def __init__(self, master: str, slave: str):
        super().__init__("I2C")