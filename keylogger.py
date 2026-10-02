#Import libraries
#Get user, hash, directory, network information
#Output to cmd
#Save information to .txt file

import os
import platform
import socket
from pathlib import Path

# Added libraries
import hashlib
from datetime import datetime

# Old implementation
# import tkinter as tk


#Getting system information
info = platform.uname()
print(f"OS/System: {info.system}")
print(f"Release:   {info.release}")
print(f"Version:   {info.version}")
print(f"Machine architecture:   {info.machine}")


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

# Old implementation
# print(f"Username:  {os.getlogin()}")
# print(f"Username:  {os.environ.get('USERNAME') or os.environ.get('USER')}")

# New implementation
username = os.environ.get("USERNAME") or os.environ.get("USER") or "Unknown"

print(f"Username:  {username}")
print(f"Path: {Path.cwd()}")


#Getting file hash / integrity information
def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


#Hash current Python file
current_file = Path(__file__)

file_hash = calculate_hash(current_file)

print(f"File: {current_file}")
print(f"SHA256: {file_hash}")


#Save information to .txt file
with open("system_info.txt", "w", encoding="utf-8") as file:

    file.write("SYSTEM INFORMATION\n")
    file.write("==========================\n")

    file.write(f"OS/System: {info.system}\n")
    file.write(f"Release: {info.release}\n")
    file.write(f"Version: {info.version}\n")
    file.write(f"Machine architecture: {info.machine}\n")

    file.write(f"Private IP Address: {get_private_ip()}\n")

    file.write(f"Username: {username}\n")
    file.write(f"Path: {Path.cwd()}\n")

    file.write("\nFILE INTEGRITY\n")
    file.write("==========================\n")

    file.write(f"File: {current_file}\n")
    file.write(f"SHA256: {file_hash}\n")


print("Information saved to system_info.txt")


#Keylogger functionality
#This lab version records only input typed directly into this program

# Old graphical implementation
#
# def start_keylogger():
#
#     window = tk.Tk()
#
#     window.title("Keylogger Lab")
#     window.geometry("500x250")
#
#     label = tk.Label(
#         window,
#         text="Keylogger Lab\n\nType inside this window.\nPress ESC to stop."
#     )
#
#     label.pack(expand=True)
#
#
#     def record_key(event):
#
#         #Stop program with ESC
#         if event.keysym == "Escape":
#             window.destroy()
#             return
#
#
#         #Normal characters
#         if event.char:
#             key = event.char
#
#         #Special keys
#         else:
#             key = f"[{event.keysym}]"
#
#
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#
#         #Save keystrokes to file
#         with open("keylog.txt", "a", encoding="utf-8") as log_file:
#
#             log_file.write(
#                 f"{timestamp} | {key}\n"
#             )
#
#
#         print(f"Key pressed: {key}")
#
#
#     window.bind("<KeyPress>", record_key)
#
#     window.mainloop()


# New terminal implementation
def start_keylogger():

    print("Starting terminal keylogger lab...")
    print("Type something below.")
    print("Type EXIT to stop.\n")

    while True:

        user_input = input("> ")

        #Stop program
        if user_input == "EXIT":
            print("Keylogger lab stopped.")
            break

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #Save input to file
        with open("keylog.txt", "a", encoding="utf-8") as log_file:

            log_file.write(
                f"{timestamp} | {user_input}\n"
            )

        print(f"Captured: {user_input}")


print("Starting keylogger lab...")

start_keylogger()