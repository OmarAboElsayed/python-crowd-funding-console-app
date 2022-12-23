import re
import json

def validate_email(email):
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if email_regex.search(email):
        return email
    else:
        print("In-valid email!")
        return 0


def confirmed_password(password, confirm_password):
    if confirm_password == password:
        return password
    else:
        print("passwords don't matched")
        return 0


def validate_phone(mobile_phone):
    mobile_regex = re.compile(r"^020?[10,11,12, 15]\d{8}")
    if mobile_regex.search(mobile_phone):
        return mobile_phone
    else:
        print("Invalid phone number")
        return 0


def create_user():
    first_name = input("Please Enter Your First name : ")
    last_name = input("Please Enter Your  Last name : ")
    email = input("Please Enter Your Email : ")
    password = input("Please Enter Your Password : ")
    confirm_password = input("Please Enter Your Confirm password : ")
    mobile_phone = input("Please Enter Your Mobile phone : ")

    email = validate_email(email)
    if email:
        password = confirmed_password(password, confirm_password)
        if password:
            phone = validate_phone(mobile_phone)
            if phone:
                new_user = {"First_Name": first_name,
                            "Last_Name": last_name,
                            "Email": email,
                            "Password": password,
                            "Mobile": phone,
                            "Activated": True}
                return new_user

    return False


def add_user(user_data):
    users_data = open("users.json", "a")
    json.dump(user_data, users_data)
    users_data.write("\n")
    users_data.close()


def register():
    user_data = create_user()
    if user_data:
        add_user(user_data)
        print("Registration Succeeded!")
    else:
        print("Registration Failed!")