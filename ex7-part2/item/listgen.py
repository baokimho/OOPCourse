# Copyright Sami Pyöttiälä 2021



def double_char_list_of(characters):
    """List comprehensions"""
    doubled = [2*c for c in characters]
    return doubled   


def cartesian_product(one_sequence, another_sequence):
    """List comprehensions"""
    g = [(x, y) for x in one_sequence for y in another_sequence]
    return g




a_word = "abc234"
double_char_word = double_char_list_of(a_word)
print(double_char_word)



one_sequence = 'abcdefg'
another_sequence = (1, 2, 3, 4)
generated = cartesian_product
print(generated)

