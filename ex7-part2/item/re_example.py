# Copyright Sami Pyöttiälä 2021



import re


pattern = r'cat'
text = 'The cat is on the roof.'
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")
print()


"""
pattern = r'[aeiou]'  #r means raw string, for example then \ is not special char
text = 'otapple'
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")
print()




pattern = r'^a.*s$'  
text = 'apples'
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")
print()


pattern = r'\d{3}-\d{2}-\d{4}'
text = 'My number is 123-45-6789'
match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
print(match)
print()

pattern = r'\d{3}-\d{2}-\d{4}'
text = 'My number is 123-455-6789'
match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
print(match)
print()


# substitute
text = 'Hello 123, this is a test 456'
new_text = re.sub(r'\d+', 'number', text)
print(new_text)
print()


"""




