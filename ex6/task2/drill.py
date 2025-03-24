from tool import Tool

class Drill(Tool):
    def __init__(self, manufacturer, model, rpm, is_cordless):
        super().__init__(manufacturer, model)
        assert isinstance(rpm, (int, float)) and rpm >0, "RPM must be a positive number>"
        self.__rpm = rpm
        self.__is_cordless = is_cordless

    def get_rpm(self):
        return self.__rpm
    
    def set_rpm(self, new_rpm):
        assert isinstance(new_rpm,(int, float)) and new_rpm >0, "RPM must be a positive number."
        self.__rpm = new_rpm
    
    def is_cordless(self):
        return self.__is_cordless
    
    def use(self):
        print(f"Using drill {self.get_info()} with {self.__rpm} RPM.")

        