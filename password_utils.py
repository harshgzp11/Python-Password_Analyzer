def has_uppercase(password):
    for ch in password:
        if ch.isupper():
            return True
    return False

def has_lowercase(password):
    for ch in password:
        if ch.islower():
            return True
    return False

def has_digit(password):
    for ch in password:
        if ch.isdigit():
            return True
    return False

def has_special_char(password):
    for ch in password:
        if ch in "!@#$%^&*":
            return True
    return False

def get_feedback(password):
    feedback=[]

    if not has_uppercase(password):
        feedback.append("Add an uppercase letter")
    if not has_lowercase(password):
        feedback.append("Add a lowercase letter")
    if not has_digit(password):
        feedback.append("Add a digit")
    if not has_special_char(password):
        feedback.append("Use a special Character")
    if len(password)<8:
        feedback.append("Increase password length")
    if has_space(password):
        feedback.append("Remove spaces from the password")

    return feedback

def has_space(password):
    for ch in password:
        if ch==" ":
            return True
    return False


def check_strength(password):
    score=0

    if len(password)>=8:
        score=score+1

    if has_uppercase(password):
        score=score+1

    if has_lowercase(password):
        score += 1

    if has_digit(password):
        score += 1

    if has_special_char(password):
        score += 1

    if score<=2:
        return "Weak"
    elif score<=4:
        return "Medium"
    else:
        return "Strong"