# Cold Email Sender

This Python script automates the process of sending personalized cold emails to a list of contacts. By reading contact details from a CSV file, it customizes each email's content and sends it using the SMTP protocol.

## Features

- **Automated Emails**: Send emails to multiple contacts in one go.
- **Personalized Content**: Customize the email body for each recipient.
- **Secure Authentication**: Uses secure methods to authenticate with your email provider.

## Prerequisites

- Python 3.x
- An email account with SMTP access (e.g., Gmail)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/SiddheshSonar/Cold-Email-Sender.git
   cd cold-email-sender
    ```

2. **Install the Required Packages:**

Use pip to install the required packages:

   ```bash
   pip install pandas
   ```

## Setup

1. Csv File:
    - Ensure you have a CSV file named hr_contacts.csv in the same directory as the script. The CSV should have the following columns:
        - `name`: The recipient's name.
        - `email`: The recipient's email address.
        
2. Email Credentials:
    - Update the script with your email credentials. If using Gmail, ensure that 2-Step Verification is enabled and use an App Password for authentication. To enable 2-Step Verification and generate an App Password, follow the instructions [here](https://support.google.com/accounts/answer/185833?hl=en).

3. SMTP Configuration:
    - By default, the script uses Gmail's SMTP server. Update these settings if using a different provider:
        ```bash
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        ```

4. Customize Email Content:
    - Update the subject and body_template variables in the script to personalize your email's subject line and body.

## Notes
1. Email Security: Ensure that your credentials are not hardcoded in publicly accessible code. Consider using environment variables or a secure vault.

2. Email Limits: Be aware of your email provider's sending limits to avoid being flagged as spam.

3. Testing: Before sending emails to a large list, test the script with a small number of contacts to ensure it works as expected.

4. This project uses the following Python libraries:
    - [pandas](https://pandas.pydata.org/) for handling CSV files
    - [smtplib](https://docs.python.org/3/library/smtplib.html) for sending emails
    - [email](https://docs.python.org/3/library/email.html) for composing email messages