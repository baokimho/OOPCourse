# def print_user_info(user):
#     print(f"Name: {user['name']}")
#     print(f"Age: {user['age']}")
#     print(f"Email: {user['email']}")

# def print_admin_info(admin):
#     print(f"Name: {admin['name']}")
#     print(f"Age: {admin['age']}")
#     print(f"Email: {admin['email']}")

def print_person_info(person):
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"Email: {person['email']}")

#Example usage
user = {"name": "Kim", "age": 20, "email": "baokim@gmail.com"}
admin = {"name": "Ho", "age": 21, "email":"kimho@gmail.com"}

print_person_info(user)
print("\n")
print_person_info(admin)