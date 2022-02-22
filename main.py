#!/usr/bin/env python3

"""
    3dscon - A tool to connect 3DS consoles via SMB
    (from the terminal)
"""

import os

def connect(consoleName,user,password,ip):
    """
        Connect to a 3DS console via SMB
    """
    COMMAND_STRING = f"sudo mount -t cifs //{consoleName}/microSD /mnt -o user={user},password={password},ip={ip},servern={consoleName},vers=1.0"
    if os.system(COMMAND_STRING):
        return True
    else:
        return False

def main():
    print("Welcome to 3dscon! \nTo start, we'll need your console's info.")
    consoleName = input("Enter the console name: ")
    user = input("Enter the username: ")
    password = input("Enter the password: ")
    ip = input("Enter the IP address: ")
    print("Please enter your computer's password below if needed.")
    if connect(consoleName,user,password,ip):
        print("Connected! View your 3DS' files in /mnt")
    else:
        print("Not connected! There might be a connection problem with your 3DS, or you might have entered the wrong info.")

if __name__ == "__main__":
    main()