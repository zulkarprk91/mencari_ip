#!/usr/bin/python3
import os
import time as t
import requests
import pyfiglet
import webbrowser
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Constants
API_URL = 'https://ipapi.co/{}/json/'

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display banner
def display_banner():
    clear_screen()
    banner = pyfiglet.figlet_format("IP Tracker")
    print(Fore.GREEN + banner)
    print(Fore.GREEN + """
 ==============================================
[+] Author  : zulkarnaen
[+] GitHub  : https://github.com/zulkarprk91
 ==============================================
    """)

# Display menu
def display_menu():
    print(Fore.CYAN + """
Commands:
  show       - Show available commands
  iptracker  - Track an IP address
  help       - Show usage information
  update     - Update the tool
  exit       - Quit the tool
    """)

# Fetch IP location data
def get_location(ip):
    try:
        response = requests.get(API_URL.format(ip))
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                print(Fore.RED + "Error: " + data.get("reason", "Unknown error"))
                return None
            return data
        else:
            print(Fore.RED + f"Error: Unable to fetch data (Status Code: {response.status_code})")
            return None
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        return None

# Display IP location data
def display_location(data):
    print(Fore.YELLOW + "IP Location Details:")
    for key, value in data.items():
        print(Fore.CYAN + f"  {key}: {value}")
    if "latitude" in data and "longitude" in data:
        lat, lon = data["latitude"], data["longitude"]
        maps_url = f"https://google.com/maps/place/{lat},{lon}/@{lat},{lon},16z"
        print(Fore.GREEN + "\nGoogle Maps: " + maps_url)
        open_map = input(Fore.CYAN + "Do you want to open this location on Google Maps? [yes/no]: ").strip().lower()
        if open_map in ['yes', 'y']:
            webbrowser.open(maps_url)

# Command handlers
def handle_iptracker():
    ip = input(Fore.YELLOW + "Enter IP Address: ").strip()
    print(Fore.CYAN + f"Fetching data for IP: {ip}...")
    data = get_location(ip)
    if data:
        display_location(data)

def handle_update():
    print(Fore.GREEN + "Updating IP Tracker...")
    # Placeholder for actual update logic
    print(Fore.YELLOW + "Update completed. Restart the tool to apply changes.")

# Main command loop
def command_loop():
    while True:
        command = input(Fore.MAGENTA + "Iptracker > ").strip().lower()
        if command == "help":
            display_menu()
        elif command == "show":
            display_menu()
        elif command == "iptracker":
            handle_iptracker()
        elif command == "update":
            handle_update()
        elif command == "exit":
            print(Fore.YELLOW + "Thank you for using IP Tracker. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid command. Type 'help' for available commands.")

# Main function
def main():
    display_banner()
    display_menu()
    command_loop()

if __name__ == "__main__":
    main()
