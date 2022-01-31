import smtplib
import ssl
from email.message import EmailMessage
from getpass import getpass

sender_email = input("Enter your email: ")
receiver_email = input("Enter receiver email: ")
subject = input("Enter message subject: ")
body = input("Enter your message here: ")

password = getpass("Enter your email password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email ...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Success!")

# Commentary
"""
Line 1-4:
    The appropriate modules required to get the program to run are imported.
    Line 1 is for the transfer protocol, line 2 for security, and line 3 to
    compose the email to be sent. Line 4 however, allows the us to input our
    email password securely. I used the PyCharm IDE in writing this code, and
    to get the getpass() module to work, I had to go to 'Edit Configurations'
    and then select 'Emulate terminal in output console' before running the
    program.
    
Line 6-9:
    Inputs from the user is collected using basic input() statements.

Line 11:
    The syntax here is a method from the getpass module. It accepts the arguments
    similar to that of the input() method. Without input however, it has a
    default output of 'Password: '.

Line 13-17:
    Line 13 instantiates the EmailMessage module imported, from which the input
    collected from the users in Line 6-9 are assigned to the appropriate methods
    to formulate a complete mail.

Line 19:
    This is syntax from initiating ssl.
    
Line 21-25:
    Line 21 is a basic print statement which signals to the user that the email
    is being sent. If successful, Line 25 prints. The block of code from line 22-24
    applies the syntax from the 'smtplib' module, which is the protocol for sending
    emails. Line 23 performs the login, and if successful, then line 25 sends the
    email based of the parameters passed to it.
"""