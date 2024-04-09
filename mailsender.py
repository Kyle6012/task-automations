import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender's email credentials
sender_email = input ("your_email@example.com: ")
password = input("your_password: ")

# Read recipient email addresses from a CSV file named "recipients.csv"
with open('recipients.csv', 'r') as file:
	reader = csv.reader(file)
	recipients = [row[0] for row in reader]

# Compose the email message
subject = input("Your subject : ")
message = ""
while True:
	line = input("Your message to the recipients: ")
	if line == "":
		break
	message += line + "\n"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587

try: 
	server = smtplib.SMTP(smtp_server, smtp_port)
	server.ehlo()
	server.starttls()
	server.login(sender_email, password) 

# Send the email to each recipient 
	for recipient_email in recipients: 
		msg['To'] = recipient_email 
		server.sendmail(sender_email, recipient_email, msg.as_string()) 
		print(f"Email sent to: {recipient_email}") 
finally:
# Close the connection to the SMTP server
	server.quit()

print("All emails sent successfully!")



