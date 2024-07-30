import imaplib
import email
from email.header import decode_header

# Your Gmail credentials
username = "your_email@gmail.com"
password = "password" #better to use app password

def delete_all_emails(username, password):
    # Connect to the Gmail IMAP server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    
    # Login to your account
    mail.login(username, password)
    
    # Select the mailbox you want to delete in
    # if you want SPAM, use "INBOX.SPAM"
    mail.select("inbox")

    # Search for all emails in the selected mailbox
    status, messages = mail.search(None, "ALL")
    if status != "OK":
        print("No messages found!")
        return

    # Convert messages to a list of email IDs
    email_ids = messages[0].split()
    print(f"Found {len(email_ids)} emails. Deleting...")

    # Delete all emails
    for email_id in email_ids:
        mail.store(email_id, "+FLAGS", "\\Deleted")
    
    # Permanently remove deleted emails
    mail.expunge()
    
    # Close the mailbox
    mail.close()
    
    # Logout from the server
    mail.logout()

    print("All emails deleted.")

if __name__ == "__main__":
    delete_all_emails(username, password)
