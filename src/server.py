import subprocess
import os
import time

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

def checkArduino():
    # check if arduino with client code is connected
    # returns whatever object for arduino on success

    # conditions
    # ...

    return False

def send_ip():
    # send ip to arduino
    # return result

    return False

def handleArduino(ard):
    # get ip, send to arduino
    # return once disconnected 

def main():
    while True:
        res = checkArduino()
        if res:
            handleArduin(res)
        else:
            # might change this later depending on how usb works
            time.sleep(4)
        


