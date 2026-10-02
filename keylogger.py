#Import libraries
#Get user, hash, directory, network information
#Output to cmd
#Save information to .txt file

import os
import psutil
import platform
import socket
from pathlib import Path

#Getting system information
info = platform.uname()
print(f"OS/System: {info.system}")
print(f"Release:   {info.release}")
print(f"Version:   {info.version}")
print(f"Machine:   {info.machine}")

#Getting network information
def get_private_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        private_ip = s.getsockname()[0]
    except Exception:
        private_ip = "127.0.0.1"
    finally:
        s.close()
    return private_ip

print("Your Private IP Address:", get_private_ip())

#Getting username and directory
print(f"Username:  {os.getlogin()}")
print(f"Username:  {os.environ.get('USERNAME') or os.environ.get('USER')}")
print(f"Path: {Path.cwd()}")


