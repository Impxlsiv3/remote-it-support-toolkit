import platform
import socket

def get_system_info():
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Node: {platform.node()}")
    print(f"Processor: {platform.processor()}")
    print(f"IP Address: {socket.gethostbyname(socket.gethostname())}")

if __name__ == "__main__":
    get_system_info()
