# FP PROJRECT 05 = PASSWRD GENERATOR APP

# 🔐 Password Generator App

# Heroboard Entry #5 - Day 5 Project 05

import random
import string

print("🔐 Welcome to the Password Generator!")
print("Let's forge your ultmate password.\n")

# Ask user how long the password should be

length = int(input("How long do you want your password? "))

# Define possible characters (letters + digits + symbols)

characters = string.ascii_letters + string.digits + string.punctuation

# Genarate password

password = ''.join(random.sample(characters, length))

# Show the result

print(f"\n🧪 Your new password is: \n➡️ {password}\n")

# Bonus message

if length < 6:
print("⚠️ That password is short. Consider using at least 8 characters.")
elif length >= 12:
print("🛡️ Ultra strong! This one's a fortress.")
else:
print("👍 Looks like a decent password!")
