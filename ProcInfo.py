import psutil
import sys
import time
import datetime
import schedule

def ProcessScan():

    listprocess = []

    for proc in psutil.process_iter():

        try:
            info = proc.as_dict(attrs=["pid","name","username","status"])

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["start_time"] = datetime.datetime.fromtimestamp(proc.create_time()).strftime("%d-%m-%Y %H:%M:%S")

            listprocess.append(info)

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    return listprocess

def DisplayProcess():
    Border = "-"*60

    Data = ProcessScan()

    print(Border)
    print("Running Process Information")
    print(Border)

    for info in Data:

        print("PID           :",info["pid"])
        print("Process Name  :",info["name"])
        print("User Name     :",info["username"])
        print("Status        :",info["status"])
        print("CPU Usage     : %.2f %%"%info["cpu_percent"])
        print("Memory Usage  : %.2f %%"%info["memory_percent"])
        print("Start Time    : %s\n"%info["start_time"])
        print(Border)

    print("---------------------- Processes Ended ---------------------")
    print(Border)

def PlatformSurvillance():
    DisplayProcess()

def main():

    Border="-"*60

    print(Border)
    print("--------------- Process Monitoring System ------------------")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This application displays :")
            print("1. Running Processes")
            print("2. Creates Log File")
            print("3. Scheduler Support")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Usage :")
            print("python ProcInfo.py Time")
            print("Example :")
            print("python ProcInfo.py 1")
        else:
            print("Scheduler Started Successfully")
            print("Press CTRL+C to Stop")

            schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillance)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of Arguments")

if __name__=="__main__":
    main()