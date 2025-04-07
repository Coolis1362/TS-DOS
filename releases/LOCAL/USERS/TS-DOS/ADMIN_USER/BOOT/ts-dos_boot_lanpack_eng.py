import os
import sys
import time
import requests # type: ignore
import webbrowser # type: ignore
from bs4 import BeautifulSoup # type: ignore
import keyboard # type: ignore
import random # type: ignore
import pytz # type: ignore
from datetime import datetime # type: ignore
import platform
import subprocess # type: ignore


import time

def say(command):
    options = command.split()
    if "-slow" in options:
        message = " ".join(options[1:])
        for char in message:
            print(char, end="", flush=True)
            time.sleep(0.1)  # Delay for dramatic effect
        print()  # New line after message
    elif "--banner" in options:
        import pyfiglet   # type: ignore # Requires the pyfiglet library
        message = " ".join(options[1:])
        print(pyfiglet.figlet_format(message))
    else:
        message = " ".join(options)
        print(message)



def is_supported(file_name):
    # Check for macOS and Linux-specific file extensions
    unsupported_extensions = [".dmg", ".pkg", ".deb", ".sh"]
    return not any(file_name.endswith(ext) for ext in unsupported_extensions)

def install(file_url, tosys=False):
    file_name = file_url.split("/")[-1]  # Extract file name from the URL

    if not is_supported(file_name):
        print(f"❌ The file '{file_name}' is not supported on TS-DOS. It appears to be for macOS or Linux.")
        return

    if "." in file_name:  # Detect file extensions
        print(f"Processing file: '{file_name}'...\n")

        try:
            # Download the file
            print(f"Downloading '{file_name}' from {file_url}...\n")
            response = requests.get(file_url, stream=True)
            if response.status_code == 200:
                # Save the file locally
                with open(file_name, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
                print(f"✅ File '{file_name}' downloaded successfully!")

                if file_name.endswith((".exe", ".msi")) and tosys:
                    # Execute the file on the host OS
                    subprocess.run([file_name], check=True)
                    print(f"✅ '{file_name}' installed successfully on the host OS!")
                else:
                    print(f"Note: '{file_name}' downloaded but not installed. Use 'tosys' for host OS installation.")
            else:
                print(f"❌ Failed to download '{file_name}'. Error Code: 189")
        except Exception as e:
            print(f"An unexpected error occurred while downloading '{file_name}': {e}")
    else:
        print(f"❌ File extension not recognized for installation: '{file_name}'.")

def text_editor():
            print("*********************************")
            print("*       TS-DOS TEXT EDITOR      *")
            print("*********************************")
        
            print("\nStart typing your text below. Press ENTER after each line.")
            print("To exit the editor, type 'exit' and press ENTER.")
        
            while True:
                user_input = input()
                if user_input.lower() == "exit":
                    print("Exiting text editor...")
                    break

def system_check():
    print("Initializing system check...\n")
    
    # Fetch system details
    system_name = platform.system()
    release = platform.release()

    # Progress simulation
    print("Checking operating system...")
    for i in range(1, 101):  # Simulate progress with numbers
        print("#", end="", flush=True)
    print("\n")

    # Check if the system is Windows
    if system_name == "Windows":
        print(f"✅ System check complete: {system_name} {release} detected.")
        print("This system is compatible.")
        return True  # Indicates the system is Windows
    else:
        print(f"❌ System check complete: {system_name} {release} detected.")
        print("This service only supports Windows.")
        return False  # Indicates the system is not Windows

def ts_dos_fatal_error_screen():
    os.system("cls")  # Clears the screen (use 'clear' on Unix systems)
    print("\n" + "#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 30 + "FATAL ERROR DETECTED" + " " * 31 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 20 + "A FATAL SYSTEM ERROR HAS OCCURRED." + " " * 19 + "#")
    print("#" + " " * 24 + "SYSTEM ABORT IN PROGRESS." + " " * 25 + "#")
    print("#" + " " * 20 + "PLEASE RESTART TS-DOS IMMEDIATELY." + " " * 19 + "#")
    print("#" + " " * 78 + "#")
    
    # Random symbols, numbers, and codes
    print("#" * 80)
    for i in range(10):
        print("#", end="")
        for _ in range(78):
            char = random.choice(["%", "&", "#", "X", "1", "0", "A", "B", "F"])
            print(char, end="")
        print("#")
    print("#" * 80)

    # Faux memory dump
    print("\nInitiating Memory Dump...")
    for step in range(1, 101, 5):
        time.sleep(0.1)
        print(f"Progress: {step}% {'#' * (step // 10)}")
    
    print("\nSystem Halted.")
    input("Press any key to restart TS-DOS...")
    os.system("cls")
    print("Recovering TS-DOS...")
    time.sleep(2)
    print("System Restart Successful.")
    os.system('cls')
    ts_dos()

def ts_dos():

    print("Checking for TS-DOS...")
    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)

    print(" TS-DOS found!")
    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)
    print(" Loading TS-DOS...")
    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)
    print(" Clearing screen...")
    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)
    os.system('cls')
    print("Starting TS-DOS...")
    for step in range(100):
        print("#", end="", flush=True)
        time.sleep(0.05)
    time.sleep(1)
    print("")
    print("Welcome to TS-DOS!")
    print("Type 'help' for a list of commands or 'exit' to return to Command Prompt or type in 'welcome.exe' to get started.")
    time.sleep(1)
    print("********************************************")
    time.sleep(1)
    print("*       TS-DOS 1.0.2 TS-DOS KERNEL 1.0.2   *")
    time.sleep(1)
    print("*      TS-DOS SYSTEM 1.0.2 TS-DOS PYTHON   *")
    time.sleep(1)
    print("*   COPYRIGHT (C) 2025 TADEO A GONZALEZ    *")
    time.sleep(1)
    print("*       ALL RIGHTS RESERVED                *")
    time.sleep(1)
    print("*         LANGUAGE PACK=ENG                *")
    time.sleep(1)
    print("********************************************")
    
    while True:
        command = input("LOCAL\\USERS\\TS-DOS\\ADMIN_USER>> ").strip().lower()
        
        if command == "exit":
            print("Returning to Command Prompt...")
            sys.exit()
        elif command == "help":
            print("""
Available Commands:
- exit: Return to Command Prompt
- help: Shows all commands
- kernel <path>: Path needed for kernel command to work
- kernel --version: Displays the kernel version
- system <path>: Similar to kernel for system-related paths
- system --version: Displays the system version
- python --support: Shows Python is also supported
- python --version: Displays the version of Python installed
- welcome.exe: Displays a welcome message
- restart: Restarts TS-DOS
- internet: Checks internet connectivity
- website <url>: Opens a website in your browser
- site-content <url>: Displays the title and snippet of a website
- email: Launches Microsoft Outlook (if installed)
- python --filerunning: Shows The .py File This Version Of TS-DOS is running on
- ls: Lists the files in the current directory
- ctrlaltdel: Prompts to exit TS-DOS and Command Prompt
- blsod: Simulates a Black Screen of Death (BSOD) error screen
- info.txt: Displays information about the OS
- lan_pack.txt: Displays information about the language pack
- clear: Clears the screen
- time: Displays the current time
- time zone: Displays the current timezone
- version.txt: Displays the version of TS-DOS
- winver: Displays the Windows version and release details
- text-editor: Opens a simple text editor
- install <file_url> [tosys]: Downloads and installs a file from the given URL
- screensaver: starts the screensaver
            """)
        elif command.startswith("kernel"):
            if command == "kernel --version":
                print("TS-DOS Kernel Version: 1.0.2")
            else:
                print("Kernel command requires a valid path. Example: 'kernel <path>'")
        elif command.startswith("system"):
            if command == "system --version":
                print("TS-DOS System Version: 1.0.2")
            else:
                print("System command requires a valid path. Example: 'system <path>'")
        elif command == "python --support":
            print("Yes, Python is supported in TS-DOS!")
        elif command == "python --version":
            print(f"Python Version: {sys.version.split()[0]}")
        elif command == "welcome.exe":
            os.system('cls')
            print("**********************************************")
            print("*         WELCOME TO TS-DOS!                 *")
            print("*THIS IS A SIMULATED ENVIRONMENT FOR WINDOWS *")
            print("*         THANK YOU FOR USING TS-DOS!        *")
            print("**********************************************")
        elif command == "restart":
            print("restarting TS-DOS...")
            for step in range(100):
                print("#", end="", flush=True)
                time.sleep(0.05)
                
            print(" TS-DOS is restarting...")
            time.sleep(1)
            os.system('cls')
            ts_dos()
        
        elif command == "internet":
            try:
                print("Checking internet connectivity...")
                time.sleep(1)
                print("Connecting And Responding To www.google.com...")
                # Test connection to a website
                response = requests.get("https://www.google.com", timeout=5)
                for step in range(100):
                    print("#", end="", flush=True)
                    time.sleep(0.05)
                if response.status_code == 200:
                    print(" Internet is working!")
                else:
                    print(" Internet connection exists, but the site returned an error.")
            except requests.ConnectionError:
                print(" No internet connection detected.")
                return "INTERNET_CONNECTION_FAILED"
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif command.startswith("website "):
            url = command.split(" ", 1)[1]  # Extract URL after the command
            print(f"Opening {url} in your browser...")
            for step in range(100):
                print("#", end="", flush=True)
                time.sleep(0.05)
            webbrowser.open(url)
            print("")
            print("Website opened successfully!")
        elif command.startswith("site-content "):
            url = command.split(" ", 1)[1]
            try:
                print(f"Fetching content from {url}...")
                for step in range(100):
                    print("#", end="", flush=True)
                    time.sleep(0.05)
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, "html.parser")
                print("Website Title:", soup.find("title").text)
                print("Website Snippet:", soup.body.text[:200])
            except requests.exceptions.RequestException as e:
                print("An error occurred:", e)

        elif command == "email":
            # Open Microsoft Outlook
            print("Launching Microsoft Outlook...")
            try:
                os.system("start outlook")  # Launches Outlook if installed
            except Exception as e:
                print(f"Error: Unable to launch Outlook. {e}")
            print(f"Unknown command: {command}. Type 'help' for a list of commands.")

        elif command == "python --filerunning":

            print("RUNNING ON ts-dos_boot_lanpack_eng.py")
        
        elif command == "ls":
            print("BOOT")
            print("|")
            print("|")
            print("|----- ts-dos_boot_lanpack_eng.py")
            print("|----- ts-dos.bat")
            print("")
            print("INFO")
            print("|----- info.txt")
        
        elif command == "ctrlaltdel":
            print("Are You sure You Want to end TS-DOS and Commsand Prompt?")
            time.sleep(1)
            print("Press Y to confirm or N to cancel.")
            while True:
                if keyboard.is_pressed('y'):
                    print("Exiting TS-DOS and Command Prompt...")
                    for step in range(100):
                        print("#", end="", flush=True)
                        time.sleep(0.05)
                    print(" \nTS-DOS and Command Propmt is exiting...")
                    os.system("taskkill /F /IM cmd.exe")
                    os._exit(0)
                elif keyboard.is_pressed('n'):
                    print("Cancelled exit.")
                    break
                time.sleep(0.1)

        elif command == "blsod":
            print("Starting Black Screen of Death Simulator...")
            for step in range(100):
                print("#", end="", flush=True)
                time.sleep(0.05)
            ts_dos_fatal_error_screen()

        elif command == "info.txt":
            print("""{
    "os type": "text-based",
    "written in": "Python",
    "based on": "MS-DOS"
}""")
        elif command == "lan_pack.txt":
            print("LANAGUGE PACK == ENG")

        elif command == "clear":
            os.system('cls')

        elif command == "time":
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print("Current Time:", current_time)

        elif command == "time zone":
            # Get the local timezone
            local_tz = pytz.timezone("US/Eastern")  # Replace with your local timezone if needed
            local_time = datetime.now(local_tz)
            utc_offset = local_time.strftime('%z')  # Get UTC offset in the format ±HHMM
            utc_offset_formatted = f"UTC {utc_offset[:3]}:{utc_offset[3:]}"  # Format as ±HH:MM

            print(f"Time Zone: {utc_offset_formatted}")

        elif command == "version.txt":
            print("TS-DOS 1.0.2 Full Realease")

        elif command == "winver":
            # Fetch the Windows version and release details
            system = platform.system()
            release = platform.release()
            version = platform.version()
            if system == "Windows":
                print(f"Windows Version: {release} ({version})")

        elif command == "text-editor":
            text_editor()

        elif command.startswith("install"):
            parts = command.split()
            if len(parts) == 3:
                file_url = parts[1]
                tosys = "tosys" in parts
                install(file_url, tosys)
            else:
                print("Invalid syntax. Use: install <file_url> [tosys]")

        elif command == "screensaver":
            os.system("cls")
            print("Starting screensaver...")
            time.sleep(1)
            os.system("curl ascii.live/forrest")

        elif command == "say":
            print("Please enter the text you want to say:")
            text = input()
            say(text)

