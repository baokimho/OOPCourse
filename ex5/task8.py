class Property:
    def __init__(self, square_feet: float, num_bedrooms: int, num_bathrooms: int):
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms

    def display(self):
        print(f"Square Feet: {self.square_feet}")
        print(f"Bedrooms: {self.num_bedrooms}")
        print(f"Bathrooms: {self.num_bathrooms}")

    @classmethod
    def prompt_init(cls):
        square_feet = float(input("Enter square feet: "))
        num_bedrooms = int(input("Enter number of bedrooms: "))
        num_bathrooms = int(input("Enter number of bathrooms: "))
        return {"square_feet": square_feet, "num_bedrooms": num_bedrooms, "num_bathrooms": num_bathrooms}


def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        else:
            print("Please enter yes or no.")


class Apartment(Property):
    def __init__(self, square_feet, num_bedrooms, num_bathrooms, balcony, laundry):
        super().__init__(square_feet, num_bedrooms, num_bathrooms)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print(f"Balcony: {self.balcony}")
        print(f"Laundry: {self.laundry}")

    @classmethod
    def prompt_init(cls):
        details = Property.prompt_init()
        balcony = get_yes_no_input("Does the apartment have a balcony? (y/n) ")
        laundry = get_yes_no_input("Does the apartment have laundry? (y/n) ")
        details.update({"balcony": balcony, "laundry": laundry})
        return cls(**details)


class House(Property):
    def __init__(self, square_feet, num_bedrooms, num_bathrooms, num_stories, garage, fenced_yard):
        super().__init__(square_feet, num_bedrooms, num_bathrooms)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced_yard = fenced_yard

    def display(self):
        super().display()
        print(f"Stories: {self.num_stories}")
        print(f"Garage: {self.garage}")
        print(f"Fenced Yard: {self.fenced_yard}")

    @classmethod
    def prompt_init(cls):
        details = Property.prompt_init()
        num_stories = int(input("Enter number of stories: "))
        garage = get_yes_no_input("Does the house have a garage? (y/n) ")
        fenced_yard = get_yes_no_input("Does the house have a fenced yard? (y/n) ")
        details.update({"num_stories": num_stories, "garage": garage, "fenced_yard": fenced_yard})
        return cls(**details)


class Purchase:
    def __init__(self, price, taxes):
        self.price = price
        self.taxes = taxes

    def display(self):
        print(f"Price: {self.price}")
        print(f"Taxes: {self.taxes}")

    @classmethod
    def prompt_init(cls):
        price = float(input("Enter the price: "))
        taxes = float(input("Enter the taxes: "))
        return cls(price, taxes)


class Rental:
    def __init__(self, furnished, utilities, rent):
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        print(f"Furnished: {self.furnished}")
        print(f"Utilities Included: {self.utilities}")
        print(f"Rent: {self.rent}")

    @classmethod
    def prompt_init(cls):
        furnished = get_yes_no_input("Is the property furnished? (y/n) ")
        utilities = get_yes_no_input("Are utilities included? (y/n) ")
        rent = float(input("Enter the rent: "))
        return cls(furnished, utilities, rent)


if __name__ == "__main__":
    property_details = Property.prompt_init()
    property = Property(**property_details)
    property.display()

    apartment = Apartment.prompt_init()
    apartment.display()

    house = House.prompt_init()
    house.display()

    purchase = Purchase.prompt_init()
    purchase.display()

    rental = Rental.prompt_init()
    rental.display()
