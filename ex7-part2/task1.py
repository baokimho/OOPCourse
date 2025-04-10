def square_numbers(numbers):
    squares = []
    for x in numbers:
        squares.append(x**2)
    return squares

def filter_even(numbers):
    evens = []
    for x in numbers:
        if x % 2 == 0:
            evens.append(x)
    return evens

def sort_by_length(words):
    def get_length(word):
        return len(word)
    return sorted(words, key=get_length)

def index_even_positions(items):
    result = []
    i = 0
    for idx, val in enumerate(items):
        if idx % 2 == 0:
            result.append((idx, val))
    return result

def test_all():
    numbers = [1, 2, 3, 4]
    words = ['banana', 'apple', 'kiwi']

    squares_lambda = list(map(lambda x: x**2, numbers))
    evens_lambda = list(filter(lambda x: x % 2 == 0, numbers))
    sorted_lambda = sorted(words, key=lambda x: len(x))
    enum_lambda = list(filter(lambda pair: pair[0] % 2 == 0, enumerate(words)))

    squares_for = square_numbers(numbers)
    evens_for = filter_even(numbers)
    sorted_for = sort_by_length(words)
    enum_for = index_even_positions(words)

    assert squares_lambda == squares_for
    assert evens_lambda == evens_for
    assert sorted_lambda == sorted_for
    assert enum_lambda == enum_for

    print("All tests passed.")

test_all()