if __name__ == "__main__":
    if system_check():
        print("System check passed. Starting TS-DOS...")
        ts_dos()
    else:
        print("ERROR CODE 189: SYSTEM NOT SUPPORTED PLEASE USE WINDOWS")
        print("EXITIING TS-DOS...")
        time.sleep(1)
        for step in range(100):
            print("#", end="", flush=True)
            time.sleep(0.05)

        print(" TS-DOS is exiting...")
        os.system("cls") # Clears the screen If Windows
        os.system("clear") # Clears the screen If Unix
        sys.exit(0)

def ts_dos_fatal_error_screen():
    os.system("cls")  # Clears the screen (use 'clear' on Unix systems)
    print("\n" + "#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 30 + "FATAL ERROR DETECTED" + " " * 31 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 20 + "A FATAL SYSTEM ERROR HAS OCCURRED." + " " * 19 + "#")
    print("#" + " " * 24 + "SYSTEM ABORT IN PROGRESS." + " " * 25 + "#")
    print("#" + " " * 20 + "PLEASE RESTART TS-DOS IMMEDIATELY." + " " * 19 + "#")
    print("#" + " " * 78 + "#")
    
    # Random symbols, numbers, and codes
    print("#" * 80)
    for i in range(10):
        print("#", end="")
        for _ in range(78):
            char = random.choice(["%", "&", "#", "X", "1", "0", "A", "B", "F"])
            print(char, end="")
        print("#")
    print("#" * 80)

    # Faux memory dump
    print("\nInitiating Memory Dump...")
    for step in range(1, 101, 5):
        time.sleep(0.1)
        print(f"Progress: {step}% {'#' * (step // 10)}")
    
    print("\nSystem Halted.")
    input("Press any key to restart TS-DOS...")
    os.system("cls")
    print("Recovering TS-DOS...")
    time.sleep(2)
    print("System Restart Successful.")
    os.system('cls')
    ts_dos()

def check_for_fatal_errors():
    try:
        requests.get("https://www.google.com", timeout=5)
    except requests.ConnectionError:
        return "INTERNET_CONNECTION_FAILED"

    # Simulate a memory error check
    memory_ok = True  # Replace with actual memory check logic if applicable
    if not memory_ok:
        return "MEMORY_FAILURE"

    # Simulate a kernel load check
    kernel_loaded = True  # Replace with actual kernel check logic if applicable
    if not kernel_loaded:
        return "KERNEL_NOT_LOADED"

    # Simulate other potential system checks
    system_integrity = True  # Replace with custom checks for system state
    if not system_integrity:
        return "SYSTEM_INTEGRITY_CHECK_FAILED"

    # If no errors are detected, return None
    return None

error = check_for_fatal_errors()

if error:  # Check the condition
    ts_dos_fatal_error_screen()

while True:
    check_for_fatal_errors()


