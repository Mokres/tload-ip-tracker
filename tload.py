#!/usr/bin/env python3
# TIMO - IP Tracker

import requests
import os
import socket
from colorama import init, Fore, Style

init(autoreset=True)

def clear():
    os.system('clear')

def logo():
    print(Fore.RED + """
    ╔══════════════════════════════════╗
    ║   ▀▀█▀▀ █░░ █▀▀█ █▀▀█ █▀▀▄      ║
    ║   ░░█░░ █░░ █░░█ █▄▄█ █░░█      ║
    ║   ░░▀░░ ▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀░      ║
    ║         IP INTELLIGENCE          ║
    ╚══════════════════════════════════╝
    """ + Style.RESET_ALL)

def track(ip):
    try:
        r = requests.get(f'http://ip-api.com/json/{ip}?fields=status,country,regionName,city,zip,lat,lon,isp,org,as,proxy,hosting,mobile')
        data = r.json()
        
        if data['status'] == 'success':
            print(Fore.GREEN + "\n[+] IP: " + Fore.WHITE + ip)
            print(Fore.GREEN + "[+] Land: " + Fore.WHITE + data['country'])
            print(Fore.GREEN + "[+] Region: " + Fore.WHITE + data['regionName'])
            print(Fore.GREEN + "[+] Stadt: " + Fore.WHITE + data['city'])
            print(Fore.GREEN + "[+] PLZ: " + Fore.WHITE + data['zip'])
            print(Fore.GREEN + "[+] Koordinaten: " + Fore.WHITE + str(data['lat']) + ", " + str(data['lon']))
            print(Fore.GREEN + "[+] ISP: " + Fore.WHITE + data['isp'])
            print(Fore.GREEN + "[+] Organisation: " + Fore.WHITE + data['org'])
            print(Fore.GREEN + "[+] AS: " + Fore.WHITE + data['as'])
            print(Fore.GREEN + "[+] Proxy/VPN: " + (Fore.RED + "JA" if data['proxy'] else Fore.GREEN + "NEIN"))
            print(Fore.GREEN + "[+] Hosting: " + (Fore.RED + "JA" if data['hosting'] else Fore.GREEN + "NEIN"))
            print(Fore.GREEN + "[+] Mobil: " + (Fore.YELLOW + "JA" if data['mobile'] else Fore.GREEN + "NEIN"))
        else:
            print(Fore.RED + "Fehler: Ungültige IP")
    except:
        print(Fore.RED + "Fehler bei Verbindung")

def main():
    clear()
    logo()
    
    while True:
        print(Fore.CYAN + "\n[1] IP tracken")
        print(Fore.CYAN + "[2] Meine IP")
        print(Fore.CYAN + "[3] Ende")
        
        wahl = input(Fore.YELLOW + "\nWahl: " + Fore.WHITE)
        
        if wahl == "1":
            ip = input(Fore.YELLOW + "IP: " + Fore.WHITE)
            track(ip)
        elif wahl == "2":
            ip = requests.get('https://api.ipify.org').text
            print(Fore.GREEN + f"\nDeine IP: {ip}")
            track(ip)
        elif wahl == "3":
            print(Fore.RED + "Tschau!")
            break
        else:
            print(Fore.RED + "Falsche Wahl")

if __name__ == "__main__":
    main()