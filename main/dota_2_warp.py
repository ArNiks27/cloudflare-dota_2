import psutil
import subprocess
import time
import os

DOTA_PROCESS = "dota2.exe"
WARP_CLI_PATH = r"C:\Program Files\Cloudflare\Cloudflare WARP\warp-cli.exe"

def is_dota_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and proc.info['name'].lower() == DOTA_PROCESS:
            return True
    return False

def disconnect_warp():
    try:
        subprocess.run([WARP_CLI_PATH, "disconnect"], check=True, capture_output=True)
    except Exception:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == "warp-taskbar.exe":
                proc.terminate()

def main():
    while True:
        print("ищу...")
        if is_dota_running():
            disconnect_warp()
        time.sleep(5) 

if __name__ == "__main__":
    main()
