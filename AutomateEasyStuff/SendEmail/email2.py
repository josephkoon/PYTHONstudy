#IMAP for retrieving emails

import imapclient

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

imapObj.login(' jospehandrewkoon@gmail.com ', '530165Jk!')


