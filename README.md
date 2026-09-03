# System Process Logger with Scheduling

A lightweight System Process Monitoring and Logging System developed in Python. This project uses `psutil` to collect information about currently running processes and `schedule` to execute process scans automatically at a user-defined time interval.

## 🚀 Features

- 🔍 Detects currently running processes
- 🆔 Displays Process ID (PID)
- 📌 Displays process name
- 👤 Displays username
- 🔄 Displays process status
- ⚡ Displays CPU usage
- 💾 Displays memory usage
- 🕒 Displays process start time
- ⏰ Supports scheduled process monitoring
- 🛡️ Handles `NoSuchProcess`, `AccessDenied`, and `ZombieProcess` exceptions
- 💻 Supports command-line arguments

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| psutil | Process and system information |
| schedule | Task scheduling |
| datetime | Process start-time formatting |
| sys | Command-line arguments |
| time | Scheduler loop |

## 📂 Project Structure

```text
System-Process-Logger/
│
├── ProcInfo.py
└── README.md
```

## ⚙️ How It Works

The application scans all available system processes using `psutil.process_iter()` and collects:

- Process ID
- Process Name
- Username
- Status
- CPU Usage
- Memory Usage
- Start Time

The collected information is then displayed in the terminal.

The application can also schedule the monitoring function at a user-defined interval.

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/System-Process-Logger.git
cd System-Process-Logger
```

### 2. Install Dependencies

```bash
pip install psutil schedule
```

## ▶️ Running the Project

Run the application by providing the monitoring interval in minutes:

```bash
python ProcInfo.py 1
```

The above command schedules process monitoring every **1 minute**.

For example:

```bash
python ProcInfo.py 5
```

This schedules monitoring every **5 minutes**.

## 🆘 Help

To display the available features:

```bash
python ProcInfo.py --h
```

or:

```bash
python ProcInfo.py --H
```

The application displays:

```text
1. Running Processes
2. Creates Log File
3. Scheduler Support
```

## 📖 Usage

To display usage instructions:

```bash
python ProcInfo.py --u
```

or:

```bash
python ProcInfo.py --U
```

Example:

```text
Usage :
python ProcInfo.py Time

Example :
python ProcInfo.py 1
```

## 📋 Example Output

```text
------------------------------------------------------------
Running Process Information
------------------------------------------------------------
PID           : 1234
Process Name  : chrome.exe
User Name     : User
Status        : running
CPU Usage     : 2.50 %
Memory Usage  : 1.20 %
Start Time    : 03-09-2026 21:15:30
------------------------------------------------------------
```

## 🛡️ Exception Handling

During process scanning, some processes may terminate or deny access to their information.

The application handles:

```python
psutil.NoSuchProcess
psutil.AccessDenied
psutil.ZombieProcess
```

This prevents an individual inaccessible process from stopping the complete monitoring application.

## 🔄 Application Flow

```text
Start Application
       │
       ▼
Read Command-Line Argument
       │
       ▼
Validate Time Interval
       │
       ▼
Start Scheduler
       │
       ▼
ProcessScan()
       │
       ▼
Scan Running Processes
       │
       ▼
Collect Process Information
       │
       ├── PID
       ├── Name
       ├── Username
       ├── Status
       ├── CPU Usage
       ├── Memory Usage
       └── Start Time
       │
       ▼
Display Process Information
       │
       ▼
Wait for Next Scheduled Run
       │
       └──────────────► Repeat
```

## 🎯 Use Cases

- System process monitoring
- Learning Python system programming
- Understanding process management
- Monitoring CPU and memory usage
- Learning command-line applications
- Learning task scheduling in Python
- Building a foundation for system-monitoring applications

## 🔮 Future Enhancements

Possible improvements include:

- Persistent log-file generation
- CSV/JSON report generation
- Email notifications
- High CPU/memory alerts
- Process start/stop notifications
- Database storage
- Graphical monitoring dashboard
- Process filtering and searching
- GUI-based monitoring

## 👨‍💻 Author

**Sahil Ashok Dhole**

MSc Computer Science Student

Course : Python Automation & Machine Learning

Project : System Process Logger with Scheduling

GitHub: `github.com/sahildhole09`

LinkedIn: `https://www.linkedin.com/in/sahil-dhole-9b606138a`
"# SystemProcessLogger" 
