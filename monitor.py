import time, commands, os

# Write time and PID to txt file and read it from monitor file if timedelta is bigger than
# desired range kill current process and start new one

try:
    file = open("monitor_time.txt")
except:
    file = open("monitor_time.txt","w")
    file.write(str(time.time()) + "|" + pid)
    print(time.time())
    file.close()

def write_time_and_pid:
    #prevent to freeze
    file = open("monitor_time.txt", "w")
    file.write(str(time.time()) + "|" + str(os.getpid()))
    print(time.time())
    file.close()

while 1:
    time.sleep(30)
    try:
        file = open("monitor_time.txt")
        timestamp, pid = file.read().split("|")
        file.close()
        print(timestamp, pid)
    except Exception as e:
        print (e)
    print(time.time() - float(timestamp))
    if time.time() - float(timestamp)>123:
        print(commands.getoutput("kill -9 " + pid))
        print (os.system("script.py &"))





