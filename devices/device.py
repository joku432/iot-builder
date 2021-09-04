from devices.devicenetwork import GenericDeviceNetwork

class _PinMapping:
    def __init__(self, pins = {}):
        pass

class GenericDevice:
    def __init__(self, name: str, pins: _PinMapping):
        pass

class Sensor(GenericDevice):
    pass

class SensorNode(GenericDevice):
    pass

