import smtplib,os
from dotenv import load_dotenv

load_dotenv()


# try:
#     print("Attempting to connect to Gmail on Port 465...")
#     server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     server.login('odidikaanthony02@gmail.com', os.getenv('MAIL_PASSWORD'))
#     print("SUCCESS! Your network allows email connections.")
#     server.quit()
# except Exception as e:
#     print(f"FAILED: {e}")
import requests

# 1. Paste your actual Brevo API key here (just for this test)
API_KEY = os.getenv(('BREVO_API_KEY'))

# 2. Put the exact email you used to sign up for Brevo here
YOUR_EMAIL = "odidikaanthony02@gmail.com"

api_url = "https://api.brevo.com/v3/smtp/email"
headers = {
    "accept": "application/json",
    "api-key": API_KEY,
    "content-type": "application/json"
}

payload = {
    "sender": {"name": "My Website", "email": YOUR_EMAIL},
    "to":[{"email": YOUR_EMAIL, "name": "Me"}],
    "subject": "Testing Brevo API",
    "htmlContent": "<p>If you see this, Brevo works perfectly!</p>"
}

print("Sending request to Brevo...")
response = requests.post(api_url, json=payload, headers=headers)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

