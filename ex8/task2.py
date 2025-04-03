# def check_access(user):
#     if user['role'] == 'admin' and user['active'] and user['age'] > 18:
#         return True
#     elif user['role'] == 'user' and user['active'] and user['age'] > 18:
#         return True
#     else:
#         return False

def check_access(user):
    return user["role"] in {'admin', 'user'} and user['activate'] and user['age'] > 18


#Example
kim = {'role': 'admin', 'activate': True, 'age': 20}
kim1 = {'role': 'admin', 'activate': True, 'age': 10}
kim2 = {'role': 'customer', 'activate': True, 'age': 30}

print(check_access(kim))
print(check_access(kim1))
print(check_access(kim2))