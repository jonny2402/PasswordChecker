"""
This module contains a class and a method for checking the strength of a password.
"""

import re

class PasswordStrengthChecker:
    """
    A class used to check the strength of a password.

    ...

    Attributes
    ----------
    common_passwords : set
        a set of common passwords that should be avoided

    Methods
    -------
    check_strength(password)
        Checks the strength of a password.
    """

    COMMON_PASSWORDS = set(["password", "123456", "123456789", "12345678", "12345",
                            "1234567", "admin", "1234567890", "letmein", "123456789",
                            "1234", "qwertyuiop", "123321", "password1", "123123"])

    def check_strength(self, password):
        """
        Checks the strength of a password.

        Parameters
        ----------
        password : str
            The password to check.

        Returns
        -------
        tuple
            A tuple containing the strength of the password and a list of feedback.
        """

        score = 0
        feedback = []

        if password in self.COMMON_PASSWORDS:
            feedback.append("Avoid common passwords.")
            return ('very weak', feedback)

        if len(password) < 8:
            feedback.append("Use at least 8 characters.")
        else:
            score += 1

        if not (re.search(r'[A-Z]', password) and re.search(r'[a-z]', password)):
            feedback.append("Include both uppercase and lowercase letters.")
        else:
            score += 1

        if not re.search(r'\d', password):
            feedback.append("Include numbers.")
        else:
            score += 1

        if not re.search(r'[^a-zA-Z\d]', password):
            feedback.append("Add special characters (e.g., @, #, $).")
        else:
            score += 1

        strength = ['very weak', 'weak', 'moderate', 'strong', 'very strong'][score]
        return (strength, feedback)



def main():
    """
    Main function to run the PasswordStrengthChecker.
    It prompts the user to enter passwords and checks their strength.
    """

    checker = PasswordStrengthChecker()
    password_history = {}

    while True:
        password = input("\nEnter a password to check its strength (or 'quit' to exit): ")
        if password.lower() == 'quit':
            break

        strength, feedback = checker.check_strength(password)
        password_history[password] = (strength, feedback)

        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Suggestions to improve your password:")
            for suggestion in feedback:
                print(f" - {suggestion}")

    print("\nPassword History:")
    for pwd, (strength, _) in password_history.items():
        print(f"{pwd}: {strength}")

if __name__ == "__main__":
    main()
