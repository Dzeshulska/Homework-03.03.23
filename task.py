registration = [ ]
print(registration)

registar_data = " "
print(registar_data)

user_login = input(("Enter your login: "))
user_password = input(("Enter your password: "))
print((f"{user_login} {user_password}"))

user_login = input(("Enter your login: "))
if len(user_login) < 5:
    print("Error")

user_password = input((("Enter your password: ")))
if len(user_password) > 10:
    print("Eror")

    
