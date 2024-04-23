import re

class SMSBlocker:
    def __init__(self, blocked_numbers):
        self.blocked_numbers = blocked_numbers

    def block_sms(self, sender_number, message):
        if sender_number in self.blocked_numbers:
            print(f"SMS from {sender_number} blocked: {message}")
        else:
            print(f"SMS from {sender_number} allowed: {message}")

# Function to get user input for blocked numbers
def get_blocked_numbers():
    blocked_numbers = []
    while True:
        number = input("Enter a number to block (or 'done' to finish): ")
        if number.lower() == 'done':
            break
        blocked_numbers.append(number)
    return blocked_numbers

# Get blocked numbers from the user
blocked_numbers = get_blocked_numbers()

# Create an instance of SMSBlocker
sms_blocker = SMSBlocker(blocked_numbers)

# Example SMS messages
sms_messages = [
    {"sender_number": "123456789", "message": "Hello there!"},
    {"sender_number": "987654321", "message": "This is a blocked message."},
    {"sender_number": "999888777", "message": "Another message."},
]

# Check and block SMS messages
for sms in sms_messages:
    sender_number = sms["sender_number"]
    message = sms["message"]
    sms_blocker.block_sms(sender_number, message)
