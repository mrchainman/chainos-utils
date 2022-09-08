from imapclient import IMAPClient

username = ""
password = ""
imap_server = ""

client = IMAPClient(imap_server)
client.login(username, password)
