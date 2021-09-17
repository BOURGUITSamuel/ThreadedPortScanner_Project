import socket
import re
import time
import threading
import concurrent.futures
import colorama
from colorama import Fore
import pyfiglet

colorama.init()

# Add Banner
ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

# Using lock for Multithreading.
print_lock = threading.Lock()

# Ask user to input the IP address they want to scan.
while True:
    ip_entered = input(Fore.WHITE + "Enter the IP to scan:")
    if ip_add_pattern.search(ip_entered):
        print(Fore.GREEN + f"{ip_entered}" + Fore.WHITE + " is a valid ip address")
        break
    else:
        print(f"Please enter a valid ip address !")
        continue


def scan(ip, port):
    """Scans the IP address entered by the user"""
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.BLUE + f"[{port}]" + Fore.GREEN + " Opened")
    except socket.error:
        pass


def main():
    """Execute Multithreading"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1000):
            executor.submit(scan, ip_entered, port + 1)


if __name__ == '__main__':
    main()
    time.sleep(20)
