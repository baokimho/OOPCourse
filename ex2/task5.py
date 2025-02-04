def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    # Function to calculate the average of results
    def average(person):
        return (person["result1"] + person["result2"] + person["result3"]) / 3

    # Calculate averages
    avg1 = average(person1)
    avg2 = average(person2)
    avg3 = average(person3)

    # Find the person with the smallest average
    smallest = min((avg1, person1), (avg2, person2), (avg3, person3), key=lambda x: x[0])

    return smallest[1]

person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))
