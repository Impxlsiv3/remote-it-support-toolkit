import shutil
import os

def collect_logs(dest_folder="collected_logs"):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    log_paths = ["/var/log/syslog", "/var/log/auth.log"]
    for log in log_paths:
        if os.path.exists(log):
            shutil.copy(log, dest_folder)
            print(f"Copied {log}")
        else:
            print(f"Log not found: {log}")

if __name__ == "__main__":
    collect_logs()
