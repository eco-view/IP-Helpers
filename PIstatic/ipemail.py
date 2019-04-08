from urllib.request import urlopen
import re
import smtplib
import socket
import os

# setup login credentials
from_address = '<yourEmail>@gmail.com'
to_address = '<yourEmail>@gmail.com'
subject = 'LAST IP'
username = '<yourUsername>'
password = '<password>'

# set Relative Path
package_dir = os.path.dirname(os.path.abspath(__file__))
public_file = os.path.join(package_dir,'last_ip.txt')
local_file = os.path.join(package_dir,'last_local.txt')
print("Directory: ", package_dir)
print("Public path: ", public_file)
print("Local path: ", local_file)

# how we get our ip address
url = 'http://checkip.dyndns.org'
print("Our chosen IP address service is: ", url)

# Open up the url and read the contents
request = urlopen(url).read().decode('utf-8')
# We extract the IP
ourIP = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", request)
ourIP = ''.join(ourIP)
print("Public IP address: ", ourIP)


# set execFlag
execFlag = False

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        localIP = s.getsockname()[0]
    except:
        localIP = '127.0.0.1'
    finally:
        s.close()
    return str(localIP)


def send_email(ourIP, localIP):
    # Body of the email
    hostname = socket.gethostname()
    # body_tip = 'startMSG'
    # body_text1 = ourIP + ' is our public IP address.'
    # body_text2 = localIP + ' is our local IP.'
    # body_text3 = hostname + ' is our hostname.'
    # body_text_cap = 'endMSG'
    body_text = {"publicIP": ourIP, "localIP": localIP, "hostname": hostname}
    msg = '\r\n'.join(['To: %s' % to_address,
                        'From: %s' % from_address,
                        'Subject: %s' % subject,
                        '', '{' + str(body_text) + '}'])
                        # '', body_text1, body_text2, body_text3, body_text_cap])
    # # actually send email
    # print(body_text)
    # print(msg)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls() # our security for transmission of creds
    server.login(username, password)
    server.sendmail(from_address, to_address, msg)
    server.quit()
    print("Our email has been sent!")


localIP = get_local_ip()
print("Local IP address: ", localIP)


# Open up last_local.txt, extract contents
with open(local_file, 'rt') as last_local:
    last_local = last_local.read() # Read the text file

# Check to see if local IP has changed
if last_local == localIP:
    print("Our local IP address has not changed.")
else:
    print("We have a new local IP address.")
    with open(local_file, 'wt') as last_local:
        last_local.write(localIP)
    print("We have written the new local IP address to file.")
    execFlag = True


# Open up last_ip.txt, extract contents
with open(public_file, 'rt') as last_ip:
    last_ip = last_ip.read() # Read the text file

# Check to see if IP has changed
if last_ip == ourIP:
    print("Our public IP address has not changed.")
else:
    print("We have a new public IP address.")
    with open(public_file, 'wt') as last_ip:
        last_ip.write(ourIP)
    print("We have written the new IP address to text file.")
    execFlag = True


if execFlag is True:
    send_email(ourIP, localIP)
else:
    pass
