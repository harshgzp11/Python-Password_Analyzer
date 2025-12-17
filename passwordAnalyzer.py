import password_utils

password = input("Enter your password: ")
strength = password_utils.check_strength(password)
feedback= password_utils.get_feedback(password)
print("Password strength: ", strength)

if feedback:
    print("Suggestions: ")
    for items in feedback:
        print("-", items)