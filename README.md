# Download Raspian
https://downloads.raspberrypi.org/NOOBS_latest


# IP-Helpers

#### Prepare folder location

```
   cd Desktop 
```

#### Clone repository from GitHub

```
   git clone https://github.com/eco-view/IP-Helpers.git
```

#### Navigate to directory

```
   cd Desktop/IP-Helpers
```

#### Install necessary Python modules

```
   pip3 install -r requirements.txt 
```

#### OPTIONAL: Check for installed libraries

```
   pip3 freeze
```
#### Edit files with your own credentials

#### ../COMPUTERstatic/getgmail.py
```python
15 mail.login('<yourEmail>@gmail.com', '<password>')
```

#### ../PIstatic/ipemail.py
```python
8  from_address = '<yourEmail>@gmail.com'
9  to_address = '<yourEmail>@gmail.com'
10 subject = 'LAST IP'
11 username = '<yourUsername>'
12 password = '<password>'
```
