import re
import random
import time

# Generate 30,000-word text
words = ["word"] * 30000
text = " ".join(words)

# Generate a random 20-character string
random.seed(42)
target_str = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=20))

# Insert the target string 500 times at random positions in the text
positions = sorted(random.sample(range(len(text)), 500))
text_with_inserts = []
last_idx = 0
for pos in positions:
    text_with_inserts.append(text[last_idx:pos])
    text_with_inserts.append(target_str)
    last_idx = pos
text_with_inserts.append(text[last_idx:])
text = ''.join(text_with_inserts)

# Save the original text for reuse in tests
original_text = text

times_re = []
for i in range(200):
    t1 = time.time()
    i = re.sub(target_str, "REPLACED", original_text)
    t2 = time.time()
    times_re.append(t2 - t1)

average_re = sum(times_re) / len(times_re)
print(f"(a) Average time using re.sub: {average_re:.6f} seconds")


def custom_substitute(text, target, replacement):
    return text.replace(target, replacement)

times_custom = []
for i in range(200):
    t1 = time.time()
    i = custom_substitute(original_text, target_str, "REPLACED")
    t2 = time.time()
    times_custom.append(t2 - t1)

average_custom = sum(times_custom) / len(times_custom)
print(f"(c) Average time using custom_substitute: {average_custom:.6f} seconds")

print("\n(d) Comparison:")
if average_re < average_custom:
    print(f"re.sub is faster by {average_custom - average_re:.6f} seconds on average")
else:
    print(f"custom_substitute is faster by {average_re - average_custom:.6f} seconds on average")
