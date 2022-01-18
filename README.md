# monitor_running
Monitor script and restart if it is unresponsive

The running script writes txt file epoch time and unix PID number,

The monitor script is read time from file and give a decision to restart.

Usage:
import it from unresponsive program or put following code inside


    def write_time_and_pid:
        #prevent to freeze
        file = open("monitor_time.txt", "w")
        file.write(str(time.time()) + "|" + pid)
        print(time.time())
        file.close()
    
 
 call it from desired interval
 
 
 also run monitor.py in same directory to read monitor_time.txt
