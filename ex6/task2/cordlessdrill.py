from drill import Drill

class CordlessDrill(Drill):
    def __init__(self,manufacturer, model, rpm, battery_life):
        super().__init__(manufacturer, model, rpm, True)
        assert isinstance(battery_life, (int, float)) and battery_life >0, "Battery life must be a non-negative."
        self.__battery_life = battery_life

    def charge_battery(self, hours):
        assert isinstance(hours,(int,float)) and hours >0 , "Charge time must be positive."
        self.__battery_life += hours
        print(f"Charge battery by {hours}. Total battery life: {self.__battery_life} hours.")
