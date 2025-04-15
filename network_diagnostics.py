import subprocess

def run_diagnostics():
    print("Pinging 8.8.8.8...")
    result = subprocess.run(["ping", "-c", "4", "8.8.8.8"], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    run_diagnostics()
