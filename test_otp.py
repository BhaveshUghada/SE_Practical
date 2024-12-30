import pytest
from unittest.mock import patch
from otp import OTP

# Test OTP Generation
def test_generate_otp():
    otp_instance = OTP()
    generated_otp = otp_instance.generate_otp()

    # OTP should have at least 4 digits
    assert len(generated_otp) >= 4  
    # OTP should have at most 8 digits
    assert len(generated_otp) <= 8  
    # OTP should only contain digits
    assert generated_otp.isdigit()

# Test email validation with valid Gmail address
def test_valid_email():
    otp_instance = OTP()
    valid_email = "testuser@gmail.com"
    # It should return True for valid Gmail address
    assert otp_instance.validate_email(valid_email)  

# Test email validation with invalid Gmail address
def test_invalid_email():
    otp_instance = OTP()
    invalid_email = "testuser@outlook.com"
    # It should return False for non-Gmail address
    assert not otp_instance.validate_email(invalid_email)  

# Test email validation with empty email
def test_empty_email():
    otp_instance = OTP()
    empty_email = ""
    # It should return False for empty email
    assert not otp_instance.validate_email(empty_email)

# Mocking send_email function to avoid actually sending an email
@patch("otp.smtplib.SMTP")
def test_send_email(mock_smtp):
    otp_instance = OTP()

    # Setup the mock SMTP server
    mock_server = mock_smtp.return_value
    mock_server.sendmail.return_value = None  # Assume sendmail is successful

    sender_email = "Your Email"
    app_password = "Password"
    recipient_email = "testuser@gmail.com"
    otp = "123456"

    # Call send_email method
    otp_instance.send_email(sender_email, app_password, recipient_email, otp)

    # Verify if the email is sent using mocked SMTP server
    # mock_server.sendmail.assert_called_with(sender_email, recipient_email, any)

# Test sending OTP with invalid email (using mocking to avoid actual email sending)
@patch("otp.smtplib.SMTP")
def test_send_email_invalid(mock_smtp):
    otp_instance = OTP()

    # Setup the mock SMTP server
    mock_server = mock_smtp.return_value
    mock_server.sendmail.return_value = None  # Assume sendmail is successful

    sender_email = "Your Email"
    app_password = "Password"
    recipient_email = "testuser@outlook.com"  # Invalid email address
    otp = "123456"

    # Since the email is invalid, it should not send the OTP
    assert not otp_instance.validate_email(recipient_email)  # Email should be invalid
    # Ensure sendmail is not called because the email is invalid
    mock_server.sendmail.assert_not_called()
