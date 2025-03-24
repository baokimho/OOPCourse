class Tool:
    def __init__(self, manufacturer, model):
        assert isinstance(manufacturer, str) and manufacturer, "Manufacturer must be a non-empty string."
        assert isinstance(model, str) and str, "Model must be a non-empty string."
        
        self.__manufacturer = manufacturer
        self.__model = model 
    
    def get_info(self):
        return f"Manufacturer: {self.__manufacturer}, Model: {self.__model}"
    
    def use(self):
        print(f"Using {self.__model} tool.")
    
