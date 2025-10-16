import random

otp = random.randint(000000, 999999)
username=input("Username: ")
print("Hello..!",username)
print("Here is your 6 digit OTP for login:",otp)
password=input("Enter the otp to login:")
if password==str(otp):
    print("Login successful!")
else:
    password!=str(otp)
    print("Login failed!")