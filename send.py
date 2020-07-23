from inbox import Inbox
from smtplib import SMTP

inbox = Inbox()

SMTP_HOST = 'localhost:1025'
SMTP_USERNAME = 'username'
SMTP_PASSWORD = 'password'
body='hi'
@inbox.collate
def handle(to, sender, body):
    """
    Forward a message via an authenticated SMTP connection with
    starttls.
    """
    conn = SMTP(SMTP_HOST, 25, 'localhost')
	
    conn.starttls()
    conn.ehlo_or_helo_if_needed()
    conn.login(SMTP_USERNAME, SMTP_PASSWORD)
    conn.sendmail(sender, to, body)
	
    conn.quit()

inbox.serve(address='localhost', port=1025)