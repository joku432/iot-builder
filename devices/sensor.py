from .genericdevice import GenericDevice


class Sensor(GenericDevice):
    def __init__(self, voltage: float):
        self.voltage = voltage
