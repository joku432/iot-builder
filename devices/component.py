class GenericComponent:
    def __init__(self, name: str):
        pass

class Sensor(GenericComponent):
    def __init__(self):
        super().__init__("Sensor")

class Motor(GenericComponent):
    def __init__(self):
        super().__init__("Motor")