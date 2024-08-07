import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

contacts = pd.read_csv('hr_contacts.csv')  # Make sure your CSV name and file path is correct

# Email account credentials
email_address = 'your_email_id'
email_password = 'your_email_app_password'  # Use your App Password here if using 2FA (Check the README for more info)

# SMTP setup for Gmail (adjust if you're using another provider)
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Email content
subject = "Your Subject Here"
body_template = """
Hi [Name],

Your message here.
"""

# Setup the server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(email_address, email_password)

# Send email to each contact considering the csv has a column 'Email' and 'Name' (Change the column name if different)
for index, contact in contacts.iterrows():
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = contact['Email']
    msg['Subject'] = subject

    # If you csv has the full name then to get the first name only, put the code below
    # contact['Name'] = contact['Name'].split()[0]
    
    # Personalize the message
    personalized_body = body_template.replace("[Name]", contact.get('Name', 'there'))
    msg.attach(MIMEText(personalized_body, 'plain'))
    
    try:
        server.send_message(msg)
        print(f"Email sent to {contact['Email']}")
    except Exception as e:
        print(f"Failed to send email to {contact['Email']}: {e}")

server.quit()