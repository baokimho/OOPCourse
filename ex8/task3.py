# def create_user(name, age, email, address, phone, role, active):
#     return {'name': name,
#             'age': age,
#             'email': email,
#             'address': address,
#             'phone': phone,
#             'role': role,
#             'active': active
#             }

def create_user(**kwargs):
    return kwargs

user = create_user(name="kim", age=25, email="kim@example.com", address="123 Street", 
                   phone="123456789", role="admin", active=True)

print(user)