import os

def clear_cache():
    os.system("sudo apt-get clean")
    os.system("sudo rm -rf ~/.cache/thumbnails/*")
    print("System cache cleaned.")

if __name__ == "__main__":
    clear_cache()
