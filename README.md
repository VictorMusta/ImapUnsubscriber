
# IMAP Unsubscriber Script

## Introduction

This script automates the process of unsubscribing from unwanted emails by searching for "unsubscribe" links in your inbox and following them. It is designed to work with Gmail and uses an application-specific password for secure access.


## Security Warning

**Important**: Be cautious when using this script. Malicious websites may use unsubscribe links to distribute malware or ransomware. Verify the legitimacy of unsubscribe links before running the script. This script does not perform any verification and will follow links blindly.

## Disclaimer

Use this script at your own risk. The author is not responsible for any damage or data loss resulting from its use.

## Environmental Impact

Sending emails has a carbon footprint. For example, an email with a 3MB attachment sent to 10 people can generate approximately 570g of CO2. Reducing the number of unwanted emails can help lower your carbon footprint.

### Tips to Reduce Email CO2 Emissions

1. **Reduce the size of attachments**.
2. **Use download links instead of attachments**.
3. **Use instant messaging services**.
4. **Use file transfer services**.
5. **Unsubscribe from unnecessary newsletters**.

## Prerequisites

- Python 3.x
- `imaplib`, `email`, `BeautifulSoup`, and `requests` libraries

## Setup

1. **Generate an Application-Specific Password**:
   - Go to your Google Account.
   - Navigate to the "Security" section.
   - Under "Signing in to Google", select "App passwords".
   - Follow the instructions to generate an application-specific password.

2. **Install Required Libraries**:
   ```bash
   pip install beautifulsoup4 requests
    ```

3. **Configure the Script**:
   - Replace the placeholders `your_email` and `your_password` in the script with your email address and the application-specific password.

## Usage

Run the script to automatically unsubscribe from emails containing "unsubscribe" links.

```bash
python unsubscriber.py
```




