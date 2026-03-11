import smtplib

try:
    print("Attempting to connect to Gmail on Port 465...")
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login('odidikaanthony02@gmail.com', 'ghyt mcvi ockp tqnv')
    print("SUCCESS! Your network allows email connections.")
    server.quit()
except Exception as e:
    print(f"FAILED: {e}")