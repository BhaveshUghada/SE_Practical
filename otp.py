import random
import smtplib
import re  # Import regex module
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class OTP:
    def __init__(self):
        self.otp = None

    def generate_otp(self):
        """Generate a random OTP with 4 to 8 digits."""
        self.otp = str(random.randint(1000, 99999999))
        return self.otp

    def validate_email(self, email):
        """Validate Gmail address format using regex."""
        pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
        if re.match(pattern, email):
            return True
        else:
            print("Invalid email address. Please enter a valid Gmail address.")
            return False

    def send_email(self, sender_email, app_password, recipient_email, otp):
        """Send OTP to the provided email."""
        # Create email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = "Your One-Time Password (OTP)"
        body = f"Your OTP is: {otp}\n\nOTP sent successfully!!!!"
        message.attach(MIMEText(body, "plain"))

        try:
            # Connect to Gmail SMTP server
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Secure the connection
                server.login(sender_email, app_password)  # Authenticate
                server.sendmail(sender_email, recipient_email, message.as_string())
            print("OTP sent successfully!")
        except Exception as e:
            print(f"Failed to send OTP: {e}")

# Main program
if __name__ == "__main__":
    sender_email = "Your Email"
    app_password = "Password"  # Your App Password

    otp_instance = OTP()
    
    recipient_email = input("Enter your Gmail address: ")

    # Validate the recipient email
    if otp_instance.validate_email(recipient_email):
        # Generate and send OTP
        otp = otp_instance.generate_otp()
        print(f"Generated OTP: {otp}")  # Debug: Remove in production
        otp_instance.send_email(sender_email, app_password, recipient_email, otp)
    else:
        print("OTP not sent due to invalid email format.")
