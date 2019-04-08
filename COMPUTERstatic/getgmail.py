# # LOGIN
import imaplib
import email
import re
import ast
import os

# FILE PATH
package_dir = os.path.dirname(os.path.abspath(__file__))
save_string = os.path.join(package_dir,'piAddress.txt')
# print(save_string)

mail = imaplib.IMAP4_SSL('imap.gmail.com')
# imaplib module implements connection based on IMAPv4 protocol
mail.login('<yourEmail>@gmail.com', '<password>')
# >> ('OK', [username at gmail.com Vineet authenticated (Success)'])

# SELECTING A LABEL
mail.list() # Lists all labels in GMail
mail.select('inbox') # Connected to inbox.
# print("HOOK...")

# SEARCHING THRU INBOX
result, data = mail.uid('search', None, "ALL")
# search and return uids instead
i = len(data[0].split()) # data[0] is a space separate string
for x in range(i):
    latest_email_uid = data[0].split()[x] # unique ids wrt label selected
    mail.uid('search', None, '(HEADER Subject "LAST IP")')
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    # fetch the email body (RFC822) for the given ID
    # print(result)
    # print(email_data)
    # print(email_data.decode('utf-8'))
    raw_email = email_data[0][1]


# PARSING RAW EMAIL (( raw means BYTES ))
email_message = raw_email.decode('utf-8')
# Extract Dictionary
isolated_info = re.findall("(?<={)(.*)(?=})", email_message)
isolated_info = isolated_info[0]
address_dict = ast.literal_eval(isolated_info)
# print(address_dict)

# # converts byte literal to string removing b''
# email_message = email.message_from_string(raw_email_string)
# this will loop through all the available multiparts in mail

# SAVE TO FILE
# print(save_string)
# location in relative folder
myfile = open(save_string, 'w')
myfile.write(str(address_dict))
myfile.close()

# print("...EOF")
