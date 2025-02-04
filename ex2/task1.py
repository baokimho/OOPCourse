# Initial queue
queue = ["Matti", "Riikka", "Antti", "Jenni", "Anu", "Ville", "Jarno"]

# Time t + 1: The first person in the queue leaves after paying for their purchases.
queue.pop(0)

# Time t + 2: Ville recruits Anni to queue on his behalf.
queue[queue.index("Ville")] = "Anni"

# Time t + 3: Jarno leaves, tired of the constant waiting.
queue.remove("Jarno")

# Time t + 4: Marjo joins the end of the queue.
queue.append("Marjo")

# Time t + 5: As a gentleman, Antti lets the two people behind him go ahead of him.
index_antti = queue.index("Antti")
queue.insert(index_antti + 3, queue.pop(index_antti))

# Check if Jenni is in the queue and her position
is_jenni_in_queue = "Jenni" in queue
jenni_position = queue.index("Jenni") + 1 if is_jenni_in_queue else None

# Determine the third last person in the queue
third_last_person = queue[-3]

# Output the results
print(f"Is Jenni in the queue? {'Yes' if is_jenni_in_queue else 'No'}")
if is_jenni_in_queue:
    print(f"Jenni's position in the queue: {jenni_position}")
print(f"The third last person in the queue: {third_last_person}")