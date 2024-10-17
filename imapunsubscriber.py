import imaplib
import email
from bs4 import BeautifulSoup
import requests

# Replace the values with your email address and password
# Warning: using your main password is not recommended for security reasons.

# For a Gmail address:
# I recommend creating an "application-specific password" on your Google account
# to avoid using your main password.
# To do this, go to https://myaccount.google.com/security-checkup
# click on "App passwords" in the "Signing in to Google" section.
# Create an app password for the "Other (custom name)" application.
# Use this app password to log in to your mailbox.
your_email = 'TEMPLATE'
your_password = 'TEMPLATE'

# WARNING: Many malicious websites use unsubscribe links to send malware/ransomware.
# Please use this script with caution and verify that the unsubscribe links are legitimate.
# This script will not verify them
# and will follow them blindly.
# It is recommended to manually verify the unsubscribe links before following them.

# Connect to the mailbox
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(your_email, your_password)
mail.select('inbox')

# Search for emails containing "unsubscribe"
status, messages = mail.search(None, '(BODY "unsubscribe")')

# Extract unsubscribe links
for num in messages[0].split():
    status, data = mail.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                soup = BeautifulSoup(part.get_payload(decode=True), 'html.parser')
                for link in soup.find_all('a', href=True):
                    if 'unsubscribe' in link['href']:
                        unsubscribe_link = link['href']
                        # Automate the unsubscription
                        response = requests.get(unsubscribe_link)
                        if response.status_code == 200:
                            print(f'Successfully unsubscribed from {unsubscribe_link}')
                        else:
                            print(f'Failed to unsubscribe from {unsubscribe_link}')

# Disconnect from the mailbox
mail.logout()
