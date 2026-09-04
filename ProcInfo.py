import psutil
import sys
import os
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

def CreateLog(FolderName):
    Border = "-"*60

    Ret = False

    Ret = os.path.exists(FolderName)
    if(Ret == False):
        os.mkdir(FolderName)
        print("Directory created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"ProcessLog_%s.log"%timestamp)

    fobj = open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("Process Information System\n")
    fobj.write("Log Created : "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    Data = ProcessScan()

    for info in Data:

        fobj.write("PID            : %s\n"%info["pid"])
        fobj.write("Process Name   : %s\n"%info["name"])
        fobj.write("User Name      : %s\n"%info["username"])
        fobj.write("Status         : %s\n"%info["status"])
        fobj.write("CPU Usage      : %.2f %%\n"%info["cpu_percent"])
        fobj.write("Memory Usage   : %.2f %%\n"%info["memory_percent"])
        fobj.write("Start Time     : %s\n"%info["start_time"])
        fobj.write(Border+"\n")

    fobj.write("Process Information Finish\n")
    fobj.write(Border+"\n")

    fobj.close()

    print("Log file created :",FileName)

def PlatformSurvillance(FolderName):
    CreateLog(FolderName)

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
            print("python ProcInfo.py Time FolderName")
            print("Example :")
            print("python ProcInfo.py 1 ProcessLog")

        else:
            print("Invalid Argument")

    elif(len(sys.argv)==3):     
        print("Scheduler Started Successfully")
        print("Press CTRL+C to Stop")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillance,sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of Arguments")

if __name__=="__main__":
    main()