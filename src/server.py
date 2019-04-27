import subprocess
import os
import time
import sys
import serial

def checkCurl():
    # check if package curl is available
    check = subprocess.call(['which', 'curl'], stdout=open(os.devnull,"wb"))

    if check == 0:
        return True
    else:
        return False

def get_ip():
    # run curl on the adress icanhazip.com for ip
    process_args = ['curl', 'icanhazip.com']
    result = subprocess.Popen(process_args, stdout=subprocess.PIPE, stderr=open(os.devnull, "wb"))
    ipbin = result.communicate()[0]
    ip = ipbin.decode("utf-8")
    ip = ip[:-1]

    return ip

def checkArduino():
    try:
        arduino = serial.Serial(path, baud, timeout=10)
    except Exception as e:
        return False
    print("arduino connected")
    time.sleep(2)
    ip = get_ip()
    arduino.write(get_ip().encode('ascii'))
    time.sleep(1)
    
    # loop untill arduino is disconnected
    try:
        while arduino.read():
            time.sleep(2)
    except Exception as e:
        print("arduino disconnected")
        arduino.close()
        return False

    print("arduino disconnected")
    arduino.close()
    return False


def main():
    if not checkCurl():
        print("Error, curl not installed");
        sys.exit(1)
    
    while True:
        arduino = checkArduino()
        time.sleep(1)

if __name__ == '__main__':
    main()
