''' This Python project provides a fun and interactive way to translate messages into a secret code language and decode them back to the original message. 
The coding process involves shifting letters and adding random characters for security, while the decoding reverses these operations based on specific rules. 
The program supports two modes: "coding" for encryption and "decoding" for decryption, making it an excellent introduction to basic cryptography concepts. 
Perfect for beginners who want to explore string manipulation and randomness in Python. '''

import string #for using string.ascii_letters
import random #for using random.choice()

# Function to get valid input for coding or decoding
def get_valid_ip():
    while True:
        # Prompt user for input
        ip = input()
        # Check if the input is 'C' for coding or 'D' for decoding
        if(ip.capitalize() == 'C' or ip.capitalize() == 'D'):
            return ip  # Return valid input
        else:
            # If invalid input, prompt the user again
            print("Invalid input, Try again!!")

# Prompt the user to choose between coding or decoding
print("Do you want to code or decode??\nEnter 'C' for coding and 'D' for decoding.")
ipchoice = get_valid_ip().capitalize()  # Get and store the valid input (either 'C' or 'D')

# If the user chooses to code a message
if(ipchoice == 'C'):
    msg = input("Enter your message that you want to code:\n")  # Get the message to code
    
    # If the message length is greater than or equal to 3
    if(len(msg) >= 3):
        # Split the message into two parts: the first character and the rest
        msg1 = msg[1:len(msg)]  # Message excluding the first character
        msg2 = msg[0]  # First character of the message
        
        # Randomly generate 6 letters to append to the coded message
        l1 = random.choice(string.ascii_letters)
        l2 = random.choice(string.ascii_letters)
        l3 = random.choice(string.ascii_letters)
        l4 = random.choice(string.ascii_letters)
        l5 = random.choice(string.ascii_letters)
        l6 = random.choice(string.ascii_letters)
        
        # Create the coded message by combining the random letters with the split message
        coded_msg = l1 + l2 + l3 + msg1 + msg2 + l4 + l5 + l6
        
        # Output the final coded message
        print(f"Your message is successfully coded as: '{coded_msg}'")
    
    # If the message length is lesser than 3
    else:
        # Reverse the message and append the first character at the end
        coded_msg = msg[len(msg):0:-1] + msg[0]
        
        # Output the final coded message
        print(f"Your message is successfully coded as: '{coded_msg}'")
    
# If the user chooses to decode a message
else:
     # Prompt the user to input the message they want to decode
    msg = input("Enter your message that you want to decode:\n")
    
    # If the message length is less than or equal to 3
    if(len(msg) < 3):
        # Reverse the message (excluding the first character) and append the first character at the end
        decoded_msg = msg[len(msg):0:-1] + msg[0]
        
        # Output the final decoded message
        print(f"Your message is successfully decoded as: '{decoded_msg}'")
    
    # If the message length is greater than 3
    else:
        # Decode the message by removing the first 3 and last 3 random characters
        # msg[len(msg)-4] is the first letter of the original message
        # msg[3:(len(msg)-4)] is the middle part of the original message
        decoded_msg = msg[len(msg)-4] + msg[3:(len(msg)-4)]
        
        # Output the final decoded message
        print(f"Your message is successfully decoded as: '{decoded_msg}'")
