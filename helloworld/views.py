# Importing the render function from the django.shortcuts module.
from django.shortcuts import render
import socket
# Importing the time module.
import time
# Importing the datetime module.
import datetime
# Importing the pytz module.
import pytz

def hello(request):
    # Getting the hostname of the machine.
    hostname = socket.gethostname()
    # Getting the IP address of the machine.
    ip = socket.gethostbyname(hostname)
    # Getting the current time in UTC.
    current_time = datetime.datetime.now(pytz.utc)
    # Setting the timezone to India.
    india = pytz.timezone("Asia/Kolkata")
    # Converting the time from UTC to IST.
    current_time = current_time.astimezone(india)
    # Returning the response to the browser.
    return render(request, 'hello.html', {'hostname': hostname, 'ip': ip, 'current_time': current_time.strftime("%Y-%m-%d %H:%M:%S")})

