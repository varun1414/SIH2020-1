import imaplib
import pprint

imap_host = 'localhost:1025'
imap_user = 'bro@localhost'
imap_pass = 'password'

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login to server
imap.login(imap_user, imap_pass)

#imap.select('Inbox')

tmp, data = imap.search(None, 'ALL')
for num in data[0].split():
	tmp, data = imap.fetch(num, '(RFC822)')
	print('Message: {0}\n'.format(num))
	pprint.pprint(data[0][1])
	break
imap.close()
