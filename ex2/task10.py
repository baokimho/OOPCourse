class RealProperty:
    def __init__(self,rooms:int, square_metres: float,pricce_sqm:int ):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_sqm = pricce_sqm
    #Part 1
    def bigger(self, compared_to):
        return self.square_metres > compared_to.square_metres
    #Part 2
    def price_difference(self, compared_to):
        return abs(self.square_metres * self.price_sqm - compared_to.square_metres * compared_to.price_sqm)
    #Part 3
    def more_expensive(self, compared_to):
        return self.square_metres * self.price_sqm > compared_to.square_metres * compared_to.price_sqm
#example
central_studio = RealProperty(1, 30, 2000)
downtown_two_bedroom = RealProperty(2, 50, 3000)
#Part 1
print(central_studio.bigger(downtown_two_bedroom)) # False
print(downtown_two_bedroom.bigger(central_studio)) # True
#Part 2
print(central_studio.price_difference(downtown_two_bedroom)) 
print(downtown_two_bedroom.price_difference(central_studio)) 
#Part 3
print(central_studio.more_expensive(downtown_two_bedroom)) # False
print(downtown_two_bedroom.more_expensive(central_studio)) # True