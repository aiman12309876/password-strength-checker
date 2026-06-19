import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    if len(password) >= 12:
        strength += 2
        feedback.append("Good length (12+ characters)")
    elif len(password) >= 8:
        strength += 1
        feedback.append("Moderate length (8-11 characters)")
    else:
        feedback.append("Too short (less than 8 characters)")
    
    if re.search(r'[A-Z]', password):
        strength += 1
        feedback.append("Contains uppercase letters")
    else:
        feedback.append("Missing uppercase letters")
    
    if re.search(r'[a-z]', password):
        strength += 1
        feedback.append("Contains lowercase letters")
    else:
        feedback.append("Missing lowercase letters")
    
    if re.search(r'[0-9]', password):
        strength += 1
        feedback.append("Contains numbers")
    else:
        feedback.append("Missing numbers")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 2
        feedback.append("Contains special characters")
    else:
        feedback.append("Missing special characters")
    
    common_patterns = ['password', '123456', 'qwerty', 'abc123', 'admin']
    if password.lower() in common_patterns:
        strength = 0
        feedback.append("Password is too common")
        return "VERY WEAK", feedback
    
    if strength >= 7:
        return "STRONG", feedback
    elif strength >= 5:
        return "MEDIUM", feedback
    else:
        return "WEAK", feedback

def main():
    print("\n" + "=" * 60)
    print("PASSWORD STRENGTH CHECKER".center(60))
    print("=" * 60)
    print("Enter a password to check its strength")
    print("Type 'quit' to exit")
    print("=" * 60 + "\n")
    
    while True:
        password = input("Enter password: ")
        
        if password.lower() == 'quit':
            print("\n" + "=" * 60)
            print("Thanks for using Password Strength Checker".center(60))
            print("=" * 60 + "\n")
            break
        
        if len(password) == 0:
            print("Password cannot be empty\n")
            continue
        
        strength, feedback = check_password_strength(password)
        
        print("\n" + "-" * 60)
        print("Password Strength: " + strength)
        print("-" * 60)
        print("Feedback:")
        for item in feedback:
            print("  - " + item)
        print("-" * 60 + "\n")

if __name__ == "__main__":
    main()