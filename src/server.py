import subprocess
import os

def checkCurl():
    check = subprocess.call(['which', 'curl'], stdout=open(os.devnull,"wb"))

    if check == 0:
        return True
    else:
        return False

def get_ip():
    process_args = ['curl', 'icanhazip.com']
    result = subprocess.Popen(process_args, stdout=subprocess.PIPE, stderr=open(os.devnull, "wb"))
    ipbin = result.communicate()[0]
    ip = ipbin.decode("utf-8")
    ip = ip[:-1]

    return ip
