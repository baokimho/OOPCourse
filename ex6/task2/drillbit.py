from cordlessdrill import CordlessDrill

class DrillBit:
    def __init__(self, diameter):
        assert isinstance(diameter, (int, float)) and diameter >0, "Diameter must be a positive number."
        self.__diameter = diameter

    def is_compatible(self, drill):
        if isinstance(drill, CordlessDrill) and self.__diameter >10:
            return False
        return True
    
    def get_diameter(self):
        return self.__diameter