import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

# Email configuration
smtp_server = "smtp.example.com"  # Replace with your SMTP server address
smtp_port = 587
sender_email = "your-email@example.com"  # Replace with your email address
receiver_email = "recipient@example.com"  # Replace with the recipient's email address
subject = "Test Email"
message_text = "This is a test email sent from a Raspberry Pi."

# Prompt for the email password securely
sender_password = getpass("Enter your email password: ")

# Create a MIMEText object for the email body
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(message_text, "plain"))

# Create an SMTP connection
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")

    # Close the SMTP connection
    server.quit()

except Exception as e:
    print("Error: " + str(e))
