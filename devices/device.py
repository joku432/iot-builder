from .devicenetwork import GenericDeviceNetwork
from .component import *


class _PinMapping:
    def __init__(self, pins = {}):
        self.pins = pins

class GenericDevice:
    def __init__(self, name: str, pins: _PinMapping):
        self.name = name
        self.pins = pins

class SensorNode(GenericDevice):
    def __init__(self, name: str, pins: _PinMapping, components = []):
        super().__init__(name, pins)
        self.components = components