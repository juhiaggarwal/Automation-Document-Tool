import random

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(to_email, otp):
    print(f"Sending OTP {otp} to {to_email}")  # Replace with actual email sending logic