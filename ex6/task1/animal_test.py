from animal import Animal
from mammal import Mammal
from wolf import Wolf
from bird import Bird
from dog import Dog

def run_a_tests():
    a1 = Animal(6, 4)
    a2 = Animal(4, 4)

    a1.make_sound()
    print(a1.get_legs())

    a2.make_sound()
    print(a2.get_legs())


def run_b_tests():
    a3 = Mammal(3)
    a4 = Bird(2)
    wolf1 = Wolf("Raasinkorpi", 5)

    make_it_do_the_sound(a3)
    make_it_do_the_sound(a4)
    make_it_do_the_sound(wolf1)

    wolf1.make_sound()
    print(a3.get_legs())


def run_age_tests():
    animal1 = Animal(4, 3)
    mammal1 = Mammal(5)
    bird1 = Bird(2)
    wolf1 = Wolf("ABC Pack", 4)

    print(f"Animal age: {animal1.get_age()}")
    print(f"Mammal age: {mammal1.get_age()}")
    print(f"Bird age: {bird1.get_age()}")
    print(f"Wolf age: {wolf1.get_age()}")

    # Test setting new age
    wolf1.set_age(6)
    print(f"Updated Wolf age: {wolf1.get_age()}")

    # Test pack name update
    print(f"Original pack name: {wolf1.get_pack_name()}")
    wolf1.set_pack_name("New Pack")
    print(f"Updated pack name: {wolf1.get_pack_name()}")


def make_it_do_the_sound(any_animal: Animal):
    any_animal.make_sound()


def run_c_tests():
    a4 = Wolf("Raasinkorpi", 6)
    a4.make_sound()
    print(a4.get_legs())


def run_d_tests():
    a5 = Bird(3)
    a5.make_sound()
    print(a5.get_legs())


# New tests for encapsulation, getters, and setters
def test_encapsulation():
    print("\nTesting Encapsulation...")

    # Animal class
    a = Animal(4, 5)
    try:
        print(a.__age)  # This should fail
    except AttributeError:
        print("Encapsulation works: Cannot access __age directly.")

    # Wolf class
    w = Wolf("Moon Pack", 4)
    try:
        print(w.__pack_name)  # This should fail
    except AttributeError:
        print("Encapsulation works: Cannot access __pack_name directly.")


def test_getters():
    print("\nTesting Getters...")

    a = Animal(4, 5)
    assert a.get_legs() == 4
    assert a.get_age() == 5
    print("get_legs() and get_age() work correctly.")

    w = Wolf("Moon Pack", 4)
    assert w.get_pack_name() == "Moon Pack"
    print("get_pack_name() works correctly.")


def test_setters():
    print("\nTesting Setters...")

    a = Animal(4, 5)
    a.set_age(10)
    assert a.get_age() == 10
    print("set_age() updates age correctly.")

    w = Wolf("Moon Pack", 4)
    w.set_pack_name("Shadow Pack")
    assert w.get_pack_name() == "Shadow Pack"
    print("set_pack_name() updates pack name correctly.")


def run_dog_tests():
    print("\nTesting Dog class...")

    # Creating a Dog instance
    d = Dog("Golden Retriever", 3)

    # Encapsulation test
    try:
        print(d.__breed)  
    except AttributeError:
        print("Encapsulation works: Cannot access __breed directly.")

    # Getter test
    print(f"The dog's breed is: {d.get_breed()}")

    # Setter test
    d.set_breed("Labrador")
    print(f"The dog's updated breed is: {d.get_breed()}")

    # Dynamic binding test → Dog should bark, not howl
    print("Dog sound test output:")
    d.make_sound()  # Expected: *Dog barking* Woof! Woof!

    # Fetching test
    d.fetch("ball")  # Expected: *The Labrador dog fetches the ball happily!*

    # Wag tail test
    d.wag_tail()  # Expected: *The dog wags its tail excitedly!*



# Running the active tests
print("a-tests:")
run_a_tests()

print("\nb-tests:")
run_b_tests()

print("\nAge tests:")
run_age_tests()

print("\nEncapsulation tests:")
test_encapsulation()

print("\nGetter tests:")
test_getters()

print("\nSetter tests:")
test_setters()

print("\nDog Tests:")
run_dog_tests()
# Keeping c-tests and d-tests but not running them

print()
print("c-tests:")
run_c_tests()

print()
print("d-tests:")
run_d_tests()

