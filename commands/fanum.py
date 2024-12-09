import psutil
import time
def handle_fanum():
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            proc.cpu_percent(interval=0)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    # allow for a second to pass to get the CPU usage
    time.sleep(1)
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_info = proc.info
            process_info['cpu_percent'] = proc.cpu_percent(interval=0)
            processes.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
    top_processes = processes[:20]
    print(f"{'PID':<10} {'Process Name':<25} {'CPU Usage (%)':<15}")
    print("="*50)
    for process in top_processes:
        print(f"{process['pid']:<10} {process['name']:<25} {process['cpu_percent']:<15.2f}")

